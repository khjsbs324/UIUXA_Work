import re,json,math,base64
from pathlib import Path
from PIL import ImageFont
from figma_prepare import d,BASE
from mildo_dom import Node

INK='#33352e'; MUTED='#626357'; CREAM='#fffef2'; LINEN='#e9e5dc'
items=[]; frames=[]; notes=[]; assets={}; texts=[]
font=ImageFont.truetype('C:/Windows/Fonts/malgun.ttf',140)
def cls(n):return n.attrs.get('class','').split()
def style(n):return dict(re.findall(r'([\w-]+)\s*:\s*([^;]+)',n.attrs.get('style','')))
def hidden(n):return any(c in cls(n) for c in ['mobile-announcement-text','gnb-text-short','mobile-only-btn-text','state-controls','skip-link']) or n.tag in ['script','style','#comment'] or (n.tag=='input' and n.attrs.get('type') in ['checkbox','radio','hidden'])
def plain(n,all=False):
 if isinstance(n,str):return re.sub(r'\s+',' ',n)
 if not all and hidden(n):return ''
 if n.tag=='br':return '\n'
 if n.tag in ['svg','path','circle','rect','line','#comment','script','style']:return ''
 return ''.join(plain(c,all) for c in n.children).strip()
def paragraphs(n):
 if n.tag in ['svg','script','style','#comment','input']:return ''
 if n.tag=='br':return '\n'
 out=''.join(paragraphs(c) if isinstance(c,Node) else re.sub(r'\s+',' ',c) for c in n.children)
 return out+ ('\n' if n.tag in ['div','p','h1','h2','h3','h4','li','legend','label','a','summary','fieldset'] else ' ')
def add(kind,name,x,y,w,h,**kw):
 z=dict(key='n'+str(len(items)),kind=kind,name=name,x=round(x,2),y=round(y,2),w=round(w,2),h=round(max(1,h),2),parent=current,**kw);items.append(z);return z
def wrap(s,w,size):
 out=[]
 for para in s.split('\n'):
  line=''
  for word in para.strip().split(' '):
   test=(line+' '+word).strip()
   if font.getlength(test)*size/140*1.075>w and line:out.append(line);line=word
   else:line=test
  out.append(line)
 return '\n'.join(out)
def txt(s,x,y,w,size=14,color=INK,align='LEFT',serif=False,lh=None,spacing=0,name=None):
 s=s.strip()
 if not s:return 0
 lh=lh or size*1.85
 s=wrap(s,w,size)
 h=len(s.split('\n'))*lh+3
 add('text',name or s.replace('\n',' ')[:64],x,y,w,h,text=s,size=size,color=color,align=align,font='Batang' if serif else 'Noto Sans KR',lh=lh,spacing=spacing)
 texts.append(s)
 return h
def rule(x,y,w,color='#c9c9bc'):add('frame','구분선',x,y,w,1,fill=color)
def photo(scene,x,y,w,h=None):
 h=h or w
 add('frame','화보 '+str(scene),x,y,w,h,fill='#d6cdbf',scene=scene)
 return h
