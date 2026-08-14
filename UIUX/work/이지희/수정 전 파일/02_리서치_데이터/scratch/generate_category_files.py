import sys
import re
import os

sys.stdout.reconfigure(encoding='utf-8')

ref_path = r'C:\UIUX이지희\Antigravity\새 리서치\[신규리서치]_위케티_레퍼런스_119.md'
anal_path = r'C:\UIUX이지희\Antigravity\새 리서치\신규리서치119_분석,분류.md'
output_dir = r'C:\UIUX이지희\Antigravity\새 리서치'

with open(ref_path, 'r', encoding='utf-8') as f:
    ref_text = f.read()

with open(anal_path, 'r', encoding='utf-8') as f:
    anal_text = f.read()

# Parse site blocks from ref_text
site_blocks_raw = re.split(r'##\s*\[SITE\s*(\d+)\]', ref_text)

sites = {}
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
    
    sites[s_num] = {
        'num': s_num,
        'name': name,
        'url': url,
        'cat': cat,
        'tag': tag,
        'content': s_content
    }

# Parse table rows from anal_text for summary tables
table_data = {}
for line in anal_text.splitlines():
    if line.strip().startswith('| SITE '):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 7:
            s_id_str = parts[1]
            m = re.search(r'\d+', s_id_str)
            if m:
                s_num = int(m.group(0))
                table_data[s_num] = {
                    'id': f'SITE {s_num:03d}',
                    'name': parts[2],
                    'url': parts[3],
                    'cat': parts[4],
                    'desc': parts[5],
                    'tag': parts[6]
                }

# Strategy categorization
strategy_groups = {
    '전략1_안식처_레이아웃': {
        'title': '전략 1: 안식처 레이아웃 (Sanctuary Layout)',
        'filename': '신규리서치119_전략1_안식처_레이아웃.md',
        'desc': '몽환적 파스텔 오라 배경, 0.5px 미세 구분선 및 1.5:2.5 비대칭 에디토리얼 그리드를 통해 고요하고 평온한 시각적 안식을 제공하는 사이트 모음.',
        'sites': []
    },
    '전략2_공감각_시각화': {
        'title': '전략 2: 공감각 시각화 (Sensory Visualization)',
        'filename': '신규리서치119_전략2_공감각_시각화.md',
        'desc': '차의 맛과 향 파라미터를 비주얼 아로마 휠, 파스텔 수색 그래디언트 애니메이션, 테이스팅 게이지 슬라이더로 시각화한 사이트 모음.',
        'sites': []
    },
    '전략3_감정_진단_퀴즈': {
        'title': '전략 3: 감정 진단 퀴즈 (Emotional Diagnosis Quiz)',
        'filename': '신규리서치119_전략3_감정_진단_퀴즈.md',
        'desc': '"오늘 하루 어땠나요?" 3단계 내면 상태 감정 진단 퀴즈 폼, 무드 파인더 및 스마트 큐레이션 인터랙션을 제공하는 사이트 모음.',
        'sites': []
    },
    '전략4_심리스_빌더': {
        'title': '전략 4: 심리스 빌더 (Seamless Custom Builder)',
        'filename': '신규리서치119_전략4_심리스_빌더.md',
        'desc': 'DIY 기프트 커스텀 폼, 라이브 이니셜 각인 미리보기 시뮬레이터, 정기구독 슬라이딩 및 슬라이드아웃 Cart Drawer를 제공하는 사이트 모음.',
        'sites': []
    }
}

for s_num in range(1, 120):
    s_info = sites[s_num]
    t = s_info['tag']
    if '전략 1' in t or '전략1' in t:
        strategy_groups['전략1_안식처_레이아웃']['sites'].append(s_num)
    elif '전략 2' in t or '전략2' in t:
        strategy_groups['전략2_공감각_시각화']['sites'].append(s_num)
    elif '전략 3' in t or '전략3' in t:
        strategy_groups['전략3_감정_진단_퀴즈']['sites'].append(s_num)
    elif '전략 4' in t or '전략4' in t:
        strategy_groups['전략4_심리스_빌더']['sites'].append(s_num)

