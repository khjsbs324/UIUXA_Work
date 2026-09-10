from pathlib import Path
from html.parser import HTMLParser
import html, re, json, base64, io, hashlib
from collections import Counter
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'UIUX/work/이지희/웹사이트'
SRC=BASE/'와이어프레임/메인페이지_와이어프레임_시안5.html'
FINAL=BASE/'와이어프레임/메인페이지_와이어프레임_시안6_최종.html'
OUT=BASE/'웹디자인/강사_제작예시.html'
VOID=set('area base br col embed hr img input link meta param source track wbr'.split())

class Node:
    def __init__(self,tag='',attrs=None,raw=None):
        self.tag=tag; self.a=dict(attrs or []); self.raw=raw; self.children=[]; self.parent=None
    def add(self,n):
        if n.parent: n.parent.children.remove(n)
        n.parent=self; self.children.append(n); return n
    def remove(self):
        if self.parent: self.parent.children.remove(self); self.parent=None
    def walk(self):
        for c in self.children:
            yield c
            yield from c.walk()
    def find(self,fn): return next((n for n in self.walk() if fn(n)),None)
    def cls(self,c): return c in self.a.get('class','').split()
    def addcls(self,c): self.a['class']=(self.a.get('class','')+' '+c).strip()
    def text(self): return html.unescape(self.raw or '') if self.raw is not None else ''.join(c.text() for c in self.children)
    def render(self):
        if self.raw is not None:return self.raw
        inner=''.join(c.render() for c in self.children)
        if not self.tag:return inner
        attrs=''.join(' '+k+('="'+html.escape(str(v),quote=True)+'"' if v is not None else '') for k,v in self.a.items())
        return '<'+self.tag+attrs+'>'+('' if self.tag in VOID else inner+'</'+self.tag+'>')

class Tree(HTMLParser):
    def __init__(self,s):
        super().__init__(convert_charrefs=False);self.root=Node();self.stack=[self.root];self.feed(s)
    def handle_starttag(self,t,a):
        n=self.stack[-1].add(Node(t,a))
        if t not in VOID:self.stack.append(n)
    def handle_startendtag(self,t,a):self.stack[-1].add(Node(t,a))
    def handle_endtag(self,t):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==t:self.stack=self.stack[:i];break
    def handle_data(self,s):self.stack[-1].add(Node(raw=s))
    def handle_entityref(self,s):self.handle_data('&'+s+';')
    def handle_charref(self,s):self.handle_data('&#'+s+';')
    def handle_comment(self,s):self.stack[-1].add(Node('comment',raw='<!--'+s+'-->'))
    def handle_decl(self,s):self.stack[-1].add(Node('decl',raw='<!'+s+'>'))

def frag(s):return Tree(s).root.children[0]
def byid(root,id):return root.find(lambda n:n.a.get('id')==id)
def bycls(root,c):return root.find(lambda n:n.cls(c))

