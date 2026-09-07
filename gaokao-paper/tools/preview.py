#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一键预览：起本地服务 + 自动刷新 + 自动打开浏览器

为什么需要它
------------
改排版时最短的反馈循环是「改完刷新就能看到」。
但导出的 HTML 用 file:// 打开时，每次改动都要手动刷新，
频繁调版式时很烦。

这个脚本做三件事：
  1. 起一个本地 HTTP 服务
  2. 往页面里注入自动刷新脚本（文件一变就 reload）
  3. 自动打开浏览器

用法
----
    python3 tools/preview.py                 # 预览 html/ 下最新一份
    python3 tools/preview.py xxx.html        # 预览指定文件
    python3 tools/preview.py --dir html      # 预览整个目录（可点选）

自动刷新原理
------------
页面每 1.5 秒用 HEAD 请求问一次服务端「文件改了没」，
服务端比对 mtime，变了就让浏览器 reload。
脚本只在服务端注入，**不修改原 HTML 文件**，正式交付不受影响。
"""
import http.server
import os
import socketserver
import subprocess
import sys
import threading
import time
import webbrowser
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(ROOT, 'html')

# 注入到 </body> 前的自动刷新脚本
AUTO_REFRESH = """
<script>
(function () {
  var KEY = '__preview_mtime__';
  var first = true;
  async function check() {
    try {
      var r = await fetch(location.pathname + '?t=' + Date.now(), { method: 'HEAD' });
      var mt = r.headers.get('X-File-Mtime');
      if (!mt) return;
      if (first) { sessionStorage.setItem(KEY, mt); first = false; return; }
      if (sessionStorage.getItem(KEY) !== mt) {
        sessionStorage.setItem(KEY, mt);
        location.reload();
      }
    } catch (e) { /* ignore */ }
  }
  setInterval(check, 1500);
  check();
  // 顶部小提示条
  var b = document.createElement('div');
  b.textContent = '预览模式：文件变动会自动刷新（Ctrl+P 打印即 PDF）';
  b.style.cssText = 'position:fixed;right:10px;bottom:10px;z-index:9999;'
    + 'background:rgba(47,85,151,.9);color:#fff;font:12px/1.6 sans-serif;'
    + 'padding:6px 12px;border-radius:6px;pointer-events:none;opacity:.75';
  document.addEventListener('DOMContentLoaded', function(){ document.body.appendChild(b); });
})();
</script>
"""


class Handler(http.server.SimpleHTTPRequestHandler):
    """在返回 HTML 时注入自动刷新脚本，并带上文件 mtime"""

    def _mtime(self, path):
        try:
            return str(int(os.path.getmtime(path)))
        except OSError:
            return '0'

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path) and path.lower().endswith(('.html', '.htm')):
            try:
                with open(path, 'rb') as f:
                    body = f.read()
                html = body.decode('utf-8', errors='replace')
                if '</body>' in html:
                    html = html.replace('</body>', AUTO_REFRESH + '</body>')
                else:
                    html += AUTO_REFRESH
                data = html.encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(data)))
                self.send_header('X-File-Mtime', self._mtime(path))
                self.send_header('Cache-Control', 'no-store')
                self.end_headers()
                import io as _io
                if self.command == 'HEAD':
                    return None
                return _io.BytesIO(data)
            except OSError:
                pass
        # 非 HTML：走默认逻辑，但也带 mtime
        r = super().send_head()
        return r

    def end_headers(self):
        # 禁止缓存，否则刷新看不到新内容
        if 'Cache-Control' not in self._headers_buffer_all():
            pass
        super().end_headers()

    def _headers_buffer_all(self):
        try:
            return b''.join(self._headers_buffer).decode('latin-1')
        except Exception:
            return ''

    def log_message(self, fmt, *args):
        # 静音轮询日志，否则每 1.5 秒刷一行没法看
        msg = fmt % args
        if 'HEAD' in msg and '?t=' in msg:
            return
        sys.stderr.write('  [预览] %s\n' % msg)


def pick_latest(directory):
    """目录下最近修改的 HTML"""
    best, bt = None, -1
    for name in os.listdir(directory):
        if not name.lower().endswith(('.html', '.htm')):
            continue
        p = os.path.join(directory, name)
        try:
            t = os.path.getmtime(p)
        except OSError:
            continue
        if t > bt:
            best, bt = p, t
    return best


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    serve_dir = DEFAULT_DIR
    target = None

    if '--dir' in sys.argv:
        i = sys.argv.index('--dir')
        if i + 1 < len(sys.argv):
            serve_dir = sys.argv[i + 1]

    if args:
        target = os.path.abspath(args[0])
        if os.path.isfile(target):
            serve_dir = os.path.dirname(target)

    serve_dir = os.path.abspath(serve_dir)
    if not os.path.isdir(serve_dir):
        os.makedirs(serve_dir, exist_ok=True)
        print('  目录不存在，已创建：%s' % serve_dir)
        print('  请先在应用里导出一份 HTML 到该目录。')

    if target is None:
        target = pick_latest(serve_dir)

    os.chdir(serve_dir)

    # 端口：从 8765 起找一个空闲的
    port = 8765
    for _ in range(20):
        try:
            httpd = socketserver.ThreadingTCPServer(('127.0.0.1', port), Handler)
            break
        except OSError:
            port += 1
    else:
        print('  找不到空闲端口'); sys.exit(1)

    httpd.daemon_threads = True
    rel = os.path.relpath(target, serve_dir) if target else ''
    url = 'http://127.0.0.1:%d/%s' % (port, quote(rel.replace(os.sep, '/')))

    print('  预览服务已启动')
    print('  目录：%s' % serve_dir)
    if rel:
        print('  文件：%s' % rel)
    print('  地址：%s' % url)
    print('  文件变动会自动刷新；Ctrl+C 退出\n')

    threading.Timer(0.8, lambda: webbrowser.open(url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n  已停止')
        httpd.shutdown()


if __name__ == '__main__':
    main()
