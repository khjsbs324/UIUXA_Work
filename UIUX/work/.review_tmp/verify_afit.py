from pathlib import Path
from playwright.sync_api import sync_playwright
import json,re
root=Path(__file__).resolve().parent
source=root.parent/'허지민/와이어프레임/메인페이지_와이어프레임_시안5_최종.html'
target=root.parent/'허지민/웹디자인/강사_제작예시.html'
with sync_playwright() as p:
 b=p.chromium.launch(headless=True)
 page=b.new_page(viewport={'width':1440,'height':1000},java_script_enabled=False)
 page.goto(source.as_uri(),wait_until='domcontentloaded')
 texts=page.evaluate('''()=>{let w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT),n,a=[];while(n=w.nextNode()){if(!n.parentElement.closest('script,style')&&n.textContent.trim())a.push(n.textContent.trim())}return a}''')
 page.goto(target.as_uri(),wait_until='load')
 fulltext=page.locator('body').text_content();norm=lambda s:re.sub(r'\s+','',s)
 missing=sorted(set(s for s in texts if norm(s) not in norm(fulltext)))
 print('MISSING SOURCE TEXT',json.dumps(missing,ensure_ascii=False))
 print('SECTIONS',page.locator('main section').evaluate_all('(es)=>es.map(e=>e.id)'))
 print('SCRIPT COUNT',page.locator('script').count(),'PRODUCT COUNT',page.locator('.prd-card').count(),'REPORT COUNT',page.locator('.routine-report').count())
 print('INLINE HANDLERS',page.evaluate('''()=>[...document.querySelectorAll('*')].flatMap(e=>[...e.attributes].filter(a=>/^on/i.test(a.name)).map(a=>a.name))'''))
 print('INVALID LINKS',page.locator('a[href^="#"]').evaluate_all('''es=>es.filter(e=>e.hash.length>1&&!document.getElementById(decodeURIComponent(e.hash.slice(1)))).map(e=>({text:e.textContent,href:e.hash}))'''))
 for width in [1440,390]:
  page.set_viewport_size({'width':width,'height':1000})
  page.goto(target.as_uri(),wait_until='load')
  page.screenshot(path=str(root/f'afit-{width}.jpg'),full_page=True)
  page.screenshot(path=str(root/f'afit-top-{width}.jpg'))
  print('LAYOUT',width,page.evaluate('''()=>({doc:document.documentElement.scrollWidth,viewport:innerWidth,height:document.body.scrollHeight,overflow:[...document.querySelectorAll('main *')].filter(e=>{const r=e.getBoundingClientRect();return r.width&&r.right>innerWidth+2&&!e.closest('.hero-stage,.brand-marquee,.ingredient-stage,.fact-stage,svg')}).slice(0,15).map(e=>({tag:e.tagName,cls:e.className,right:e.getBoundingClientRect().right}))})'''))
 page.set_viewport_size({'width':1440,'height':1000})
 for id in ['hero','manifesto','philosophy','science','spotlight','curation','calculator','archive','reviews']:
  page.locator('#'+id).scroll_into_view_if_needed()
  page.screenshot(path=str(root/f'afit-{id}.jpg'))
 page.locator('input[name="filter-cat"][value="sports"]').check(force=True)
 print('FILTER SPORTS',page.locator('.prd-card:visible').count())
 page.locator('input[name="filter-timing"][value="sleep"]').check(force=True)
 print('EMPTY FILTER',page.locator('.prd-card:visible').count(),page.locator('#archiveEmptyState').is_visible())
 page.locator('#archiveFilterNav button[type="reset"]').click()
 print('RESET FILTER',page.locator('.prd-card:visible').count())
 page.locator('#prd-card-01 .formula-detail summary').click()
 print('DETAIL',page.locator('#prd-card-01 .formula-detail-body').is_visible())
 page.locator('input[name="meal-cost"][value="13000"]').check()
 page.locator('#daysSlider').select_option('30')
 print('CALCULATOR',page.locator('.calculation-row:visible').inner_text())
 page.locator('input[name="question-1"][value="6"]').check()
 page.locator('.reports-panel>summary').click()
 print('REPORT',page.locator('.routine-report:visible').count(),page.locator('.routine-report:visible h3').inner_text())
 page.locator('input[name="question-2"][value="4"]').check()
 page.locator('input[name="question-3"][value="5"]').check()
 print('REPORT SELECTIONS',page.locator('.routine-report:visible .selected-timing:visible').inner_text(),page.locator('.routine-report:visible .selected-goal:visible').inner_text())
 page.locator('.btn-gnb').click()
 print('CHECKOUT',page.locator('#checkoutModal').is_visible())
 page.screenshot(path=str(root/'afit-modal.jpg'))
 page.locator('#btnSubmitOrder').click()
 print('PREVIEW',page.locator('#checkout-preview-panel').is_visible())
 print('EXTERNAL ASSETS',page.locator('[src^="http"],link[href^="http"],script').count())
 print('DUPLICATE IDS',page.evaluate('''()=>{let ids=[...document.querySelectorAll('[id]')].map(e=>e.id);return ids.filter((e,i)=>ids.indexOf(e)!==i)}'''))
 for filename in ['curationData','quickViewData']:
  records=json.loads((root/(filename+'.json')).read_text(encoding='utf-8'))
  missing_values=[]
  for i,record in enumerate(records):
   for k,v in record.items():
    clean=re.sub(r'<[^>]*>','',v)
    if norm(clean) not in norm(fulltext):missing_values.append((i,k))
  print('MISSING DATA',filename,missing_values)
 b.close()
