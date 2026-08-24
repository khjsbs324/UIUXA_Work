import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

anal_path = r'C:\UIUX이지희\Antigravity\새 리서치\신규리서치119_분석,분류.md'

with open(anal_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

table_cats = {}
for line in lines:
    if line.strip().startswith('| SITE '):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 7:
            s_id = parts[1]
            m = re.search(r'\d+', s_id)
            if m:
                s_num = int(m.group(0))
                c = parts[4]
                table_cats[s_num] = c

for s_num in range(1, 120):
    print(f'SITE {s_num:03d}: {table_cats.get(s_num, "MISSING")}')
