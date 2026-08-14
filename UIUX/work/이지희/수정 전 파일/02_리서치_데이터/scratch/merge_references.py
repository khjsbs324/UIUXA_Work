import os
import re
import urllib.parse

path_200 = r"C:\UIUX이지희\Antigravity\자동화\02_리서치_데이터\01_기존_리서치\사이트 리서치\[리서치_데이터] 위케티_200개_사이트_레퍼런스.txt"
path_119 = r"C:\UIUX이지희\Antigravity\자동화\02_리서치_데이터\02_신규_리서치\[신규리서치]_위케티_레퍼런스_119.txt"
out_dir = r"C:\UIUX이지희\Antigravity\자동화\02_리서치_데이터\01_기존_리서치\사이트 리서치"
out_file = os.path.join(out_dir, "[리서치_데이터] 위케티_통합_사이트_레퍼런스.md")

def clean_url(url):
    url = url.strip()
    url = re.sub(r'^https?://', '', url, flags=re.IGNORECASE)
    url = re.sub(r'^www\.', '', url, flags=re.IGNORECASE)
    url = url.rstrip('/')
    return url.lower()

def clean_brand(name):
    name = re.sub(r'\(.*?\)', '', name)
    name = re.sub(r'[^a-zA-Z0-9가-힣]', '', name)
    return name.lower().strip()

# Parse File 1 (200개)
with open(path_200, 'r', encoding='utf-8') as f:
    text_200 = f.read()

# Parse sections
current_tier = "디자인+사용성 적합"
items_200 = []

blocks_200 = re.split(r'\n(?=\d+\.\s*브랜드명:)', text_200)

for block in blocks_200:
    if "[제1부]" in block or "디자인+사용성 적합" in block:
        current_tier = "디자인+사용성 적합"
    elif "[제2부]" in block or "사용성 적합" in block:
        current_tier = "사용성 적합"
    elif "[제3부]" in block or "디자인 적합" in block:
        current_tier = "디자인 적합"

    m_brand = re.search(r'브랜드명:\s*(.+)', block)
    m_url = re.search(r'웹사이트 주소:\s*(.+)', block)
    m_cat = re.search(r'카테고리:\s*(.+)', block)
    m_desc = re.search(r'브랜드 소개:\s*(.+)', block)
    m_mood = re.search(r'비주얼 무드:\s*(.+)', block)
    m_feat = re.search(r'주요 프론트엔드 기능:\s*(.+)', block)
    m_why = re.search(r'WICKETA 활용 이유:\s*(.+)', block)

    if m_brand and m_url:
        items_200.append({
            'source': '기존_200개',
            'brand': m_brand.group(1).strip(),
            'url': m_url.group(1).strip(),
            'category': m_cat.group(1).strip() if m_cat else '프리미엄 브랜드',
            'description': m_desc.group(1).strip() if m_desc else '',
            'visual_mood': m_mood.group(1).strip() if m_mood else '',
            'frontend_features': m_feat.group(1).strip() if m_feat else '',
            'wicketa_reason': m_why.group(1).strip() if m_why else '',
            'tier': current_tier
        })

print(f"Parsed {len(items_200)} items from 200 file")

# Parse File 2 (119개)
with open(path_119, 'r', encoding='utf-8') as f:
    text_119 = f.read()

blocks_119 = re.split(r'-{5,}\n\[SITE\s+\d+\]', text_119)
items_119 = []

for block in blocks_119:
    m_site = re.search(r'사이트명:\s*(.+)', block)
    m_url = re.search(r'URL:\s*(.+)', block)
    m_cat = re.search(r'카테고리:\s*(.+)', block)
    m_kw = re.search(r'주요 키워드:\s*(.+)', block)
    m_design = re.search(r'디자인 특징:\s*(.+)', block)
    m_ux = re.search(r'UX 특징:\s*(.+)', block)
    m_why = re.search(r'WICKETA 활용 이유 및 전략 태그:\s*(.+)', block)

    if m_site and m_url:
        design_str = m_design.group(1).strip() if m_design else ''
        ux_str = m_ux.group(1).strip() if m_ux else ''
        combined_feat = f"디자인: {design_str} | UX: {ux_str}" if design_str and ux_str else design_str or ux_str

        # Assign tier based on strategy tag or features
        why_str = m_why.group(1).strip() if m_why else ''
        if '전략 1' in why_str or '레이아웃' in why_str or '여백' in why_str:
            tier = "디자인 적합"
        elif '전략 2' in why_str or '시각화' in why_str or '전략 3' in why_str:
            tier = "디자인+사용성 적합"
        elif '전략 4' in why_str or '빌더' in why_str or '기능' in why_str:
            tier = "사용성 적합"
        else:
            tier = "디자인+사용성 적합"

        items_119.append({
            'source': '신규_119개',
            'brand': m_site.group(1).strip(),
            'url': m_url.group(1).strip(),
            'category': m_cat.group(1).strip() if m_cat else '프리미엄 브랜드',
            'description': m_kw.group(1).strip() if m_kw else '',
            'visual_mood': design_str,
            'frontend_features': ux_str,
            'wicketa_reason': why_str,
            'tier': tier
        })

