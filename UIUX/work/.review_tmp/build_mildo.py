from mildo_dom import *
import re, base64, json, itertools
from collections import Counter

raw=SOURCE.read_text(encoding='utf-8')
doc=Parser(raw).root
body=doc.find(tag='body'); body.attrs['id']='top'
head=doc.find(tag='head')
scripts='\n'.join(n.text() for n in doc.nodes() if n.tag=='script')
def detach(n):
    if n.parent: n.parent.children.remove(n)
    n.parent=None
    return n
def wrap(n, tag='div', cls=''):
    p=n.parent; i=p.children.index(n); w=Node(tag,{'class':cls}); p.children[i]=w; w.parent=p; w.add(n); return w
def add_start(n,c):
    n.children.insert(0,c); c.parent=n
def box(cls,*children):
    n=Node('div',{'class':cls})
    for c in children: n.add(detach(c) if isinstance(c,Node) and c.parent else c)
    return n
def photo(scene, alt):
    return Node('div',{'class':'editorial-photo scene-'+str(scene),'role':'img','aria-label':alt})
def note(n, label='화보 구성과 원본 설명'):
    w=wrap(n,'details','production-notes')
    add_start(w,Node('summary',children=[label]))
    n.addclass('original-direction'); n.attrs.pop('style',None)
    return w
def linkify(n, href):
    n.tag='a'; n.attrs['href']=href; n.attrs.pop('type',None)

# Retain the source's complete body copy. Discard executable code and obsolete styling only.
for n in list(doc.nodes()):
    if n.tag in ('script','style'):
        detach(n); continue
    if n.tag=='#comment':
        detach(n); continue
    old=n.attrs.get('style','')
    declarations={p.split(':',1)[0].strip():p.split(':',1)[1].strip() for p in old.split(';') if ':' in p}
    # Reuse meaningful spacing while replacing the wireframe's visual treatment.
    for key in list(declarations):
        if key in ('background','background-color','background-image','color','font-family','font-weight','border-radius','box-shadow','backdrop-filter','transition','transform') or key.startswith('border'):
            declarations.pop(key,None)
    if 'font-size' in declarations:
        match=re.fullmatch(r'([\d.]+)px',declarations['font-size'])
        if match:
            size=float(match[1])
            if size<12: declarations['font-size']='12px'
            elif size<15: declarations['font-size']='14px'
    if declarations: n.attrs['style']=';'.join(k+':'+v for k,v in declarations.items())
    else: n.attrs.pop('style',None)
    handler=n.attrs.get('onclick','')
    for a in list(n.attrs):
        if a.lower().startswith('on'): del n.attrs[a]
    if 'addToCart' in handler:
        title=re.search(r"addToCart\('([^']+)'",handler)[1]
        index={'01. 유자 청송':1,'04. 적송 홍화':2,'08. 백단 묵향':3,'밀도 3종 디스커버리 킷':4}[title]
        n.tag='label'; n.attrs.pop('type',None); n.attrs['for']='cart'+str(index); n.addclass('add-to-cart')
    elif 'openDiagnosisModal' in handler: linkify(n,'#diagnosisModal')
    elif 'toggleCartDrawer' in handler: linkify(n,'#cartDrawer')
    elif 'openPackagingModal' in handler: linkify(n,'#packagingModal')
    elif 'openAtelierModal' in handler: linkify(n,'#atelierModal')
    elif 'openVipPreorderModal' in handler: linkify(n,'#vipPreorderModal')
    elif 'openUserMenuModal' in handler: linkify(n,'#userMenuModal')
    elif 'close' in handler:
        if n.tag=='button': linkify(n,'#close'); n.addclass('close-link'); n.attrs['aria-label']='닫기'
    elif 'clearCart' in handler:
        n.attrs.update({'type':'reset','form':'cartState'})
    elif 'checkoutOrder' in handler: linkify(n,'#previewNotice')
    elif 'restartQuiz' in handler: n.attrs.update({'type':'reset','form':'quizForm'})
    elif 'location.href' in handler and n.tag=='button':
        target=re.search(r'targetProd=p(\d+)',handler)
        linkify(n,{'1':'#story-1','4':'#story-2','8':'#story-3','15':'#discovery'}.get(target[1] if target else '', '#catalog'))
    if n.tag=='a':
        href=n.attrs.get('href','')
        label=' '.join(n.text().split())
        if '메인_페이지.html' in href: n.attrs['href']='#top'
        elif '브랜드_소개.html' in href:
            n.attrs['href']='#perfumery-process' if 'safe' in href or 'ingredient' in href else '#manifesto'
        elif '카테고리.html' in href:
            target=re.search(r'targetProd=p(\d+)',href)
            n.attrs['href']={'1':'#story-1','4':'#story-2','8':'#story-3','15':'#discovery','16':'#vipPreorderModal'}.get(target[1] if target else '', '#catalog')
        if n.attrs.get('title')=='디스커버리 킷 보러가기' or ('크레딧' in label and n.attrs.get('href')=='#catalog'): n.attrs['href']='#discovery'
        if '한국 자연 원료' in label or '안전 조향' in label: n.attrs['href']='#perfumery-process'
        if '3단계 레이어링 리추얼' in label: n.attrs['href']='#layering-guide'
        if '휴대용 마패 오브제' in label: n.attrs['href']='#story-3'
    if n.tag=='form':
        # Static mock-up forms must never send names/phone numbers to any endpoint.
        n.tag='div'; n.attrs.pop('action',None); n.attrs.pop('method',None)
        for btn in n.nodes():
            if btn.tag=='button' and btn.attrs.get('type')=='submit': linkify(btn,'#previewNotice')

