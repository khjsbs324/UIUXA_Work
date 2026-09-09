from pathlib import Path
from mildo_dom import Parser,Node
from html import escape as E
import re,json,base64,copy,io
from PIL import Image

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'박찬미/웹사이트'
SOURCE=BASE/'와이어프레임'
OUT=BASE/'웹디자인/강사_제작예시.html'
main=Parser((SOURCE/'와이어프레임_시안5_최종.html').read_text(encoding='utf-8')).root.find(tag='body')
brand=Parser((SOURCE/'브랜드소개_시안3.html').read_text(encoding='utf-8')).root.find(tag='body')
cat=Parser((SOURCE/'카테고리_시안2.html').read_text(encoding='utf-8')).root.find(tag='body')
data=json.loads((HERE/'halo-data.json').read_text(encoding='utf-8'))
assets={
 'hero':'exec-b2f46f96-d80c-4dc0-a57d-f0d4a4fea69d.png',
 'running':'exec-05df2dcd-0b59-4d14-9c35-e2b6603743f3.png',
 'catalog':'exec-b4eb2701-c0fc-4f8f-b7b1-9467edd36a5c.png'}
gen=Path('C:/Users/SBS/.codex/generated_images/01a0852b-41c2-7122-9841-7c29116b9175')
def image_uri(file):
 # Lossy encoding only; no visual editing or cropping. Keep each CSS value under the browser token limit.
 out=io.BytesIO();Image.open(file).save(out,format='WEBP',quality=92,method=6)
 return 'data:image/webp;base64,'+base64.b64encode(out.getvalue()).decode()
asset_css=':root{'+''.join('--'+k+':url('+image_uri(gen/v)+');' for k,v in assets.items())+'}'
cols={'running':('01','CITY RUNNING','시티 러닝 & 마라톤',4,1),'hiking':('02','TRAIL & CLIMB','트레일 하이킹 & 클라이밍',3,5),'surfing':('03','WATER ACTIVE','서핑 & 수상 액티브',3,8),'tennis':('04','COURT & FAIRWAY','테니스 & 골프 라운딩',3,11),'fitness':('05','FITNESS & TRAINING','피트니스 & 크로스핏',3,14)}
def txt(n):return ' '.join(n.text().split()) if n else ''
def inside(n):return ''.join(c.html() if isinstance(c,Node) else E(c) for c in n.children)
def cleantext(s):
 s=s.replace('행동의 차이가 스포츠의 결과를 바꿉니다','행동의 차이가 운동의 흐름을 바꿉니다').replace('설계 원칙을 실전 기어로 입증하는 4단계 연구 과정','설계 원칙을 실전에서 확인하기 위한 4단계 연구 과정')
 s=re.sub(r'[📷⚙️💡⚡☑️]','',s)
 s=s.replace('[','').replace(']','').replace('시각 자료: ','').replace('대표 배경 사진 영역 / HERO BACKGROUND IMAGE','').replace('3D 정면 렌더','제품 디테일').replace('렌더 도해','소재 디테일').replace('렌더','디테일')
 s=re.sub(r'1-ATHLETE JOURNEY SCENE [123]|PAIN SCENE VIEW|MOTION SCENE VIEW|소재 근접 디테일 [123]','',s)
 s=re.sub(r'이미지 들어갈 공간 \d+:\s*','',s).replace('디테일링','도해').replace('3D 디테일 1장','구조')
 return s
