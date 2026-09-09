from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).parent
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,args=['--no-proxy-server'])
 page=b.new_page(viewport={'width':1440,'height':1000})
 page.goto('http://madechiel.co.kr/',wait_until='networkidle')
 print(page.evaluate('''()=>[...document.styleSheets].map(s=>s.href)'''))
 for y in range(0,16000,750):
  page.evaluate('(y)=>window.scrollTo(0,y)',y)
  page.wait_for_timeout(250)
 page.evaluate('window.scrollTo(0,0)')
 page.wait_for_timeout(500)
 page.screenshot(path=str(root/'reference-loaded.jpg'),full_page=True)
 for i,y in enumerate([0,1100,2500,4200,5700,7100]):
  page.evaluate('(y)=>window.scrollTo(0,y)',y)
  page.wait_for_timeout(700)
  page.screenshot(path=str(root/f'ref-{i}.jpg'))
 styles=page.evaluate('''()=>[...document.querySelectorAll('body *')].filter(e=>e.children.length===0&&e.textContent.trim()).map(e=>({text:e.textContent.trim().slice(0,60),cls:e.className,size:getComputedStyle(e).fontSize,color:getComputedStyle(e).color,font:getComputedStyle(e).fontFamily}))''')
 print(json.dumps(styles[:65],ensure_ascii=False))
 b.close()
