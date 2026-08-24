param(
  [string]$SourceRoot = (Join-Path $PSScriptRoot '자동화'),
  [string]$OutputRoot = (Join-Path $PSScriptRoot '최종 수정 파일')
)

$ErrorActionPreference = 'Stop'
$clientDir = Join-Path $SourceRoot '03_클라이언트\01_가상_클라이언트'
$clientFiles = Get-ChildItem -LiteralPath $clientDir -File -Filter '*.txt' | Where-Object { $_.BaseName -match '^\[가상클라이언트_(\d+)\]\s*([^_]+)' } | Sort-Object { [int]([regex]::Match($_.BaseName, '^\[가상클라이언트_(\d+)\]').Groups[1].Value) }

if ($clientFiles.Count -ne 20) { throw "가상 클라이언트는 20명이어야 합니다. 현재: $($clientFiles.Count)" }

New-Item -ItemType Directory -Path $OutputRoot -Force | Out-Null
foreach ($name in @('사이트맵','서비스 흐름도','화면 설계서')) {
  New-Item -ItemType Directory -Path (Join-Path $OutputRoot $name) -Force | Out-Null
}

function Get-Field([string]$text, [string]$label, [string]$fallback) {
  $m = [regex]::Match($text, "(?m)^- $([regex]::Escape($label)):\s*(.+)$")
  if ($m.Success) { return $m.Groups[1].Value.Trim() }
  return $fallback
}

function Escape-Html([string]$value) {
  return [System.Net.WebUtility]::HtmlEncode($value)
}

function Write-Utf8([string]$path, [string]$content) {
  $parent = Split-Path -Parent $path
  if ($parent) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
  [System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))
}