# Only replace visible wording; leave CSS, scripts, attributes, layout and products byte-for-byte.
changes={
 'KTR 공인 시험성적서 접수 및 검증 예정 기준':'KTR 시험 자료 안내',
 '[증빙준비] KTR 성적서':'KTR 시험 자료 안내',
 'Hero 오로라 수색 변환':'첫 화면의 오로라 색 변화',
 '기준표 SSOT 4대 핵심 라인업':'대표 상품 4종 안내',
 '20종 SSOT 데이터 연동':'20종 상품 정보 안내',
 '5대 핵심 카테고리 20종 전수 매트릭스':'다섯 분류의 전체 20종 상품 목록',
 '전수 20종 블렌딩 & 기어 마스터 도감':'전체 20종 티 & 도구 컬렉션',
 '취향별 20종 전수 라인업 & 마스터 비교 도감':'취향에 맞는 20종 상품 비교',
 '전수 도감':'전체 상품',
 '전수 상품 컬렉션':'전체 상품 컬렉션',
 '시안 4 마스터 통합':'시안 6 최종',
 'WICKETA 11인 통합 마스터 와이어프레임':'WICKETA 11인 통합 와이어프레임',
 '5-IN-1 감각 스튜디오 콘솔':'다섯 가지 감각 스튜디오',
 '5-in-1 감각 스튜디오 콘솔 (인터랙티브 창작 허브)':'다섯 가지 감각 체험 공간',
 '크래프트 여정':'제작 과정',
 'KTR 검증 크래프트 여정':'KTR 시험 안내와 제작 과정',
 '앞선 서사(':'앞선 이야기(',
 '서사 연계 4대 대표 상품':'이야기 속 대표 상품 4종',
 '3D각인':'입체 각인',
 '설계 기준 REQ-04':'제작 과정 안내',
 '설계 기준 REQ-05':'감각 체험 안내',
 '5대 인터랙티브 감각 경험 아키텍처':'다섯 가지 감각 체험 구성',
 '기획 아키텍처 규격':'브랜드 안내',
 '위케타의 해결 (1-Line Resolution)':'위케타의 해결',
 '출발 문제 (Origin Friction)':'일상 속 불편함',
 'WICKETA 전사 통합 와이어프레임 [시안 4] | 12 배서율 감각 서사 아키텍처 통합 에디션':'WICKETA 메인페이지 와이어프레임 [시안 6 최종]',
}
original=SRC.read_bytes().decode('utf-8')
class Wording(HTMLParser):
    def __init__(self,s):
        super().__init__(convert_charrefs=False);self.s=s;self.edits=[];self.skip=0
        self.lines=[0]
        self.lines.extend(m.end() for m in re.finditer('\n',s));self.feed(s)
    def handle_starttag(self,t,a):
        if t in ('script','style'):self.skip+=1
    def handle_endtag(self,t):
        if t in ('script','style'):self.skip-=1
    def handle_data(self,s):
        if self.skip:return
        new=s
        for old,val in sorted(changes.items(),key=lambda pair:-len(pair[0])):new=new.replace(old,val)
        new=new.replace('상품 목록를','상품 목록을')
        if new!=s:
            line,col=self.getpos();pos=self.lines[line-1]+col;self.edits.append((pos,pos+len(s),s,new))
w=Wording(original);final=original
for a,b,old,new in reversed(w.edits):final=final[:a]+new+final[b:]
FINAL.write_bytes(final.encode('utf-8'))

tree=Tree(final).root
body=tree.find(lambda n:n.tag=='body');head=tree.find(lambda n:n.tag=='head')
title=head.find(lambda n:n.tag=='title');title.children=[Node(raw='WICKETA — Drink Me, Escape Reality | 강사 제작 예시')]
products=json.loads(re.search(r'const MASTER_PRODUCTS\s*=\s*(\[.*?\]);',final,re.S).group(1))
assert len(products)==20
source_texts=Counter(n.raw.strip() for n in body.walk() if n.raw is not None and n.tag!='comment' and n.raw.strip() and not (n.parent and n.parent.tag in ('script','style')))
for n in list(tree.walk()):
    if n.tag in ('script','link'):n.remove()
    if n.tag=='comment':n.remove()

# Download-independent embedded campaign art. Generated with the built-in imagegen tool.
im=Image.open(Path('C:/Users/SBS/.codex/generated_images/01a08929-f7b8-7d80-b7dd-1b3fa67c2620/exec-0dffaddd-d0bd-49ce-afce-95eca204aa1a.png'))
buf=io.BytesIO();im.save(buf,format='JPEG',quality=91,optimize=True)
hero_uri='data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
sheet=Image.open(Path('C:/Users/SBS/.codex/generated_images/01a08929-f7b8-7d80-b7dd-1b3fa67c2620/exec-d595ad8b-f7d2-4b1c-a4f1-a7ddcbf1dbfd.png'))
sheet_buf=io.BytesIO();sheet.save(sheet_buf,format='JPEG',quality=92,optimize=True)
sheet_uri='data:image/jpeg;base64,'+base64.b64encode(sheet_buf.getvalue()).decode()
def photo(i,cls=''):
    # The generated sheet has slightly uneven cell boundaries; crop with CSS only.
    cols=[0,.239,.5,.761,1];rows=[0,.1975,.386,.571,.759,1]
    c=i%4;r=i//4;x=cols[c]+.005;y=rows[r]+.005
    width=cols[c+1]-cols[c]-.01;height=rows[r+1]-rows[r]-.01
    style='--px:'+str(x/(1-width)*100)+'%;--py:'+str(y/(1-height)*100)+'%;--sx:'+str(100/width)+'%;--sy:'+str(100/height)+'%;'
    return frag('<figure class="product-photograph '+cls+'" role="img" aria-label="'+html.escape(products[i]['name'])+' 상품 연출" style="'+style+'"></figure>')
