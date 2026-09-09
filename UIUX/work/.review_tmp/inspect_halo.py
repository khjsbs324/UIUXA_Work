from mildo_dom import Parser,Node
from pathlib import Path
base=Path(__file__).resolve().parents[1]/'박찬미/웹사이트/와이어프레임'
for fname in ['와이어프레임_시안5_최종.html','브랜드소개_시안3.html','카테고리_시안2.html']:
 d=Parser((base/fname).read_text(encoding='utf-8')).root.find(tag='body')
 lines=[]
 def walk(n,dep=0):
  if n.tag in ['script','svg','path','#comment','style']:return
  text=' '.join(n.text().split())
  lines.append(' '*dep+n.tag+' '+str(n.attrs)+' '+(text[:220] if not n.elements() or n.tag in ['h1','h2','h3','h4','p'] else ''))
  for c in n.elements():walk(c,dep+1)
 walk(d)
 (base.parent.parent.parent/'.review_tmp'/('halo_'+fname+'.txt')).write_text('\n'.join(lines),encoding='utf-8')
 print(fname)
 for n in d.elements():
  if n.tag not in ['script','#comment']:print(n.tag,n.attrs, ' | '.join(' '.join(x.text().split()) for x in n.nodes() if x.tag in ['h1','h2','h3'])[:1000])
