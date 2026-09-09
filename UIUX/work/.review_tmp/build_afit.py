from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parent
source=root.parent/'허지민/와이어프레임/메인페이지_와이어프레임_시안5_최종.html'
target=root.parent/'허지민/웹디자인/강사_제작예시.html'
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True)
 page=browser.new_page()
 page.route('http**/*',lambda route:route.abort())
 page.goto(source.as_uri(),wait_until='domcontentloaded')
 data={key:json.loads((root/(filename+'.json')).read_text(encoding='utf-8')) for key,filename in [('curation','curationData'),('products','quickViewData')]}
 html=page.evaluate((root/'build_afit.js').read_text(encoding='utf-8'),data)
 css=(root/'afit-design.css').read_text(encoding='utf-8')
 html=html.replace('</head>','<style>\n'+css+'\n</style>\n</head>')
 target.write_text(html,encoding='utf-8')
 print(target, target.stat().st_size)
 browser.close()