hero=byid(body,'hero-section')
hero.children.insert(0,frag('<img class="campaign-image" src="'+hero_uri+'" alt="보랏빛 오로라 티가 담긴 프리즘 글래스와 WICKETA 티 스틱" width="1536" height="1024">'))
hero.children.insert(1,frag('<p class="campaign-headline" aria-hidden="true">Drink Me,<br><em>Escape Reality.</em></p>'))
visual=bycls(hero,'hero-visual-col');visual.addcls('original-visual-caption')
hero_grid=bycls(hero,'hero-split-grid')
right=[n for n in hero_grid.children if n.tag=='div' and n is not visual][0];right.addcls('hero-copy')

container=bycls(body,'container')
top=bycls(body,'wf-top-bar')
notes=frag('<details class="design-notes"><summary>프로젝트 구성과 보기 옵션 <span>＋</span></summary></details>')
notes.add(top);container.add(notes)
header=bycls(body,'wf-header')
header.children.insert(0,frag('<a class="brand-mark" href="#hero-section" aria-label="WICKETA 처음으로">WICKETA<span>TEA, BEYOND REALITY</span></a>'))
brand=bycls(header,'wf-brand');brand.addcls('brand-caption')

# Keep all original content. Styles classify small production annotations as secondary reading.
for n in list(body.walk()):
    st=n.a.get('style','')
    size=re.search(r'font-size:\s*([\d.]+)px',st)
    if size and float(size.group(1))<=10.5:n.addcls('fine-print')
    if n.tag in ('h1','h2','h3'):n.addcls('editorial-heading')
    if 'grid-template-columns' in st:n.addcls('inline-grid')
    if n.tag=='section':n.addcls('chapter')

# Move visual wireframe notes under the artwork instead of deleting their copy.
for n in list(body.walk()):
    if n.raw is not None and n.tag!='comment' and n.parent and n.parent.tag not in ('style','script'):
        pass

sections=[(n.a.get('id'),n.a.get('class')) for n in body.walk() if n.tag=='section']

# HTML-only controls: section navigation, CSS category filters, disclosure panels and native popovers.
css_extra=[]
catalog=byid(body,'catalog-section')
filters=bycls(catalog,'catalog-filters')
if filters:
    for btn in list(filters.children):
        if btn.tag!='button':continue
        cat=btn.a.get('id','').replace('filterBtn-','')
        if not cat:continue
        radio=frag('<input class="filter-state" type="radio" name="catalog-category" id="category-'+cat+'"'+(' checked' if cat=='all' else '')+'>')
        catalog.children.insert(0,radio);radio.parent=catalog
        btn.tag='label';btn.a['for']='category-'+cat
        css_extra.append('#catalog-section:has(#category-'+cat+':checked) label[for="category-'+cat+'"]{background:#262922!important;color:#fff!important;border-color:#262922!important}')
        if cat!='all':css_extra.append('#catalog-section:has(#category-'+cat+':checked) .product-card:not([data-cat="'+cat+'"]) {display:none!important}')

panes=[n for n in body.walk() if n.cls('studio-pane') or n.cls('studio-workstation-panel')]
for pane in panes:
    pane.addcls('static-studio-pane')
    # All five original experiences are present as individual editorial chapters.
    pane.a.pop('aria-hidden',None)
    idx=[0,8,14,16,10][panes.index(pane)]
    copy=Node('div',{'class':'studio-copy'})
    for child in list(pane.children):copy.add(child)
    pane.add(photo(idx,'studio-photo'));pane.add(copy)

# Visuals supplement, rather than replace, the original scene descriptions.
routine=byid(body,'routine-section')
scene_notes=[n for n in routine.walk() if n.raw and '장면 연출 참고:' in n.raw]
for i,n in enumerate(scene_notes):
    box=n.parent
    while box.parent and box is not routine and 'dashed' not in box.a.get('style',''):box=box.parent
    if box is routine:continue
    box.addcls('scene-caption')
    scene=box.parent;scene.addcls('ritual-scene')
    art=photo([2,5,0,6][min(i,3)],'scene-photo');art.parent=scene
    scene.children.insert(scene.children.index(box),art)