function Get-RelativeLink([string]$fromDir, [string]$toPath) {
  return [System.IO.Path]::GetRelativePath($fromDir, $toPath).Replace('\','/')
}

$manifest = @()
$statusRows = @()
$products = @('오로라 믹솔로지 티','미드나잇 GABA 릴랙스','제로 칼로리 클린 티','브루잉 타이머 키트','감정 다이얼 큐레이션','글래스 리추얼 세트','논알콜 하이볼 스틱','테아닌 카밍 티','아로마 휠 샘플러','30일 감정 구독 팩','파스텔 글래스웨어','카카오 선물 패키지','비건 블렌딩 티','오피스 퀵브루 스틱','업사이클 틴케이스')

foreach ($file in $clientFiles) {
  $match = [regex]::Match($file.BaseName, '^\[가상클라이언트_(\d+)\]\s*([^_]+)')
  $no = [int]$match.Groups[1].Value
  $id = '{0:D2}' -f $no
  $name = $match.Groups[2].Value
  $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
  $role = Get-Field $text '직책' 'WICKETA 프로젝트 이해관계자'
  $industry = Get-Field $text '업종' '맞춤형 티와 디지털 웰니스'
  $purpose = Get-Field $text '핵심 목적' '개인화된 티 탐색과 사전 신청 경험 구축'
  $focusToken = ($file.BaseName -split '_')[-1] -replace '\.txt$',''
  $clientKey = "${id}_${name}"

  $siteDir = Join-Path $OutputRoot "사이트맵\$clientKey"
  $flowDir = Join-Path $OutputRoot "서비스 흐름도\$clientKey"
  $screenDir = Join-Path $OutputRoot "화면 설계서\$clientKey"
  New-Item -ItemType Directory -Path $siteDir,$flowDir,$screenDir -Force | Out-Null

  $screenIds = @('SCR-100','SCR-110','SCR-120','SCR-130','SCR-140','SCR-150','SCR-160','SCR-170','SCR-180','SCR-190','SCR-200')
  $siteMmd = @"
flowchart TD
  A[SCR-100 메인 진입] --> B[SCR-110 브랜드 이야기]
  B --> C[SCR-120 $focusToken 핵심 경험]
  C --> D[SCR-130 대표 상품 탐색]
  D --> E[SCR-140 감정 진단]
  E --> F[SCR-150 맞춤 추천]
  F --> G[SCR-160 리추얼 체험]
  G --> H[SCR-170 구독과 선물]
  H --> I[SCR-180 신뢰 정보]
  I --> J[SCR-190 사전 신청]
  J -->|성공| K[SCR-200 신청 완료]
  J -->|오류| J
"@
  $siteMd = @"
# WICKETA $name 사이트맵

## 프로젝트 기준

- 클라이언트 ID: $id
- 이름: $name
- 역할: $role
- 업종: $industry
- 핵심 목적: $purpose
- 특화 초점: $focusToken
- 기준 화면 ID: `SCR-100`~`SCR-200`

## 전역 내비게이션

- 홈 `SCR-100`
- 브랜드 `SCR-110`
- 상품 `SCR-130`
- 맞춤 추천 `SCR-150`
- 리추얼 `SCR-160`
- 구독·선물 `SCR-170`
- 신청 `SCR-190`

## 화면 계층

| ID | 화면·영역 | 역할 | 다음 화면 |
|---|---|---|---|
| SCR-100 | 메인 진입 | WICKETA와 $focusToken 가치 제시 | SCR-110 |
| SCR-110 | 브랜드 이야기 | 철학·원료·제작 근거 제공 | SCR-120 |
| SCR-120 | 핵심 경험 | 클라이언트 특화 경험 설명 | SCR-130 |
| SCR-130 | 대표 상품 | 핵심 상품 3종 분산 강조 | SCR-140 |
| SCR-140 | 감정 진단 | 사용자의 현재 상태 입력 | SCR-150 |
| SCR-150 | 맞춤 추천 | 진단 기반 상품 추천 | SCR-160 |
| SCR-160 | 리추얼 체험 | 브루잉 타이머와 사용법 제공 | SCR-170 |
| SCR-170 | 구독과 선물 | 구독 주기와 선물 옵션 선택 | SCR-180 |
| SCR-180 | 신뢰 정보 | 성분·인증·FAQ 제공 | SCR-190 |
| SCR-190 | 사전 신청 | 연락처와 동의 수집 | SCR-200 |
| SCR-200 | 신청 완료 | 접수 결과와 다음 단계 안내 | SCR-100 |

## Mermaid

```mermaid
$siteMmd
```

## 연결 산출물

- [서비스 흐름도](../../서비스%20흐름도/$clientKey/서비스_흐름도.md)
- [화면 설계서](../../화면%20설계서/$clientKey/화면_설계서.md)
"@
  $siteSvg = @"
<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="900" viewBox="0 0 1440 900" role="img" aria-labelledby="title desc"><title id="title">WICKETA $name 사이트맵</title><desc id="desc">메인 진입부터 신청 완료까지 이어지는 화면 계층</desc><rect width="1440" height="900" fill="#f5f3ee"/><style>.t{font:700 28px Arial,sans-serif;fill:#20231f}.n{fill:#fff;stroke:#343a35;stroke-width:2}.s{font:18px Arial,sans-serif;fill:#20231f}.l{stroke:#657068;stroke-width:2;marker-end:url(#a)}</style><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#657068"/></marker></defs><text x="70" y="65" class="t">WICKETA $id $name · 사이트맵</text>
$(for($i=0;$i -lt 11;$i++){ $x=80+(($i%4)*335); $y=110+([math]::Floor($i/4)*245); $label=@('메인 진입','브랜드 이야기',"$focusToken 핵심 경험",'대표 상품','감정 진단','맞춤 추천','리추얼 체험','구독과 선물','신뢰 정보','사전 신청','신청 완료')[$i]; if($i -gt 0){$px=80+((($i-1)%4)*335)+260;$py=110+([math]::Floor(($i-1)/4)*245)+60;"<line x1='$px' y1='$py' x2='$x' y2='$($y+60)' class='l'/>"}; "<rect x='$x' y='$y' width='260' height='120' rx='16' class='n'/><text x='$($x+20)' y='$($y+45)' class='s'>$($screenIds[$i])</text><text x='$($x+20)' y='$($y+80)' class='s'>$([System.Security.SecurityElement]::Escape($label))</text>" })
</svg>
"@

  Write-Utf8 (Join-Path $siteDir '사이트맵.md') $siteMd
  Write-Utf8 (Join-Path $siteDir '사이트맵.mmd') $siteMmd
  Write-Utf8 (Join-Path $siteDir '사이트맵.svg') $siteSvg

  $flowMmd = @"
flowchart LR
  A[SCR-100 방문] --> B[SCR-120 핵심 가치 확인]
  B --> C[SCR-140 감정 진단]
  C --> D{입력 완료?}
  D -->|아니오| E[오류 안내와 포커스 이동]
  E --> C
  D -->|예| F[SCR-150 맞춤 추천]
  F --> G[SCR-160 리추얼 체험]
  G --> H[SCR-170 구독·선물 선택]
  H --> I[SCR-190 사전 신청]
  I --> J{유효성 통과?}
  J -->|아니오| K[인라인 오류와 입력 유지]
  K --> I
  J -->|예| L[SCR-200 완료 안내]
"@
  $flowMd = @"
# WICKETA $name 서비스 흐름도

## 연결 기준

- 클라이언트 ID·이름: $id $name
- 기준 사이트맵: [사이트맵](../../사이트맵/$clientKey/사이트맵.md)
- 화면 설계서: [화면 설계서](../../화면%20설계서/$clientKey/화면_설계서.md)
- 핵심 목표: $purpose

## 정상 흐름

1. `SCR-100` 메인 진입
2. `SCR-110` 브랜드 근거 확인
3. `SCR-120` $focusToken 핵심 경험 탐색
4. `SCR-130` 대표 상품 비교
5. `SCR-140` 감정 진단 입력
6. `SCR-150` 맞춤 추천 확인
7. `SCR-160` 브루잉 리추얼 체험
8. `SCR-170` 구독 또는 선물 옵션 선택
9. `SCR-190` 사전 신청 제출
10. `SCR-200` 접수 완료 확인

## 예외·복구 흐름

- 진단 미완료: 누락 항목 안내 후 `SCR-140` 유지
- 추천 결과 없음: 전체 상품과 상담 연결 제공
- 신청 오류: 입력값을 보존하고 첫 오류 필드로 포커스 이동
- 네트워크 실패: 재시도 버튼과 문의 경로 제공
- 완료 후 재진입: `SCR-200`에서 메인 또는 추천 결과로 이동

## 상태 기준

| 상태 | 표시 내용 | 사용자 복구 |
|---|---|---|
| 기본 | 입력과 CTA 활성 | 작업 시작 |
| 로딩 | 진행 상태와 중복 제출 차단 | 완료까지 대기 |
| 빈 결과 | 대체 상품과 상담 안내 | 조건 수정 |
| 오류 | 원인과 수정 방법 | 입력 수정·재시도 |
| 완료 | 접수 번호와 다음 절차 | 메인 복귀 |

## Mermaid

```mermaid
$flowMmd
```
"@
  $flowSvg = @"
<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="900" viewBox="0 0 1440 900" role="img" aria-labelledby="title desc"><title id="title">WICKETA $name 서비스 흐름도</title><desc id="desc">탐색, 진단, 추천, 신청과 오류 복구 흐름</desc><rect width="1440" height="900" fill="#f5f3ee"/><style>.t{font:700 28px Arial,sans-serif;fill:#20231f}.n{fill:#fff;stroke:#343a35;stroke-width:2}.e{fill:#fff2ef;stroke:#9e4438;stroke-width:2}.s{font:17px Arial,sans-serif;fill:#20231f}.l{stroke:#657068;stroke-width:2;marker-end:url(#a)}</style><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#657068"/></marker></defs><text x="70" y="65" class="t">WICKETA $id $name · 서비스 흐름도</text>
<rect x="80" y="130" width="240" height="100" rx="16" class="n"/><text x="105" y="190" class="s">탐색 SCR-100~130</text><line x1="320" y1="180" x2="390" y2="180" class="l"/><rect x="400" y="130" width="240" height="100" rx="16" class="n"/><text x="425" y="190" class="s">진단 SCR-140</text><line x1="640" y1="180" x2="710" y2="180" class="l"/><rect x="720" y="130" width="240" height="100" rx="16" class="n"/><text x="745" y="190" class="s">추천 SCR-150</text><line x1="960" y1="180" x2="1030" y2="180" class="l"/><rect x="1040" y="130" width="240" height="100" rx="16" class="n"/><text x="1065" y="190" class="s">리추얼 SCR-160</text>
<line x1="1160" y1="230" x2="1160" y2="340" class="l"/><rect x="1040" y="350" width="240" height="100" rx="16" class="n"/><text x="1065" y="410" class="s">구독·선물 SCR-170</text><line x1="1040" y1="400" x2="970" y2="400" class="l"/><rect x="720" y="350" width="240" height="100" rx="16" class="n"/><text x="745" y="410" class="s">신청 SCR-190</text><line x1="720" y1="400" x2="650" y2="400" class="l"/><rect x="400" y="350" width="240" height="100" rx="16" class="n"/><text x="425" y="410" class="s">완료 SCR-200</text><line x1="840" y1="450" x2="840" y2="560" class="l"/><rect x="720" y="570" width="240" height="100" rx="16" class="e"/><text x="745" y="620" class="s">오류: 입력 유지</text><text x="745" y="650" class="s">수정 후 재시도</text>
</svg>
"@
  Write-Utf8 (Join-Path $flowDir '서비스_흐름도.md') $flowMd
  Write-Utf8 (Join-Path $flowDir '서비스_흐름도.mmd') $flowMmd
  Write-Utf8 (Join-Path $flowDir '서비스_흐름도.svg') $flowSvg

  $screenJsonObject = [ordered]@{
    clientId=$id; clientName=$name; project='WICKETA'; focus=$focusToken
    sourceClientFile=$file.Name
    screens=@(
      [ordered]@{id='SCR-100';name='메인페이지';sections=@('SEC-01','SEC-02','SEC-03','SEC-04','SEC-05','SEC-06','SEC-07','SEC-08','SEC-09','SEC-10');states=@('Default','Loading','Empty','Error','Success');nextScreens=@('SCR-200')},
      [ordered]@{id='SCR-200';name='신청 완료 대화상자';states=@('Default','Success');nextScreens=@('SCR-100')}
    )
  }
  $screenJson = $screenJsonObject | ConvertTo-Json -Depth 8
  $productRows = for($i=0;$i -lt $products.Count;$i++){ "| PROD-{0:D2} | {1} | {2} |" -f ($i+1),$products[$i],(@('대표 강조','맞춤 추천','리추얼','구독·선물','전체 모음')[$i%5]) }
  $screenMd = @"
# WICKETA $name 화면 설계서

## 설계 기준

- 클라이언트 ID·이름: $id $name
- 역할: $role
- 특화 초점: $focusToken
- 사이트맵: [사이트맵](../../사이트맵/$clientKey/사이트맵.md)
- 서비스 흐름도: [서비스 흐름도](../../서비스%20흐름도/$clientKey/서비스_흐름도.md)
- 구현 파일: [와이어프레임](와이어프레임.html)

## 메인페이지 10개 섹션

| 섹션 | 역할 | 핵심 UI | 상태 |
|---|---|---|---|
| SEC-01 | Hero와 핵심 CTA | 제목·요약·신청 링크 | 기본 |
| SEC-02 | 브랜드 이야기 | 철학·제작 근거 | 기본 |
| SEC-03 | $focusToken 핵심 경험 | 특화 콘텐츠 | 기본·로딩 |
| SEC-04 | 대표 상품 | 상품 3종 강조 | 기본·품절 |
| SEC-05 | 감정 진단 | 선택 버튼 | 기본·오류 |
| SEC-06 | 맞춤 추천 | 추천 상품 4종 | 로딩·빈 결과·완료 |
| SEC-07 | 리추얼 체험 | 180초 타이머 | 기본·진행·완료 |
| SEC-08 | 구독과 선물 | 주기·포장 선택 | 기본·오류 |
| SEC-09 | 신뢰와 FAQ | 성분·정책·문의 | 기본 |
| SEC-10 | 사전 신청 | 이름·연락처·동의 | 기본·오류·완료 |

## 상품 15개 분산 배치

| ID | 상품 | 배치 목적 |
|---|---|---|
$($productRows -join "`n")

## 접근성·상태 규칙

- 페이지당 `h1` 1개와 의미 단위별 `section` 사용
- 모든 입력에 `label for`와 `id` 연결
- 오류 요약은 `role="alert"`, 처리 결과는 `aria-live="polite"`로 안내
- 대화상자 열림 시 내부로 포커스 이동, 닫힘 시 실행 버튼으로 복귀
- ESC 닫기와 키보드 탭 순서 지원
- 로딩 중 중복 제출 차단, 오류 발생 시 입력값 유지
- 모션 축소 환경에서 애니메이션 비활성화

## 검증 대상

- 화면 ID와 사이트맵·서비스 흐름도 일치
- 10개 섹션과 15개 상품 존재
- 상대 경로만 사용
- 기본·로딩·빈 결과·오류·완료 상태 정의
"@
  Write-Utf8 (Join-Path $screenDir '화면_설계서.md') $screenMd
  Write-Utf8 (Join-Path $screenDir '화면_목록.json') $screenJson

  $cards = for($i=0;$i -lt 15;$i++){ "<article class='card'><span>PROD-{0:D2}</span><h3>{1}</h3><p>{2}</p></article>" -f ($i+1),(Escape-Html $products[$i]),(@('대표 제품의 문제 해결 가치','현재 감정에 맞춘 추천','3분 리추얼과 함께 사용','구독 또는 선물 구성','전체 상품 비교')[$i%5]) }
  $html = @"
<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>WICKETA $name 와이어프레임</title><style>:root{--ink:#20231f;--muted:#667068;--paper:#f5f3ee;--card:#fff;--line:#ccd1ca;--accent:#2f5142}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:system-ui,"Noto Sans KR",sans-serif;line-height:1.6}.wrap{width:min(1120px,calc(100% - 32px));margin:auto}header{position:sticky;top:0;background:#f5f3eef2;border-bottom:1px solid var(--line);z-index:5}nav{min-height:64px;display:flex;align-items:center;justify-content:space-between}nav a{color:inherit;margin-left:16px}.hero{min-height:70vh;display:grid;align-content:center}.eyebrow{letter-spacing:.12em;color:var(--muted)}h1{font-size:clamp(3rem,8vw,7rem);line-height:.9;margin:.2em 0}section{padding:72px 0;border-top:1px solid var(--line)}h2{font-size:clamp(1.8rem,4vw,3.4rem)}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px}.btn,button{display:inline-block;border:1px solid var(--ink);border-radius:999px;background:transparent;color:inherit;padding:11px 16px;font:inherit;cursor:pointer}.primary{background:var(--accent);color:#fff;border-color:var(--accent)}.choices{display:flex;gap:8px;flex-wrap:wrap}.choices button[aria-pressed="true"]{background:var(--ink);color:#fff}.field{display:grid;gap:6px;margin:14px 0}.field input{padding:12px;border:1px solid #727972;border-radius:8px}.status{min-height:48px;padding:12px;background:#e7e9e5;border-radius:8px}.error{background:#f7dfdc}.success{background:#dcecdf}dialog{border:0;border-radius:18px;padding:28px;width:min(520px,calc(100% - 32px))}dialog::backdrop{background:#0008}:focus-visible{outline:3px solid #7b4eff;outline-offset:3px}@media(max-width:760px){.grid{grid-template-columns:1fr}nav a:not(:last-child){display:none}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;animation:none!important;transition:none!important}}</style></head><body><header><nav class="wrap" aria-label="주요 메뉴"><strong>WICKETA · $id</strong><div><a href="#brand">브랜드</a><a href="#products">상품</a><a href="#apply">신청</a></div></nav></header><main><section class="hero" id="home"><div class="wrap"><p class="eyebrow">$id · $(Escape-Html $role)</p><h1>$(Escape-Html $focusToken)<br>나만의 3분 안식처</h1><p>$(Escape-Html $purpose)</p><a class="btn primary" href="#diagnosis">감정 진단 시작</a></div></section><section id="brand"><div class="wrap"><p class="eyebrow">SEC-02</p><h2>복잡한 하루를 단순한 리추얼로</h2><p>WICKETA는 원료 정보, 제작 과정과 사용 근거를 투명하게 연결합니다.</p></div></section><section id="focus"><div class="wrap"><p class="eyebrow">SEC-03</p><h2>$(Escape-Html $focusToken) 핵심 경험</h2><p>$(Escape-Html $industry)</p><div class="card">클라이언트 요구를 브랜드 경험과 전환 흐름에 연결한 특화 영역</div></div></section><section id="products"><div class="wrap"><p class="eyebrow">SEC-04</p><h2>대표 상품을 먼저 깊게 탐색</h2><div class="grid">$($cards[0..2] -join '')</div></div></section><section id="diagnosis"><div class="wrap"><p class="eyebrow">SEC-05</p><h2>오늘의 감정 진단</h2><div class="choices" role="group" aria-label="현재 상태"><button type="button" aria-pressed="false">집중</button><button type="button" aria-pressed="false">휴식</button><button type="button" aria-pressed="false">수면</button></div></div></section><section id="recommend"><div class="wrap"><p class="eyebrow">SEC-06</p><h2>맞춤 추천</h2><div class="grid">$($cards[3..6] -join '')</div></div></section><section id="ritual"><div class="wrap"><p class="eyebrow">SEC-07</p><h2>180초 브루잉 리추얼</h2><p id="timer" aria-live="polite">03:00 · 시작 전</p><button type="button" id="timerBtn">타이머 시작</button></div></section><section id="subscription"><div class="wrap"><p class="eyebrow">SEC-08</p><h2>구독과 선물</h2><div class="grid">$($cards[7..10] -join '')</div></div></section><section id="trust"><div class="wrap"><p class="eyebrow">SEC-09</p><h2>성분·정책·자주 묻는 질문</h2><details><summary>카페인과 원료 정보는 어디서 확인하나요?</summary><p>각 상품의 검증 상태와 출처를 구분하여 제공합니다.</p></details><details><summary>신청 후 변경할 수 있나요?</summary><p>접수 번호와 함께 변경 경로를 안내합니다.</p></details><div class="grid" style="margin-top:24px">$($cards[11..14] -join '')</div></div></section><section id="apply"><div class="wrap"><p class="eyebrow">SEC-10</p><h2>웰컴 키트 사전 신청</h2><form id="applyForm" novalidate><label class="field" for="userName">이름<input id="userName" name="userName" autocomplete="name" required></label><label class="field" for="contact">연락처<input id="contact" name="contact" autocomplete="tel" inputmode="tel" required></label><label><input id="agree" type="checkbox" required> 개인정보 수집 동의</label><p><button class="primary" type="submit">신청하기</button></p><div id="formStatus" class="status" role="status" aria-live="polite">필수 정보를 입력해 주세요.</div></form></div></section></main><dialog id="completeDialog" aria-labelledby="dialogTitle"><h2 id="dialogTitle">신청 완료</h2><p>접수 번호 <strong>WK-$id-001</strong>이 발급되었습니다.</p><button type="button" id="closeDialog">확인</button></dialog><script>document.querySelectorAll('.choices button').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.choices button').forEach(x=>x.setAttribute('aria-pressed','false'));b.setAttribute('aria-pressed','true')}));let left=180,interval;document.querySelector('#timerBtn').addEventListener('click',()=>{clearInterval(interval);left=180;interval=setInterval(()=>{left--;document.querySelector('#timer').textContent=`${String(Math.floor(left/60)).padStart(2,'0')}:${String(left%60).padStart(2,'0')} · 진행 중`;if(left<=0){clearInterval(interval);document.querySelector('#timer').textContent='00:00 · 완료'}},1000)});const form=document.querySelector('#applyForm'),status=document.querySelector('#formStatus'),dialog=document.querySelector('#completeDialog');form.addEventListener('submit',e=>{e.preventDefault();const first=[...form.elements].find(x=>x.willValidate&&!x.checkValidity());if(first){status.className='status error';status.setAttribute('role','alert');status.textContent='필수 입력과 동의 항목을 확인해 주세요.';first.focus();return}status.className='status success';status.setAttribute('role','status');status.textContent='입력 확인 완료';dialog.showModal();document.querySelector('#closeDialog').focus()});document.querySelector('#closeDialog').addEventListener('click',()=>{dialog.close();form.querySelector('button[type=submit]').focus()});dialog.addEventListener('cancel',()=>form.querySelector('button[type=submit]').focus());</script></body></html>
"@
  Write-Utf8 (Join-Path $screenDir '와이어프레임.html') $html

  $screenSvg = @"
<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="2400" viewBox="0 0 1440 2400" role="img" aria-labelledby="title desc"><title id="title">WICKETA $name 화면 설계</title><desc id="desc">10개 섹션으로 구성된 메인페이지 와이어프레임</desc><rect width="1440" height="2400" fill="#f5f3ee"/><style>.h{font:700 38px Arial,sans-serif;fill:#20231f}.s{font:22px Arial,sans-serif;fill:#20231f}.b{fill:#fff;stroke:#6a716b;stroke-width:2}</style><text x="70" y="70" class="h">WICKETA $id $name · 화면 설계</text>$(for($i=0;$i -lt 10;$i++){ $y=110+($i*220); $labels=@('Hero','브랜드 이야기',"$focusToken 핵심 경험",'대표 상품','감정 진단','맞춤 추천','리추얼 체험','구독과 선물','신뢰·FAQ','사전 신청') ; "<rect x='70' y='$y' width='1300' height='180' rx='18' class='b'/><text x='100' y='$($y+55)' class='s'>SEC-{0:D2}</text><text x='100' y='$($y+105)' class='h'>$([System.Security.SecurityElement]::Escape($labels[$i]))</text>" -f ($i+1) })</svg>
"@
  Write-Utf8 (Join-Path $screenDir '와이어프레임.svg') $screenSvg

  $manifest += [ordered]@{id=$id;name=$name;role=$role;industry=$industry;focus=$focusToken;source="../자동화/03_클라이언트/01_가상_클라이언트/$($file.Name)";outputs=[ordered]@{sitemap="사이트맵/$clientKey/사이트맵.md";serviceFlow="서비스 흐름도/$clientKey/서비스_흐름도.md";screenSpec="화면 설계서/$clientKey/화면_설계서.md";wireframe="화면 설계서/$clientKey/와이어프레임.html"}}
  $statusRows += "| $id | $name | 완료 | 완료 | 완료 | 렌더링 대기 |"
}

$manifestJson = [ordered]@{schemaVersion='1.0.0';project='WICKETA';generatedDate='2026-08-14';clientCount=$manifest.Count;sectionStandard=10;productStandard=15;clients=$manifest} | ConvertTo-Json -Depth 10
Write-Utf8 (Join-Path $OutputRoot 'client-manifest.json') $manifestJson

$pipeline = @"
# WICKETA 설계 자동화 파이프라인

## 단일 기준

1. `client-manifest.json`을 번호·이름·입력·출력 경로의 유일한 기준으로 사용한다.
2. 각 클라이언트는 `사이트맵 → 서비스 흐름도 → 화면 설계서` 순서로 생성한다.
3. 클라이언트별 결과는 `NN_이름` 폴더 한 곳에 표준 파일명으로 저장한다.
4. 사이트맵과 서비스 흐름도는 `md/mmd/svg/png`, 화면 설계서는 `md/json/html/svg/png/pdf`를 생성한다.
5. 문서 내부 링크는 상대 경로만 사용한다.
6. 메인페이지는 10개 섹션, 상품은 15개를 여러 섹션에 분산한다.
7. 화면 ID는 `SCR-100`~`SCR-200`, 섹션 ID는 `SEC-01`~`SEC-10`으로 고정한다.
8. HTML은 `h1` 1개, `section` 10개, 실제 폼과 레이블, 오류·완료 상태, 대화상자 포커스 복귀를 포함한다.
9. 생성 후 `검증.ps1`을 실행하고 모든 항목이 통과한 경우에만 완료로 기록한다.
10. 캐시·로그·의존성은 최종 결과 폴더에 저장하지 않는다.

## 완료 조건

- 20명 각각 사이트맵 4종, 서비스 흐름도 4종, 화면 설계서 6종 존재
- 매니페스트의 ID·이름과 모든 폴더명이 일치
- 절대 경로와 존재하지 않는 참조 없음
- HTML 구조·접근성 최소 기준 통과
- `workflow-status.md`와 `검증_보고서.md` 갱신
"@
Write-Utf8 (Join-Path $OutputRoot '설계 자동화 파이프라인.md') $pipeline

$readme = @"
# 이지희 WICKETA 최종 수정 파일

이 폴더는 기존 `자동화` 원본을 변경하지 않고, 번호·경로·산출물 연결·접근성 문제를 수정해 새로 생성한 최종 결과입니다.

## 구조

- `client-manifest.json`: 20명 단일 기준
- `설계 자동화 파이프라인.md`: 수정된 생성·검증 규칙
- `사이트맵/NN_이름`: 클라이언트별 4종
- `서비스 흐름도/NN_이름`: 클라이언트별 4종
- `화면 설계서/NN_이름`: 클라이언트별 6종
- `workflow-status.md`: 완료 현황
- `검증.ps1`: 자동 검증
- `검증_보고서.md`: 검증 결과

## 사용 순서

1. `client-manifest.json`에서 대상 클라이언트 확인
2. 사이트맵 → 서비스 흐름도 → 화면 설계서 순서로 검토
3. `와이어프레임.html` 실행
4. `검증.ps1` 실행 후 보고서 확인
"@
Write-Utf8 (Join-Path $OutputRoot 'README.md') $readme

$status = "# WICKETA 설계 자동화 진행 현황`n`n| ID | 이름 | 사이트맵 | 서비스 흐름도 | 화면 설계서 | PNG·PDF |`n|---|---|---|---|---|---|`n" + ($statusRows -join "`n") + "`n"
Write-Utf8 (Join-Path $OutputRoot 'workflow-status.md') $status

$renderer = @'
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
'@
Write-Utf8 (Join-Path $OutputRoot 'render_outputs.js') $renderer

Write-Output "Generated text outputs for $($manifest.Count) clients at $OutputRoot"


