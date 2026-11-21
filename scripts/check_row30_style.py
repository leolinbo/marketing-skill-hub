import os, zipfile, xml.etree.ElementTree as ET

p = r'C:\Users\HUAWEI\Downloads\ENCORE社媒客户清单 V0 20261023张林波.xlsx'
with zipfile.ZipFile(p, 'r') as z:
    sheet_root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    for r in sheet_root.findall('.//s:row', ns):
        if r.get('r') == '30':
            for c in r.findall('s:c', ns):
                print(c.get('r'), c.attrib)