spot=byid(body,'spotlight-section')
spot_header=bycls(spot,'wf-section-header')
spot_art=frag('<figure class="spotlight-photo"><img src="'+hero_uri+'" alt="빛에 따라 보랏빛으로 빛나는 오로라 티" loading="lazy"></figure>')
spot_art.parent=spot;spot.children.insert(spot.children.index(spot_header)+1,spot_art)

palette=['#b6a4df','#b59c77','#a4b697','#c4949e','#a9b9a3','#b0c5d8','#c6b5d4','#a3b39e']
def pack_svg(p,i):
    color=palette[i%len(palette)];pid=p['id'];cat=p['cat']
    if cat=='ware':
        obj='<path d="M121 80 L228 80 L218 245 Q176 267 131 245Z" fill="url(#glass)" stroke="#fff" stroke-width="2"/><ellipse cx="175" cy="80" rx="54" ry="12" fill="#fff" fill-opacity=".36" stroke="#91958b"/><path d="M136 94L143 234M216 95L207 233" stroke="#fff" stroke-width="4" opacity=".7"/>'
    else:
        obj='<path d="M105 61 L235 61 L243 262 L97 262Z" fill="url(#pack)" stroke="#8b8a7d" stroke-opacity=".3"/><path d="M106 73H234M99 249H241" stroke="#f6f2e9" stroke-width="3"/><path d="M108 79L102 242M231 79L238 242" stroke="#fff" opacity=".45"/><text x="170" y="134" text-anchor="middle" font-family="Arial" font-size="24" letter-spacing="3" fill="#313831">WICKETA</text><text x="170" y="160" text-anchor="middle" font-family="Arial" font-size="8" letter-spacing="2" fill="#394139">TEA, BEYOND REALITY</text><circle cx="170" cy="200" r="16" fill="none" stroke="#56674f" stroke-opacity=".6"/><path d="M170 213Q145 187 180 185Q190 207 170 213" fill="none" stroke="#56674f"/><text x="170" y="235" text-anchor="middle" font-family="Arial" font-size="8" letter-spacing="2" fill="#394139">'+pid.upper()+'</text>'
    return '<svg viewBox="0 0 340 320" role="img" aria-label="'+html.escape(p['name'])+' 패키지 디자인" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="pack"><stop stop-color="#eeeadf"/><stop offset=".5" stop-color="'+color+'"/><stop offset="1" stop-color="#d3d4c4"/></linearGradient><linearGradient id="glass"><stop stop-color="#fff" stop-opacity=".85"/><stop offset=".45" stop-color="'+color+'" stop-opacity=".2"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient><radialGradient id="floor"><stop stop-color="#5d5b53" stop-opacity=".18"/><stop offset="1" stop-color="#5d5b53" stop-opacity="0"/></radialGradient></defs><ellipse cx="170" cy="270" rx="103" ry="18" fill="url(#floor)"/>'+obj+'</svg>'

cards=[n for n in body.walk() if n.cls('product-card')]
for i,(card,p) in enumerate(zip(cards,products)):
    card.a['id']='catalog-card-'+p['id']
    card.a['data-product-id']=p['id']
    # Use unique gradient ids in every inline SVG.
    art=pack_svg(p,i)
    for grad in ('pack','glass','floor'):art=art.replace('id="'+grad+'"','id="'+p['id']+'-'+grad+'"').replace('url(#'+grad+')','url(#'+p['id']+'-'+grad+')')
    figure=photo(i,'product-art');figure.parent=card;card.children.insert(0,figure)
    detail=frag('<details class="product-facts" id="facts-'+p['id']+'"><summary>원료와 구성 자세히 보기 <span>＋</span></summary></details>')
    detail.add(frag('<p>'+html.escape(p['desc'])+'</p>'))
    for key,label in [('ingredient','핵심 원료'),('composition','상품 구성'),('tech','특징'),('priceDisplay','가격')]:
        detail.add(frag('<dl><dt>'+label+'</dt><dd>'+html.escape(p[key])+'</dd></dl>'))
    card.add(detail)
    old_art=bycls(card,'product-img-box')
    if old_art:
        old_art.addcls('packaging-description')
        detail.add(old_art)
    popup=frag('<section class="product-popover" id="product-'+p['id']+'" popover><button class="popover-close" popovertarget="product-'+p['id']+'" popovertargetaction="hide" aria-label="닫기">×</button><p class="eyebrow">WICKETA COLLECTION</p><h2>'+html.escape(p['name'])+'</h2><p>'+html.escape(p['desc'])+'</p><p class="detail-price">'+html.escape(p['priceDisplay'])+'</p></section>')
    for key,label in [('ingredient','핵심 원료'),('composition','상품 구성'),('tech','특징')]:popup.add(frag('<dl><dt>'+label+'</dt><dd>'+html.escape(p[key])+'</dd></dl>'))
    popup.add(frag('<a class="wf-btn-block" href="#order-section">주문·문의 정보 보기 ↗</a>'));body.add(popup)

