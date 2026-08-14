import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

client_dir = r'C:\UIUX이지희\Antigravity\클라이언트 분석'

files = [f for f in os.listdir(client_dir) if f.endswith('.md')]

# Sort files numerically
def file_num(fname):
    m = re.search(r'\d+', fname)
    return int(m.group(0)) if m else 0

files.sort(key=file_num)

client_info = []

for fname in files:
    fpath = os.path.join(client_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Extract key metadata
    target_m = re.search(r'\*\*분석 대상\*\*:\s*`?\[?(.*?)\]?`?\s*$', text, re.MULTILINE)
    brand_m = re.search(r'\*\*브랜드명\*\*:\s*(.*)', text)
    topic_m = re.search(r'프로젝트의 중심 주제\*\*:\s*(.*)', text)
    title_m = re.search(r'#\s*(.*)', text)
    
    target = target_m.group(1).strip() if target_m else ''
    brand = brand_m.group(1).strip() if brand_m else ''
    topic = topic_m.group(1).strip() if topic_m else ''
    title = title_m.group(1).strip() if title_m else ''
    
    # First 5 lines snippet
    snippet = "\n".join([line for line in text.splitlines()[:10] if line.strip()])
    
    client_info.append({
        'orig_filename': fname,
        'num': file_num(fname),
        'target': target,
        'brand': brand,
        'topic': topic,
        'title': title,
        'snippet': snippet
    })

for info in client_info:
    print(f"=== {info['orig_filename']} ===")
    print(f"Title: {info['title']}")
    print(f"Target: {info['target']}")
    print(f"Brand: {info['brand']}")
    print(f"Topic: {info['topic']}")
    print(f"Snippet:\n{info['snippet']}\n")
