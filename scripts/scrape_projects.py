import urllib.request
import re

url = 'https://jorebportfolio.my.canva.site/projects'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        
    # extract words
    matches = re.findall(r'([A-Z][a-zA-Z0-9\s]{4,40})', html)
    unique_titles = []
    for m in matches:
        m_s = m.strip()
        if any(w in m_s.lower() for w in ['bungalow', 'modern', 'residence', 'interior', 'dining', 'kitchen', 'bedroom', 'living', 'villa', 'apartment', 'minimalist', 'lighting', 'house']):
            if m_s not in unique_titles:
                unique_titles.append(m_s)
                
    print("Project titles found:")
    for ut in unique_titles[:20]:
        print(" -", ut)
        
except Exception as e:
    print("Error:", e)