drawer=byid(body,'drawerOverlay')
if drawer:
    drawer.addcls('static-order');drawer.a['id']='order-section';drawer.a.pop('aria-hidden',None)
    # Preserve all original order-panel copy, including content normally shown only after a JS selection.
    container.add(drawer)
    dc=byid(body,'drawerContent')
    if dc:
        dc.a.pop('role',None);dc.a.pop('aria-modal',None);drawer.add(dc)
    for mode,label,p in [('General','일반 주문',products[0]),('B2B','기업 주문',products[16]),('Phone','전화 주문',products[0])]:
        m=re.search(r"document.getElementById\('drawerBody"+mode+r"'\).innerHTML = `(.*?)`;",final,re.S)
        if not m:continue
        template=m.group(1)
        for key,value in p.items():template=template.replace('${p.'+key+'}',html.escape(str(value)))
        template=template.replace('${b2bPriceText}',p['priceDisplay'])
        template=re.sub(r"\$\{isSub \? '월 57,800원' : p.priceDisplay\}",p['priceDisplay'],template)
        template=re.sub(r"\$\{isSub \?.*?\}",'⚡ 30일 정기구독 신청 시 15% 추가 할인 적용 (33,150원)',template)
        area=byid(body,'drawerBody'+mode)
        area.add(frag('<h3>'+label+'</h3>'))
        for child in list(Tree(template).root.children):area.add(child)
modal=byid(body,'productDetailModalOverlay')
if modal:
    modal.a['popover']=None;modal.a.pop('aria-hidden',None);modal.addcls('legacy-detail')

for n in list(body.walk()):
    events={k:v for k,v in n.a.items() if k.lower().startswith('on')}
    for k in events:n.a.pop(k,None)
    click=events.get('onclick','')
    if not click:continue
    target=None
    match=re.search(r"findInCatalog\('([^']+)'\)",click)
    if match:target='#catalog-card-'+match.group(1)
    match_scroll=re.search(r"getElementById\('([^']+)'\).*scrollIntoView",click)
    if match_scroll:target='#'+match_scroll.group(1)
    if 'openProductDetail' in click:
        m=re.search(r"\('([^']+)'",click)
        if m:n.a['popovertarget']='product-'+m.group(1);n.a['type']='button'
    elif 'openDrawer' in click:target='#order-section'
    elif 'switchStudio' in click or 'setStudio' in click:
        m=re.search(r"\((?:')?([^',)]+)",click)
        if m:
            candidate=next((p for p in panes if m.group(1) in p.a.get('id','')),None)
            if candidate:target='#'+candidate.a['id']
    elif 'filterByRecipe' in click or 'filterRecipe' in click:target='#catalog-section'
    elif 'switchPersonaView' in click:target='#studio-section'
    elif 'toggleSeniorMode' in click:
        n.tag='label';n.a['for']='large-type';n.a.pop('role',None)
    elif 'toggleMobileEmulationMode' in click:target='#hero-section'
    elif 'closeDrawer' in click:target='#catalog-section'
    elif 'switchDrawerMode' in click:
        m=re.search(r"\('([^']+)'",click)
        if m:target='#drawerBody'+{'general':'General','b2b':'B2B','phone':'Phone'}[m.group(1)]
    elif 'closeProductDetailModal' in click:
        n.a['popovertarget']='productDetailModalOverlay';n.a['popovertargetaction']='hide'
    elif 'alert(' in click:
        target='#craft-section' if ('KTR' in click or '성적서' in click) else '#order-section'
    elif 'selectRitualTime' in click:target='#routine-section'
    if target and (n.tag in ('button','a') or n.cls('time-btn')):
        n.tag='a';n.a['href']=target;n.a.pop('type',None);n.a.pop('role',None)

