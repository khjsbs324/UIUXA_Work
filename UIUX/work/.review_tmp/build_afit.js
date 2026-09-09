({curation, products}) => {
 const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
 const el=(tag,cls,html='')=>{let e=document.createElement(tag);e.className=cls;e.innerHTML=html;return e};
 const escape=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
 // The delivered document contains no script. This script is only the authoring tool.
 $$('script,link').forEach(e=>e.remove());
 document.title='A:FIT — 나를 위한 1:1 맞춤 웰니스';
 $$('[style]').forEach(e=>{
   let s=e.getAttribute('style');
   s=s.replace(/#111827|#0C0F12|#131920|#0A0D10/gi,'#252923').replace(/#374151|#4B5563/gi,'#555b4d').replace(/#6B7280/gi,'#707569').replace(/#F9FAFB|#F8FAFC|#F3F4F6/gi,'#f3f4ee').replace(/#E5E7EB|#D1D5DB/gi,'#dddfd2');
   e.setAttribute('style',s);
 });
 const bottle=(label='DUAL FORMULA',tone='lime')=>`<div class="studio-bottle ${tone}"><div class="studio-cap"></div><div class="studio-neck"></div><div class="studio-glass"><div class="studio-liquid"></div><div class="studio-label"><small>PERSONAL WELLNESS</small><b>A:FIT</b><span>ALL-IN-ONE + FIT</span><i>${label}</i><em>1:1 DAILY FORMULA<br>100 ml</em></div></div></div>`;
 // Full-bleed slanted product stage, based on the reference's main visual.
 const hero=$('#hero');
 const scene=el('div','hero-stage',`<div class="hero-halo"></div><div class="hero-product-line" aria-hidden="true">${bottle('01 WORK')}${bottle('06 PRO','cream')}${bottle('12 SLEEP','pink')}${bottle('14 EYE','blue')}</div><div class="hero-stage-caption">PERSONALIZED WELLNESS, PERFECTLY FIT.</div><div class="hero-slant"></div>`);
 hero.prepend(scene);
 $('.hero-wide-grid > div:first-child').classList.add('hero-copy');
 $('.hero-copy').prepend(el('div','hero-wordmark','A:FIT'));
 $('.hero-copy h1').innerHTML='나를 위한<br>1:1 맞춤 웰니스';
 $('.hero-visual-card').classList.add('hero-product-info');
 const anatomy=$('.bottle-canvas-box');
 anatomy.classList.add('anatomy-render');
 $('.hero-product-info').prepend(el('span','eyebrow','SIGNATURE DUAL PACK'));
 $('.metrics-pill-group').classList.add('hero-metrics');
 const eyebrow={manifesto:'INTRO',philosophy:'BEFORE & AFTER',science:'TECHNOLOGY',spotlight:'SIGNATURE FORMULA',curation:'FIND YOUR FIT',calculator:'BENEFIT & GUIDE',archive:'PRODUCT',reviews:'STORIES'};
 for(const [id,text] of Object.entries(eyebrow)){
  const h=$(`#${id} h2`);h.before(el('div','eyebrow',text));
 }
 // Branding story keeps every paragraph and three core beliefs.
 const mg=$('.manifesto-grid');
 mg.classList.add('editorial-manifesto');
 mg.children[0].classList.add('manifesto-copy');
 mg.children[1].classList.add('core-beliefs');
 const ingredient=el('div','ingredient-stage',`<div class="ingredient-orbit orbit-one"></div><div class="ingredient-orbit orbit-two"></div><div class="ingredient-orbit orbit-three"></div><div class="ingredient-copy"><span>ALL-IN-ONE</span><strong>상단 정제<br><i>×</i><br>하단 액상</strong><span>DUAL FORMULATION</span></div>${bottle('YOUR DAILY FIT')}<span class="ingredient-foot">복잡한 영양제와 식사를 한 병에.</span>`);
 mg.before(ingredient);
 $('#manifesto').append(el('div','brand-marquee','A:FIT PERSONAL WELLNESS · A:FIT PERSONAL WELLNESS'));
 // The before/after panels keep both timelines, drawings and summaries.
 $('#philosophy .grid-2').classList.add('comparison-grid');
 $$('#philosophy .card').forEach((e,i)=>{e.classList.add(i?'after-panel':'before-panel');e.prepend(el('div','comparison-label',i?'After':'Before'))});
 // Evidence strip uses only figures that already occur in the supplied wireframe.
 const fact=el('div','fact-stage',`<div class="fact-watermark" aria-hidden="true">A:FIT</div><div class="eyebrow">THE SCIENCE OF YOUR DAILY FIT</div><h2>정확하게 담고,<br>신선하게 전달합니다.</h2><div class="fact-numbers"><div><span>건기식 법적 규격</span><strong>100<small>%</small></strong><p>식약처 기능성 인정 기준</p></div><div><span>무균 질소 밀폐 공정</span><strong>0<small>%</small></strong><p>산화율 0% 유지</p></div><div><span>자연으로 돌아가는 용기</span><strong>180<small>일</small></strong><p>토양 생분해 에코용기</p></div></div><p class="fact-note">* 원본 와이어프레임의 가상 콘셉트 수치이며, 실제 시험 결과가 아닙니다.</p>`);
 $('#science').prepend(fact);
 $$('.process-step-item').forEach((e,i)=>e.prepend(el('div','process-art',`<span>${['◌','⠿','≋','◎','✧'][i]}</span>`)));
 $$('.spotlight-row').forEach((row,i)=>{
  row.classList.add('signature-'+i);
  row.querySelector('.spotlight-img-box').insertAdjacentHTML('afterbegin',`<div class="spot-scene" aria-hidden="true">${bottle(['06 PRO','12 SLEEP','14 EYE'][i],['lime','pink','blue'][i])}</div><span class="spot-scene-index">0${i+1}</span>`);
  const old=row.querySelector('.spotlight-bottle-render');old.classList.add('original-bottle-caption');
 });
 // Radio selections replace JS filters and remain fully keyboard operable.
 const extraCSS=[];
 for(const [id,dim] of [['filterPillsCat','cat'],['filterPillsTiming','timing'],['filterPillsGoal','goal']]){
  $$('#'+id+' button').forEach((b,i)=>{
   const val=b.getAttribute('onclick').match(/'([^']+)'/)[1];
   const label=el('label','filter-choice',`<input type="radio" name="filter-${dim}" value="${val}" ${i===0?'checked':''}><span>${b.innerHTML}</span>`);b.replaceWith(label);
   if(val!=='all')extraCSS.push(`#archive:has(input[name="filter-${dim}"][value="${val}"]:checked) .prd-card:not([data-${dim}="${val}"]){display:none}`);
  });
 }
 // All 15 quick-view data records become real HTML details, never lost with script removal.
 $$('.prd-card').forEach((card,i)=>{
  card.querySelector('.prd-bottle-box').insertAdjacentHTML('afterbegin',`<div class="collection-bottle" aria-hidden="true">${bottle(String(i+1).padStart(2,'0')+' / DAILY FIT',['lime','cream','pink','blue'][i%4])}</div>`);
  const data=products[i];
  const d=el('details','formula-detail',`<summary>상세보기 <span>+</span></summary><div class="formula-detail-body"><span class="eyebrow">${escape(data.cat)}</span><h4>${escape(data.name)}</h4><p>${escape(data.target)}</p><h5>전문가 핵심 처방 요약</h5><p>${data.summary}</p><h5>상단 캡슐 정제 구성</h5><p>${data.cap}</p><h5>하단 고농축 액상 포뮬러</h5><p>${data.liq}</p><h5>추천 섭취 골든타임:</h5><p>${data.timing}</p><a class="btn primary" href="#checkoutModal">이 처방으로 정기구독 시작하기 (월 79,800원)</a></div>`);
  card.querySelector('button[onclick^="openQuickView"]').replaceWith(d);
 });
 const reportTemplate=$('#diagResult');
 // Display all three questions, with one choice per question and seven authored reports.
 for(let n=1;n<=3;n++){
  const pane=$('#diagStep'+n);pane.style.display='block';
  pane.querySelectorAll('.diag-option-btn').forEach((b,i)=>{
   const label=el('label','diag-option-btn',`<input type="radio" name="question-${n}" value="${i}" ${i===0?'checked':''}><span class="diag-choice-content">${b.innerHTML}</span>`);b.replaceWith(label);
  });
 }
 const reportHost=el('details','reports-panel','<summary>맞춤 처방 리포트 확인하기 <span>↗</span></summary>');
 reportHost.id='routine-reports';
 curation.forEach((data,i)=>{
  const report=reportTemplate.cloneNode(true);report.id='report-'+i;report.classList.add('routine-report');report.style.display='';
  const fields={curationBadge:'badge',curationTitle:'title',curationDesc:'desc',curationIngredients:'ing',curationBottleTag:'tag',curationLabel:'label',curationEngraveMsg:'engrave'};
  for(const [id,key] of Object.entries(fields))report.querySelector('#'+id).textContent=data[key];
  report.querySelectorAll('[id]').forEach(e=>e.id+='-'+i);
  reportHost.append(report);
  extraCSS.push(`#curation:has(input[name="question-1"][value="${i}"]:checked) #report-${i}{display:block}`);
 });
 const defaultReport=el('details','original-report','<summary>기본 처방 안내</summary>');
 reportTemplate.style.display='block';defaultReport.append(reportTemplate);reportHost.append(defaultReport);
 $('#diagQuizContainer').append(reportHost);
 const states=(ids,title,parent)=>{
  const details=el('details','state-notes',`<summary>${title}</summary>`);
  ids.forEach(id=>{const e=$('#'+id);if(e){e.style.display='block';details.append(e)}});parent.append(details);
 };
 states(['diagLoading','diagError'],'분석 진행 및 재시도 안내',$('#diagQuizContainer'));
 states(['archiveFilterError'],'상품 목록 연결 안내',$('#archive .wrap-wide'));
 $('#archiveEmptyState').style.display='';
 extraCSS.push('#archiveEmptyState{display:none!important}#productCardGrid:not(:has(.prd-card:not([style*="display: none"]))) #archiveEmptyState{display:block!important}');
 // Empty results for all radio combinations are precomputed with CSS.
 const cards=$$('.prd-card').map(e=>({cat:e.dataset.cat,timing:e.dataset.timing,goal:e.dataset.goal}));
 const values=dim=>$$(`#archive input[name="filter-${dim}"]`).map(e=>e.value);
 for(const c of values('cat'))for(const t of values('timing'))for(const g of values('goal')){
  if(!cards.some(x=>(c==='all'||x.cat===c)&&(t==='all'||x.timing===t)&&(g==='all'||x.goal===g)))extraCSS.push(`#archive:has(input[name="filter-cat"][value="${c}"]:checked):has(input[name="filter-timing"][value="${t}"]:checked):has(input[name="filter-goal"][value="${g}"]:checked) #archiveEmptyState{display:block!important}`);
 }
 // 4 meal costs × 30 days: authored calculation table switched only by CSS.
 $$('#mealPresetGroup button').forEach((b,i)=>{
  const amount=[7000,8500,11000,13000][i];b.replaceWith(el('label','calc-preset-btn',`<input type="radio" name="meal-cost" value="${amount}" ${i===1?'checked':''}><span>${b.innerHTML}</span>`));
 });
 const select=el('select','days-select',Array.from({length:30},(_,i)=>`<option value="${i+1}" ${i===19?'selected':''}>${i+1}일</option>`).join(''));select.id='daysSlider';select.setAttribute('aria-label','월 구독 일수 선택');$('#daysSlider').replaceWith(select);
 $('#selectedDays').parentElement.replaceWith(el('label','selected-days-label','선택 일수:'));
 $('.selected-days-label').setAttribute('for','daysSlider');
 const calcRows=el('div','calculation-rows');
 const originalFormula=$('#calcFormulaBox');const originalResults=$('.calc-results-grid');
 for(const amount of [7000,8500,11000,13000])for(let day=1;day<=30;day++){
  const money=((amount-2660)*day).toLocaleString('en-US'),time=Math.round(day*.5);
  const row=el('div','calculation-row',`<div class="calc-formula-box"><b>[투명 산출 근거 및 계산식]</b><div>• 식비 절감식: (${amount.toLocaleString('en-US')}원 - A:FIT 2,660원) × ${day}일 = <strong>${money}원</strong></div><div>• 시간 절약식: 1회 식사·준비 30분(0.5시간) × ${day}일 = <strong>${time}시간</strong></div></div><div class="calc-results-grid"><div><span>한 달 절약 식비</span><strong>${money}<small>원</small></strong></div><div><span>절약된 식사·준비 시간</span><strong>약 ${time}<small>시간</small></strong></div></div>`);
  row.id=`calc-${amount}-${day}`;calcRows.append(row);
  extraCSS.push(`.calc-box:has(input[name="meal-cost"][value="${amount}"]:checked):has(option[value="${day}"]:checked) #${row.id}{display:block}`);
 }
 originalFormula.replaceWith(calcRows);originalResults.remove();
 // Keep layout annotations available without placing construction instructions in the product flow.
 const designNotes=el('details','state-notes','<summary>원본 이미지 구성 안내</summary>');
 $$('#calculator span').filter(e=>e.textContent.startsWith('권장:')).forEach(e=>designNotes.append(e));
 $('#calculator .wrap-wide').append(designNotes);
 // Original status copy is retained, reachable within the subscription panel.
 states(['checkoutLoadingBox','checkoutSuccessBox','checkoutErrorBox'],'접수 진행 및 완료 화면 안내',$('#checkoutModal .modal-dialog'));
 const plan=$('#orderPlanName');const productSelect=el('select','',products.map(p=>`<option>${escape(p.name)}</option>`).join(''));productSelect.id=plan.id;plan.replaceWith(productSelect);
 $('#btnSubmitOrder').type='button';$('#btnSubmitOrder').setAttribute('onclick','previewCheckout()');
 const formNote=el('p','form-note','가상 프로젝트 신청 화면입니다. 입력 정보는 전송되거나 저장되지 않습니다.');$('#checkoutFormBox form').prepend(formNote);
 // Reuse the empty original quick-view shell as an optional field guide, retaining source labels.
 const q=$('#quickViewModal');q.classList.add('source-field-guide');
 const guide=el('details','state-notes','<summary>상세 영양 처방 리포트 항목 안내</summary>');q.style.display='block';q.classList.remove('modal');q.removeAttribute('id');guide.append(q);$('#archive .wrap-wide').append(guide);
 // Replace JS action surfaces with native links, radios, details or local panel targets.
 $$('[onclick]').forEach(e=>{
  const code=e.getAttribute('onclick');if(e.tagName!=='BUTTON'){e.removeAttribute('onclick');return}
  let href='#curation';
  if(/openCheckout|subscribeFrom/.test(code))href='#checkoutModal';
  else if(/openCs|openConsult|connectKakao|copyCsPhone/.test(code))href='#csModal';
  else if(/closeQuick/.test(code))href='#archive';
  else if(/closeCs/.test(code))href=code.includes('reviews')?'#reviews':'#hero';
  else if(/closeCheckout/.test(code))href='#hero';
  else if(/resetAllFilters/.test(code))href='#archive-reset';
  else if(/goStep\((\d)/.test(code))href='#diagStep'+code.match(/goStep\((\d)/)[1];
  else if(/retryCheckout|backToCheckout/.test(code))href='#checkoutFormBox';
  else if(/previewCheckout/.test(code))href='#checkout-preview';
  const a=el('a',e.className,e.innerHTML);for(const at of e.attributes)if(!['onclick','type','class'].includes(at.name))a.setAttribute(at.name,at.value);a.href=href;e.replaceWith(a);
 });
 // A native reset button resets every filter within this form.
 const archiveForm=el('form','archive-form');archiveForm.id='archive-reset';
 $('#archiveFilterNav').before(archiveForm);archiveForm.append($('#archiveFilterNav'));archiveForm.append($('#productCardGrid'));
 $$('a[href="#archive-reset"]').forEach(a=>{const b=el('button',a.className,a.innerHTML);b.type='reset';a.replaceWith(b)});
 const reset=el('button','filter-reset','전체 필터 초기화 ↺');reset.type='reset';$('#archiveFilterNav').append(reset);
 const success=$('#checkoutSuccessBox');success.id='checkout-preview';
 // Content panels use :target and expose all content without executable attributes.
 $$('.modal').forEach(m=>{m.setAttribute('aria-modal','true');m.insertBefore(el('a','modal-backdrop',''),m.firstChild);m.firstChild.href='#hero';m.firstChild.setAttribute('aria-label','닫기')});
 $$('a').forEach(a=>{if(a.getAttribute('href')==='브랜드소개.html')a.href='#manifesto';if(a.getAttribute('href')==='카테고리.html')a.href='#archive';if(a.getAttribute('href')==='메인페이지.html')a.href='#hero'});
 $$('.gnb-search-wrap').forEach(e=>{const input=e.querySelector('input');input.placeholder='컬렉션';const a=el('a','search-link',e.querySelector('svg').outerHTML);a.href='#archive';a.setAttribute('aria-label','15종 컬렉션 탐색');e.querySelector('svg').replaceWith(a)});
 $$('*').forEach(e=>[...e.attributes].forEach(a=>{if(/^on/i.test(a.name)||a.value.startsWith('javascript:'))e.removeAttribute(a.name)}));
 const faq=$('#reviews .faq-item').parentElement;faq.classList.add('faq-section');faq.querySelector('h3').before(el('div','eyebrow','FAQ'));
 $$('.faq-item summary').forEach(e=>e.prepend(el('b','question-mark','Q')));
 document.body.append(el('a','back-top','↑<span>TOP</span>'));$('.back-top').href='#hero';
 const stateGuide=$('#checkoutModal .state-notes');stateGuide.id='checkout-state-guide';
 // The application CTA opens an explicit preview; no fabricated submission is made.
 const previewModal=el('div','modal',`<a class="modal-backdrop" href="#checkoutModal" aria-label="신청서로 돌아가기"></a><div class="modal-dialog"><a href="#checkoutModal" class="preview-close">×</a><p class="form-note">신청 완료 화면 미리보기 · 실제 구독 신청은 접수되지 않습니다.</p></div>`);
 previewModal.id='checkout-preview-panel';previewModal.setAttribute('role','dialog');previewModal.setAttribute('aria-modal','true');previewModal.setAttribute('aria-label','구독 신청 완료 화면 미리보기');
 const preview=success.cloneNode(true);preview.querySelectorAll('[id]').forEach(e=>e.removeAttribute('id'));preview.removeAttribute('id');previewModal.lastElementChild.append(preview);document.body.append(previewModal);
 $('a[href="#checkout-preview"]').href='#checkout-preview-panel';
 // Reflect the selected timing and health goal in each authored report.
 const timingNames=$$('#diagStep2 .diag-opt-title').map(e=>e.textContent);
 const goalNames=$$('#diagStep3 .diag-opt-title').map(e=>e.textContent);
 $$('.routine-report [id^="curationTimingGuide-"]').forEach(e=>{
  e.innerHTML='추천 섭취 골든타임: '+timingNames.map((v,i)=>`<span class="selected-timing timing-${i}">${escape(v)}</span>`).join('')+'<br>선택한 건강 목표: '+goalNames.map((v,i)=>`<span class="selected-goal goal-${i}">${escape(v)}</span>`).join('');
 });
 timingNames.forEach((_,i)=>extraCSS.push(`#curation:has(input[name="question-2"][value="${i}"]:checked) .timing-${i}{display:inline}`));
 goalNames.forEach((_,i)=>extraCSS.push(`#curation:has(input[name="question-3"][value="${i}"]:checked) .goal-${i}{display:inline}`));
 const diagnosisForm=el('form','diagnosis-form');$('#diagQuizContainer').before(diagnosisForm);diagnosisForm.append($('#diagQuizContainer'));
 $$('#diagQuizContainer a').filter(e=>/진단 다시 하기|처음부터 다시 선택하기/.test(e.textContent)).forEach(e=>{const reset=el('button',e.className,e.innerHTML);reset.type='reset';e.replaceWith(reset)});
 const style=el('style','');style.textContent=extraCSS.join('\n');document.head.append(style);
 return '<!doctype html>\n'+document.documentElement.outerHTML;
}