print(f"Parsed {len(items_119)} items from 119 file")

# Deduplication
seen_urls = set()
seen_brands = set()
merged_items = []

duplicates_count = 0

for item in items_200 + items_119:
    c_u = clean_url(item['url'])
    c_b = clean_brand(item['brand'])

    if c_u in seen_urls or (c_b and c_b in seen_brands):
        duplicates_count += 1
        continue

    seen_urls.add(c_u)
    if c_b:
        seen_brands.add(c_b)
    merged_items.append(item)

print(f"Total merged unique items: {len(merged_items)} (Duplicates removed: {duplicates_count})")

# Categorize into 3 tiers
tier1 = [x for x in merged_items if x['tier'] == "디자인+사용성 적합"]
tier2 = [x for x in merged_items if x['tier'] == "사용성 적합"]
tier3 = [x for x in merged_items if x['tier'] == "디자인 적합"]

# Markdown output generation
md_lines = []
md_lines.append("# WICKETA (위케티) UI/UX 레퍼런스 통합 데이터베이스")
md_lines.append("")
md_lines.append(f"> **기존 200개 레퍼런스 및 신규 119개 레퍼런스 전수 교차 검증 및 중복 정제 병합본**  ")
md_lines.append(f"> **총 수록 브랜드 수**: {len(merged_items)}개 (중복 {duplicates_count}건 정제 완료)  ")
md_lines.append(f"> **작성 일시**: 2026-08-13  ")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📌 수집 및 분류 요약")
md_lines.append(f"- **[제1부] 디자인+사용성 적합 ({len(tier1)}개)**: 파스텔 여백, 몽환적 선/질감 표현과 커스텀 폼/인터랙션 UX 결합")
md_lines.append(f"- **[제2부] 사용성 적합 ({len(tier2)}개)**: 다이내믹 퀴즈 폼, 스티키 네비게이션, 브루잉 타이머, 실시간 시뮬레이터 UX")
md_lines.append(f"- **[제3부] 디자인 적합 ({len(tier3)}개)**: 시각적 여백 미학, 모듈러 그리드, 3D 오브제 회전 뷰, 에디토리얼 타이포그래피")
md_lines.append("")
md_lines.append("---")
md_lines.append("")

def render_tier(title, items):
    md_lines.append(f"## {title} (총 {len(items)}개)")
    md_lines.append("")
    for idx, item in enumerate(items, 1):
        md_lines.append(f"### {idx}. {item['brand']}")
        md_lines.append(f"- **웹사이트 주소**: [{item['url']}]({item['url']})")
        md_lines.append(f"- **카테고리**: {item['category']}")
        if item['description']:
            md_lines.append(f"- **브랜드 소개/키워드**: {item['description']}")
        if item['visual_mood']:
            md_lines.append(f"- **비주얼 무드 / 디자인 특징**: {item['visual_mood']}")
        if item['frontend_features']:
            md_lines.append(f"- **주요 프론트엔드 / UX 기능**: {item['frontend_features']}")
        if item['wicketa_reason']:
            md_lines.append(f"- **WICKETA 활용 이유 & 전략**: {item['wicketa_reason']}")
        md_lines.append("")

render_tier("[제1부] 디자인+사용성 적합", tier1)
render_tier("[제2부] 사용성 적합", tier2)
render_tier("[제3부] 디자인 적합", tier3)

with open(out_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(md_lines))

print(f"Successfully generated merged MD file at: {out_file}")

# Delete original TXT files if output file was created and is non-empty
if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
    if os.path.exists(path_200):
        os.remove(path_200)
        print(f"Deleted original file: {path_200}")
    if os.path.exists(path_119):
        os.remove(path_119)
        print(f"Deleted original file: {path_119}")
else:
    print("Error: Merged file creation failed or file too small!")
