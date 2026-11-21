import urllib.request
import re
import json

url = 'https://jorebportfolio.my.canva.site/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        
    print("Page length:", len(html))
    
    # Save raw html for analysis
    with open('canva_raw.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    # Search for all strings inside json
    texts = re.findall(r'"([^"]{10,120})"', html)
    relevant = [t for t in texts if any(k in t.lower() for k in ['architect', 'interior', 'project', 'design', 'contact', 'email', 'phone', 'joreb', 'studio', 'portfolio', 'house', 'cafe', 'villa'])]
    print("Relevant strings found:", len(relevant))
    for r in relevant[:25]:
        print(" >", r)
        
    emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html))
    print("Emails:", emails)
    
except Exception as e:
    print("Error:", e)