head.find(tag='title').children=['밀도 MILDO | 향의 밀도, 일상의 기품']
head.add(Node('meta',{'name':'description','content':'조선 마패의 기품에서 출발한 밀도. 세 단계 향 선택 체계와 나만의 레이어링, 오래 곁에 두는 공예 오브제를 만나보세요.'}))
head.add(Node('#comment',children=['\n강사 제작예시 · 2026-09-09\n원본: ../와이어프레임/와이어프레임_시안7_최종.html\n디자인 레퍼런스: 레퍼런스1.txt [메인 페이지], https://www.aesop.com/ 및 https://kr.aesop.com/\n반영: 크림색 바탕, 차콜 헤더·푸터, 넓은 여백, 교차형 사진·설명 분할, 절제된 타이포그래피, 사각 아웃라인 버튼, 상품 진열.\n이미지: built-in imagegen으로 생성한 MILDO 콘셉트 화보. 제품의 실제 사진이 아닌 디자인 예시.\n최종 프롬프트 요약 1: 한국 서재 자연광, 가죽 가방 스트랩에 결착된 황동 마패 캡과 MILDO 앰버 향수 보틀, 왼쪽 카피 여백.\n최종 프롬프트 요약 2: 3×2 이미지 아틀라스, 유자·솔잎 20ml / 홍화·적송 50ml / 백단·먹 75ml / 3종 시향 키트 / 황동 공예 손 / 한옥 조향 아틀리에.\nCSS·이미지는 이 파일 안에 포함. 외부 네트워크, JavaScript, 라이브러리 불필요.\n원본의 화보 연출 문구는 각 화보 아래 details에 보존. 진단 4문항과 6가지 결과는 정적 HTML 및 CSS로 변환.\n신청·결제는 정보 전송 없는 디자인 예시. 원본의 기획 가격 및 운영 검토 문구 유지.\n']))

# Header: quiet, two-level centered masthead.
gnb=body.find(cls='gnb-grid')
gnb.add(fragment('<span class="header-location">SEOUL, KOREA<br>HERITAGE &amp; PERFUMERY</span>'))
user=body.find(cls='user-menu-btn'); user.attrs['aria-label']='사용자 메뉴 열기'
gnb.find(cls='gnb-nav').add(fragment('<a class="gnb-link" href="#discovery">디스커버리 킷</a>'))
gnb.find(cls='gnb-nav').add(fragment('<a class="gnb-link" href="#atelier-booking">선물과 아틀리에</a>'))

