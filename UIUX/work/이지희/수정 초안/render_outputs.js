const fs = require('fs');
const path = require('path');
const { chromium } = require(process.argv[3]);
(async()=>{
  const root=path.resolve(process.argv[2]);
  const browser=await chromium.launch({headless:true, ...(process.argv[4] ? {executablePath:process.argv[4]} : {})});
  const page=await browser.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:1});
  page.setDefaultTimeout(120000);
  for(const type of ['사이트맵','서비스 흐름도']){
    for(const dir of fs.readdirSync(path.join(root,type))){
      const svg=path.join(root,type,dir,type==='사이트맵'?'사이트맵.svg':'서비스_흐름도.svg');
      const png=svg.replace(/\.svg$/,'.png');
      await page.goto('file:///'+svg.replace(/\\/g,'/'));
      await page.screenshot({path:png,fullPage:false,timeout:120000});
    }
  }
  for(const dir of fs.readdirSync(path.join(root,'화면 설계서'))){
    const html=path.join(root,'화면 설계서',dir,'와이어프레임.html');
    await page.goto('file:///'+html.replace(/\\/g,'/'),{waitUntil:'load'});
    await page.screenshot({path:path.join(path.dirname(html),'와이어프레임.png'),fullPage:true,timeout:120000});
    await page.pdf({path:path.join(path.dirname(html),'화면_설계서.pdf'),format:'A4',printBackground:true});
  }
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});