import zipfile
import xml.etree.ElementTree as ET
import os
import shutil
import datetime

# 目标表格：Downloads 目录下的表格
xlsx_path = r"C:\Users\HUAWEI\Downloads\ENCORE社媒客户清单 V0 20261023张林波.xlsx"
backup_path = r"C:\Users\HUAWEI\Downloads\ENCORE社媒客户清单 V0 20261023张林波.backup_beki.xlsx"

if not os.path.exists(backup_path):
    shutil.copyfile(xlsx_path, backup_path)
    print("Backup created at:", backup_path)

extract_dir = r"d:\marketing\scripts\xlsx_extract_downloads"
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

# Row 28 是 Light Connect (Arhan Technologies)，插入到 Row 29 (NO# 25)
target_row_idx = '29'
row29 = None
for r in sheetData.findall('s:row', ns_sheet):
    if r.get('r') == target_row_idx:
        row29 = r
        break

if row29 is None:
    row29 = ET.SubElement(sheetData, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row')
    row29.set('r', target_row_idx)

for c in list(row29):
    row29.remove(c)

today_str = datetime.date.today().strftime('%Y/%m/%d')
values = {
    'A': ('25', 'n'),
    'B': (today_str, 's'),
    'C': ('Beki Tobiasson (Beki Tobiasson Art)', 's'),
    'D': ('https://bekitobiassonartist.com', 's'),
    'E': ('美国 (犹他州)', 's'),
    'F': ('美国知名当代油画家（写实/具象/花卉），作品参展春维尔艺术博物馆等主流展馆；拥有10x12英尺私人油画画室，要求5000K色温、95+ CRI顶级显色照明用于专业画室调色', 's'),
    'G': ('是', 's'),
    'H': ('终端艺术工作室/画家主理人', 's'),
    'I': ('A (高意向专业买家)', 's'),
    'J': ('Beki Tobiasson', 's'),
    'K': ('+1 801-358-6625', 's'),
    'L': ('bekitobiasson@gmail.com', 's'),
    'M': ('油画艺术创作与展览、艺术工作室运营', 's'),
    'N': ('画室专业照明：5000K、CRI 95+ 高显色防眩光轨道灯/洗墙灯或筒灯，适配10x12英尺油画工作室', 's'),
    'O': ('Shopify(encorebeam.com)表单直接询盘，询问10x12画室需配置几盏灯。业务员需提供照度方案、询问层高与轨道/筒灯偏好，加WhatsApp推进', 's'),
    'P': ('待分配', 's'),
    'Q': ('否', 's'),
    'R': ('待跟进', 's'),
    'S': ('官网独立站询盘直达，已完成全网深度艺术背景背调', 's'),
    'T': ('表单ID: ContactForm-AVFJHdFhzSVdoYTBIN__contact_form_dJqVC7；归属encorebeam.com零售站', 's'),
}

for col, (val, vtype) in values.items():
    cell_ref = f"{col}{target_row_idx}"
    c_elem = ET.SubElement(row29, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')
    c_elem.set('r', cell_ref)
    c_elem.set('s', '2')
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

print("SUCCESS: Successfully inserted Beki Tobiasson into Downloads Excel row 29!")
