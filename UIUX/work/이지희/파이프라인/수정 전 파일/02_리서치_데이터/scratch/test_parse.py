import sys
import re
import os

sys.stdout.reconfigure(encoding='utf-8')

# Read full database 119
ref_path = r'C:\UIUX이지희\Antigravity\새 리서치\[신규리서치]_위케티_레퍼런스_119.md'
anal_path = r'C:\UIUX이지희\Antigravity\새 리서치\신규리서치119_분석,분류.md'

with open(ref_path, 'r', encoding='utf-8') as f:
    ref_text = f.read()

with open(anal_path, 'r', encoding='utf-8') as f:
    anal_text = f.read()

# Parse site blocks from ref_text
site_blocks_raw = re.split(r'##\s*\[SITE\s*(\d+)\]', ref_text)

site_dict = {}
for i in range(1, len(site_blocks_raw), 2):
    s_num = int(site_blocks_raw[i])
    s_content = site_blocks_raw[i+1].strip()
    
    # Extract fields
    name_m = re.search(r'-\s*\*\*사이트명\*\*:\s*(.*)', s_content)
    url_m = re.search(r'-\s*\*\*URL\*\*:\s*(.*)', s_content)
    cat_m = re.search(r'-\s*\*\*카테고리\*\*:\s*(.*)', s_content)
    tag_m = re.search(r'-\s*\*\*WICKETA 활용 이유 및 전략 태그\*\*:\s*\[(전략\s*\d[^\]]*)\]', s_content)
    
    name = name_m.group(1).strip() if name_m else f'SITE {s_num:03d}'
    url = url_m.group(1).strip() if url_m else ''
    cat = cat_m.group(1).strip() if cat_m else ''
    tag = tag_m.group(1).strip() if tag_m else ''
    
    site_dict[s_num] = {
        'num': s_num,
        'name': name,
        'url': url,
        'cat': cat,
        'tag': tag,
        'raw_block': f'## [SITE {s_num:03d}] {name}\n\n' + s_content
    }

# Also parse summary table from anal_text
table_rows = {}
for line in anal_text.splitlines():
    if line.strip().startswith('| SITE '):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 7:
            # | SITE 001 | **Bellocq Tea Atelier** | [url] | category | desc | tag |
            s_id_str = parts[1] # e.g. SITE 001
            m = re.search(r'\d+', s_id_str)
            if m:
                s_num = int(m.group(0))
                table_rows[s_num] = {
                    'name': parts[2].replace('**', ''),
                    'url': parts[3],
                    'cat': parts[4],
                    'desc': parts[5],
                    'tag': parts[6]
                }

print(f'Parsed {len(site_dict)} site details and {len(table_rows)} table rows.')