# Hero is a single full-width photograph with the entire original lead text.
hero=body.find(cls='hero-cinematic-stage'); hero.attrs={'id':'hero','class':'hero-cinematic-stage'}
hero_text=detach(hero.find(cls='hero-text-col')); hero_visual=detach(hero.find(cls='hero-visual-col'))
hero_text.find(tag='p').addclass('hero-main-desc')
hero_text.elements()[-1].addclass('hero-trust-bar')
seal=hero.elements()[0].find(tag='div'); seal=detach(seal); seal.attrs={'class':'hero-seal'}
hero.children=[]
hero.add(fragment('<div class="hero-photo" role="img" aria-label="가죽 가방에 결착된 황동 마패 보틀, 한국 서재의 오후 자연광"></div>'))
hero.add(box('container hero-layout',hero_text)); hero.add(seal)
hero.add(fragment('<a class="hero-scroll" href="#manifesto">SCROLL TO DISCOVER <span>↓</span></a>'))
archive=Node('details',{'class':'production-notes hero-production'})
archive.add(Node('summary',children=['마패 보틀 화보 · 원본 연출 설명']))
archive.add(hero_visual)
body.children.insert(body.children.index(hero)+1,archive); archive.parent=body

# Brand manifesto: full image at left, unboxed three-part narrative at right.
manifesto=body.find(id='manifesto'); grid=manifesto.find(cls='grid-2'); grid.attrs={'class':'manifesto-layout'}
text_col,visual_col=grid.elements(); text_col.addclass('editorial-copy'); visual_col.addclass('manifesto-visual')
for w in list(visual_col.nodes()):
    if w.cls('wireframe-box'): note(w)
add_start(visual_col,photo(5,'장인의 손끝에서 다듬어지는 황동 마패의 섬세한 결'))
grid.children=[visual_col,text_col]
answers=text_col.elements()[-1]; answers.addclass('manifesto-answers')

# Three levels: comparable open columns with fine horizontal rules.
system=body.find(id='mapae-system'); levels=[n for n in system.nodes() if n.cls('signature-row-grid')]
levels[0].parent.attrs={'class':'level-comparison'}
for i,n in enumerate(levels,1):
    n.attrs={'class':'signature-row-grid level-card level-'+str(i)}
    add_start(n,Node('div',{'class':'level-index'},[f'0{i}']))
    for ch in n.elements()[1:]: ch.attrs.pop('style',None)
levels[0].parent.elements()[-1].attrs={'class':'level-footnote'}

# Signature stories: retain every note, price, specification and layering step.
for i in range(1,4):
    sec=body.find(id='story-'+str(i)); sec.addclass('signature-story')
    container=sec.find(cls='container'); nodes=container.elements(); intro=nodes[0]
    intro.attrs={'class':'signature-intro'}
    copy=box('editorial-copy',*list(intro.elements()))
    visual=box('story-photo',photo(i,['유자 청송, 청유자와 솔잎의 맑은 아침','적송 홍화, 붉은 꽃잎과 깊은 적송의 향','백단 묵향, 놋쇠 마패와 선비 서재의 묵향'][i-1]))
    intro.children=[]; intro.add(visual); intro.add(copy)
    if i==1:
        second=nodes[1]; left,right=second.elements()
        left.addclass('scent-experience'); copy.add(detach(left))
        visual.add(detach(right)); right.attrs={'class':'story-source-notes'}
        note(right,'유자 청송 화보 · 원본 연출 설명')
        detach(second)
    if i==2:
        nodes[1].attrs={'class':'grid-2 ingredient-notes'}
        for n in nodes[1].elements():
            n.attrs={'class':'ingredient-panel'}
            for e in n.elements():
                if len(e.text().strip())==2 and not e.elements(): e.attrs={'class':'ingredient-character'}
        nodes[2].attrs={'class':'layering-guide','id':'layering-guide'}
        nodes[2].find(cls='grid-3').addclass('layering-steps')
    if i==3:
        nodes[1].attrs={'class':'modular-guide'}
        nodes[1].find(cls='grid-4').addclass('modular-parts')
        nodes[2].attrs={'class':'grid-2 object-specs'}
        diagrams=[
            '<rect x="79" y="20" width="22" height="16" rx="2"/><path d="M78 36V48C58 54 51 66 51 89C51 117 66 131 90 131S129 117 129 89C129 66 122 54 102 48V36Z"/><rect x="66" y="76" width="48" height="29"/><path d="M75 113H105M88 20V12H109V17"/>',
            '<ellipse cx="90" cy="44" rx="34" ry="11"/><path d="M56 44V105C56 120 124 120 124 105V44M60 97C60 110 120 110 120 97M60 104C60 117 120 117 120 104"/><path d="M72 51V91M108 51V91"/>',
            '<circle cx="90" cy="72" r="40"/><circle cx="90" cy="72" r="33"/><path d="M55 96V107C55 125 125 125 125 107V96M73 83L80 70L77 58L87 64L100 63L109 73L103 84M80 70L98 76L103 84M79 76L77 91M96 78L93 91"/>',
            '<ellipse cx="90" cy="112" rx="45" ry="13"/><path d="M45 111V120C45 138 135 138 135 120V111M90 111L106 46M104 33C92 19 117 20 107 7M78 137H145"/><ellipse cx="90" cy="111" rx="4" ry="2"/>'
        ]
        for ni,part in enumerate(nodes[1].find(cls='modular-parts').elements()):
            add_start(part,fragment('<svg class="module-drawing" viewBox="0 0 180 150" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true">'+diagrams[ni]+'</svg>'))
            source_caption=part.find(cls='wireframe-box')
            note(source_caption,'원본 이미지 구성 보기')