# Domain categorization (6 domains)
domain_groups = {
    '도메인1_현대다도_프리미엄티': {
        'title': '도메인 1: 현대 다도 & 프리미엄 티 리추얼',
        'filename': '신규리서치119_도메인1_현대다도_프리미엄티.md',
        'desc': '현대적 다도 문화, 프리미엄 잎차, 말차 리추얼 및 오가닉 티 브랜딩 벤치마킹 사이트 모음.',
        'sites': []
    },
    '도메인2_니치프래그런스_퍼퓸하우스': {
        'title': '도메인 2: 니치 프래그런스 & 퍼퓸 하우스',
        'filename': '신규리서치119_도메인2_니치프래그런스_퍼퓸하우스.md',
        'desc': '감각적 니치 향수, 퍼퓸 아카이브, 올팩토리 올웨이즈 스토리텔링 벤치마킹 사이트 모음.',
        'sites': []
    },
    '도메인3_웰니스스킨케어_보태니컬아포테케리': {
        'title': '도메인 3: 웰니스 스킨케어 & 보태니컬 아포테케리',
        'filename': '신규리서치119_도메인3_웰니스스킨케어_보태니컬아포테케리.md',
        'desc': '자연주의 아포테케리, 생체 리듬 맞춤 스킨케어, 웰니스 리추얼 벤치마킹 사이트 모음.',
        'sites': []
    },
    '도메인4_홈프래그런스_센티드캐멀': {
        'title': '도메인 4: 홈 프래그런스 & 센티드 캐멀',
        'filename': '신규리서치119_도메인4_홈프래그런스_센티드캐멀.md',
        'desc': '공간 디퓨저, 센티드 캔들, 아로마 테라피 라이프스타일 벤치마킹 사이트 모음.',
        'sites': []
    },
    '도메인5_기능성음료_보태니컬엘릭서': {
        'title': '도메인 5: 기능성 음료 & 보태니컬 엘릭서',
        'filename': '신규리서치119_도메인5_기능성음료_보태니컬엘릭서.md',
        'desc': '무알콜 에디토리얼 음료, 보태니컬 엘릭서, 믹솔로지 게이지 벤치마킹 사이트 모음.',
        'sites': []
    },
    '도메인6_라이프스타일오브제_웰니스': {
        'title': '도메인 6: 라이프스타일 오브제 & 웰니스',
        'filename': '신규리서치119_도메인6_라이프스타일오브제_웰니스.md',
        'desc': '티 세라믹, 감각적 아티스틱 오브제, 바스 리추얼 벤치마킹 사이트 모음.',
        'sites': []
    }
}

for s_num in range(1, 120):
    s_info = sites[s_num]
    c = s_info['cat']
    
    if s_num in [48, 117, 118]:
        domain_groups['도메인5_기능성음료_보태니컬엘릭서']['sites'].append(s_num)
    elif s_num in [7, 20, 21, 54, 106, 107, 108, 109, 110, 111, 112, 113, 114]:
        domain_groups['도메인4_홈프래그런스_센티드캐멀']['sites'].append(s_num)
    elif s_num in [8, 10, 16, 36]:
        domain_groups['도메인6_라이프스타일오브제_웰니스']['sites'].append(s_num)
    elif s_num in [6, 11, 13, 15, 19, 39, 43, 46, 47, 57, 58, 59, 94, 95, 99, 103]:
        domain_groups['도메인3_웰니스스킨케어_보태니컬아포테케리']['sites'].append(s_num)
    elif s_num in [5, 9, 12, 17, 22, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 44, 45, 55, 56, 77, 81, 82]:
        domain_groups['도메인2_니치프래그런스_퍼퓸하우스']['sites'].append(s_num)
    else:
        domain_groups['도메인1_현대다도_프리미엄티']['sites'].append(s_num)

# Helper to build Markdown content for a group
def generate_md_for_group(group_key, group_data, cat_type='전략'):
    s_list = group_data['sites']
    title = group_data['title']
    desc = group_data['desc']
    
    md = []
    md.append(f"# 📂 [신규리서치119] {title}")
    md.append("")
    md.append(f"> **프로젝트**: WICKETA (위케티) 브랜드 UI/UX 신규 레퍼런스 카테고리별 세분화 파일")
    md.append(f"> **분류 기준**: {cat_type} 카테고리 - {title}")
    md.append(f"> **포함 사이트 수**: **총 {len(s_list)}개 사이트**")
    md.append(f"> **카테고리 설명**: {desc}")
    md.append("")
    md.append("---")
    md.append("")
    md.append(f"## 📊 1. {title} - 포함 사이트 요약 목록 ({len(s_list)}개)")
    md.append("")
    md.append("| SITE ID | 사이트명 | URL | 원본 카테고리 | 주요 비주얼 & UX 특징 | WICKETA 전략 태그 |")
    md.append("|:---:|:---|:---|:---|:---|:---|")
    
    for s_num in s_list:
        t_info = table_data.get(s_num, {})
        s_info = sites[s_num]
        s_id = f"SITE {s_num:03d}"
        s_name = t_info.get('name', s_info['name'])
        s_url = t_info.get('url', s_info['url'])
        s_cat = t_info.get('cat', s_info['cat'])
        s_desc = t_info.get('desc', '')
        s_tag = t_info.get('tag', s_info['tag'])
        md.append(f"| {s_id} | {s_name} | {s_url} | {s_cat} | {s_desc} | {s_tag} |")
    
    md.append("")
    md.append("---")
    md.append("")
    md.append(f"## 🔍 2. {title} - 사이트별 상세 레퍼런스 분석 정보")
    md.append("")
    
    for s_num in s_list:
        s_info = sites[s_num]
        md.append(f"## [SITE {s_num:03d}] {s_info['name']}")
        md.append("")
        md.append(s_info['content'])
        md.append("")
        md.append("---")
        md.append("")
        
    return "\n".join(md)

# Generate Strategy files
for g_key, g_data in strategy_groups.items():
    f_name = g_data['filename']
    f_path = os.path.join(output_dir, f_name)
    content = generate_md_for_group(g_key, g_data, cat_type="4대 UI/UX 설계 전략")
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {f_name} ({len(g_data['sites'])} sites)")

# Generate Domain files
for g_key, g_data in domain_groups.items():
    f_name = g_data['filename']
    f_path = os.path.join(output_dir, f_name)
    content = generate_md_for_group(g_key, g_data, cat_type="6대 산업 도메인")
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {f_name} ({len(g_data['sites'])} sites)")

print("\nAll 10 category files generated successfully!")
