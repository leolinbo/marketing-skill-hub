import zipfile
import xml.etree.ElementTree as ET
import os
import shutil
import datetime

def update_excel_file(xlsx_path, target_row_idx, no_num):
    if not os.path.exists(xlsx_path):
        print(f"File not found: {xlsx_path}")
        return False

    backup_path = xlsx_path.replace('.xlsx', f'.backup_jonas_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.xlsx')
    shutil.copyfile(xlsx_path, backup_path)
    print(f"Backup created at: {backup_path}")

    extract_dir = os.path.join(r"d:\marketing\scripts\xlsx_extract_jonas", os.path.basename(xlsx_path))
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)

    with zipfile.ZipFile(xlsx_path, 'r') as z:
        z.extractall(extract_dir)

    sst_file = os.path.join(extract_dir, 'xl', 'sharedStrings.xml')
    tree_sst = ET.parse(sst_file)
    root_sst = tree_sst.getroot()
    ns_sst = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

    existing_strings = []
    for si in root_sst.findall('s:si', ns_sst):
        t_elem = si.find('s:t', ns_sst)
        if t_elem is not None and t_elem.text is not None:
            existing_strings.append(t_elem.text)
        else:
            runs = si.findall('s:r', ns_sst)
            if runs:
                text = "".join([r.find('s:t', ns_sst).text for r in runs if r.find('s:t', ns_sst) is not None and r.find('s:t', ns_sst).text])
                existing_strings.append(text)
            else:
                existing_strings.append("")

    def get_string_id(s):
        if s in existing_strings:
            return existing_strings.index(s)
        else:
            existing_strings.append(s)
            si = ET.SubElement(root_sst, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si')
            t = ET.SubElement(si, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
            t.text = s
            return len(existing_strings) - 1

    sheet_file = os.path.join(extract_dir, 'xl', 'worksheets', 'sheet1.xml')
    tree_sheet = ET.parse(sheet_file)
    root_sheet = tree_sheet.getroot()
    ns_sheet = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

    sheetData = root_sheet.find('s:sheetData', ns_sheet)

    row_elem = None
    for r in sheetData.findall('s:row', ns_sheet):
        if r.get('r') == str(target_row_idx):
            row_elem = r
            break

    if row_elem is None:
        row_elem = ET.SubElement(sheetData, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row')
        row_elem.set('r', str(target_row_idx))

    # Keep existing styles mapping if cells already exist
    existing_styles = {}
    for c in list(row_elem):
        ref = c.get('r')
        col = ''.join([ch for ch in ref if ch.isalpha()])
        existing_styles[col] = c.get('s', '2')
        row_elem.remove(c)

    today_str = datetime.date.today().strftime('%Y/%m/%d')
    values = {
        'A': (str(no_num), 'n'),
        'B': (today_str, 's'),
        'C': ('Jonas Concepcion (Lightsome Studio / Joncon Creativeworks)', 's'),
        'D': ('http://www.joncon.net/', 's'),
        'E': ('美国 (纽约州 Beacon / Newburgh)', 's'),
        'F': ('资深商业与建筑照明工业设计及工程专家（15-20+年行业经验），现任Lightsome Studio联合创始人/首席设计师（专做高端建筑与住宅装饰性高性能灯具），兼Joncon Creativeworks主理人；曾任德国Selux北美设计工程师，RPI照明科学硕士毕业（全球顶尖LRC）；持有导轨(USD681873S1)、挡光格栅Baffle(USD693960S1)等多项照明核心专利；深谙光学设计、热仿真、SolidWorks建模与灯具制造工艺。', 's'),
        'G': ('是', 's'),
        'H': ('独立照明产品设计师 / 高端灯具品牌商 / 工程顾问', 's'),
        'I': ('A (资深照明专家 & 高端建筑灯具产品决策人)', 's'),
        'J': ('Jonas Concepcion', 's'),
        'K': ('+1 848-219-4476', 's'),
        'L': ('jonasconcepcion@gmail.com', 's'),
        'M': ('高端建筑与商业/住宅灯具设计与研发、光学系统定制、照明产品工程化与供应链整合', 's'),
        'N': ('高品质商业与建筑照明系统：超薄磁吸轨道灯系统、深防眩筒射灯、高CRI/高显色光学模组、DALI-2/0-10V智能调光驱动、定制铝型材与精密五金配套', 's'),
        'O': ('在Pinterest点赞我方产品引流。已准备Ins(@infamous_panda)同行视角破冰话术，建议以“建筑与展陈照明设计灵感Lookbook/工程选型手册”切入，探寻其Lightsome Studio项目配合或供应链代工机会。', 's'),
        'P': ('待分配', 's'),
        'Q': ('否', 's'),
        'R': ('互动中 (Pinterest点赞，待Ins私信)', 's'),
        'S': ('Pinterest点赞破冰，已获取Ins(@infamous_panda)、电话、邮箱及个人网站，已完成全网深度背景背调，待发送Ins同行交流私信递送图册。', 's'),
        'T': ('Ins: @infamous_panda；电话: 848-219-4476；邮箱: jonasconcepcion@gmail.com；官网: www.joncon.net；地址: Beacon, NY；RPI照明硕士，持多项照明专利；对光学与工程结构极度专业，沟通需保持同行平等专业视角，切忌硬推销。', 's'),
    }

    cols = [chr(ord('A') + i) for i in range(20)]
    for col in cols:
        val_tuple = values.get(col, ('', 's'))
        val, vtype = val_tuple
        cell_ref = f"{col}{target_row_idx}"
        c_elem = ET.SubElement(row_elem, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')
        c_elem.set('r', cell_ref)
        c_elem.set('s', existing_styles.get(col, '2'))
        v_elem = ET.SubElement(c_elem, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
        if vtype == 's':
            c_elem.set('t', 's')
            v_elem.text = str(get_string_id(val))
        else:
            v_elem.text = str(val)

    root_sst.set('count', str(len(existing_strings)))
    root_sst.set('uniqueCount', str(len(existing_strings)))

    tree_sst.write(sst_file, encoding='utf-8', xml_declaration=True)
    tree_sheet.write(sheet_file, encoding='utf-8', xml_declaration=True)

    with zipfile.ZipFile(xlsx_path, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for root, dirs, files in os.walk(extract_dir):
            for f in files:
                full_path = os.path.join(root, f)
                arcname = os.path.relpath(full_path, extract_dir)
                z_out.write(full_path, arcname)

    print(f"SUCCESS: Successfully inserted Jonas Concepcion into {xlsx_path} row {target_row_idx} (NO# {no_num})!")
    return True

if __name__ == '__main__':
    # 1. Update Downloads Excel (Row 31, NO# 27)
    downloads_path = r"C:\Users\HUAWEI\Downloads\ENCORE社媒客户清单 V0 20261023张林波.xlsx"
    update_excel_file(downloads_path, target_row_idx=31, no_num=27)

    # 2. Synchronize to Desktop as well
    desktop_path = r"C:\Users\HUAWEI\Desktop\ENCORE社媒客户清单 V0 20261023张林波.xlsx"
    if os.path.exists(desktop_path):
        shutil.copyfile(downloads_path, desktop_path)
        print(f"Synchronized updated file to Desktop: {desktop_path}")