process=body.find(id='perfumery-process'); process_grid=process.find(cls='grid-4')
process_grid.attrs={'class':'process-steps'}
for i,n in enumerate(process_grid.elements(),1):
    n.attrs={'class':'process-step'}
    add_start(n,Node('span',{'class':'process-index'},[f'0{i}']))
process.find(cls='container').add(box('process-layout',photo(5,'황동 마패를 다듬는 장인의 손과 공예 과정'),process_grid))

discovery=body.find(id='discovery'); discovery.find(cls='discovery-grid').attrs={'class':'discovery-grid'}
dvisual=discovery.find(cls='discovery-visual-col'); dvisual.attrs={'class':'discovery-visual-col'}
old_children=list(dvisual.children); dvisual.children=[]; dvisual.add(photo(4,'한지 시향 카드와 세 가지 향이 담긴 밀도 디스커버리 키트'))
caption=Node('div',{'class':'photo-caption'},old_children); dvisual.add(caption)

products=[n for n in body.nodes() if n.cls('product-card')]
for i,n in enumerate(products,1):
    n.attrs={'class':'product-card','id':'featured-'+str(i)}
    thumb=n.find(cls='product-card-thumb'); thumb.attrs={'class':'product-card-thumb'}
    cap=Node('div',{'class':'product-caption'},list(thumb.children)); thumb.children=[]
    thumb.add(photo(i,'밀도 '+['유자 청송 20ml','적송 홍화 50ml','백단 묵향 75ml','3종 디스커버리 킷'][i-1])); thumb.add(cap)

atelier=body.find(id='atelier-booking'); services=atelier.find(cls='grid-2'); services.attrs={'class':'service-list'}
for i,n in enumerate(services.elements()):
    n.attrs={'class':'service-row'}
    content=box('editorial-copy',*list(n.elements())); n.children=[]
    n.add(photo(7 if i==0 else 6,'능화창 문양 상자와 붉은 한지 띠지, 황동 노리개를 더한 옥색 보자기 포장' if i==0 else '차분한 한옥 공간의 프라이빗 조향 아틀리에'))
    n.add(content)

epilogue=body.find(id='epilogue'); epilogue.attrs={'id':'epilogue','class':'epilogue'}
epilogue.find(cls='container').attrs={'class':'container epilogue-inner'}
epilogue.find(cls='container').elements()[3].attrs={'class':'epilogue-paths'}
for n in epilogue.find(cls='epilogue-paths').elements(): n.attrs={'class':'epilogue-path'}

# Native fragment dialogs. Every original hidden panel stays accessible.
for modal_id in ['diagnosisModal','packagingModal','vipPreorderModal','atelierModal','userMenuModal']:
    n=body.find(id=modal_id); n.attrs={'id':modal_id,'class':'css-modal','role':'dialog','aria-label':{'diagnosisModal':'나만의 마패 향 찾기','packagingModal':'선물 포장 선택','vipPreorderModal':'VIP 사전 오픈 알림','atelierModal':'아틀리에 사전 오픈 알림','userMenuModal':'사용자 메뉴'}[modal_id]}
    n.elements()[0].attrs={'class':'modal-sheet'}
    n.elements()[0].add(fragment('<a class="modal-bottom-close" href="#close">닫고 돌아가기 ↑</a>'))
