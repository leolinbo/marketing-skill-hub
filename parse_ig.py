import re

file_path = r'C:/Users/HUAWEI/.gemini/antigravity/brain/25d52917-39ed-40f1-8753-da824e68d3f3/.system_generated/steps/55/output.txt'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

patterns = [
    ('biography', r'"biography":"([^"]+)"'),
    ('full_name', r'"full_name":"([^"]+)"'),
    ('category_name', r'"category_name":"([^"]+)"'),
    ('external_url', r'"external_url":"([^"]+)"'),
    ('og:description', r'<meta property="og:description" content="([^"]+)"'),
    ('og:title', r'<meta property="og:title" content="([^"]+)"'),
    ('title', r'<title>([^<]+)</title>')
]

for label, p in patterns:
    matches = re.findall(p, text)
    if matches:
        print(f"=== {label} ===")
        for m in set(matches[:5]):
            print(m)