omit={'hero-cinematic-placeholder','silhouette-icon-box','silhouette-label','process-scroll-controls','btn-toggle-role-desc','compare-check-label','collection-tabs-bar','mobile-swipe-hint'}
audit=[]
def render(n,prefix='',visual=True):
 if isinstance(n,str):return E(cleantext(n))
 if n.tag in ['#comment','script','style','svg'] or any(n.cls(c) for c in omit):return ''
 tag=n.tag; t=txt(n); style=n.attrs.get('style',''); classes=n.attrs.get('class','').split(); attr=''
 if t and not n.elements() and any(x in t for x in ['DESIGN VARIATION','3D HARDWARE MATERIAL STAGE','ATHLETIC FIELD COMPARISON SCENE','CROPPED MOTION SCENE','3D NITROGEN DISPERSION BLUEPRINT','STATUS: ACTIVE','현재 단계:','100vw ATHLETIC','모바일 목록 보기 방식']):return ''
 if tag in ['input','select','option','label','textarea','form']:return ''
 if tag=='button' or tag=='a':
  action=n.attrs.get('onclick',''); href=n.attrs.get('href','')
  sku=re.search(r'openProductModal\((\d+)',action)
  if sku:href='#gear-'+sku[1]
  elif 'Launch' in action or 'javascript:' in href:href='#launch'
  elif 'Compare' in action:href='#comparison'
  elif 'filterCatalogByPhase' in action:href='#catalog'
  elif not href:return ''
  elif not href.startswith('#'):href='#catalog'
  elif prefix and href!='#':href='#'+prefix+href[1:]
  if href=='#':href='#home'
  tag='a';attr+=' href="'+E(href,quote=True)+'"';classes+=['text-link']
 if 'id' in n.attrs:attr+=' id="'+prefix+n.attrs['id']+'"'
 if 'grid-template-columns' in style:
  v=re.search(r'grid-template-columns\s*:\s*([^;]+)',style)[1]
  count=int(re.search(r'repeat\((\d+)',v)[1]) if re.search(r'repeat\((\d+)',v) else v.count('fr')
  classes+=['layout-grid','grid-'+str(max(2,min(count,4)))]
 if 'display:flex' in style.replace(' ','') and 'flex-direction:column' not in style.replace(' ',''):classes+=['flex-row']
 if 'padding:' in style or 'padding: ' in style:
  m=re.search(r'padding:\s*(\d+)',style)
  if m and int(m[1])>=16:classes+=['inset']
 if re.search(r'margin-(bottom|top):\s*(1[6-9]|[2-9]\d)',style):classes+=['block-gap']
 if re.search(r'font-size:\s*(3\d|[4-9]\d)',style):classes+=['large-type']
 elif re.search(r'font-size:\s*(1[6789]|2\d)',style):classes+=['medium-type']
 if re.search(r'font-size:\s*(9|10|11)',style):classes+=['small-type']
 if 'font-weight:900' in style.replace(' ',''):classes+=['bold']
 if 'border-top' in style:classes+=['ruled-top']
 # A design placeholder becomes an actual photograph with its descriptive caption retained.
 if visual and ('dashed' in style or '--border-dash' in style) and ('height:' in style or len(t)<220) and tag=='div':
  if '이미지 들어갈 공간 10' in t:
   return '''<figure class="refill-diagram"><svg viewBox="0 0 1100 350" role="img" aria-label="알루미늄 외장 78퍼센트와 PP 리필 코어 22퍼센트의 분리형 구조 도해"><defs><linearGradient id="metal-refill"><stop stop-color="#637672"/><stop offset=".2" stop-color="#e6eee6"/><stop offset=".46" stop-color="#a6b7aa"/><stop offset=".6" stop-color="#f4f7f0"/><stop offset="1" stop-color="#788e84"/></linearGradient><linearGradient id="pp-refill"><stop stop-color="#afc9c7"/><stop offset=".5" stop-color="#e6f2ed"/><stop offset="1" stop-color="#95afb0"/></linearGradient></defs><path d="M110 185 H970" stroke="#879d90" stroke-dasharray="5 7"/><g><rect x="135" y="90" width="140" height="200" rx="19" fill="url(#metal-refill)" stroke="#8b9f91"/><ellipse cx="205" cy="95" rx="70" ry="17" fill="#aabeb0" stroke="#849b8a"/><ellipse cx="205" cy="95" rx="51" ry="11" fill="#64796b"/><text x="205" y="207" text-anchor="middle" fill="#33483c" font-size="23" letter-spacing="7">HALO</text><path d="M275 275 H340 V300" fill="none" stroke="#829a8b"/><text x="355" y="307" font-size="13" fill="#40594c">AL6061 / 78%</text></g><g><rect x="498" y="112" width="97" height="156" rx="15" fill="url(#pp-refill)" stroke="#8aa9a2"/><ellipse cx="547" cy="118" rx="48" ry="13" fill="#e2eee6"/><path d="M550 107 V62 H643" fill="none" stroke="#829a8b"/><text x="657" y="67" font-size="13" fill="#40594c">PP REFILL CORE / 22%</text><text x="547" y="210" text-anchor="middle" fill="#5f7e73" font-size="10">REPLACE. REUSE.</text></g><g><rect x="855" y="115" width="141" height="103" rx="17" fill="url(#metal-refill)" stroke="#8b9f91"/><ellipse cx="926" cy="120" rx="70" ry="15" fill="#c5d3c5" stroke="#8b9f91"/><path d="M926 224 V271 H855" fill="none" stroke="#829a8b"/><text x="852" y="294" font-size="13" fill="#40594c">REUSABLE CAP</text></g></svg><figcaption>REFILL ARCHITECTURE / CONCEPT — 알루미늄 하우징 &amp; 리필 코어 분해 구조<br>AL6061 외장 금속 바디(78%)와 내부 교체형 PP 리필 카트리지 코어(22%)의 정밀 체결 구조</figcaption></figure>'''
  if '운동을 멈추고 주머니' in t or '페이스 유지 상태로' in t:
   ishalo='페이스 유지' in t
   steps=['움직임 유지','한 손 분리','노터치 도포','다시 체결'] if ishalo else ['멈춤','수납 열기','손에 덜기','얼굴에 바르기','손 닦기']
   return '<figure class="action-visual '+('halo-action' if ishalo else 'conventional-action')+'"><div class="action-path">'+''.join('<div><span>'+str(j+1).zfill(2)+'</span><small>'+s+'</small></div>' for j,s in enumerate(steps))+'</div><figcaption>'+E(cleantext(t))+'</figcaption></figure>'
  classes+=['source-visual']
  return '<figure class="'+E(' '.join(classes))+'"><figcaption>'+E(cleantext(t))+'</figcaption></figure>'
 if classes:attr+=' class="'+E(' '.join(classes),quote=True)+'"'
 if tag in ['br','hr']:return '<'+tag+'>'
 return '<'+tag+attr+'>'+''.join(render(c,prefix,visual) for c in n.children)+'</'+tag+'>'
