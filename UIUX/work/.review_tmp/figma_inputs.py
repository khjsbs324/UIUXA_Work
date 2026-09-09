import json
from figma_prepare import d
print(json.dumps([n.attrs for n in d.nodes() if n.tag=='input' and n.attrs.get('type') not in ('checkbox','radio','hidden')],ensure_ascii=True,indent=2))
