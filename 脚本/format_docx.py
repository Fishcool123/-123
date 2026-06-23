"""
美化 Pandoc 生成的 docx 文件，应用规范中文排版样式。
用法：py.exe format_docx.py <input.docx>
输出：<input>_formatted.docx
依赖：python-docx
"""
import sys
import copy
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

# ============================================================
# 样式配置（可按需调整）
# ============================================================
CN_BODY_FONT = '宋体'          # 正文中文
EN_BODY_FONT = 'Times New Roman'  # 正文西文
CN_HEADING_FONT = '黑体'      # 标题中文
EN_HEADING_FONT = 'Arial'     # 标题西文
CODE_FONT = 'Consolas'        # 代码字体

BODY_SIZE = Pt(11)            # 正文字号（五号）
H1_SIZE = Pt(18)              # 一级标题（小二号）
H2_SIZE = Pt(15)              # 二级标题（小三号）
H3_SIZE = Pt(13)              # 三级标题（四号）
CODE_SIZE = Pt(9)             # 代码字号
TABLE_SIZE = Pt(9.5)          # 表格字号

LINE_SPACING = 1.5            # 正文行距
HEADING_SPACING_BEFORE = Pt(12)
HEADING_SPACING_AFTER = Pt(6)

PAGE_MARGIN = Cm(2.0)         # 页边距


def set_run_font(run, cn_font, en_font, size, bold=False, color=None, italic=False):
    """设置 run 的中英文字体、大小、粗细、颜色"""
    run.font.size = size
    run.bold = bold
    run.italic = italic
    rPr = run._element.get_or_add_rPr()
    # 东亚字体
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} />')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:eastAsia'), cn_font)
    rFonts.set(qn('w:ascii'), en_font)
    rFonts.set(qn('w:hAnsi'), en_font)
    rFonts.set(qn('w:cs'), en_font)
    if color:
        run.font.color.rgb = color


def set_paragraph_spacing(para, line_spacing=None, before=Pt(0), after=Pt(0),
                          alignment=None, first_line_indent=None):
    """设置段落间距、对齐方式、首行缩进"""
    pf = para.paragraph_format
    if line_spacing:
        pf.line_spacing = line_spacing
    pf.space_before = before
    pf.space_after = after
    if alignment is not None:
        para.alignment = alignment
    if first_line_indent:
        pf.first_line_indent = first_line_indent


def set_cell_text_format(cell, cn_font, en_font, size, bold=False):
    """格式化表格单元格中的所有文本"""
    for para in cell.paragraphs:
        for run in para.runs:
            set_run_font(run, cn_font, en_font, size, bold=bold)


def is_heading(style_name):
    """判断段落样式是否为标题"""
    return style_name and style_name.startswith('Heading')


def is_code_block(para):
    """判断段落是否为代码块（Pandoc 生成的 SourceCode 样式）"""
    style = para.style.name if para.style else ''
    return 'Source Code' in style or 'Verbatim' in style


def format_table(table, doc):
    """格式化表格：字体、边框、表头底色"""
    # 设置表格边框
    tbl = table._tbl
    tblPr = tbl.find(qn('w:tblPr'))
    if tblPr is None:
        tblPr = parse_xml(f'<w:tblPr {nsdecls("w")} />')
        tbl.insert(0, tblPr)

    # 设置表格边框
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="666666"/>'
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="666666"/>'
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="666666"/>'
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="666666"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="666666"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="666666"/>'
        f'</w:tblBorders>'
    )
    # 移除旧边框，添加新边框
    existing = tblPr.find(qn('w:tblBorders'))
    if existing is not None:
        tblPr.remove(existing)
    tblPr.append(borders)

    # 格式化每个单元格
    is_header = True
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                para.paragraph_format.space_before = Pt(1)
                para.paragraph_format.space_after = Pt(1)
                para.paragraph_format.line_spacing = 1.15
                for run in para.runs:
                    set_run_font(run, CN_BODY_FONT, EN_BODY_FONT, TABLE_SIZE,
                                 bold=is_header)
            # 表头行加灰色底色
            if is_header:
                shading = parse_xml(
                    f'<w:shd {nsdecls("w")} w:fill="E8E8E8" w:val="clear"/>'
                )
                cell._tc.get_or_add_tcPr().append(shading)
        is_header = False


def format_docx(input_path):
    """主函数：打开 docx 并应用全部样式"""
    doc = Document(input_path)

    # ----- 1. 设置页面边距 -----
    for section in doc.sections:
        section.top_margin = PAGE_MARGIN
        section.bottom_margin = PAGE_MARGIN
        section.left_margin = PAGE_MARGIN + Cm(0.5)  # 左侧略宽，装订用
        section.right_margin = PAGE_MARGIN

    # ----- 2. 遍历所有段落 -----
    for para in doc.paragraphs:
        style_name = para.style.name if para.style else ''

        if is_heading(style_name):
            # --- 标题样式 ---
            level = int(style_name.replace('Heading ', ''))
            if level == 1:
                size, before, after = H1_SIZE, HEADING_SPACING_BEFORE, HEADING_SPACING_AFTER
                cn_f, en_f = CN_HEADING_FONT, EN_HEADING_FONT
            elif level == 2:
                size, before, after = H2_SIZE, HEADING_SPACING_BEFORE, HEADING_SPACING_AFTER
                cn_f, en_f = CN_HEADING_FONT, EN_HEADING_FONT
            else:
                size, before, after = H3_SIZE, Pt(8), Pt(4)
                cn_f, en_f = CN_HEADING_FONT, EN_HEADING_FONT

            set_paragraph_spacing(para, line_spacing=1.3, before=before, after=after)
            for run in para.runs:
                set_run_font(run, cn_f, en_f, size, bold=True)

        elif is_code_block(para):
            # --- 代码块 ---
            set_paragraph_spacing(para, line_spacing=1.2, before=Pt(2), after=Pt(2))
            # 代码块底色
            shading = parse_xml(
                f'<w:shd {nsdecls("w")} w:fill="F5F5F5" w:val="clear"/>'
            )
            para._element.get_or_add_pPr().append(shading)
            for run in para.runs:
                set_run_font(run, CODE_FONT, CODE_FONT, CODE_SIZE)

        else:
            # --- 正文段落 ---
            set_paragraph_spacing(para, line_spacing=LINE_SPACING,
                                  before=Pt(1), after=Pt(1))
            for run in para.runs:
                if run.bold:
                    set_run_font(run, CN_HEADING_FONT, EN_HEADING_FONT,
                                 run.font.size or BODY_SIZE, bold=True)
                else:
                    set_run_font(run, CN_BODY_FONT, EN_BODY_FONT,
                                 run.font.size or BODY_SIZE)

    # ----- 3. 格式化所有表格 -----
    for table in doc.tables:
        format_table(table, doc)

    # ----- 4. 保存 -----
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_formatted{ext}"
    doc.save(output_path)
    print(f"OK: {os.path.basename(output_path)}")
    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: py.exe format_docx.py <file.docx>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"文件不存在: {input_file}")
        sys.exit(1)

    format_docx(input_file)