for form_id in ['vipPreorderForm','atelierAlertForm']:
    form=body.find(id=form_id)
    add_start(form,fragment('<p class="form-notice">디자인 예시입니다. 입력한 정보는 저장하거나 전송하지 않습니다.</p>'))
    for n in form.nodes():
        if n.tag=='button' and n.attrs.get('type')=='submit': linkify(n,'#previewNotice')

# Four-question diagnosis and every recommendation branch from the source script.
quiz=body.find(id='quizOptions'); quiz.tag='form'; quiz.attrs={'id':'quizForm','class':'quiz-form'}
questions=re.findall(r'q:\s*"([^"]+)"',scripts[:scripts.index('let currentStep')])
options=re.findall(r'\{ text: "([^"]+)", score: "([^"]+)", kw: "([^"]+)" \}',scripts[:scripts.index('let currentStep')])
for qi,q in enumerate(questions):
    field=Node('fieldset'); field.add(Node('legend',children=[q]))
    for oi,(txt,score,kw) in enumerate(options[qi*3:qi*3+3],1):
        field.add(fragment(f'<label class="quiz-option"><input type="radio" id="q{qi+1}a{oi}" name="q{qi+1}" value="{oi}" required><span>{escape(txt)}</span></label>'))
    quiz.add(field)
quiz.add(fragment('<a class="btn-black" href="#quizResultContainer">나를 위한 마패 조향 처방전 확인 →</a>'))
result=body.find(id='quizResultContainer'); result.attrs={'id':'quizResultContainer','class':'quiz-result'}
result_intro=fragment('<p class="quiz-incomplete">네 가지 문항을 모두 선택하면 추천 향과 레이어링 방법이 나타납니다.</p>'); add_start(result,result_intro)
# Keep original default result text as a reading reference, while presenting all computed alternatives.
original=Node('details',{'class':'production-notes result-original'}); original.add(Node('summary',children=['대표 처방 예시 · 유자 청송']))
for n in list(result.children):
    if n is result_intro: continue
    original.add(detach(n) if isinstance(n,Node) else n)
    if not isinstance(n,Node): result.children.remove(n)
result.add(original)
branches=re.findall(r"getElementById\('resultBadge'\)\.className =.*?(?=\n\s*\} else|\n\s*\}\n\s*\})",scripts,re.S)[:6]
for bi,branch in enumerate(branches):
    card=Node('article',{'class':'diagnosis-answer answer-'+str(bi)})
    for field,tag in [('resultBadge','span'),('resultSubBadge','small'),('resultTitle','h3'),('resultReasonText','p'),('resultDesc','p'),('resultLayering','p'),('resultProductLink','a')]:
        match=re.search(r"getElementById\('"+field+r"'\)\.innerText = (['`])(.*?)\1;",branch,re.S)
        if match:
            txt=match[2].replace('${kwTime}','선택한 시간대').replace('${kwDensity}','선택한 향의 밀도')
            attrs={'class':'result-'+field}
            if tag=='a': attrs['href']='#'+('story-2' if bi in (1,4) else 'story-3' if bi==5 else 'story-1')
            card.add(Node(tag,attrs,[txt]))
    result.add(card)
result.add(fragment('<button type="reset" form="quizForm" class="btn-outline">다시 선택하기</button>'))

# CSS-only cart: one selectable unit per featured product, all 16 combinations calculated at build time.
state=Node('form',{'id':'cartState','class':'state-controls','aria-label':'대표 상품 선택'})
for i in range(1,5): state.add(Node('input',{'type':'checkbox','id':'cart'+str(i),'name':'cart'+str(i),'aria-label':['유자 청송 담기','적송 홍화 담기','백단 묵향 담기','디스커버리 킷 담기'][i-1]}))
add_start(body,state)
cart=body.find(id='cartDrawer'); cart.attrs={'id':'cartDrawer','class':'css-modal cart-modal','role':'dialog','aria-label':'선택 상품 장바구니'}
cart_children=list(cart.children); cart.children=[]; cart.add(Node('div',{'class':'modal-sheet cart-sheet'},cart_children))
body.find(id='cartDrawerBackdrop').attrs={'id':'cartDrawerBackdrop','hidden':None}
body.find(id='drawerItemList').attrs={'id':'drawerItemList'}
names=['01. 유자 청송','04. 적송 홍화','08. 백단 묵향','밀도 3종 디스커버리 킷']; prices=[39000,49000,69000,19000]
for i,(name,price) in enumerate(zip(names,prices),1):
    row=fragment(f'<div class="cart-row cart-row-{i}"><div class="cart-product"><strong>{name}</strong><span>{price:,} KRW · 1개</span><label for="cart{i}" class="remove-item">선택 해제</label></div></div>')
    add_start(row,photo(i,name)); body.find(id='drawerItemList').add(row)
