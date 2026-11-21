import zipfile, xml.etree.ElementTree as ET
p = r'C:\Users\HUAWEI\Downloads\ENCORE社媒客户清单 V0 20261023张林波.xlsx'
with zipfile.ZipFile(p, 'r') as z:
    sst_root = ET.fromstring(z.read('xl/sharedStrings.xml'))
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    strings = []
    for si in sst_root.findall('s:si', ns):
        t = si.find('s:t', ns)
        if t is not None and t.text:
            strings.append(t.text)
        else:
            runs = si.findall('s:r', ns)
            strings.append(''.join([r.find('s:t', ns).text for r in runs if r.find('s:t', ns) is not None and r.find('s:t', ns).text]))
    
    sheet_root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    for r in sheet_root.findall('.//s:row', ns):
        if r.get('r') == '31':
            cells = {}
            for c in r.findall('s:c', ns):
                ref = c.get('r')
                t = c.get('t')
                v = c.find('s:v', ns)
                val = v.text if v is not None else ''
                if t == 's' and val.isdigit():
                    val = strings[int(val)]
                cells[ref] = val
            cols = [chr(ord('A') + i) for i in range(20)]
            for col in cols:
                print(f'{col}31: {cells.get(col + "31", "")}')
