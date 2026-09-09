from mildo_dom import *
import re, base64, struct

p=SOURCE.parent.parent/'웹디자인/강사_제작예시.html'
d=Parser(p.read_text(encoding='utf-8')).root
css=d.find(tag='style').text()
stripped=re.sub(r'''/\*.*?\*/|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*' ''', '', css, flags=re.S|re.X)
stack=[]; pairs={'}':'{',')':'(',']':'['}
for c in stripped:
    if c in '{([': stack.append(c)
    elif c in '})]': assert stack and stack.pop()==pairs[c], f'Unbalanced CSS: {c}'
assert not stack
images=re.findall(r'data:image/png;base64,([A-Za-z0-9+/=]+)',css)
print('CSS delimiters: balanced')
print('Embedded PNG dimensions:',[struct.unpack('>II',base64.b64decode(v)[16:24]) for v in images])
print('Main sections:',[n.attrs.get('id') for n in d.nodes() if n.tag=='section'])
assert all(n.find(tag='h3') and n.find(tag='p') for n in d.nodes() if n.cls('diagnosis-answer'))
print('Diagnosis: all 6 results contain headings and descriptions')
assert len(re.findall(r'--cart-total:',css))==16
assert len(re.findall(r' \.answer-\d\{display:block\}',css))==81
print('CSS selection states: 16 cart combinations, 81 diagnosis combinations')
assert all(n.attrs.get('type')=='reset' for n in d.nodes() if n.tag=='button')
assert all(not n.attrs.get('action') for n in d.nodes() if n.tag=='form')
print('Forms: no data submission or checkout endpoint')
print('File size:',round(p.stat().st_size/1024/1024,2),'MiB')