for node_id in ['drawerTotalAmount','floatingCartTotal','floatingCartBadge','drawerCartCount']:
    n=body.find(id=node_id); n.addclass('css-total' if 'Total' in node_id or 'Amount' in node_id else 'css-count')
    n.children=[Node('span',{'class':'cart-zero'},n.children)]
widget=body.find(id='floatingCartWidget'); linkify(widget,'#cartDrawer'); widget.attrs.pop('style',None)
widget.attrs['aria-label']='선택 상품 장바구니 확인'
toast=body.find(id='cartToast'); toast.attrs={'id':'cartToast','class':'cart-toast'}
toast.add(fragment('<a href="#cartDrawer">장바구니 보기 →</a>'))
for n in [body.find(id='drawerEmptyState'),body.find(id='drawerFooter')]: n.attrs.pop('style',None)
pkg=body.find(id='vipPkgSelectedDisplay'); pkg.children=[Node('span',{'class':'pkg-basic'},pkg.children),Node('span',{'class':'pkg-premium'},['[프리미엄] 전통 수제 보자기 & 노리개 (+5,000 KRW)'])]

# In-file catalogue uses only the source's own product data. No invented product descriptions.
catalog=fragment('<div id="catalog" class="css-modal catalog-modal" role="dialog" aria-label="밀도 16종 카탈로그"><div class="modal-sheet"><a class="close-link" href="#close" aria-label="닫기">×</a><span class="section-tag">THE COMPLETE COLLECTION</span><h2>밀도 16종 전 상품 카탈로그</h2><p>14종 향수·오브제 본품 + 2종 입문·선물 세트</p><div class="catalog-list"></div><a class="modal-bottom-close" href="#close">닫고 돌아가기 ↑</a></div></div>')
data=re.findall(r"'([^']+)': \{ price: (\d+), spec: '([^']+)' \}",scripts)
used=set()
for name,price,spec in data:
    m=re.match(r'(\d+)\.',name)
    if not m or int(m[1]) in used: continue
    num=int(m[1]); used.add(num)
    target={1:'#story-1',4:'#story-2',8:'#story-3',15:'#discovery',16:'#vipPreorderModal'}.get(num,'#mapae-system')
    catalog.find(cls='catalog-list').add(fragment(f'<a class="catalog-item" href="{target}"><span class="catalog-number">{num:02}</span><span><strong>{escape(name)}</strong><small>{escape(spec)}</small></span><span>{int(price):,} KRW</span></a>'))
body.add(catalog)
body.add(fragment('<div id="previewNotice" class="css-modal" role="dialog" aria-label="디자인 예시 안내"><div class="modal-sheet"><a class="close-link" href="#close" aria-label="닫기">×</a><span class="section-tag">MILDO · DESIGN PREVIEW</span><h2>디자인 예시 화면입니다</h2><p>실제 결제나 신청은 진행되지 않으며 입력한 정보도 전송되지 않습니다.</p><a href="#curated-showcase" class="btn-outline">컬렉션으로 돌아가기 →</a></div></div>'))
body.add(fragment('<a class="back-top" href="#top" aria-label="맨 위로">↑</a>'))

# Scope generic original inline layouts that need simple mobile stacking.
for n in body.nodes():
    if 'grid-template-columns' in n.attrs.get('style',''): n.addclass('inline-grid')

