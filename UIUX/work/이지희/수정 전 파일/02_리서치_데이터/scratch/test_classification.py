import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ref_path = r'C:\UIUX이지희\Antigravity\새 리서치\[신규리서치]_위케티_레퍼런스_119.md'
anal_path = r'C:\UIUX이지희\Antigravity\새 리서치\신규리서치119_분석,분류.md'

with open(ref_path, 'r', encoding='utf-8') as f:
    ref_text = f.read()

with open(anal_path, 'r', encoding='utf-8') as f:
    anal_text = f.read()

# Parse site blocks
site_blocks_raw = re.split(r'##\s*\[SITE\s*(\d+)\]', ref_text)

site_dict = {}
for i in range(1, len(site_blocks_raw), 2):
    s_num = int(site_blocks_raw[i])
    s_content = site_blocks_raw[i+1].strip()
    
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
        'content': s_content
    }

# Parse table rows from anal_text
table_rows = {}
for line in anal_text.splitlines():
    if line.strip().startswith('| SITE '):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 7:
            s_id_str = parts[1]
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

# Helper to assign Strategy
def get_strategy_key(s_num):
    s_info = site_dict[s_num]
    t = s_info['tag']
    if '전략 1' in t or '전략1' in t:
        return '전략1_안식처_레이아웃'
    elif '전략 2' in t or '전략2' in t:
        return '전략2_공감각_시각화'
    elif '전략 3' in t or '전략3' in t:
        return '전략3_감정_진단_퀴즈'
    elif '전략 4' in t or '전략4' in t:
        return '전략4_심리스_빌더'
    return '기타'

# Helper to assign Domain Category
def get_domain_key(s_num):
    s_info = site_dict[s_num]
    c = s_info['cat']
    
    # Check site number ranges / specifics if defined, or string matching
    # 6 Domains:
    # 1. 현대 다도 & 프리미엄 티 리추얼 (38개)
    # 2. 니치 프래그런스 & 퍼퓸 하우스 (32개)
    # 3. 웰니스 스킨케어 & 보태니컬 아포테케리 (26개)
    # 4. 홈 프래그런스 & 센티드 캐멀 (10개)
    # 5. 기능성 음료 & 보태니컬 엘릭서 (7개)
    # 6. 라이프스타일 오브제 & 웰니스 (6개)

    if '기능성 음료' in c or '엘릭서' in c or s_num in [48]:
        return '도메인5_기능성_음료_및_보태니컬_엘릭서'
    elif '홈 프래그런스' in c or '센티드 캐멀' in c or '캐멀' in c or '캔들' in c or s_num in [7, 20, 54, 106, 107, 108, 109, 110, 111, 112, 113]:
        return '도메인4_홈_프래그런스_및_센티드_캐멀'
    elif '라이프스타일 오브제' in c or '오브제' in c or s_num in [8, 10, 16]:
        return '도메인6_라이프스타일_오브제_및_웰니스'
    elif '스킨케어' in c or '뷰티' in c or '보태니컬' in c or '아포테케리' in c or '스파' in c or '코스탈' in c or '생체' in c:
        return '도메인3_웰니스_스킨케어_및_보태니컬_아포테케리'
    elif '프래그런스' in c or '퍼퓸' in c or '향' in c or '조향' in c or '아로마' in c:
        return '도메인2_니치_프래그런스_및_퍼퓸_하우스'
    elif '티' in c or '다도' in c or '녹차' in c or '말차' in c or '차' in c:
        return '도메인1_현대_다도_및_프리미엄_티'
    else:
        return '도메인1_현대_다도_및_프리미엄_티'

# Check counts
strat_groups = {}
domain_groups = {}

for s_num in range(1, 120):
    sk = get_strategy_key(s_num)
    dk = get_domain_key(s_num)
    strat_groups.setdefault(sk, []).append(s_num)
    domain_groups.setdefault(dk, []).append(s_num)

print('=== Strategy Groups ===')
for k, v in strat_groups.items():
    print(f'{k}: {len(v)} sites -> {v[:5]}...')

print('\n=== Domain Groups ===')
for k, v in domain_groups.items():
    print(f'{k}: {len(v)} sites -> {v[:5]}...')
