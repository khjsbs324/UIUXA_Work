param([string]$Root=(Join-Path $PSScriptRoot '최종 수정 파일'))
$ErrorActionPreference='Stop'
$manifestPath=Join-Path $Root 'client-manifest.json'
$manifest=Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json

function Write-Utf8([string]$path,[string]$content){[IO.File]::WriteAllText($path,$content,[Text.UTF8Encoding]::new($false))}
function E([string]$value){[Net.WebUtility]::HtmlEncode($value)}

$profiles=@{
 '01'=@('Editorial Sanctuary','브랜드 철학을 탐색하는 무중력 에세이 스크롤','디렉터의 선택 근거를 보여주는 컬렉션 편집기')
 '02'=@('Mixology Lab','향과 맛을 겹쳐 보는 아로마 블렌딩 랩','베이스 티·노트·피니시를 조합하는 레시피 믹서')
 '03'=@('Curation Magazine','시즌과 감정에 따라 바뀌는 셀렉트 매거진','MD 큐레이션 근거와 대안 상품을 비교하는 편집 보드')
 '04'=@('Spatial Journey','다도 공간을 이동하며 상품을 발견하는 3D 투어','공간 장면별 다기·향·티 페어링 핫스폿')
 '05'=@('Hospitality Suite','투숙 상황별 인룸 티타임 서비스','체크인 시간과 객실 무드에 맞춘 어메니티 플래너')
 '06'=@('Wellness Bento','이너뷰티 목표를 카드가 아닌 데이터 블록으로 조합','성분·섭취 시간·뷰티 루틴 페어링 매트릭스')
 '07'=@('Social Challenge Feed','레시피 영상과 참여 흐름이 이어지는 소셜 피드','믹솔로지 챌린지 촬영·업로드·투표 스튜디오')
 '08'=@('Immersive Hideaway','디지털 피로를 낮추는 비밀 안식처 탐색','화면 자극 강도와 사운드를 조절하는 캄테크 모드')
 '09'=@('Quick Brew Dashboard','업무 중 3분 안에 끝나는 퀵브루 대시보드','회의 사이 남은 시간에 맞춘 원클릭 브루잉')
 '10'=@('Aurora Discovery','색과 기분으로 제품을 찾는 오로라 탐색','수색 변화와 칼로리를 함께 비교하는 비주얼 파인더')
 '11'=@('Precision Ritual','초 단위 재현성을 관리하는 정밀 리추얼 도구','온도·시간·용량 프리셋을 저장하는 브루 프로파일')
 '12'=@('Family Zero-Labor','가족이 함께 쓰는 노동 제로 하이볼 흐름','연령·카페인 민감도별 안전 옵션과 가족 번들')
 '13'=@('3D Home Cafe Studio','홈카페 레시피를 입체적으로 조합하는 스튜디오','글래스·베이스·가니시를 회전 조합하는 3D 믹서')
 '14'=@('Focus Calm Mode','수험 시간표와 연결되는 무카페인 집중 모드','공부 블록별 집중·휴식 음료를 예약하는 플래너')
 '15'=@('Active Wellness Guide','시니어도 쉽게 탐색하는 큰 글자 웰니스 가이드','복용 시간과 주의사항을 우선 안내하는 안전 큐레이션')
 '16'=@('Family Rhythm Planner','가족 일정에 맞춘 웰빙 스파클링 플래너','아침·하교·퇴근 시간대별 가족 음료 예약')
 '17'=@('Night Illustration','야간 창작자를 위한 어두운 에디토리얼 리추얼','작업 강도에 맞춰 뇌식과 휴식을 전환하는 나이트 모드')
 '18'=@('Hydration Coaching','수분 리추얼을 단계별로 안내하는 코칭 화면','수업·운동 전후 섭취 루틴과 체크인 기록')
 '19'=@('Architectural Table','테이블웨어를 공간 그리드로 설계하는 쇼룸','재질·크기·동선을 비교하는 비스포크 테이블 빌더')
 '20'=@('Vegan Community','비건 원료와 업사이클링 활동을 잇는 커뮤니티','패키지 회수·재사용 미션과 투명한 인증 추적')
}
$layoutCycle=@('editorial','lab','dashboard','spatial','social')
$products=@('Aurora Cold Brew','Midnight GABA','Zero Sugar Earl Grey','Botanical Sparkling','Calm Blue Chamomile','Focus Citrus Mate','Sleep Lavender Rooibos','Vegan Berry Tonic','Three-Minute Office Stick','Mood Dial Sampler','Glass Ritual Kit','Mixology Shaker Set','Initial Tin Gift','Family Zero-Caffeine Pack','Senior Easy-Brew Pack','Thirty-Day Rhythm Box','Hydration Beauty Blend','Upcycle Refill Pouch','Hotel Welcome Pairing','Architect Table Set')

