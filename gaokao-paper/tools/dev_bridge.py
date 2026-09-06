# -*- coding: utf-8 -*-
"""开发用桥接服务 —— 让前端在纯浏览器里也能跑

用途：
    不想每次都启动完整 Tauri（编译 Rust 要几分钟）时，
    用这个服务在浏览器里调试前端界面与 Python 逻辑。

    python3 tools/dev_bridge.py        # 默认 8765
    然后浏览器打开 http://localhost:8765/

工作原理：
    1. 静态文件服务（src/ 目录）
    2. /api/<cmd> 转发到 py/main.py 对应命令
    3. /slices/ 提供题目切图

注意：这只是开发辅助，正式使用请跑 `npm run tauri dev`。
"""
import http.server, socketserver, subprocess, sys, os, json, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, 'src')
PY = os.path.join(ROOT, 'py', 'main.py')
SLICES = os.path.join(ROOT, 'src', 'slices')   # 在 frontendDist 内
PORT = 8765

# 参数解析：支持 `8765`、`--port 8765`、`--port=8765`、`--help`。
# 早期版本只有 `int(sys.argv[1])`，用户输入 `--port 8765` 会抛
# ValueError: invalid literal for int()，报错完全看不懂。
_args = sys.argv[1:]
if any(a in ('-h', '--help') for a in _args):
    print('用法: python3 tools/dev_bridge.py [PORT | --port PORT]')
    print('\n浏览器模式下用的本地桥接服务，默认端口 8765。')
    sys.exit(0)
for i, a in enumerate(_args):
    if a == '--port' and i + 1 < len(_args):
        PORT = int(_args[i + 1]); break
    if a.startswith('--port='):
        PORT = int(a.split('=', 1)[1]); break
    if not a.startswith('-'):
        PORT = int(a); break

# 前端命令 → Python CLI 参数
CMD_MAP = {
    'py_health':   lambda a: ['health'],
    'py_list':     lambda a: ['list']
                   + (['--subject', a['subject']] if a.get('subject') else [])
                   + (['--q', a['q']] if a.get('q') else [])
                   + (['--limit', str(a['limit'])] if a.get('limit') else []),
    'py_stats':    lambda a: ['stats'],
    'py_kp_catalog': lambda a: ['kp-catalog']
                   + (['--subject', a['subject']] if a.get('subject') else []),
    'py_compose':  lambda a: ['compose', '--config', a['config']],
    'py_extract':  lambda a: ['extract', '--pdf', a['pdf'],
                              '--subject', a['subject']],
    'py_export_html': lambda a: ['export-html', '--ids', a['ids'],
                                 '--outdir', a['outdir']]
                   + (['--title', a['title']] if a.get('title') else []),
    'py_progress': lambda a: ['progress', '--payload', a['payload']],
    'py_due':      lambda a: ['due'],
    'py_export_progress': lambda a: ['export-progress']
                   + (['--outdir', a['outdir']] if a.get('outdir') else []),
    'app_paths':   lambda a: None,     # 特殊处理
}