css=Path(__file__).with_name('mildo_design.css').read_text(encoding='utf-8')
image_dir=Path(r'C:/Users/SBS/.codex/generated_images/01a08517-2733-79a3-9639-45f7447633ac')
hero_b64=base64.b64encode((image_dir/'exec-d7af10d9-90ae-4f9b-b24d-aa9098f1e08a.png').read_bytes()).decode()
atlas_b64=base64.b64encode((image_dir/'exec-8f25e18e-08c5-4e4d-ae65-0f94bf0eb2c3.png').read_bytes()).decode()
gift_b64=base64.b64encode((image_dir/'exec-45db14d7-8a72-4204-a10a-3b7547c6a385.png').read_bytes()).decode()
css=':root{--hero-image:url("data:image/png;base64,'+hero_b64+'");--atlas-image:url("data:image/png;base64,'+atlas_b64+'");--gift-image:url("data:image/png;base64,'+gift_b64+'")}\n'+css
for bits in itertools.product([0,1],repeat=4):
    selector='body'+''.join((':has(#cart'+str(i+1)+':checked)' if v else ':not(:has(#cart'+str(i+1)+':checked))') for i,v in enumerate(bits))
    css+=selector+'{--cart-count:"'+str(sum(bits))+'";--cart-total:"'+format(sum(p*b for p,b in zip(prices,bits)),',')+' KRW"}\n'
for i in range(1,5):
    css+=f'body:has(#cart{i}:checked) .cart-row-{i}{{display:flex}}body:has(#cart{i}:checked) label[for="cart{i}"].add-to-cart{{background:#393b32!important;color:#fffef2!important}}body:has(#cart{i}:checked) label[for="cart{i}"].add-to-cart::after{{content:" ✓"}}\n'
for answers in itertools.product([1,2,3],repeat=4):
    c=Counter(answers)
    answer=0 if c[1]==2 and c[2]==2 else 1 if c[2]==2 and c[3]==2 else 2 if c[1]==2 and c[3]==2 else 3 if c[1]>=2 else 4 if c[2]>=2 else 5
    selector='body'+''.join(f':has(#q{i+1}a{a}:checked)' for i,a in enumerate(answers))
    css+=selector+f' .answer-{answer}'+'{display:block}\n'
css+='body'+''.join(f':has(input[name="q{i}"]:checked)' for i in range(1,5))+' .quiz-incomplete{display:none}\n'
head.add(Node('style',children=[css]))
# A landmark for the complete page content, leaving utility dialogs outside it.
main=Node('main',{'id':'main-content'})
start=body.children.index(hero)
body.children.insert(start,main); main.parent=body
for n in list(body.elements()):
    if n.tag=='section' or n is archive: main.add(detach(n))
add_start(body,fragment('<a class="skip-link" href="#main-content">본문 바로가기</a>'))
out=SOURCE.parent.parent/'웹디자인/강사_제작예시.html'
out.write_text('<!DOCTYPE html>\n'+doc.html(),encoding='utf-8')

def text_fragments(root):
    counts=Counter()
    def walk(n):
        if n.tag in ('script','style','#comment','head'): return
        for c in n.children:
            if isinstance(c,Node): walk(c)
            elif (v:=' '.join(c.split())): counts[v]+=1
    walk(root); return counts
original_counts=text_fragments(Parser(raw).root.find(tag='body'))
final_doc=Parser(out.read_text(encoding='utf-8')).root
final_counts=text_fragments(final_doc.find(tag='body'))
missing=original_counts-final_counts
ids=[n.attrs['id'] for n in final_doc.nodes() if 'id' in n.attrs]
broken=[n.attrs['href'] for n in final_doc.nodes() if n.tag=='a' and n.attrs.get('href','').startswith('#') and n.attrs['href'][1:] not in ids and n.attrs['href']!='#close']
report={'source':str(SOURCE),'output':str(out),'bytes':out.stat().st_size,'original_text_fragments':sum(original_counts.values()),'preserved_text_fragments':sum(original_counts.values())-sum(missing.values()),'missing':dict(missing),'scripts':sum(n.tag=='script' for n in final_doc.nodes()),'event_handlers':[(n.tag,a) for n in final_doc.nodes() for a in n.attrs if a.startswith('on')],'duplicate_ids':[k for k,v in Counter(ids).items() if v>1],'broken_fragments':broken,'catalogue_products':len(used),'quiz_questions':len(questions),'quiz_outcomes':len(branches),'external_assets':[(n.tag,n.attrs.get('src') or n.attrs.get('href')) for n in final_doc.nodes() if (n.tag in ('img','script','iframe','link') and (n.attrs.get('src') or n.attrs.get('href')))]}
Path(__file__).with_name('mildo_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