def box(n,x,y,w,fs=14,color=INK,align='LEFT',aux=False):
 if hidden(n):return 0
 cs=cls(n); st=style(n)
 if n.tag=='input':
  add('frame','입력 필드 · '+n.attrs.get('id',''),x,y,w,48,stroke='#c9c9bc')
  txt(n.attrs.get('placeholder',''),x+15,y+12,w-30,13,'#77796b',lh=22)
  return 48
 if 'catalog-item' in cs:
  es=n.elements();rule(x,y,w)
  txt(plain(es[0]),x,y+23,35,25,'#959783',serif=True,lh=34)
  txt(plain(es[1].find(tag='strong')),x+55,y+19,w-230,17,lh=27)
  txt(plain(es[1].find(tag='small')),x+55,y+50,w-230,11,MUTED,lh=19)
  txt(plain(es[2]),x+w-155,y+29,155,13,align='RIGHT',lh=23)
  return 88
 if 'cart-row' in cs:
  es=n.elements();xx=x;yy=y+20;rule(x,y,w)
  for c in es:
   if c.cls('editorial-photo'):box(c,xx,yy,90,fs,color,align,aux);xx+=110
   else:box(c,xx,yy,w-110,fs,color,align,aux)
  return 170
 if 'product-grid-4' in cs:
  cw=(w-84)/4
  for j,card in enumerate(n.elements()):
   xx=x+j*(cw+28);cy=y
   txt(plain(card.find(cls='product-card-top')),xx,cy,cw,10,MUTED,lh=18)
   cy+=54;box(card.find(cls='editorial-photo'),xx,cy,cw);cy+=cw+12
   txt(paragraphs(card.find(cls='product-caption')).strip(),xx,cy,cw,10,'#8b897b','CENTER',lh=17)
   cy+=76;txt(plain(card.find(cls='product-card-title')),xx,cy,cw,18,align='CENTER',lh=28)
   cy+=45;txt(plain(card.find(cls='product-card-desc')),xx,cy,cw,13,MUTED,'CENTER',lh=24.7)
   cy+=86;rule(xx,cy,cw);txt(plain(card.find(cls='product-card-notes')),xx,cy+13,cw,10,MUTED,lh=18)
   cy+=65;txt(plain(card.find(cls='product-card-tpo')),xx,cy,cw,11,MUTED,lh=20)
   cy+=52;rule(xx,cy,cw)
   foot=card.find(cls='product-card-footer');e=foot.elements()[0].elements()
   txt(plain(e[0]),xx,cy+19,cw,18,lh=27)
   txt(plain(e[1]),xx,cy+52,cw,11,MUTED,lh=19)
   for k,b in enumerate(foot.elements()[-1].elements()):
    bw=(cw-8)/2;bx=xx+k*(bw+8);by=cy+90
    add('frame','상품 버튼 · '+plain(b),bx,by,bw,44,stroke='#a5a698')
    txt(plain(b),bx+15,by+12,bw-30,12,lh=20)
  return cy+134-y
 if n.tag=='svg':
  h=150 if 'module-drawing' in cs else 24
  add('svg','모듈 도식' if h==150 else '아이콘',x,y,w if h==150 else 24,h,svg=n.html().replace('currentColor','#8a8066'))
  return h+22 if h==150 else h
 if n.tag=='details' and not aux:
  notes.append(n)
  rule(x,y,w)
  return txt(plain(n.find(tag='summary'))+'  +',x,y+12,w,11,MUTED)+24
 if 'editorial-photo' in cs:
  scene=next(int(c.split('-')[1]) for c in cs if c.startswith('scene-'))
  return photo(scene,x,y,w)
 if n.tag in ['select','textarea']:
  s=plain(n) or n.attrs.get('placeholder','')
  add('frame','입력 필드',x,y,w,54,fill=CREAM,stroke='#a5a698')
  txt(s,x+16,y+12,w-32,13)
  return 62
 if 'ingredient-character' in cs:
  return txt(plain(n),x,y,w,76,'#b4ac99',serif=True,lh=88)+16
 fs=float(st.get('font-size',str(fs)).replace('px','')) if re.fullmatch(r'[\d.]+(?:px)?',st.get('font-size','')) else fs
 if n.tag in ['h1','h2','h3','h4','legend']:fs={'h1':43.2,'h2':33.12,'h3':22,'h4':18,'legend':18}[n.tag]
 if 'section-tag' in cs:fs=11;color=MUTED
 if 'section-title' in cs:fs=33.12
 if 'product-badge' in cs:fs=11
 if 'level-index' in cs:fs=56;color='#9b9d87'
 if 'process-index' in cs:fs=42;color='#94947f'
 if 'story-price-val' in cs:fs=23
 if 'product-card-title' in cs:fs=19
 if any(c in cs for c in ['product-card-notes','product-card-tpo','product-caption']):fs=11
 if n.tag=='p':color=MUTED if color==INK else color
 if 'section-header' in cs:
  ww=min(w,850); yy=y
  for c in n.elements():yy+=box(c,x+(w-ww)/2,yy,ww,fs,color,'CENTER',aux)+ (18 if c.tag!='p' else 0)
  return yy-y+44
 if any(c.startswith('btn-') and c!='btn-dual-wrap' for c in cs) or 'quiz-option' in cs:
  label=plain(n)
  ss=13 if 'quiz-option' not in cs else 13
  h=max(54,len(wrap(label,w-46,ss).split('\n'))*22+32)
  add('frame','버튼 · '+label[:45],x,y,w,h,fill=CREAM if aux else None,stroke='#a5a698')
  txt(label,x+23,y+(h-len(wrap(label,w-46,ss).split('\n'))*22)/2,w-46,ss,color,lh=22)
  return h
 children=[c for c in n.elements() if not hidden(c)]
 inline={'span','strong','b','em','br','small','u','i'}
 if n.tag in ['h1','h2','h3','h4','p','span','strong','small','a','label','legend','summary'] or (not children) or all(c.tag in inline for c in children):
  s=plain(n)
  is_serif='hero-main-title' in cs or ('section-title' in cs and n.parent.cls('epilogue-inner'))
  if is_serif and n.tag=='h2':fs=38.8
  lh=fs*1.55 if n.tag in ['h1','h2','h3','h4','legend'] or 'section-title' in cs else fs*1.85
  margin=24 if n.tag in ['h1','h2'] else (12 if n.tag in ['h3','h4','p','legend'] else 0)
  return txt(s,x,y,w,fs,color,align,is_serif,lh,1.3 if 'section-tag' in cs else 0)+margin
 # Container geometry is calculated explicitly; no Figma Auto Layout is used.
 gap=10; pad=0; top=0; bottom=0; columns=None; widths=None; center=False
 if 'container' in cs:
  if n.parent.attrs.get('id') not in ['manifesto','story-1','story-2','story-3','discovery','atelier-booking']:pad=64.8
 if 'editorial-copy' in cs or 'discovery-text-col' in cs:pad=76.3;top=35;bottom=35;gap=22;center=False;fs=15
 if 'manifesto-layout' in cs:columns=2;gap=0;widths=[1.05,1];center=True
 if 'signature-intro' in cs:columns=2;gap=0;widths=[1.07,1];center=True
 if 'signature-intro' in cs and n.parent.parent.attrs.get('id')=='story-2':children=children[::-1];widths=[1,1.07]
 if 'discovery-grid' in cs:columns=2;gap=0;children=children[::-1];widths=[1.05,1];center=True
 if 'service-row' in cs:
  columns=2;gap=0;widths=[1.05,1];center=True
  if n is n.parent.elements()[1]:children=children[::-1];widths=[1,1.05]
 if 'service-list' in cs:gap=100
 if 'grid-2' in cs:columns=2;gap=48
 if 'grid-3' in cs:columns=3;gap=40
 if 'grid-4' in cs:columns=4;gap=30
 if 'level-comparison' in cs:columns=3;gap=48;children=[c for c in children if not c.cls('level-footnote')]
 if 'level-card' in cs:gap=24
 if 'manifesto-answers' in cs:gap=0
 if n.parent.cls('manifesto-answers'):top=20;bottom=20;gap=10;rule(x,y,w)
 if n.parent.cls('level-card') and n is n.parent.elements()[2]:gap=18
 if n.parent.parent and n.parent.parent.cls('level-card') and n.parent is n.parent.parent.elements()[2]:gap=3
 if 'scent-experience' in cs:top=28;gap=24;rule(x,y,w)
 if 'story-action-bar' in cs:columns=len(children);gap=22;top=18;bottom=20;widths=[1]*len(children)
 if 'story-price-info' in cs:gap=3
 if 'ingredient-notes' in cs:pad=64.8;top=65;gap=65
 if 'ingredient-panel' in cs:gap=16;rule(x,y,w)
 if 'layering-guide' in cs:pad=64.8;top=65;gap=26
 if n.parent.cls('layering-steps'):rule(x,y,w);top=24;gap=24
 if 'modular-guide' in cs:pad=64.8;top=65;gap=24
 if n.parent.cls('modular-parts'):rule(x,y,w);top=24;gap=12
 if 'object-specs' in cs:pad=64.8;top=45;gap=65
 if n.parent.cls('object-specs'):rule(x,y,w);top=25;gap=18
 if 'process-layout' in cs:columns=2;gap=64;widths=[.9,1.1];center=True
 if 'process-steps' in cs:columns=2;gap=36
 if 'process-step' in cs:rule(x,y,w);top=24;gap=20
 if 'product-grid-4' in cs:columns=4;gap=28
 if 'product-card' in cs:gap=24
 if 'product-card-top' in cs:gap=6;bottom=16
 if 'product-card-thumb' in cs:gap=0;bottom=20
 if 'product-caption' in cs:top=10;bottom=10
 if 'product-card-footer' in cs:rule(x,y,w);top=20;gap=20
 if 'photo-caption' in cs:pad=32;top=20;bottom=20;gap=10
 if 'epilogue-inner' in cs:align='CENTER';gap=26
 if 'epilogue-paths' in cs:columns=2;gap=64;top=40;bottom=25;align='LEFT'
 if 'epilogue-path' in cs:top=26;bottom=26;rule(x,y,w);gap=25
 if 'footer-grid' in cs:columns=4;gap=48;widths=[1.35,1,1,1];bottom=35
 if 'btn-dual-wrap' in cs:columns=len(children);gap=12
 if n.tag=='fieldset':gap=12;top=18;bottom=18
 if 'modal-sheet' in cs:pad=45;top=45;bottom=35;gap=24
 if 'close-link' in cs:return 0
 # Preserve intentional inline specification rows; avoid squeezing long paragraphs.
 if 'inline-grid' in cs:
  columns=len(children);gap=12;widths=[.26,.74] if len(children)==2 else None
 elif not columns and st.get('display')=='flex' and st.get('flex-direction')!='column' and len(children)==2 and all(c.tag in inline or c.tag in ['h3','h4'] for c in children):
  columns=2;gap=12;widths=[.68,.32]
 if 'display' in st and st['display']=='flex' and st.get('flex-direction')=='column' and gap==10:
  gap=float(st.get('gap','10px').replace('px','')) if re.fullmatch(r'[\d.]+px',st.get('gap','')) else 10
 xx=x+pad; yy=y+top; ww=w-2*pad
 if columns:
  usable=ww-gap*(columns-1);weights=widths or [1]*columns
  sizes=[usable*a/sum(weights) for a in weights]
  for start in range(0,len(children),columns):
   row=children[start:start+columns]; rowitems=[]; heights=[]; cx=xx
   for j,c in enumerate(row):
    begin=len(items);h=box(c,cx,yy,sizes[j],fs,color,align,aux);rowitems.append((begin,len(items)));heights.append(h);cx+=sizes[j]+gap
   mh=max(heights,default=0)
   if center:
    for (a,b),h in zip(rowitems,heights):
     for it in items[a:b]:it['y']=round(it['y']+(mh-h)/2,2)
   yy+=mh+gap
  if children:yy-=gap
 else:
  for i,c in enumerate(children):
   h=box(c,xx,yy,ww,fs,color,align,aux)
   if h:yy+=h+gap
  if children:yy-=gap
 if 'level-comparison' in cs:
  yy+=30+box(n.find(cls='level-footnote'),xx,yy+30,ww,12,MUTED,aux=aux)
 return yy-y+bottom

