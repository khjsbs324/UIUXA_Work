from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parent
source=root.parent/'허지민/웹디자인/강사_제작예시.html'
out=root/'figma-afit'
out.mkdir(exist_ok=True)
base=source.read_text(encoding='utf-8')
capture='<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>'
css='<style>html{scroll-behavior:auto!important}body{width:1440px!important;min-width:1440px!important}.top-full{position:relative!important}*,*:before,*:after{animation:none!important;transition:none!important}.back-top{position:absolute!important;top:940px!important;bottom:auto!important}</style>'
(out/'main.html').write_text(base.replace('</head>',css+capture+'</head>'),encoding='utf-8')
with sync_playwright() as p:
 b=p.chromium.launch(headless=True)
 page=b.new_page(viewport={'width':1440,'height':1000})
 page.goto(source.as_uri())
 html=page.evaluate('''() => {
 const content=document.createElement('main');content.id='supplement';
 const section=(title,sub='')=>{let s=document.createElement('section');s.className='supplement-section';s.innerHTML='<div class="eyebrow">A:FIT / COMPLETE CONTENT</div><h2>'+title+'</h2><p class="subintro">'+sub+'</p>';content.append(s);return s};
 let s=section('15종 상세 영양 처방 리포트','각 제품의 전문가 요약 · 상단 정제 · 하단 액상 · 추천 섭취 시점');
 let grid=document.createElement('div');grid.className='detail-grid';s.append(grid);
 document.querySelectorAll('.prd-card .formula-detail-body').forEach((n,i)=>{let d=n.cloneNode(true);d.classList.add('supplement-detail');d.insertAdjacentHTML('afterbegin','<div class="report-number">'+String(i+1).padStart(2,'0')+' / 15</div>');grid.append(d)});
 s=section('7개 라이프스타일 맞춤 진단 결과','원본에 포함된 맞춤 처방과 개인화 라벨 안내');
 document.querySelectorAll('.routine-report').forEach(n=>{let d=n.cloneNode(true);d.style.display='block';d.querySelectorAll('.selected-timing,.selected-goal').forEach((t,i)=>{t.style.display=t.classList.contains('timing-0')||t.classList.contains('goal-0')?'inline':'none'});s.append(d)});
 const add=(selector,title)=>{let s=section(title);let n=document.querySelector(selector).cloneNode(true);n.classList.add('static-panel');n.style.display='block';n.querySelectorAll('details').forEach(d=>d.open=true);s.append(n)};
 add('#diagResult','기본 처방 및 개인화 라벨 안내');
 add('.faq-section','자주 묻는 질문 · 전체 답변');
 add('#csModal .modal-dialog','고객만족센터');
 add('#checkoutModal .modal-dialog','정기구독 신청 · 진행 · 완료 · 오류 안내');
 s=section('진단 및 컬렉션 상태 안내');
 for(const id of ['diagLoading','diagError','archiveEmptyState','archiveFilterError']){const n=document.getElementById(id).cloneNode(true);n.style.display='block';n.classList.add('static-panel');s.append(n)};
 s=section('원본 구성 안내');
 for(const n of document.querySelectorAll('#calculator .state-notes,#archive .state-notes:last-child')){let d=n.cloneNode(true);d.open=true;s.append(d)};
 document.body.replaceChildren(content);
 document.querySelectorAll('script').forEach(s=>s.remove());
 document.title='A:FIT · 상세 성분 · 진단 결과 · 안내';
 return '<!doctype html>'+document.documentElement.outerHTML;
 }''')
 b.close()
extra='''<style>
body{width:1440px!important;background:#f2f4ec}#supplement{width:1440px}.supplement-section{padding:65px 60px!important;overflow:visible;background:#fff;border-bottom:20px solid #f2f4ec}.supplement-section>h2{font-size:34px!important;margin-bottom:12px}.subintro{font-size:15px;margin-bottom:35px;color:#778361}.detail-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.supplement-detail{padding:25px!important;grid-area:auto;font-size:13px!important}.report-number{color:#879400;letter-spacing:3px;font-size:12px;margin-bottom:20px}.supplement-detail h4{font-size:24px}.supplement-detail h5{font-size:13px}.supplement-detail .btn{font-size:11px}.supplement-section>.routine-report{display:block!important;margin:30px 0;padding:35px!important}.supplement-section .grid-2{grid-template-columns:1fr 1fr;gap:50px}.static-panel{position:static!important;width:100%!important;max-width:1000px!important;max-height:none!important;margin:30px auto!important;display:block!important;box-shadow:none!important;padding:30px!important}.static-panel .state-notes>div{display:block!important}#archiveEmptyState{display:block!important}.faq-section{max-width:1200px!important;padding:20px!important}.source-field-guide .modal-dialog{max-height:none!important}.source-field-guide{display:block!important;position:static!important}.selected-timing:not(.timing-0),.selected-goal:not(.goal-0){display:none!important}.timing-0,.goal-0{display:inline!important}.state-notes{font-size:13px}.back-top{display:none!important}*,*:before,*:after{animation:none!important;transition:none!important}
</style>'''
(out/'details.html').write_text(html.replace('</head>',extra+capture+'</head>'),encoding='utf-8')
print(out)