def section_original(id,extra='',prefix='',doc=main):
 n=copy.deepcopy(doc.find(id=id));n.attrs.pop('style',None);n.addclass('source-section '+extra)
 return render(n,prefix)
def label(s):return '<span class="eyebrow">'+s+'</span>'
def heading(k,title,desc='',link=''):
 return '<div class="section-heading"><div>'+label(k)+'<h2>'+title+'</h2></div><div class="heading-aside">'+('<p>'+desc+'</p>' if desc else '')+link+'</div></div>'
def sprite(i,cls='',name=''):
 return '<div class="product-image '+cls+'" style="--x:'+str(((i-1)%4)*100/3)+'%;--y:'+str(((i-1)//4)*100/3)+'%" role="img" aria-label="'+E(name or data['skus'][i-1]['name'],quote=True)+' 제품 콘셉트 이미지"></div>'
def button(href,text,secondary=False):return '<a class="button'+(' secondary' if secondary else '')+'" href="'+href+'">'+text+'<span aria-hidden="true">↗</span></a>'
def accord(title,content,open=False):return '<details class="disclosure"'+(' open' if open else '')+'><summary>'+title+'<span aria-hidden="true">＋</span></summary><div class="disclosure-body">'+content+'</div></details>'
def main_card(i):return main.find(cls='shop-all-grid').find(id='nothing') if False else next(n for n in main.nodes() if n.cls('sku-card') and n.attrs.get('data-sku')==str(i))
def old_card_content(i):
 n=copy.deepcopy(main_card(i))
 for x in [n]+list(n.nodes()):x.attrs.pop('id',None)
 for k in ['sku-card-header','sku-img-box','sku-card-actions']:
  for x in list(n.nodes()):
   if x.cls(k):x.parent.children.remove(x)
 return render(n, 'original-'+str(i)+'-',False)
def product_card(p,where):
 i=p['id'];c=cols[p['col']]
 if where=='main':
  n=main_card(i);name=txt(n.find(cls='sku-card-title'));price=txt(n.find(cls='sku-price-row'));feature=txt(n.find(cls='sku-card-feature'))
 else:name=p['name'];price=p['price']+' / '+p['vol'];feature=p['feature']
 return '<article class="product-card" data-col="'+p['col']+'" data-phase="'+p['phase']+'" data-type="'+p['type']+'" data-func="'+p['func']+'" data-price="'+str(p['rawPrice'])+'"><a class="product-thumb" href="#gear-'+str(i)+'">'+sprite(i,name=name)+'<span class="product-number">'+str(i).zfill(2)+' / HALO</span><span class="product-role">'+('CORE GEAR' if p['role']=='core' else 'GEAR KIT' if p['role']=='support' else p['phase'].upper()+' WORKOUT')+'</span><span class="image-arrow" aria-hidden="true">↗</span></a><div class="product-caption"><span class="micro">'+c[1]+'</span><h3><a href="#gear-'+str(i)+'">'+E(name)+'</a></h3><p>'+E(feature)+'</p><div class="product-price">'+E(price)+'</div>'+accord('기어 정보',old_card_content(i) if where=='main' else '<p>'+E(p['roleName'])+'</p><p>'+E(p['relation'])+'</p><p>추천 상황 · '+E(p['scenario'])+'</p><p>'+E(p['dur'])+' · '+E(p['clinical'])+'</p>')+'</div></article>'

head='''<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><meta name="description" content="HALO — 운동의 흐름을 멈추지 않는 노터치 쿨링 선케어 기어. 5대 스포츠 환경, 16종의 기어와 하드웨어 설계 이야기."><title>HALO — NEVER STOP THE MOTION</title><style>'''
nav='''<a class="skip-link" href="#content">본문 바로가기</a><div class="announcement"><span>BUILT FOR YOUR NEXT MOVE.</span><a href="#launch">HALO 첫 출시 · 얼리버드 15% 혜택 <span aria-hidden="true">↗</span></a></div><header class="site-header"><a class="logo" href="#home" aria-label="HALO 홈">HALO<span>®</span></a><nav aria-label="주 메뉴"><a class="nav-shop" href="#catalog">SHOP ALL <span>16</span></a><a class="nav-brand" href="#brand">OUR STORY</a><a href="#collections">COLLECTIONS</a><a href="#process">GEAR LAB</a></nav><a class="nav-alert" href="#launch">출시 알림 <span aria-hidden="true">↗</span></a><a class="mobile-nav" href="#mobile-menu">MENU ＋</a></header><main id="content">'''
hero='''<article id="home" class="view home-view"><section class="hero"><div class="hero-topline"><span>KINETIC GEAR LAB</span><span>NO-TOUCH COOLING SUNCARE GEAR</span><span>01 — 16 / ENGINEERED FOR MOTION</span></div><div class="hero-stage"><div class="hero-wordmark" aria-hidden="true">HALO</div><div class="hero-object" role="img" aria-label="물방울이 맺힌 실버 카라비너 선 스틱과 블랙 질소 미스트 제품 콘셉트"></div><span class="hero-side-note">PRECISION HARDWARE. / EVERYDAY PERFORMANCE.</span><div class="hero-callout"><span class="crosshair">＋</span><div>ALUMINUM 6061-T6<br><span>LIGHT ON SKIN. BUILT TO MOVE.</span></div></div><span class="hero-temp">−4.2°<small>CRYO-COOLING / CONCEPT TARGET</small></span></div><div class="hero-bottom"><div><span class="eyebrow">NEVER STOP THE MOTION</span><h1>운동의 흐름을<br>멈추지 않는 선케어 기어.</h1></div><div><p>멈추지 않고 꺼내고, 묻히지 않고 덧바르는<br>노터치 쿨링 기어.</p><div class="hero-links">'''+button('#catalog','16종 기어 탐색')+button('#philosophy','핵심 기술 보기',True)+'''</div><p class="fine-print">본 페이지의 제품, 수치, 임상 및 사용자 데이터는 포트폴리오 설계를 위한 가상 정보입니다.</p></div></div><div class="hero-footnote"><span>페이스 지연 0초 · 손 오염 0.0% / 가상 설계 목표</span><span class="swatches"><i class="black"></i>에어 블랙 <i class="gray"></i>스텔스 그레이 <i class="silver"></i>매트 실버 <i class="white"></i>알파 화이트</span><a href="#launch">15% 얼리버드 알림 신청 ↗</a></div></section>'''

# Preserve the original editorial copy, values, material descriptions and field comparison.
philosophy=section_original('philosophy','manifesto')
philosophy=philosophy.replace('01. BRAND PHILOSOPHY &amp; R&amp;D MANIFESTO','01 / THE HALO APPROACH')

flagships=''
for i,sid in [(1,'spotlight'),(2,'spotlight-mist')]:
 p=data['skus'][i-1];n=main.find(id=sid);cont=n.find(cls='container')
 original=''.join(render(x,'spec'+str(i)+'-') for x in cont.elements()[2:])
 q=data['quick'][str(i)]
 flagships+='<section id="'+sid+'" class="flagship section-shell '+('reverse' if i==2 else '')+'"><div class="flagship-visual">'+sprite(i)+'<span class="visual-index">GEAR 0'+str(i)+' / '+('ONE-HAND SYSTEM' if i==1 else 'NITROGEN SYSTEM')+'</span><span class="visual-caption">'+('AL6061 / NO-TOUCH ROLLER' if i==1 else '360° MIST / QUICK DRY')+'</span></div><div class="flagship-copy">'+label('02 / FLAGSHIP GEAR 0'+str(i))+'<h2>'+('CLIP.<br>ROLL.<br>KEEP GOING.' if i==1 else 'COOL DOWN.<br>MOVE ON.')+'</h2><h3>'+p['name']+'</h3><p>'+p['feature']+'</p><div class="spec-trio"><div><strong>'+('3s' if i==1 else '360°')+'</strong><span>'+('원핸드 노터치 도포' if i==1 else '전방위 질소 분사')+'</span></div><div><strong>'+('−4.2°' if i==1 else '−3.9°')+'</strong><span>크라이오 쿨링 목표</span></div><div><strong>'+('18.4g' if i==1 else '3s')+'</strong><span>'+('초경량 바디' if i==1 else '퀵드라이')+'</span></div></div><div class="buy-line"><span>'+p['price']+'</span><span>'+q['vol']+' / SPF50+ PA++++</span></div>'+button('#gear-'+str(i),'제품 자세히 보기')+'<a class="text-link" href="#launch">15% 출시 알림 신청 ↗</a>'+accord('소재 · 사용 순서 · 8대 상세 사양','<div class="source-specs">'+original+'</div>')+'</div></section>'

process=section_original('process','lab-section')
routine=section_original('routine','routine-section')

collections='<section id="collections" class="section-shell collection-section">'+heading('05 / FIND YOUR FIELD','YOUR SPORT.<br>YOUR HALO.','5대 스포츠 종목별 풀 비주얼 & 대표 기어. 극한의 환경은 다르지만, 움직임은 이어져야 하니까.')+'<div class="collection-banner"><div>'+label('COLLECTION 01 — CITY RUNNING')+'<h3>열기는 남겨두고,<br>페이스만 가져가세요.</h3><p>아스팔트 45℃ 지열 파동 속 페이스 유지 3초 도포.<br>초경량 알루미늄 6061 바디와 함께하는 다음 킬로미터.</p></div><span>42.195 KM / NEVER STOP</span></div>'
for key,s in data['scenes'].items():
 if key=='all':continue
 c=cols[key];p=data['skus'][s['skuId']-1]
 body='<div class="collection-expanded"><div>'+sprite(s['skuId'])+'<span class="micro">'+E(s['diagramSub'])+'</span></div><div><h3>'+E(s['title'])+'</h3><p>'+E(s['desc'])+'</p><dl class="facts">'
 for title,a,b in [('대표 기술','coreTech','coreTechDesc'),('파생 기준','extLogic','extLogicDesc'),('추천 장면','recScenario','recScenarioDesc')]:
  body+='<div><dt>'+title+'</dt><dd><strong>'+E(s[a])+'</strong><p>'+E(s[b])+'</p></dd></div>'
 body+='</dl><p class="micro">'+E(cleantext(s['canvasTitle']))+' · '+E(s['canvasDesc'])+'</p><h4>'+E(s['flagName'])+'</h4><p>'+E(s['flagDesc'])+'</p><p class="tag-line">'+' / '.join(E(x) for x in s['specs'])+'</p><p>'+E(cleantext(s['flow']))+'</p><p>'+s['price']+' · '+s['vol']+'</p>'+button('#gear-'+str(s['skuId']),'대표 기어 자세히 보기')+'</div></div>'
 collections+='<details class="collection-row"><summary><span class="micro">'+c[0]+'</span><span class="collection-title">'+c[1]+'<small>'+c[2]+'</small></span><span class="collection-criterion">'+E(s['sceneCriteria'])+'</span><span class="collection-count">'+str(c[3])+' GEARS</span><span class="plus" aria-hidden="true">＋</span></summary>'+body+'</details>'
allscene=data['scenes']['all']
collections+='<p class="collection-source-desc">러닝, 하이킹, 수상, 테니스, 피트니스까지 종목별 극한 환경 기준과 1대 대표 플래그십 기어 및 파생 관계도를 확인하세요.</p>'
collections+=accord('5대 환경과 16종 하드웨어 설계 개요','<h3>'+allscene['title']+'</h3><p>'+allscene['desc']+'</p><p>'+allscene['sceneCriteria']+'</p><p>'+allscene['coreTech']+' · '+allscene['coreTechDesc']+'</p><p>'+allscene['extLogic']+' · '+allscene['extLogicDesc']+'</p><p>'+allscene['recScenario']+' · '+allscene['recScenarioDesc']+'</p>')+'<div class="section-end"><span>5대 스포츠 16종 전체 기어를 탐색하고 스펙을 횡단 비교해 보세요.</span><a class="text-link" href="#catalog">전체 기어 카탈로그 & 비교하기 ↗</a></div></section>'
shop='<section id="shop-all" class="section-shell shop-section">'+heading('06 / THE COMPLETE GEAR SYSTEM','THE GEAR EDIT.','HALO 16종 전체 기어 시스템 카탈로그', '<a class="text-link" href="#catalog">필터로 내 기어 찾기 ↗</a>')+'<div class="product-grid main-products">'+''.join(product_card(p,'main') for p in data['skus'])+'</div></section></article>'
shop=shop.replace('<div class="product-grid main-products">','<p class="shop-source-desc">위의 브랜드 철학과 5대 컬렉션 설계를 바탕으로 완성된 16종 전체 하드웨어를 규칙적인 카탈로그 그리드로 탐색하고 횡단 비교하세요.</p><div class="product-grid main-products">')

# Brand narrative is a separate CSS-routed view, keeping every source section.
bhero=brand.find(id='hero')
story=txt(bhero.find(cls='origin-story-text'))
brandhtml='<article id="brand" class="view brand-view"><section class="brand-intro section-shell"><div class="breadcrumb"><a href="#home">HOME</a><span>OUR STORY / ABOUT HALO</span></div><div class="brand-opening"><div>'+label('A PROTECTIVE RING. A CONTINUOUS MOTION.')+'<h1>ALWAYS<br>IN YOUR<br><em>ORBIT.</em></h1></div><div class="halo-orbit" role="img" aria-label="보호의 고리를 표현하는 금속빛 해무리"><span>HALO<br><small>해무리 / ˈheɪloʊ</small></span></div></div><div class="brand-naming"><h2>당신의 움직임 곁에,<br>보호의 고리.</h2><div>'
nameblock=next(n for n in brand.elements() if n.tag=='div' and 'THE MEANING OF HALO' in n.text())
brandhtml+=render(nameblock)+'<a class="text-link" href="#brand-philosophy">HALO의 세 가지 설계 원칙 보기 ↓</a></div></div></section><section class="brand-photo"><div>'+label('OUR STARTING POINT')+'<h2>우리는 운동을 멈추게 하는<br>선케어를 만들지 않는다.<br><span>운동의 흐름을 이어주는<br>노터치 선케어 기어를 설계한다.</span></h2></div><span class="micro">NEVER STOP THE MOTION / HALO KINETIC SUNCARE GEAR</span></section><section class="origin-story section-shell">'+label('THE QUESTION THAT STARTED IT ALL')+'<p>'+E(story)+'</p></section>'
for sid,cls in [('pain-points','pain-section'),('perspective','action-section'),('philosophy','principles-section'),('rnd-process','brand-research'),('sports-environments','environment-section'),('sustainable-materials','sustain-section')]:brandhtml+=section_original(sid,cls,'brand-',brand)
brandhtml+='</article>'

# CSS-only catalog, filters combine with each other. Native form reset resets all filters.
catalog='<article id="catalog" class="view catalog-view"><section class="catalog-banner"><div><div class="breadcrumb"><a href="#home">HOME</a><span>SHOP ALL / 16 GEARS</span></div>'+label('FIVE FIELDS. ONE CONTINUOUS MOTION.')+'<h1>FIND YOUR<br>EVERYDAY GEAR.</h1><p>5대 스포츠 극한 환경 속,<br>모션을 멈추지 않는 하드웨어 기어 시스템</p></div><span class="catalog-banner-note">NO-TOUCH. NO DISTRACTIONS.</span></section><form class="catalog-layout section-shell"><aside class="catalog-sidebar"><div class="filter-title">FILTER <button type="reset">초기화 ↺</button></div>'
filters=[('sport','스포츠 컬렉션',[('all','전체 기어 · 16')]+[(k,c[2]+' · '+str(c[3])) for k,c in cols.items()]),('phase','운동 단계',[('all','전체 단계'),('Pre','운동 전 · Pre'),('In','운동 중 · In'),('Post','운동 후 · Post')]),('type','제품 제형',[('all','전체 제형')]+[(x,x) for x in ['스틱','미스트','젤','크림','밤','패치']]),('func','핵심 기능',[('all','전체 기능')]+[(x,x) for x in ['쿨링','휴대','방수','세범']])]
filtercss=''
for group,title,options in filters:
 catalog+='<fieldset><legend>'+title+'</legend>'
 for v,text in options:
  id='f-'+group+'-'+v
  catalog+='<label class="filter-option"><input type="radio" id="'+id+'" name="'+group+'" value="'+v+'"'+(' checked' if v=='all' else '')+'><span>'+E(text)+'</span></label>'
  if v!='all':
   attr='col' if group=='sport' else group
   match='[data-'+attr+('="'+v+'"]' if group in ['sport','type'] else '*="'+v+'"]')
   if group=='phase':match+=':not([data-phase="All"])'
   filtercss+='.catalog-layout:has(#'+id+':checked) .product-card:not('+match.split(':not')[0]+')'+(':not([data-phase="All"])' if group=='phase' else '')+'{display:none}\n'
 catalog+='</fieldset>'
catalog+='<a href="#comparison" class="text-link">16종 스펙 비교표 ↗</a><p class="fine-print">제품명·제형·수치는 가상 제품 설계 정보입니다.</p></aside><div class="catalog-results"><div class="catalog-toolbar"><div><span class="micro">ALL GEARS /</span> <strong>내 움직임을 위한 기어</strong></div><label class="sort-control">정렬 <select name="sort" aria-label="상품 정렬"><option value="default">기어 번호순</option><option value="low">낮은 가격순</option><option value="high">높은 가격순</option></select></label></div><div class="product-grid catalog-products">'+''.join(product_card(p,'catalog') for p in data['skus'])+'</div><div class="empty-results"><span>∅</span><h2>선택하신 조건에 일치하는 기어가 없습니다</h2><p>다른 컬렉션이나 운동 단계를 선택해 보세요.</p><button class="button" type="reset">필터 초기화 ↺</button></div><div class="catalog-end"><span>HALO KINETIC GEAR LAB / COLLECTION 01—05</span><span>END OF THE EDIT.</span></div></div></form>'
for p in data['skus']:
 choices={'sport':['all',p['col']],'phase':['all']+(['Pre','In','Post'] if p['phase']=='All' else p['phase'].split('/')),'type':['all',p['type']],'func':['all']+p['func'].split()}
 filtercss+='.catalog-layout'+''.join(':has(:is('+','.join('#f-'+key+'-'+x for x in values)+'):checked)' for key,values in choices.items())+' .empty-results{display:none}\n'
 i=p['id'];rank=sorted(x['rawPrice'] for x in data['skus']).index(p['rawPrice'])
 filtercss+='.catalog-layout:has(select[name="sort"] option[value="low"]:checked) .product-card[data-price="'+str(p['rawPrice'])+'"]{order:'+str(rank)+'}.catalog-layout:has(select[name="sort"] option[value="high"]:checked) .product-card[data-price="'+str(p['rawPrice'])+'"]{order:'+str(100-rank)+'}'
 # No remote calls and no product omitted: detailed source and catalog specifications are static.
 catalog+='<section class="product-modal" id="gear-'+str(i)+'" aria-labelledby="gear-title-'+str(i)+'"><div class="modal-top"><a class="logo" href="#home">HALO</a><a class="close-link" href="#catalog">전체 기어로 돌아가기 <span aria-hidden="true">×</span></a></div><div class="product-detail-main"><div>'+sprite(i)+'</div><div class="product-detail-copy">'+label(cols[p['col']][1]+' / GEAR '+str(i).zfill(2))+'<h2 id="gear-title-'+str(i)+'">'+E(p['name'])+'</h2><p>'+E(p['feature'])+'</p><div class="detail-price">'+p['price']+' <small>'+p['vol']+'</small></div><dl class="facts">'
 for title,key in [('컬렉션 역할','roleName'),('파생 기준','relation'),('추천 상황','scenario'),('사용 단계','phase'),('제품 제형','type'),('핵심 기능','func'),('지속 기준','dur'),('성능 목표 · 가상 정보','clinical')]:catalog+='<div><dt>'+title+'</dt><dd>'+E(p[key])+'</dd></div>'
 catalog+='</dl>'+button('#launch','15% 얼리버드 출시 알림')+'<p class="fine-print">가상 브랜드의 제품 디자인 예시입니다. 제품 이미지의 패키지 문구와 실제 사양은 다를 수 있습니다.</p></div></div><div class="product-detail-extra section-shell"><div class="texture-panel"><div class="texture-art" role="img" aria-label="수분과 금속의 표면 질감을 표현한 이미지"><span>'+('CRYO / −4.2°C' if i==1 else 'FORMULA / HALO')+'</span></div><div>'+label('TEXTURE & PERFORMANCE')+'<h3>'+('손에는 남기지 않고,<br>피부에는 가볍게.' if '세범' in p['func'] or i==1 else '움직임을 고려한<br>정교한 사용감.')+'</h3><p>'+E(p['feature'])+'</p><p>'+E(p['clinical'])+'</p><p class="fine-print">제품 설계 단계의 가상 성능 목표</p></div></div>'+accord('제품 상세 정보 · 적용 부위와 소재',old_card_content(i),True)
 q=data['quick'][str(i)]
 catalog+=accord('사용 가이드 · 8대 사양','<dl class="facts">'+''.join('<div><dt>'+title+'</dt><dd>'+E(q[key])+'</dd></div>' for title,key in [('상품명','name'),('컬렉션','cvol'),('용량','vol'),('가격','price'),('사용 단계','phase'),('제형','type'),('적용 부위','part'),('지속력','dur'),('기능','func'),('제품 설명','feature'),('가상 성능','clinical')])+'</dl>')
 catalog+='<div class="related-heading">'+label('PAIR IT WITH')+'<h3>함께 움직이는 기어.</h3></div><div class="product-grid related-products">'+''.join(product_card(x,'related') for x in data['skus'] if x['col']==p['col'] and x['id']!=i)+'</div></div></section>'
catalog+='</article>'

comparison='<section id="comparison" class="overlay comparison-overlay"><div class="overlay-panel"><div class="modal-top">'+label('THE FULL SPECIFICATION')+'<a class="close-link" href="#catalog">닫기 ×</a></div><h2>16종 기어 횡단 스펙 비교</h2><p>컬렉션·운동 단계·제형·적용 부위·지속력·기능·용량·가격을 한눈에 비교하세요.</p><div class="table-scroll"><table><caption>HALO 전체 16종 가상 제품 사양 · 표를 좌우로 스크롤해 모든 사양을 확인할 수 있습니다.</caption><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in ['기어','컬렉션','운동 단계','제형','적용 부위','지속력','핵심 기능','용량','가격'])+'</tr></thead><tbody>'
for p in data['skus']:
 q=data['quick'][str(p['id'])];comparison+='<tr><th scope="row"><a href="#gear-'+str(p['id'])+'">'+str(p['id']).zfill(2)+' '+E(p['name'])+' ↗</a></th>'+''.join('<td>'+E(v)+'</td>' for v in [cols[p['col']][2],p['phase'],p['type'],q['part'],p['dur'],p['func'],p['vol'],p['price']])+'</tr>'
comparison+='</tbody></table></div><p class="fine-print">본 페이지의 제품·수치·임상·사용자 데이터는 포트폴리오 설계를 위한 가상 정보입니다.</p></div></section>'

launch='''<section id="launch" class="overlay launch-overlay"><div class="launch-panel"><a class="close-link" href="#home">닫기 ×</a><span class="eyebrow">BE THE FIRST TO MOVE.</span><h2>YOUR NEXT<br>MOVE STARTS<br><em>HERE.</em></h2><h3>빠른 출시 알림 신청</h3><p>관심 기어의 출시 소식과 15% 얼리버드 혜택을 가장 먼저 만나보세요.</p><p class="fine-print">가상 브랜드의 신청 화면 예시입니다. 입력 정보는 전송·저장되지 않으며 실제 출시 알림은 접수되지 않습니다.</p><form action="#launch-preview" method="get"><label>관심 기어<select aria-label="관심 기어"><option>전체 라인업</option>'''+''.join('<option>'+E(p['name'])+'</option>' for p in data['skus'])+'''</select></label><label>이름<input type="text" placeholder="이름을 입력해 주세요" autocomplete="off" required></label><label>이메일<input type="email" placeholder="you@example.com" autocomplete="off" required></label><label>휴대전화 <span class="optional">선택</span><input type="tel" placeholder="010-0000-0000" autocomplete="off"></label><label class="consent"><input type="checkbox" required><span>출시 알림 및 혜택 안내를 위한 개인정보 수집·이용에 동의합니다.</span></label><details class="privacy"><summary>개인정보 수집·이용 내용</summary><p>수집 목적: 출시 일정 및 얼리버드 혜택 안내<br>수집 항목: 이름, 이메일, 휴대전화(선택)<br>본 예시에서는 입력 정보를 저장하거나 전송하지 않습니다.</p></details><button class="button" type="submit">15% 알림 신청하기 <span>↗</span></button></form></div></section><section id="launch-preview" class="overlay"><div class="launch-panel"><a class="close-link" href="#home">닫기 ×</a><span class="eyebrow">HALO / FORM PREVIEW</span><h2>READY FOR<br>YOUR NEXT<br>MOVE.</h2><h3>입력 확인이 완료되었습니다.</h3><p>디자인 미리보기입니다. 실제 신청은 접수되지 않았으며 입력 정보는 저장되지 않았습니다.</p>'''+button('#catalog','16종 기어 계속 둘러보기')+'''</div></section>'''

origfooter=main.find(tag='footer')
footer='''</main><footer class="site-footer"><div class="footer-top"><div><span class="eyebrow">READY WHEN YOU ARE.</span><h2>NEVER STOP<br>THE MOTION.</h2></div><div><p>운동의 흐름을 멈추지 않는 선케어 기어.<br>당신의 다음 움직임에 HALO가 함께합니다.</p>'''+button('#launch','15% 얼리버드 출시 알림',True)+'''</div></div><div class="footer-links"><div><span class="micro">EXPLORE</span><a href="#brand">브랜드 이야기</a><a href="#catalog">16종 전체 기어</a><a href="#process">기술 · 검증</a><a href="#routine">운동 전·중·후 루틴</a></div><div><span class="micro">COLLECTIONS</span>'''+''.join('<a href="#collections">'+c[2]+'</a>' for c in cols.values())+'''</div><div><span class="micro">GEAR SUPPORT</span><a href="#comparison">전체 스펙 비교</a><a href="#launch">출시 알림 신청</a><details><summary>브랜드 · 고객지원 정보 ＋</summary><div class="footer-source">'''+render(origfooter,'footer-')+'''</div></details></div><div class="footer-note"><span class="micro">HALO KINETIC GEAR LAB</span><p>NO-TOUCH COOLING<br>SUNCARE GEAR</p><p>제품·수치·임상·사용자 데이터는<br>포트폴리오 설계를 위한 가상 정보입니다.</p></div></div><div class="footer-wordmark" aria-hidden="true">HALO<span>®</span></div><div class="footer-bottom"><span>© 2026 HALO. ALL RIGHTS RESERVED.</span><span>ENGINEERED FOR MOTION.</span><a href="#home">BACK TO TOP ↑</a></div></footer></body></html>'''

css=(HERE/'halo-design.css').read_text(encoding='utf-8')
html=head+asset_css+css+filtercss+'</style></head><body>'+nav+hero+philosophy+flagships+process+routine+collections+shop+brandhtml+catalog+comparison+launch+footer
mobile='<nav id="mobile-menu" class="overlay mobile-menu-panel" aria-label="모바일 전체 메뉴"><div class="launch-panel"><a class="close-link" href="#home">닫기 ×</a><span class="eyebrow">HALO / EXPLORE</span>'+''.join('<a href="#'+href+'">'+text+' <span>↗</span></a>' for href,text in [('catalog','전체 기어 · 16'),('brand','브랜드 이야기'),('collections','5대 스포츠 컬렉션'),('process','기술과 검증'),('routine','운동 전·중·후 루틴'),('comparison','기어 스펙 비교'),('launch','15% 출시 알림')])+'</div></nav>'
html=html.replace('</main>',mobile+'</main>')
# Normalize section links that originate in copied specifications.
doc=Parser(html).root
ids={n.attrs['id'] for n in doc.nodes() if 'id' in n.attrs}
for n in doc.nodes():
 if n.tag=='a':
  h=n.attrs.get('href','')
  if h.startswith('#') and h[1:] not in ids:
   target=re.sub(r'^(?:spec[12]-|footer-)','',h[1:])
   n.attrs['href']='#'+target if target in ids else '#catalog'
html='<!DOCTYPE html>\n'+doc.html().removeprefix('&lt;!DOCTYPE html&gt;')
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(html,encoding='utf-8')
print('Saved:',OUT,'|',len(html.encode('utf-8')),'bytes')
print('Static product inventory:',len(data['skus']),'| Scripts:',len([n for n in doc.nodes() if n.tag=='script']))