def frame(name,x,y,w,h,fill=CREAM):
 global current
 key='f'+str(len(frames));frames.append(dict(key=key,name=name,x=x,y=y,w=w,h=h,fill=fill));current=key;return frames[-1]

# Exact HTML image payloads, retained unchanged.
html=(BASE.parent/'이은수/웹사이트/웹디자인/강사_제작예시.html').read_text(encoding='utf-8')
for name in ['hero','atlas','gift']:
 b64=re.search(r'--'+name+r'-image:url\([\"\']?data:image/png;base64,([^\"\')]+)',html).group(1)
 path=BASE/('figma_'+name+'.png');path.write_bytes(base64.b64decode(b64));assets[name]=str(path)

body=d.find(tag='body');main=body.find(tag='main')
f=frame('강사_제작예시.html · Desktop 1440',100,100,1440,1000);root=f['key'];yy=0
# Masthead
f=frame('00 · 안내와 내비게이션',0,yy,1440,164);f['parent']=root
add('frame','상단 혜택 바',0,0,1440,38,fill=INK)
txt('혜택    '+plain(body.find(cls='desktop-announcement-text'))+'   →',280,9,880,11,'#f8f6eb','CENTER',lh=18)
txt('SEOUL, KOREA\nHERITAGE & PERFUMERY',64.8,64,250,9,'#707265',lh=16,spacing=1.5)
add('frame','밀도 인장',592,62,39,42,stroke='#8d8d7d')
txt('密',598,67,28,25,serif=True,lh=29)
txt('밀도 (MILDO)',644,56,205,27,serif=True,lh=35)
txt('HAUTE PERFUMERY',646,94,190,8,spacing=2.2,lh=12)
txt('메인 홈       브랜드 소개       전체 16종 카탈로그       디스커버리 킷       선물과 아틀리에',345,127,750,12,align='CENTER',lh=20)
svg=body.find(cls='user-menu-btn').find(tag='svg')
if svg:add('svg','내 계정',1338,73,24,24,svg=svg.html().replace('currentColor',INK))
rule(0,163,1440);yy=164
f=frame('01 · 마패 보틀 메인 화보',0,yy,1440,690);f['parent']=root
photo('hero',0,0,1440,690)
add('frame','화보 음영',0,0,1440,690,gradient=True)
hero=main.find(id='hero');col=hero.find(cls='hero-text-col');cy=103
cy+=txt(plain(col.find(cls='product-badge')),64.8,cy,630,10,'#e0d8c0',spacing=2)+28
cy+=txt(plain(col.find(tag='h1')),64.8,cy,630,43.2,'#fffdf0',serif=True,lh=71.3)+24
cy+=txt(plain(col.find(tag='p')),64.8,cy,630,14,'#eee9db',lh=28)+30
for j,a in enumerate(col.find(cls='hero-btn-wrap').elements()):
 label=plain(a);bw=245 if j==0 else 215;xx=64.8 if j==0 else 321.8
 add('frame','메인 CTA',xx,cy,bw,54,stroke='#a5a08b');txt(label,xx+21,cy+16,bw-42,12,'#fffdf0',lh=20)