# 不走 py/main.py，而是直接执行独立脚本的命令
SCRIPT_ONLY = {
    'py_sync_excel': 'sync_excel.py',
}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=WEB, **kw)

    def translate_path(self, path):
        """把 /slices/... 映射到项目内 slices 目录。

        为什么不用软链：
          - Windows 创建软链需要管理员权限
          - 软链曾被误建成 src/slices -> ../slices 的自引用循环，
            导致 404 且错误信息被日志函数吞掉
        """
        p = urllib.parse.urlparse(path).path
        # 同时接受 "/slices/…" 与 "slices/…"：
        # 前端刻意用不带前导斜杠的相对路径（兼容 file:// 协议），
        # 但直接手敲 URL 访问时是带斜杠的，两种都要能处理。
        if p.startswith('/slices/'):
            rest = urllib.parse.unquote(p[len('/slices/'):])
        elif p.startswith('/slices/') is False and '/slices/' in p:
            rest = urllib.parse.unquote(p.split('/slices/', 1)[1])
        else:
            return super().translate_path(path)
            # 防目录穿越
            rest = rest.replace('..', '').lstrip('/\\')
            return os.path.join(SLICES, *rest.split('/'))
        return super().translate_path(path)

    def log_message(self, fmt, *args):
        """注意：基类在 send_error 时会传入 HTTPStatus 而非字符串，
        直接对 args[0] 做 in 判断会抛 TypeError，
        进而吞掉真正的错误信息（曾导致切片 404 查不出原因）。"""
        try:
            first = args[0] if args else ''
            msg = (fmt % args) if args else str(fmt)
            if '/api/' in str(first):
                sys.stderr.write('  [api] %s\n' % first)
            elif '404' in msg or 'Traceback' in msg or 'code 5' in msg:
                sys.stderr.write('  [warn] %s\n' % msg)
        except Exception:
            pass

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        if not path.startswith('/api/'):
            self.send_error(404); return
        cmd = path[len('/api/'):]

        n = int(self.headers.get('Content-Length') or 0)
        try:
            args = json.loads(self.rfile.read(n) or b'{}')
        except Exception:
            args = {}

        if cmd == 'app_paths':
            data = {'ok': True,
                    'data_dir': os.path.join(ROOT, 'data'),
                    'bank': os.path.join(ROOT, 'data', 'bank.json'),
                    'progress': os.path.join(ROOT, 'data', 'progress.json'),
                    'slices': SLICES}
            return self._json(data)

        if cmd in SCRIPT_ONLY:
            # 独立脚本（如 sync_excel.py），不走 main.py 子命令
            script = os.path.join(os.path.dirname(PY), SCRIPT_ONLY[cmd])
            script_args = [args['path']] if args.get('path') else []
            try:
                r = subprocess.run([sys.executable, script] + script_args,
                                   capture_output=True, timeout=600, cwd=ROOT)
            except subprocess.TimeoutExpired:
                return self._json({'ok': False, 'error': '执行超时'}, 504)
            out = r.stdout.decode('utf-8', 'replace')
            err = r.stderr.decode('utf-8', 'replace')
            if r.returncode != 0:
                return self._json({'ok': False, 'error': err[-500:]}, 500)
            return self._json({'ok': True, 'log': out})

        fn = CMD_MAP.get(cmd)
        if fn is None:
            return self._json({'ok': False, 'error': '未知命令 ' + cmd}, 404)

        py_args = fn(args)
        try:
            r = subprocess.run([sys.executable, PY] + py_args,
                               capture_output=True, timeout=600, cwd=ROOT)
        except subprocess.TimeoutExpired:
            return self._json({'ok': False, 'error': '执行超时'}, 504)

        out = r.stdout.decode('utf-8', 'replace')
        # 只取最后一行 JSON（Python 侧可能有调试输出）
        line = ''
        for ln in reversed(out.splitlines()):
            if ln.strip().startswith('{'):
                line = ln; break
        if not line:
            err = r.stderr.decode('utf-8', 'replace')[-500:]
            return self._json({'ok': False, 'error': err or '无输出'}, 500)
        try:
            return self._json(json.loads(line))
        except Exception as e:
            return self._json({'ok': False, 'error': 'JSON 解析失败: %s' % e}, 500)

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


class TCP(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def resolve_slices():
    """确定切片目录。

    顺序：
      1. 项目内 ROOT/slices（正常情况）
      2. 旧开发环境 ROOT/../切片输出（迁移期兼容，仅用于提醒）
      3. 都不存在 → 返回项目内路径并标记缺失（启动时给出警告，
         而不是等到图片 404 才隐晦报错）
    """
    primary = os.path.join(ROOT, 'src', 'slices')
    if os.path.isdir(primary):
        return primary, True

    legacy = os.path.join(ROOT, 'slices')   # 旧布局（迁移期）
    if os.path.isdir(legacy):
        # 有旧目录但没迁移 —— 直接复制过来，避免在 src/ 下建软链
        # （软链在 Windows 上需要管理员权限，且曾被误建成自引用循环）
        try:
            import shutil
            os.makedirs(primary, exist_ok=True)
            for name in os.listdir(legacy):
                src, dst = os.path.join(legacy, name), os.path.join(primary, name)
                if os.path.isdir(src) and not os.path.exists(dst):
                    shutil.copytree(src, dst)
            print('已从旧目录复制切片: %s -> %s' % (legacy, primary))
            return primary, True
        except Exception as e:
            print('复制切片失败: %s' % e)
            return legacy, False
    return primary, False


def main():
    global SLICES
    SLICES, slices_ok = resolve_slices()

    print('=' * 52)
    print('  高考组卷 · 开发桥接服务')
    print('=' * 52)
    print('  浏览器打开：http://localhost:%d/' % PORT)
    print('  题库：%s' % os.path.join(ROOT, 'data', 'bank.json'))
    print('  切片：%s%s' % (SLICES, '' if slices_ok else '  ← 目录不存在！'))
    if not slices_ok:
        print()
        print('  ⚠ 切片目录不存在，带图题目将无法显示图片。')
        print('    请把切图放到: %s' % SLICES)
        print('    或从原始 PDF 重新拆题。')
    print('  停止：Ctrl+C')
    print('=' * 52)
    print()
    with TCP(('127.0.0.1', PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n已停止')


if __name__ == '__main__':
    main()
