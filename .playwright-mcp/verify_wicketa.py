from pathlib import Path
from html.parser import HTMLParser
import re,json,hashlib

base=Path(__file__).resolve().parents[1]/'UIUX/work/이지희/웹사이트'
a=(base/'와이어프레임/메인페이지_와이어프레임_시안5.html').read_bytes()
b=(base/'와이어프레임/메인페이지_와이어프레임_시안6_최종.html').read_bytes()
design=(base/'웹디자인/강사_제작예시.html').read_text(encoding='utf8')
class Inspector(HTMLParser):
    def __init__(self,s):
        super().__init__();self.tags=[];self.attrs=[];self.feed(s)
    def handle_starttag(self,t,a):self.tags.append(t);self.attrs.extend(a)

ia=Inspector(a.decode());ib=Inspector(b.decode());di=Inspector(design)
report={
 'source_unchanged':hashlib.sha256(a).hexdigest()=='7dca607410f8c2d69e467c7ab12c048b45ee76d34470ff621725b1c05029b4ed',
 'wireframe_markup_unchanged':ia.tags==ib.tags and ia.attrs==ib.attrs,
 'wireframe_scripts_unchanged':re.findall(rb'<script.*?</script>',a,re.S)==re.findall(rb'<script.*?</script>',b,re.S),
 'wireframe_styles_unchanged':re.findall(rb'<style.*?</style>',a,re.S)==re.findall(rb'<style.*?</style>',b,re.S),
 'design_no_scripts':'script' not in di.tags,
 'design_no_event_attributes':not any(k.startswith('on') for k,v in di.attrs),
 'design_no_javascript_links':not any(v and v.startswith('javascript:') for k,v in di.attrs),
 'design_no_external_assets':not any(k in ('src','href') and v and v.startswith(('https://','http://')) for k,v in di.attrs),
 'design_no_template_expressions':'${' not in design,
 'wireframe_bytes':len(b),'design_bytes':len(design.encode())
}
assert all(v for k,v in report.items() if isinstance(v,bool)),report
print(json.dumps(report,ensure_ascii=False,indent=2))
(Path(__file__).parent/'wicketa-final-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