txt(plain(col.find(cls='hero-trust-bar')),64.8,cy+82,590,10,'#eee9db',lh=20)
txt('SCROLL TO DISCOVER    ↓',64.8,647,400,9,'#dbd5c6',spacing=2,lh=18)
add('frame','메인 인장',1320,593,48,49,stroke='#c1b18a');txt('密',1330,603,30,26,'#ded5b9',serif=True,lh=30)
yy+=690
det=main.find(cls='hero-production');f=frame('화보 연출 설명 · 닫힌 상태',0,yy,1440,44,'#e8e4da');f['parent']=root
box(det,64.8,0,1310.4);yy+=44
names={'manifesto':'02 · 밀도의 세 가지 해답','mapae-system':'03 · 1·2·3마패 선택 체계','story-1':'04 · 유자 청송','story-2':'05 · 적송 홍화와 레이어링','story-3':'06 · 백단 묵향과 마패 오브제','perfumery-process':'07 · 조향과 공예','discovery':'08 · 디스커버리 킷','curated-showcase':'09 · 큐레이티드 컬렉션','atelier-booking':'10 · 선물과 아틀리에','epilogue':'11 · 밀도의 에필로그'}
for sec in main.elements():
 sid=sec.attrs.get('id')
 if sid not in names:continue
 bg={'mapae-system':'#e9e5dc','story-2':'#e8e4dc','perfumery-process':'#ece9df','curated-showcase':'#f3f1e7'}.get(sid,CREAM)
 f=frame(names[sid],0,yy,1440,1000,bg);f['parent']=root
 h=100+box(sec.find(cls='container'),0,100,1440)+100
 f['h']=math.ceil(h);yy+=f['h']
