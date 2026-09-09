from pathlib import Path
from mildo_dom import Parser,Node
BASE=Path(__file__).resolve().parent
p=BASE.parent/'이은수/웹사이트/웹디자인/강사_제작예시.html'
d=Parser(p.read_text(encoding='utf-8')).root
out=[]
def dump(n,dep=0):
 if n.tag in ('style','script','svg','#comment'): return
 attrs={k:v for k,v in n.attrs.items() if k in ('id','class','style')}
 out.append(' '*dep+'<'+n.tag+' '+str(attrs)+'>')
 for c in n.children:
  if isinstance(c,Node):dump(c,dep+1)
  elif c.strip():out.append(' '*(dep+1)+c.strip())
dump(d.find(tag='body'))
(BASE/'figma_source.txt').write_text('\n'.join(out),encoding='utf-8')
print(len(out))
