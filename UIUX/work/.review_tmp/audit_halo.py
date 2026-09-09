from pathlib import Path
from mildo_dom import Parser,Node
import re,json
here=Path(__file__).resolve().parent
base=here.parent/'박찬미/웹사이트'
out=Parser((base/'웹디자인/강사_제작예시.html').read_text(encoding='utf-8')).root.find(tag='body')
def norm(s):return re.sub(r'\s+|[\[\]📷⚙️💡⚡☑️]','',s)
target=norm(out.text());result={}
for fname in ['와이어프레임_시안5_최종.html','브랜드소개_시안3.html']:
 d=Parser((base/'와이어프레임'/fname).read_text(encoding='utf-8')).root.find(tag='body');missing=[];total=0
 for sec in d.elements():
  if sec.tag!='section':continue
  for n in sec.nodes():
   if n.tag in ['script','style','svg','#comment','button','a']:continue
   for child in n.children:
    if isinstance(child,str) and len(child.strip())>45:
     total+=1
     if norm(child) not in target:missing.append({'section':sec.attrs.get('id',''),'text':' '.join(child.split())})
 result[fname]={'total':total,'missing':missing}
(here/'halo-content-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