f=frame('12 · 브랜드 푸터',0,yy,1440,600,'#292a26');f['parent']=root
h=60+box(body.find(tag='footer').find(cls='container'),0,60,1440,12,'#e0dfd1')+45
f['h']=math.ceil(h);yy+=f['h'];frames[0]['h']=yy

# Supplementary HTML states and full original direction text are retained to the right.
ay=100
f=frame('HTML 보조 화면 · 전체 콘텐츠',1640,ay,1240,140,LINEN)
txt('MILDO · 보조 화면과 원본 연출 설명',40,34,1160,25)
txt('강사_제작예시.html의 팝업·진단·카탈로그·펼침 설명 전체',40,88,1160,13,MUTED)
ay+=180
for modal in [n for n in body.elements() if n.cls('css-modal')]:
 mid=modal.attrs.get('id','')
 f=frame('보조 화면 · '+mid,1640,ay,1240,1000)
 txt(mid,40,24,1160,11,MUTED,spacing=1)
 h=64+box(modal,40,64,1160,14,INK,aux=True)+40
 f['h']=math.ceil(h);ay+=f['h']+50
for idx,n in enumerate(notes):
 f=frame('원본 연출 설명 '+str(idx+1)+' · '+plain(n.find(tag='summary')),1640,ay,1240,600,LINEN)
 lines=re.sub(r'\n[ \t]*\n+','\n',paragraphs(n)).strip()
 h=40+txt(lines,40,40,1160,14,MUTED,lh=27)+40
 f['h']=math.ceil(h);ay+=f['h']+35

f=frame('상태별 문구 · 모바일 · 접근성 · 담기 알림',1640,ay,1240,490,LINEN)
txt('상태별 문구와 담기 알림',40,35,1160,24)
txt('본문 바로가기\n첫 주문 한정, 19,000원 웰컴 크레딧 킷\n밀도 철학 알아보기 >\n기획 보기 / 알림 >\n주문 확인 >\n디스커버리 킷이 장바구니에 담겼습니다. (본품 19,000원 웰컴 크레딧 증정)\n장바구니 보기 →',40,104,1160,14,MUTED,lh=38)
ay+=540

# Flatten source containers while retaining each main section and editable leaf layers.
plan={'frames':frames,'items':items,'assets':assets,'height':yy,'auxHeight':ay,'root':root}
(BASE/'figma_plan.json').write_text(json.dumps(plan,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'frames':len(frames),'items':len(items),'mainHeight':yy,'auxHeight':ay,'types':{k:sum(i['kind']==k for i in items) for k in ['text','frame','svg']}}))
