from html.parser import HTMLParser
from html import escape
from pathlib import Path

VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
class Node:
    def __init__(self, tag='', attrs=None, children=None):
        self.tag, self.attrs, self.children = tag, dict(attrs or []), children or []
        self.parent = None
    def add(self, child):
        self.children.append(child)
        if isinstance(child, Node): child.parent = self
        return child
    def text(self):
        return ''.join(c.text() if isinstance(c, Node) else c for c in self.children)
    def nodes(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.nodes()
    def cls(self, name): return name in self.attrs.get('class','').split()
    def addclass(self, name): self.attrs['class'] = (self.attrs.get('class','')+' '+name).strip()
    def find(self, *, tag=None, cls=None, id=None):
        return next((n for n in self.nodes() if (not tag or n.tag==tag) and (not cls or n.cls(cls)) and (not id or n.attrs.get('id')==id)), None)
    def elements(self): return [n for n in self.children if isinstance(n,Node)]
    def html(self):
        if self.tag == '#comment': return '<!--'+self.text()+'-->'
        if not self.tag: return ''.join(c.html() if isinstance(c,Node) else escape(c, quote=False) for c in self.children)
        a=''.join(' '+k+('="'+escape(str(v), quote=True)+'"' if v is not None else '') for k,v in self.attrs.items())
        if self.tag in VOID: return '<'+self.tag+a+'>'
        content=''.join(c.html() if isinstance(c,Node) else (c if self.tag in ('style','script') else escape(c,quote=False)) for c in self.children)
        return '<'+self.tag+a+'>'+content+'</'+self.tag+'>'
class Parser(HTMLParser):
    def __init__(self,s):
        super().__init__(convert_charrefs=True)
        self.root=Node(); self.stack=[self.root]; self.feed(s)
    def handle_starttag(self,t,a):
        n=self.stack[-1].add(Node(t,a))
        if t not in VOID: self.stack.append(n)
    def handle_startendtag(self,t,a): self.stack[-1].add(Node(t,a))
    def handle_endtag(self,t):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==t:
                self.stack=self.stack[:i]; break
    def handle_data(self,d): self.stack[-1].add(d)
    def handle_comment(self,d): self.stack[-1].add(Node('#comment',children=[d]))

def fragment(s): return Parser(s).root.elements()[0]
SOURCE=Path(__file__).resolve().parents[1]/'이은수/웹사이트/와이어프레임/와이어프레임_시안7_최종.html'
if __name__=='__main__':
    doc=Parser(SOURCE.read_text(encoding='utf-8')).root
    for sec in doc.find(tag='body').elements():
        if sec.tag in ('script','#comment'): continue
        print('\nSECTION',sec.tag,sec.attrs.get('id',''),sec.attrs.get('class',''))
        def outline(n, depth=0):
            if n.tag in ('svg','#comment','path','circle','style'): return
            print('  '*depth+n.tag+' '+n.attrs.get('class','')+' #'+n.attrs.get('id','')+' '+ (' '.join(n.text().split())[:140] if not n.elements() or n.tag in ('h1','h2','h3','h4','p') else ''))
            if depth<3:
                for c in n.elements(): outline(c,depth+1)
        outline(sec)