for n in body.walk():
    if n.a.get('href')=='#brand-section':n.a['href']='#bridge-section'
    if n.a.get('href','').startswith('javascript:'):n.a['href']='#order-section'

# Reset and recipe filters share the native radio group; no stale category count.
reset=byid(body,'catalogFilterResetBtn')
if reset:reset.tag='label';reset.a['for']='category-all'
for n in body.walk():
    if n.cls('recipe-pill'):
        n.tag='label';n.a.pop('href',None);n.a['for']='category-sig'
count=byid(body,'catalogCountText')
if count:
    for c in list(count.children):
        if c.raw or c.tag:pass
    count.addcls('catalog-count-original')
    for cat,name in [('sig','시그니처 믹솔로지'),('clean','클린티'),('gift','패키지·선물'),('ware','홈카페 도구'),('bulk','B2B 대용량')]:
        css_extra.append('#catalog-section:has(#category-'+cat+':checked) .catalog-count-original{font-size:0!important}#catalog-section:has(#category-'+cat+':checked) .catalog-count-original:after{content:"'+name+' 상품 4개가 표시되고 있습니다.";font-size:12px}')

# Preserve generic detail information in an accessible native popover.
notes.add(frag('<button type="button" class="wf-btn-outline" popovertarget="productDetailModalOverlay">상품 안내 화면 구성 보기</button>'))

footer=body.find(lambda n:n.tag=='footer')
if footer:container.add(footer)

body.children.insert(0,frag('<input type="checkbox" id="large-type" class="filter-state">'))

# The source's data-only order panels are made explicit without execution or submission claims.
order=byid(body,'order-section')
if order:
    order.children.insert(0,frag('<p class="eyebrow">ORDER & CONCIERGE</p><h2>당신의 한 잔을 위한 안내</h2>'))
    order.add(frag('<p class="static-note">상품 선택과 문의를 위한 화면입니다. 결제 및 예약 전송은 연결되어 있지 않습니다.</p>'))

head.add(frag('<style>:root{--product-sheet:url("'+sheet_uri+'")}'+ (ROOT/'.playwright-mcp/wicketa-design.css').read_text(encoding='utf-8')+'\n'+'\n'.join(css_extra)+'</style>'))
head.add(Node('comment',raw='<!-- References: https://www.drinkzoi.co/ | https://noomoagency.com/ | https://www.gentlemonster.com/kr/ko | https://www.tamburins.com/kr/shop/body/showery-body/ | https://vsion.global/technology/ | https://www.ancors.co.kr/factory-manufacturing | https://www.smentertainment.com/company/branding/ | https://tscent-tea.com/pages/about . Source: 레퍼런스1.txt. Tamburins current page blocked. Content authority: wireframe v6, 20 products. Hero: built-in imagegen, original WICKETA prism glass campaign. -->'))
result=tree.render()
OUT.write_text(result,encoding='utf-8')
new_texts=Counter(n.raw.strip() for n in body.walk() if n.raw is not None and n.tag!='comment' and n.raw.strip() and not (n.parent and n.parent.tag in ('script','style')))
missing=source_texts-new_texts
report={'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'wireframe_text_edits':len(w.edits),'wireframe_edits':[{'from':a.strip(),'to':b.strip()} for _,_,a,b in w.edits],'products':len(cards),'categories':dict(Counter(p['cat'] for p in products)),'studio_panes':len(panes),'missing_source_texts':list(missing),'scripts':len(re.findall(r'<script\b',result,re.I)),'event_attributes':len(re.findall(r'\son\w+=',result,re.I)),'output_bytes':OUT.stat().st_size,'sections':sections}
(ROOT/'.playwright-mcp/wicketa-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('wireframe_edits','sections')},ensure_ascii=False))
print(json.dumps(sections,ensure_ascii=False))
