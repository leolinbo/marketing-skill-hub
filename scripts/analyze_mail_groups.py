import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
extracted_dir = r'D:\marketing\extracted_mail_groups'

series_list = sorted(os.listdir(extracted_dir))

for s in series_list:
    s_path = os.path.join(extracted_dir, s)
    if not os.path.isdir(s_path):
        continue
    txt_files = [f for f in os.listdir(s_path) if f.endswith('.txt')]
    print(f"==================================================")
    print(f"SERIES: {s} (Total docs: {len(txt_files)})")
    print(f"==================================================")
    for tf in txt_files:
        with open(os.path.join(s_path, tf), 'r', encoding='utf-8', errors='ignore') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        subj = [l for l in lines if 'subject' in l.lower() and len(l) < 150]
        print(f"  File: {tf}")
        if subj:
            print(f"    Subject: {subj[0]}")
        # print first 2 key points
        key_lines = [l for l in lines[1:10] if len(l) > 20][:3]
        for kl in key_lines:
            print(f"    - {kl[:120]}")
    print()
