const {chromium}=require('../이지희/파이프라인/수정 전 파일/05_로고/node_modules/playwright');
const path=require('path'),fs=require('fs'),{pathToFileURL}=require('url');
(async()=>{
 const browser=await chromium.launch({headless:true});const page=await browser.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:1,javaScriptEnabled:false});
 const url=pathToFileURL(path.join(__dirname,'../박찬미/웹사이트/웹디자인/강사_제작예시.html')).href;
 const errors=[],requests=[];page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(/^https?:/.test(r.url()))requests.push(r.url())});
 await page.goto(url);await page.screenshot({path:path.join(__dirname,'halo-home-1440.jpg'),quality:85});
 const structure=await page.evaluate(()=>({scripts:document.scripts.length,handlers:[...document.querySelectorAll('*')].flatMap(e=>[...e.attributes].filter(a=>a.name.startsWith('on'))).length,duplicateIds:[...document.querySelectorAll('[id]')].map(e=>e.id).filter((id,i,a)=>a.indexOf(id)!==i),badLinks:[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>!document.getElementById(h.slice(1))),mainProducts:document.querySelectorAll('.main-products>.product-card').length,catalogProducts:document.querySelectorAll('.catalog-products>.product-card').length,details:document.querySelectorAll('.product-modal').length}));
 const sizes=[];
 for(const w of [1440,390]){
  await page.setViewportSize({width:w,height:1000});
  for(const hash of ['home','philosophy','spotlight','process','routine','collections','shop-all','brand','brand-philosophy','brand-rnd-process','catalog','gear-1']){
   await page.goto(url+'#'+hash);await page.waitForTimeout(150);
   if(['home','brand','catalog','gear-1'].includes(hash))await page.screenshot({path:path.join(__dirname,`halo-${hash}-${w}.jpg`),quality:82});
   if(w===1440&&['philosophy','spotlight','process','routine','collections','brand-philosophy','brand-rnd-process'].includes(hash))await page.screenshot({path:path.join(__dirname,`halo-${hash}-${w}.jpg`),quality:82});
   sizes.push(await page.evaluate(({w,hash})=>({w,hash,overflow:document.documentElement.scrollWidth-innerWidth,view:[...document.querySelectorAll('.view')].filter(e=>getComputedStyle(e).display!=='none').map(e=>e.id),offenders:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>innerWidth+2&&getComputedStyle(e).display!=='none'&&e.getBoundingClientRect().width>0&&!e.closest('.overlay,.product-modal')&&!e.closest('details:not([open])')).slice(0,6).map(e=>[e.tagName,e.className,Math.round(e.getBoundingClientRect().right)])}),{w,hash}));
  }
 }
 await page.goto(url+'#catalog');await page.setViewportSize({width:1440,height:1000});
 await page.check('#f-sport-running');const runningCount=await page.locator('.catalog-products>.product-card:visible').count();
 await page.check('#f-phase-Post');const postCount=await page.locator('.catalog-products>.product-card:visible').count();
 await page.check('#f-type-크림');const emptyCount=await page.locator('.catalog-products>.product-card:visible').count();const emptyMessage=await page.locator('.empty-results').isVisible();
 await page.getByRole('button',{name:'초기화 ↺',exact:true}).click();const resetCount=await page.locator('.catalog-products>.product-card:visible').count();
 await page.selectOption('select[name=sort]','low');const sorted=await page.locator('.catalog-products>.product-card').evaluateAll(es=>es.map(e=>({price:+e.dataset.price,order:+getComputedStyle(e).order})).sort((a,b)=>a.order-b.order).map(e=>e.price));
 const images=await page.evaluate(async()=>{const cs=getComputedStyle(document.documentElement);let out={};for(const k of ['hero','running','catalog']){const v=cs.getPropertyValue('--'+k);const img=new Image();img.src=v.slice(4,-1).replace(/^"|"$/g,'');await img.decode().catch(()=>{});out[k]={valueLength:v.length,width:img.naturalWidth,height:img.naturalHeight}}return out});
 await page.goto(url+'#launch');await page.locator('#launch input[type=text]').fill('미리보기');await page.locator('#launch input[type=email]').fill('preview@example.com');await page.locator('#launch input[type=checkbox]').check();await page.locator('#launch button[type=submit]').click();const formPreview=await page.locator('#launch-preview').isVisible();
 await page.setViewportSize({width:390,height:900});await page.goto(url+'#home');await page.locator('a.mobile-nav').click();const menuVisible=await page.locator('#mobile-menu').isVisible();await page.locator('#mobile-menu a[href="#brand"]').click();const menuClosed=!(await page.locator('#mobile-menu').isVisible());
 await page.goto(url+'#brand-sustainable-materials');await page.screenshot({path:path.join(__dirname,'halo-sustain-390.jpg'),quality:82});
 const result={javaScriptEnabled:false,structure,sizes,filters:{runningCount,postCount,emptyCount,emptyMessage,resetCount,sorted},images,formPreview,menuVisible,menuClosed,errors,requests};fs.writeFileSync(path.join(__dirname,'halo-validation.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({structure,allViewWidthsPass:sizes.every(x=>!x.overflow),filters:result.filters,images,formPreview,menuVisible,menuClosed,errors,requests},null,2));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
