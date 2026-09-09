import json,re
from figma_prepare import d,BASE
from mildo_dom import Node
p=json.loads((BASE/'figma_plan.json').read_text(encoding='utf-8'))
joined=re.sub(r'\s+','',''.join(i.get('text','') for i in p['items']))
missing=[]
def walk(n):
 if n.tag in ('script','style','#comment','svg'):return
 for c in n.children:
  if isinstance(c,Node):walk(c)
  elif len(c.strip())>1 and re.sub(r'\s+','',c) not in joined:missing.append({'text':c.strip(),'tag':n.tag,'class':n.attrs.get('class'),'id':n.attrs.get('id')})
walk(d.find(tag='body'))
print(json.dumps(missing,ensure_ascii=True,indent=2))
