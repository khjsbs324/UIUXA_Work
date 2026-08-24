import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\UIUX이지희\Antigravity\새 리서치\[신규리서치]_위케티_레퍼런스_119.md', 'r', encoding='utf-8') as f:
    text = f.read()

site_blocks = re.split(r'##\s*\[SITE\s*(\d+)\]', text)

cats_dict = {}
tags_dict = {}

for i in range(1, len(site_blocks), 2):
    s_num = int(site_blocks[i])
    s_content = site_blocks[i+1]
    
    cat_m = re.search(r'-\s*\*\*카테고리\*\*:\s*(.*)', s_content)
    tag_m = re.search(r'-\s*\*\*WICKETA 활용 이유 및 전략 태그\*\*:\s*\[(전략\s*\d[^\]]*)\]', s_content)
    
    cat = cat_m.group(1).strip() if cat_m else 'Unknown'
    tag = tag_m.group(1).strip() if tag_m else 'Unknown'
    
    cats_dict.setdefault(cat, []).append(s_num)
    tags_dict.setdefault(tag, []).append(s_num)

print('=== Unique Category Values in 119 Sites ===')
for k, v in cats_dict.items():
    print(f'Category: "{k}" -> {len(v)} sites')

print('\n=== Unique Strategy Tag Values in 119 Sites ===')
for k, v in tags_dict.items():
    print(f'Strategy: "{k}" -> {len(v)} sites')
