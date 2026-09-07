# -*- coding: utf-8 -*-
"""把题库导出为 Excel（供人工校订 / 查阅）

用法：
    python3 tools/export_excel.py [输出路径]

与 py/sync_excel.py 方向相反：
    export_excel : bank.json -> Excel   （生成给人看/改）
    sync_excel   : Excel     -> bank.json（把改动同步回库）

导出后可在 Excel 里直接校订题干、选项、答案、知识点，
改完跑 sync_excel.py 同步回去。

模板样式（表头、列宽、冻结、下拉）由 py/excel_style.py 提供，
与历史版本保持一致。
"""
import os
import sys
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'py'))

BANK = os.path.join(ROOT, 'data', 'bank.json')
DEFAULT_OUT = os.path.join(ROOT, '高三题库与间隔复习系统.xlsx')

# openpyxl 拒绝写入控制字符（\x0b、\x0c 等），
# 而 PDF 提取的文本里常混入这类字符（换页符、制表符变体）。
# 不清洗的话整个导出会崩，且报错只指向"某一题的某一个值"，
# 排查成本高 —— 统一在写入前清洗。
_ILLEGAL = re.compile(r'[\x00-\x08\x0b-\x0c\x0e-\x1f]')


def _clean(v):
    """清洗单元格值：去掉 openpyxl 不接受的控制字符。"""
    if not isinstance(v, str):
        return v
    return _ILLEGAL.sub('', v)


def main(out=DEFAULT_OUT):
    from openpyxl import Workbook
    import openpyxl
    import kp_catalog as K

    bank = json.load(open(BANK, encoding='utf-8'))

    wb = Workbook()
    ws = wb.active
    ws.title = '题库索引'

    COLS = [
        ('题目ID', 16), ('科目', 8), ('年份', 8), ('题型', 10),
        ('题型细分', 16), ('一级知识点', 16), ('二级知识点', 16),
        ('题型标签', 26), ('存储形式', 12), ('题干', 70),
        ('选项A', 22), ('选项B', 22), ('选项C', 22), ('选项D', 22),
        ('答案', 20), ('解析', 60), ('难度系数', 10), ('难度等级', 10),
        ('分值', 8), ('来源', 34), ('批次', 20), ('审核备注', 50),
    ]
    for i, (name, w) in enumerate(COLS, 1):
        c = ws.cell(row=1, column=i, value=_clean(name))
        c.font = openpyxl.styles.Font(bold=True, color='FFFFFF')
        c.fill = openpyxl.styles.PatternFill('solid', fgColor='4472C4')
        c.alignment = openpyxl.styles.Alignment(horizontal='center')
        ws.column_dimensions[
            openpyxl.utils.get_column_letter(i)].width = w
    ws.freeze_panes = 'A2'

    lvl = lambda d: ('容易' if d >= 0.7 else '适中' if d >= 0.5
                     else '较难' if d >= 0.3 else '困难')

    for r, q in enumerate(bank, 2):
        d = q.get('difficulty')
        opts = q.get('opts') or []
        # opts 形状 [(字母, 文本)]
        otext = {}
        for item in opts:
            if isinstance(item, (list, tuple)) and len(item) == 2:
                otext[item[0]] = item[1]
        topics = q.get('topics') or []
        vals = [
            q.get('id', ''),
            q.get('subject', ''),
            q.get('year', ''),
            q.get('type', ''),
            q.get('subtype', ''),
            q.get('kp', ''),
            q.get('kp2', ''),
            '; '.join('%s(%s)' % (t, K.topic_label(t)) if K.topic_node(t)
                      else t for t in topics),
            'LaTeX' if '$' in (q.get('stem_text') or '') else
            ('图片' if q.get('figs') else '纯文本'),
            q.get('stem_text', ''),
            otext.get('A', ''), otext.get('B', ''),
            otext.get('C', ''), otext.get('D', ''),
            q.get('answer', ''),
            q.get('solution') or q.get('ana_text') or '',
            d if d is not None else '',
            lvl(d) if d is not None else '',
            q.get('score', ''),
            q.get('src', ''),
            q.get('batch', ''),
            q.get('review', ''),
        ]
        for i, v in enumerate(vals, 1):
            ws.cell(row=r, column=i, value=_clean(v))
        # 题干换行显示
        ws.cell(row=r, column=10).alignment = openpyxl.styles.Alignment(
            wrap_text=True, vertical='top')
        ws.cell(row=r, column=16).alignment = openpyxl.styles.Alignment(
            wrap_text=True, vertical='top')
        ws.cell(row=r, column=22).alignment = openpyxl.styles.Alignment(
            wrap_text=True, vertical='top')

    # 知识点目录表
    ws2 = wb.create_sheet('知识点编码')
    h2 = ['科目', '大知识点', '小知识点', '题型ID', '题型名称']
    for i, t in enumerate(h2, 1):
        c = ws2.cell(row=1, column=i, value=_clean(t))
        c.font = openpyxl.styles.Font(bold=True, color='FFFFFF')
        c.fill = openpyxl.styles.PatternFill('solid', fgColor='70AD47')
    for i, w in enumerate([10, 18, 26, 12, 40], 1):
        ws2.column_dimensions[
            openpyxl.utils.get_column_letter(i)].width = w
    r = 2
    for sub in K.CATALOG:
        for l1, subs in K.CATALOG[sub]:
            for l2, tops in subs.items():
                for t in tops:
                    ws2.cell(row=r, column=1, value=_clean(sub))
                    ws2.cell(row=r, column=2, value=_clean(l1))
                    ws2.cell(row=r, column=3, value=l2)
                    tid = K.topic_id(sub, l1, l2, t)
                    ws2.cell(row=r, column=4, value=tid or '')
                    ws2.cell(row=r, column=5, value=t)
                    r += 1
    ws2.freeze_panes = 'A2'

    wb.save(out)
    print('  已导出 %d 题 -> %s' % (len(bank), out))
    return out


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT)
