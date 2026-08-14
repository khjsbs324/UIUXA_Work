import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

client_dir = r'C:\UIUX이지희\Antigravity\클라이언트 분석'

files = [f for f in os.listdir(client_dir) if f.endswith('.md')]

def file_num(fname):
    m = re.search(r'\d+', fname)
    return int(m.group(0)) if m else 0

files.sort(key=file_num)

for fname in files:
    fpath = os.path.join(client_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    target_m = re.search(r'\*\*분석 대상\*\*:\s*`?\[?(.*?)\]?`?\s*$', text, re.MULTILINE)
    brand_m = re.search(r'\*\*브랜드명\*\*:\s*(.*)', text)
    topic_m = re.search(r'프로젝트의 중심 주제\*\*:\s*(.*)', text)
    
    target = target_m.group(1).strip() if target_m else ''
    brand = brand_m.group(1).strip() if brand_m else ''
    topic = topic_m.group(1).strip() if topic_m else ''
    
    print(f"[{file_num(fname):02d}] {fname} -> Target: {target} | Topic: {topic[:40]}...")
