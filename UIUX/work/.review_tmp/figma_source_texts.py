import json
from figma_prepare import d,BASE
from mildo_dom import Node
out=[]
def walk(n):
 if n.tag in ('script','style','#comment','svg'):return
 for c in n.children:
  if isinstance(c,Node):walk(c)
  elif len(c.strip())>1:out.append(c.strip())
walk(d.find(tag='body'))
(BASE/'figma_source_texts.json').write_text(json.dumps(out,ensure_ascii=False),encoding='utf-8')
print(len(out))
