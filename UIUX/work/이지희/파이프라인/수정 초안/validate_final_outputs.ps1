param([string]$Root = (Join-Path $PSScriptRoot '최종 수정 파일'))
$ErrorActionPreference='Stop'
$manifest=Get-Content -LiteralPath (Join-Path $Root 'client-manifest.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$errors=@(); $checks=0
function Check([bool]$ok,[string]$message){$script:checks++;if(-not $ok){$script:errors += $message}}
Check ($manifest.clientCount -eq 20) '매니페스트 clientCount가 20이 아님'
$ids=@($manifest.clients.id); Check (($ids|Sort-Object -Unique).Count -eq 20) '클라이언트 ID 중복'
$names=@($manifest.clients.name); Check (($names|Sort-Object -Unique).Count -eq 20) '클라이언트 이름 중복'
$layouts=@($manifest.clients.layout); Check (($layouts|Sort-Object -Unique).Count -eq 5) '레이아웃 유형이 5종이 아님'
$concepts=@($manifest.clients.concept); Check (($concepts|Sort-Object -Unique).Count -eq 20) '클라이언트별 콘셉트가 고유하지 않음'
Check ($manifest.sectionStandard -eq 12) '섹션 표준이 12가 아님'
Check ($manifest.productStandard -eq 20) '상품 표준이 20이 아님'
foreach($c in $manifest.clients){
  $key="$($c.id)_$($c.name)"
  $site=Join-Path $Root "사이트맵\$key"; $flow=Join-Path $Root "서비스 흐름도\$key"; $screen=Join-Path $Root "화면 설계서\$key"
  foreach($f in @("$site\사이트맵.md","$site\사이트맵.mmd","$site\사이트맵.svg","$site\사이트맵.png","$flow\서비스_흐름도.md","$flow\서비스_흐름도.mmd","$flow\서비스_흐름도.svg","$flow\서비스_흐름도.png","$screen\화면_설계서.md","$screen\화면_목록.json","$screen\와이어프레임.html","$screen\와이어프레임.svg","$screen\와이어프레임.png","$screen\화면_설계서.pdf")){Check (Test-Path -LiteralPath $f) "누락: $f"}
  $html=Get-Content -LiteralPath "$screen\와이어프레임.html" -Raw -Encoding UTF8
  Check (([regex]::Matches($html,'<h1\b','IgnoreCase')).Count -eq 1) "$key h1이 1개가 아님"
  Check (([regex]::Matches($html,'<section\b','IgnoreCase')).Count -eq 12) "$key section이 12개가 아님"
  Check (([regex]::Matches($html,"class='product'",'IgnoreCase')).Count -eq 20) "$key 상품이 20개가 아님"
  Check ($html -match "data-layout=`"$([regex]::Escape($c.layout))`"") "$key 레이아웃 유형 불일치"
  Check ($html -match "WK-SEC-12") "$key WICKETA 모듈 ID 누락"
  Check (([regex]::Matches($html,'<form\b','IgnoreCase')).Count -eq 1) "$key form이 1개가 아님"
  Check (([regex]::Matches($html,'<label\b','IgnoreCase')).Count -ge 3) "$key label 부족"
  Check (([regex]::Matches($html,'aria-','IgnoreCase')).Count -ge 5) "$key aria 속성 부족"
  Check ($html -notmatch 'file:///|[A-Z]:\\') "$key HTML 절대 경로 발견"
  $siteMd=Get-Content -LiteralPath "$site\사이트맵.md" -Raw -Encoding UTF8
  $flowMd=Get-Content -LiteralPath "$flow\서비스_흐름도.md" -Raw -Encoding UTF8
  Check ($siteMd -match "클라이언트: $($c.id) · $([regex]::Escape($c.name))") "$key 사이트맵 ID·이름 불일치"
  Check ($siteMd -match "W$($c.id)-HOME") "$key 고유 화면 ID 누락"
  Check ($flowMd -match "W$($c.id)-HOME") "$key 흐름도 고유 화면 ID 누락"
  Check ($flowMd -match ([regex]::Escape($c.killerFeature))) "$key 킬러 기능 누락"
  Check ($flowMd -notmatch 'file:///|[A-Z]:\\') "$key 흐름도 절대 경로 발견"
}
$report=@("# 최종 수정 파일 검증 보고서","","- 검증일: 2026-08-14","- 검사 항목 수: $checks","- 오류 수: $($errors.Count)","- 결과: $(if($errors.Count -eq 0){'통과'}else{'실패'})","")
if($errors.Count){$report += '## 오류';$report += ''; $report += $errors|ForEach-Object{"- $_"}} else {$report += '20명 전체의 파일 세트, ID·이름, 상대 경로와 HTML 구조 최소 기준을 통과했습니다.'}
[System.IO.File]::WriteAllText((Join-Path $Root '검증_보고서.md'),($report -join "`n"),[System.Text.UTF8Encoding]::new($false))
if($errors.Count){$errors|ForEach-Object{Write-Error $_};exit 1}
Write-Output "PASS: $checks checks"



