from pathlib import Path
from playwright.sync_api import sync_playwright
import json

ROOT = Path(__file__).resolve().parent
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-proxy-server'])
    page = browser.new_page(viewport={'width':1440,'height':1000}, device_scale_factor=1)
    page.goto('http://madechiel.co.kr/', wait_until='domcontentloaded', timeout=45000)
    page.wait_for_timeout(4000)
    page.screenshot(path=str(ROOT/'reference-full.jpg'), full_page=True)
    print('REFERENCE', page.title(), page.url)
    print(page.locator('body').inner_text()[:16000])
    data=page.evaluate('''() => [...document.querySelectorAll('h1,h2,h3,section,.section,img')].map(e=>({tag:e.tagName,cls:e.className,text:e.innerText?.slice(0,100),src:e.currentSrc,rect:{w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height},font:getComputedStyle(e).fontFamily,color:getComputedStyle(e).color,bg:getComputedStyle(e).backgroundColor})).filter(e=>e.rect.w>0)''')
    (ROOT/'reference-dom.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    source=ROOT.parent/'허지민/와이어프레임/메인페이지_와이어프레임_시안5_최종.html'
    page.goto(source.as_uri(),wait_until='domcontentloaded')
    print('SOURCE SECTIONS',page.locator('section').evaluate_all('(els)=>els.map(e=>({id:e.id,text:e.innerText}))'))
    for name in ['curationData','quickViewData']:
        (ROOT/(name+'.json')).write_text(json.dumps(page.evaluate(name),ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'source-body.html').write_text(page.locator('body').inner_html(),encoding='utf-8')
    browser.close()