foreach($c in $manifest.clients){
 $id=[string]$c.id;$name=[string]$c.name;$key="${id}_${name}";$profile=$profiles[$id];$layout=$layoutCycle[([int]$id-1)%5];$concept=$profile[0];$experience=$profile[1];$killer=$profile[2]
 $homeId="W$id-HOME";$diagnosis="W$id-DIAG";$mix="W$id-MIX";$ritual="W$id-RITUAL";$builder="W$id-BUILD";$community="W$id-COMM";$done="W$id-DONE"
 $c | Add-Member -NotePropertyName layout -NotePropertyValue $layout -Force
 $c | Add-Member -NotePropertyName concept -NotePropertyValue $concept -Force
 $c | Add-Member -NotePropertyName killerFeature -NotePropertyValue $killer -Force

 $siteDir=Join-Path $Root "사이트맵\$key";$flowDir=Join-Path $Root "서비스 흐름도\$key";$screenDir=Join-Path $Root "화면 설계서\$key"
 $siteMermaid="flowchart TD`n  A[$homeId $concept] --> B[$diagnosis 감정·상황 진단]`n  B --> C[$mix 믹솔로지 탐색]`n  C --> D[$ritual 리추얼 실행]`n  D --> E[$builder 번들·구독 설계]`n  E --> F[$community 기록·커뮤니티]`n  F --> G[$done 저장·완료]`n  B -->|진단 건너뛰기| C`n  E -->|선택 오류| E"
 $siteDoc=@"
# WICKETA $name 경험 사이트맵

## 이지희 전용 설계 기준

- 클라이언트: $id · $name
- 콘셉트: $concept
- 레이아웃 유형: $layout
- 핵심 경험: $experience
- 킬러 기능: $killer
- 원본 요구 초점: $($c.focus)

## 경험 중심 정보 구조

| 화면 ID | 경험 영역 | 사용자 목적 | 고유 기능 |
|---|---|---|---|
| $homeId | $concept | 브랜드 세계관 진입 | $experience |
| $diagnosis | Mood Intake | 감정·시간·상황 입력 | 3축 감정 다이얼 |
| $mix | Mixology Explorer | 맛·향·기능 탐색 | 레시피 조합과 대안 비교 |
| $ritual | Ritual Player | 실제 180초 경험 | 사운드·타이머·수색 변화 |
| $builder | Bundle Atelier | 상품·주기·각인 선택 | $killer |
| $community | Ritual Archive | 기록·공유·재방문 | 저장·챌린지·리필 회수 |
| $done | Saved Ritual | 결과 확인 | 레시피 ID와 다음 행동 |

## 차별화 원칙

- 동일한 쇼핑몰 카드 순서를 사용하지 않고 `$layout` 레이아웃으로 구성
- $name 클라이언트의 `$($c.focus)` 요구를 첫 화면과 킬러 기능에 연결
- 상품보다 감정과 리추얼 경험을 먼저 탐색한 뒤 구매·구독으로 이동
- 실패 시 입력과 조합을 보존하고 대체 레시피 제공

```mermaid
$siteMermaid
```

- [서비스 흐름도](../../서비스%20흐름도/$key/서비스_흐름도.md)
- [화면 설계서](../../화면%20설계서/$key/화면_설계서.md)
"@
 Write-Utf8 "$siteDir\사이트맵.md" $siteDoc;Write-Utf8 "$siteDir\사이트맵.mmd" $siteMermaid
 $siteLabels=@($concept,'Mood Intake','Mixology Explorer','Ritual Player','Bundle Atelier','Ritual Archive','Saved Ritual')
 $siteNodes=for($i=0;$i -lt 7;$i++){$x=80+($i%4)*335;$y=120+[math]::Floor($i/4)*310;if($i -gt 0){$px=80+(($i-1)%4)*335+260;$py=120+[math]::Floor(($i-1)/4)*310+65;"<line class='l' x1='$px' y1='$py' x2='$x' y2='$($y+65)'/>"};"<rect class='n' x='$x' y='$y' width='260' height='130' rx='28'/><text class='s' x='$($x+22)' y='$($y+55)'>$(@($homeId,$diagnosis,$mix,$ritual,$builder,$community,$done)[$i])</text><text class='s' x='$($x+22)' y='$($y+92)'>$($siteLabels[$i])</text>"}
 $siteSvg="<svg xmlns='http://www.w3.org/2000/svg' width='1440' height='900' role='img' aria-labelledby='t d'><title id='t'>WICKETA $name 경험 사이트맵</title><desc id='d'>$concept 중심의 WICKETA 여정</desc><rect width='1440' height='900' fill='#f4f0e8'/><style>.n{fill:#fff;stroke:#6757d9;stroke-width:2}.h{font:700 28px Arial;fill:#171824}.s{font:18px Arial;fill:#171824}.l{stroke:#86a99f;stroke-width:3}</style><text x='70' y='65' class='h'>WICKETA $id · $concept</text>"+($siteNodes -join '')+"</svg>"
 Write-Utf8 "$siteDir\사이트맵.svg" $siteSvg

 $flowMermaid="flowchart LR`n  A[$homeId 몰입 진입] --> B[$diagnosis 상태 입력]`n  B --> C{추천 가능?}`n  C -->|예| D[$mix 레시피 3안 비교]`n  C -->|아니오| E[조건 완화·전체 탐색]`n  E --> D`n  D --> F[$ritual 180초 체험]`n  F --> G[$builder 번들 설계]`n  G --> H{저장 성공?}`n  H -->|예| I[$community 기록·공유]`n  H -->|아니오| J[입력 유지·재시도]`n  J --> G`n  I --> K[$done 완료]"
 $flowDoc=@"
# WICKETA $name 서비스 흐름도

## 고유 여정

- 콘셉트: $concept
- 시작 경험: $experience
- 핵심 인터랙션: $killer
- 상위 문서: [사이트맵](../../사이트맵/$key/사이트맵.md)

## 정상 흐름

1. `$homeId`에서 `$concept` 세계관 진입
2. `$diagnosis`에서 현재 감정·가용 시간·카페인 민감도 선택
3. `$mix`에서 서로 다른 믹솔로지 레시피 3안 비교
4. `$ritual`에서 수색 변화와 180초 타이머 체험
5. `$builder`에서 제품·구독 주기·패키지 조합
6. `$community`에서 리추얼 저장 또는 공유
7. `$done`에서 레시피 ID와 다음 이용 시점 확인

## 오류와 대안

- 진단 결과 없음: 조건 완화 버튼과 전체 탐색을 함께 제공
- 재고 없음: 동일 감정 목표의 대체 베이스 티 제안
- 타이머 중단: 남은 시간과 선택 레시피를 로컬 상태에 보존
- 저장 실패: 조합값을 유지하고 재시도·텍스트 복사 제공
- 접근성 모드: 사운드 없이 진동·텍스트 진행 상태 제공

```mermaid
$flowMermaid
```
"@
 Write-Utf8 "$flowDir\서비스_흐름도.md" $flowDoc;Write-Utf8 "$flowDir\서비스_흐름도.mmd" $flowMermaid
 $flowSvg="<svg xmlns='http://www.w3.org/2000/svg' width='1440' height='900' role='img' aria-labelledby='t d'><title id='t'>WICKETA $name 서비스 흐름도</title><desc id='d'>진단, 조합, 리추얼, 저장과 오류 복구</desc><rect width='1440' height='900' fill='#f4f0e8'/><style>.n{fill:#fff;stroke:#171824;stroke-width:2}.e{fill:#f9dfe9;stroke:#a43b66;stroke-width:2}.h{font:700 28px Arial;fill:#171824}.s{font:18px Arial;fill:#171824}.l{stroke:#6757d9;stroke-width:3}</style><text x='70' y='65' class='h'>WICKETA $id · $concept 서비스 흐름</text><rect class='n' x='70' y='140' width='240' height='110' rx='24'/><text class='s' x='95' y='205'>감정·상황 진단</text><line class='l' x1='310' y1='195' x2='390' y2='195'/><rect class='n' x='400' y='140' width='240' height='110' rx='24'/><text class='s' x='425' y='205'>믹솔로지 3안</text><line class='l' x1='640' y1='195' x2='720' y2='195'/><rect class='n' x='730' y='140' width='240' height='110' rx='24'/><text class='s' x='755' y='205'>180초 리추얼</text><line class='l' x1='970' y1='195' x2='1050' y2='195'/><rect class='n' x='1060' y='140' width='240' height='110' rx='24'/><text class='s' x='1085' y='205'>번들·구독 저장</text><line class='l' x1='1180' y1='250' x2='1180' y2='370'/><rect class='n' x='1060' y='380' width='240' height='110' rx='24'/><text class='s' x='1085' y='445'>기록·커뮤니티</text><line class='l' x1='1060' y1='435' x2='980' y2='435'/><rect class='n' x='730' y='380' width='240' height='110' rx='24'/><text class='s' x='755' y='445'>Saved Ritual</text><line class='l' x1='850' y1='490' x2='850' y2='610'/><rect class='e' x='730' y='620' width='240' height='110' rx='24'/><text class='s' x='755' y='675'>오류·대체 제안</text><text class='s' x='755' y='705'>입력과 조합 유지</text></svg>"
 Write-Utf8 "$flowDir\서비스_흐름도.svg" $flowSvg

 $sectionNames=@('Portal Hero','Client Vision','Mood Intake','Signature Experience','Mixology Canvas','Product Constellation','Ritual Player','Bundle Atelier','Subscription Rhythm','Community Loop','Evidence Drawer','Saved Ritual CTA')
 $rows=for($i=0;$i -lt 12;$i++){"| WK-SEC-{0:D2} | {1} | {2} |" -f ($i+1),$sectionNames[$i],(@($experience,'브랜드 관점과 선택 근거','감정·시간·민감도 진단',$killer,'향·맛·기능 조합','20개 상품의 비선형 탐색','180초 타이머·사운드','제품·각인·선물 조합','배송 주기와 리필','저장·공유·챌린지','성분·인증·정책','레시피 저장과 전환')[$i])}
 $prodRows=for($i=0;$i -lt 20;$i++){"| WK-P{0:D2} | {1} | {2} |" -f ($i+1),$products[$i],(@('Hero 오브젝트','믹솔로지 비교','리추얼 추천','번들 빌더','구독·커뮤니티')[$i%5])}
 $screenDoc=@"
# WICKETA $name 인터랙션 설계서

## 개인화 설계

- 클라이언트: $id · $name
- 콘셉트·레이아웃: $concept · $layout
- 핵심 경험: $experience
- 킬러 기능: $killer
- 사이트맵: [열기](../../사이트맵/$key/사이트맵.md)
- 서비스 흐름도: [열기](../../서비스%20흐름도/$key/서비스_흐름도.md)

## WICKETA 전용 12개 모듈

| 모듈 ID | 이름 | 역할 |
|---|---|---|
$($rows -join "`n")

## 상품 20개 경험별 분산

| 상품 ID | 상품 | 노출 맥락 |
|---|---|---|
$($prodRows -join "`n")

## 인터랙션과 상태

- 진단: 미선택·선택·추천 계산·결과 없음·추천 완료
- 믹솔로지: 기본·조합 중·충돌·대체 제안·레시피 저장
- 타이머: 준비·진행·일시정지·복귀·완료
- 빌더: 재고 있음·품절·옵션 오류·저장 실패·완료
- 커뮤니티: 비로그인·초안·업로드·신고·공개 완료

## 접근성

- `h1` 1개와 12개 `section` 랜드마크
- 모든 진단·저장 입력에 명시적 레이블 연결
- 타이머와 저장 결과를 `aria-live`로 안내
- 대화상자 포커스 이동·복귀와 ESC 닫기 지원
- 사운드 자동재생 금지 및 무음 대체 정보 제공
- 고대비·모션 축소·키보드 전용 이용 지원
"@
 Write-Utf8 "$screenDir\화면_설계서.md" $screenDoc
 $json=[ordered]@{client=[ordered]@{id=$id;name=$name;concept=$concept;layout=$layout;focus=$c.focus};screenIds=@($homeId,$diagnosis,$mix,$ritual,$builder,$community,$done);sectionCount=12;productCount=20;killerFeature=$killer;states=@('default','loading','empty','error','success')}|ConvertTo-Json -Depth 6
 Write-Utf8 "$screenDir\화면_목록.json" $json

 $cards=for($i=0;$i -lt 20;$i++){"<article class='product'><span>WK-P{0:D2}</span><h3>{1}</h3><p>{2}</p></article>" -f ($i+1),(E $products[$i]),(@('시그니처 오브젝트','향·맛 비교','오늘의 리추얼','나만의 번들','구독·리필')[$i%5])}
 $html=@"
<!doctype html><html lang="ko" data-layout="$layout"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>WICKETA $name · $concept</title><style>:root{--ink:#171824;--paper:#f4f0e8;--glass:#ffffffb8;--line:#b9b4c2;--a:#6757d9;--b:#86c9bd}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:var(--ink);background:radial-gradient(circle at 80% 10%,#d9d0ff,var(--paper) 35%);font:16px/1.6 system-ui,"Noto Sans KR",sans-serif}.wrap{width:min(1180px,calc(100% - 32px));margin:auto}header{position:sticky;top:0;z-index:8;background:#f4f0e8dd;backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}nav{min-height:64px;display:flex;justify-content:space-between;align-items:center}nav a{color:inherit;margin-left:14px}.portal{min-height:88vh;display:grid;align-items:center}.portal-grid{display:grid;grid-template-columns:1.35fr .65fr;gap:32px}.orb{min-height:430px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff,#b8a8ff 32%,#5b498f 70%);filter:saturate(.75);display:grid;place-items:center;color:#fff;text-align:center}h1{font:800 clamp(3.2rem,8vw,8rem)/.85 Georgia,serif;margin:.15em 0}h2{font:700 clamp(2rem,5vw,4.8rem)/1 Georgia,serif}section{padding:88px 0;border-top:1px solid #b9b4c266}.tag{letter-spacing:.13em;text-transform:uppercase;color:#59546e}.panel,.product{background:var(--glass);border:1px solid var(--line);border-radius:20px;padding:20px}.products{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.mixer{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.btn,button,select,input{font:inherit}.btn,button{border:1px solid var(--ink);border-radius:999px;padding:11px 16px;background:transparent;color:inherit;cursor:pointer}.primary{background:var(--ink);color:#fff}.field{display:grid;gap:6px;margin:12px 0}.field input,.field select{padding:12px;border:1px solid #777;border-radius:9px;background:#fff}.status{padding:12px;min-height:48px;background:#e8e5ee;border-radius:10px}.error{background:#f4dedd}.success{background:#d9eee5}dialog{border:0;border-radius:24px;padding:30px;width:min(540px,calc(100% - 32px))}dialog::backdrop{background:#171824bb}:focus-visible{outline:3px solid #ff4fd8;outline-offset:3px}[data-layout=lab] .portal-grid{grid-template-columns:1fr 1fr}[data-layout=dashboard] section .wrap{display:grid;grid-template-columns:280px 1fr;gap:30px}[data-layout=spatial] .products{grid-template-columns:2fr 1fr 1fr}[data-layout=social] .products{grid-template-columns:repeat(3,1fr)}@media(max-width:800px){.portal-grid,.mixer,[data-layout=dashboard] section .wrap{grid-template-columns:1fr}.products,[data-layout=spatial] .products,[data-layout=social] .products{grid-template-columns:1fr 1fr}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;transition:none!important}}</style></head><body><header><nav class="wrap" aria-label="WICKETA 경험 메뉴"><strong>WICKETA / $id</strong><div><a href="#mood">Mood</a><a href="#mix">Mix</a><a href="#ritual">Ritual</a><a href="#save">Save</a></div></nav></header><main><section class="portal"><div class="wrap portal-grid"><div><p class="tag">WK-SEC-01 · $concept</p><h1>$(E $experience)</h1><p>$(E $killer)</p><a class="btn primary" href="#mood">나의 리추얼 열기</a></div><div class="orb" role="img" aria-label="$concept 수색 오브젝트"><strong>$(E $c.focus)<br>WICKETA</strong></div></div></section><section><div class="wrap"><div><p class="tag">WK-SEC-02</p><h2>Client Vision</h2></div><div class="panel"><strong>$(E $name) · $(E $c.role)</strong><p>$(E $experience)</p></div></div></section><section id="mood"><div class="wrap"><div><p class="tag">WK-SEC-03</p><h2>Mood Intake</h2></div><div class="panel"><fieldset><legend>지금 필요한 감각</legend><button type="button" aria-pressed="false">집중</button> <button type="button" aria-pressed="false">환기</button> <button type="button" aria-pressed="false">휴식</button></fieldset></div></div></section><section><div class="wrap"><div><p class="tag">WK-SEC-04</p><h2>Signature Experience</h2></div><div class="panel"><h3>$(E $killer)</h3><p>클라이언트의 직업과 사용 맥락에서 출발한 단독 인터랙션입니다.</p></div></div></section><section id="mix"><div class="wrap"><div><p class="tag">WK-SEC-05</p><h2>Mixology Canvas</h2></div><div class="mixer"><div class="panel">Base Tea<br><select aria-label="베이스 티"><option>Rooibos</option><option>Earl Grey</option></select></div><div class="panel">Aroma<br><select aria-label="아로마"><option>Lavender</option><option>Citrus</option></select></div><div class="panel">Finish<br><select aria-label="피니시"><option>Sparkling</option><option>Still</option></select></div></div></div></section><section><div class="wrap"><div><p class="tag">WK-SEC-06</p><h2>Product Constellation</h2></div><div class="products">$($cards[0..7]-join '')</div></div></section><section id="ritual"><div class="wrap"><div><p class="tag">WK-SEC-07</p><h2>Ritual Player</h2></div><div class="panel"><p id="timer" aria-live="polite">03:00 · 준비</p><button id="timerBtn" type="button">180초 시작</button></div></div></section><section><div class="wrap"><div><p class="tag">WK-SEC-08</p><h2>Bundle Atelier</h2></div><div class="products">$($cards[8..11]-join '')</div></div></section><section><div class="wrap"><div><p class="tag">WK-SEC-09</p><h2>Subscription Rhythm</h2></div><div class="products">$($cards[12..15]-join '')</div></div></section><section><div class="wrap"><div><p class="tag">WK-SEC-10</p><h2>Community Loop</h2></div><div class="products">$($cards[16..19]-join '')</div></div></section><section><div class="wrap"><div><p class="tag">WK-SEC-11</p><h2>Evidence Drawer</h2></div><div><details><summary>원료와 인증</summary><p>검증 상태·출처·업데이트 날짜를 분리해 제공합니다.</p></details><details><summary>리필과 회수</summary><p>패키지 회수 및 재사용 절차를 안내합니다.</p></details></div></div></section><section id="save"><div class="wrap"><div><p class="tag">WK-SEC-12</p><h2>Save My Ritual</h2></div><form id="saveForm" novalidate><label class="field" for="ritualName">리추얼 이름<input id="ritualName" required></label><label class="field" for="contact">연락처<input id="contact" inputmode="tel" required></label><label><input id="agree" type="checkbox" required> 저장 및 알림 동의</label><p><button class="primary" type="submit">레시피 저장</button></p><div id="status" class="status" role="status" aria-live="polite">나만의 조합을 저장해 보세요.</div></form></div></section></main><dialog id="done" aria-labelledby="doneTitle"><h2 id="doneTitle">Ritual Saved</h2><p>레시피 ID WK-$id-R01</p><button id="close" type="button">확인</button></dialog><script>document.querySelectorAll('fieldset button').forEach(b=>b.onclick=()=>{document.querySelectorAll('fieldset button').forEach(x=>x.setAttribute('aria-pressed','false'));b.setAttribute('aria-pressed','true')});let n=180,t;timerBtn.onclick=()=>{clearInterval(t);n=180;t=setInterval(()=>{n--;timer.textContent=String(Math.floor(n/60)).padStart(2,'0')+':'+String(n%60).padStart(2,'0')+' · Brewing';if(n<=0){clearInterval(t);timer.textContent='00:00 · Ready'}},1000)};const f=document.querySelector('#saveForm'),d=document.querySelector('#done'),s=document.querySelector('#status');f.onsubmit=e=>{e.preventDefault();const bad=[...f.elements].find(x=>x.willValidate&&!x.checkValidity());if(bad){s.className='status error';s.setAttribute('role','alert');s.textContent='리추얼 이름, 연락처와 동의를 확인해 주세요.';bad.focus();return}s.className='status success';s.setAttribute('role','status');s.textContent='레시피 저장 완료';d.showModal();close.focus()};close.onclick=()=>{d.close();f.querySelector('button[type=submit]').focus()};d.oncancel=()=>f.querySelector('button[type=submit]').focus();</script></body></html>
"@
 Write-Utf8 "$screenDir\와이어프레임.html" $html

 $screenLabels=@('Portal Hero','Client Vision','Mood Intake','Signature Experience','Mixology Canvas','Product Constellation','Ritual Player','Bundle Atelier','Subscription Rhythm','Community Loop','Evidence Drawer','Saved Ritual CTA')
 $screenNodes=for($i=0;$i -lt 12;$i++){ $y=100+$i*225;"<rect class='a' x='70' y='$y' width='1300' height='185' rx='24'/><text class='s' x='105' y='$($y+45)'>WK-SEC-{0:D2}</text><text class='h' x='105' y='$($y+100)'>$($screenLabels[$i])</text>"-f($i+1)}
 $screenSvg="<svg xmlns='http://www.w3.org/2000/svg' width='1440' height='2880' role='img' aria-labelledby='t d'><title id='t'>WICKETA $name $concept</title><desc id='d'>12개 WICKETA 경험 모듈</desc><rect width='1440' height='2880' fill='#f4f0e8'/><style>.a{fill:#fff;stroke:#6757d9;stroke-width:2}.h{font:700 30px Arial;fill:#171824}.s{font:18px Arial;fill:#59546e}</style><text x='70' y='65' class='h'>WICKETA $id · $concept</text>"+($screenNodes -join '')+"</svg>"
 Write-Utf8 "$screenDir\와이어프레임.svg" $screenSvg
}

$manifest.sectionStandard=12;$manifest.productStandard=20
Write-Utf8 $manifestPath ($manifest|ConvertTo-Json -Depth 12)

$pipeline=@"
# WICKETA 이지희 전용 설계 자동화

## 핵심 원칙

- SOAPHE형 선형 상품 소개 구조를 재사용하지 않는다.
- WICKETA의 고유 흐름인 `감정 진단 → 믹솔로지 조합 → 180초 리추얼 → 번들 설계 → 저장·커뮤니티`를 사용한다.
- 20명의 직업·상황에 맞춰 콘셉트, 킬러 기능과 레이아웃을 다르게 지정한다.
- 화면 ID는 클라이언트별 `WNN-HOME`, `WNN-DIAG`, `WNN-MIX`, `WNN-RITUAL`, `WNN-BUILD`, `WNN-COMM`, `WNN-DONE`을 사용한다.
- 메인 화면은 WICKETA 전용 12개 모듈과 20개 상품으로 구성한다.
- 레이아웃은 editorial, lab, dashboard, spatial, social 5종을 순환 적용한다.
- 문서·HTML·JSON·SVG가 동일한 콘셉트와 ID를 사용해야 한다.
- 상대 경로, 접근성, 오류 복구와 상태 보존을 검증한 뒤 완료 처리한다.
"@
Write-Utf8 (Join-Path $Root '설계 자동화 파이프라인.md') $pipeline
Write-Output 'Customized 20 WICKETA client outputs.'





