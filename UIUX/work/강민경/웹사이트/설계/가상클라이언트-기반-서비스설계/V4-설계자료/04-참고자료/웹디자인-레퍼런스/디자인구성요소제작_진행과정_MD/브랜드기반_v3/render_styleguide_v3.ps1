param(
  [string]$V2Dir = (Join-Path $PSScriptRoot '..\브랜드기반_v2'),
  [string]$OutputDir = $PSScriptRoot
)

Add-Type -AssemblyName System.Drawing

$olive = [System.Drawing.ColorTranslator]::FromHtml('#4F603F')
$ink = [System.Drawing.ColorTranslator]::FromHtml('#25281F')
$paper = [System.Drawing.Color]::FromArgb(242, 255, 252, 245)
$line = [System.Drawing.ColorTranslator]::FromHtml('#CFCABC')
$sage = [System.Drawing.ColorTranslator]::FromHtml('#B8C5A9')
$blue = [System.Drawing.ColorTranslator]::FromHtml('#2457A7')

$fontTitle = New-Object System.Drawing.Font('Malgun Gothic', 13, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
$fontBody = New-Object System.Drawing.Font('Malgun Gothic', 12, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
$fontMicro = New-Object System.Drawing.Font('Malgun Gothic', 10, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)

function Add-RoundRectPath([float]$x,[float]$y,[float]$w,[float]$h,[float]$r) {
  $p = New-Object System.Drawing.Drawing2D.GraphicsPath
  $d = $r * 2
  $p.AddArc($x,$y,$d,$d,180,90)
  $p.AddArc($x+$w-$d,$y,$d,$d,270,90)
  $p.AddArc($x+$w-$d,$y+$h-$d,$d,$d,0,90)
  $p.AddArc($x,$y+$h-$d,$d,$d,90,90)
  $p.CloseFigure()
  return $p
}

function Draw-Panel($g,$spec) {
  $path = Add-RoundRectPath $spec.X $spec.Y $spec.W $spec.H 14
  $brush = New-Object System.Drawing.SolidBrush($paper)
  $pen = New-Object System.Drawing.Pen($line,1)
  $g.FillPath($brush,$path)
  $g.DrawPath($pen,$path)
  $accent = New-Object System.Drawing.SolidBrush($olive)
  $g.FillRectangle($accent,$spec.X,$spec.Y,5,$spec.H)
  $titleBrush = New-Object System.Drawing.SolidBrush($olive)
  $bodyBrush = New-Object System.Drawing.SolidBrush($ink)
  $g.DrawString($spec.Title,$fontTitle,$titleBrush,$spec.X+22,$spec.Y+14)
  $y = $spec.Y + 42
  foreach($lineText in $spec.Lines) {
    $g.DrawString($lineText,$fontBody,$bodyBrush,$spec.X+22,$y)
    $y += 23
  }
  $titleBrush.Dispose(); $bodyBrush.Dispose(); $accent.Dispose(); $pen.Dispose(); $brush.Dispose(); $path.Dispose()
}

function Draw-Pill($g,$x,$y,$w,$text,$fillColor=$olive,$textColor=[System.Drawing.Color]::White) {
  $path = Add-RoundRectPath $x $y $w 34 17
  $brush = New-Object System.Drawing.SolidBrush($fillColor)
  $textBrush = New-Object System.Drawing.SolidBrush($textColor)
  $g.FillPath($brush,$path)
  $format = New-Object System.Drawing.StringFormat
  $format.Alignment = [System.Drawing.StringAlignment]::Center
  $format.LineAlignment = [System.Drawing.StringAlignment]::Center
  $g.DrawString($text,$fontMicro,$textBrush,(New-Object System.Drawing.RectangleF($x,$y,$w,34)),$format)
  $format.Dispose(); $textBrush.Dispose(); $brush.Dispose(); $path.Dispose()
}

function Fill-RoundRect($g,$x,$y,$w,$h,$radius,$color) {
  $path = Add-RoundRectPath $x $y $w $h $radius
  $brush = New-Object System.Drawing.SolidBrush($color)
  $g.FillPath($brush,$path)
  $brush.Dispose(); $path.Dispose()
}

function Draw-Label($g,$text,$x,$y,$font,$color) {
  $brush = New-Object System.Drawing.SolidBrush($color)
  $g.DrawString($text,$font,$brush,$x,$y)
  $brush.Dispose()
}

function Draw-HeaderAnatomy($g) {
  $surface = [System.Drawing.ColorTranslator]::FromHtml('#F7F3E8')
  $soft = [System.Drawing.ColorTranslator]::FromHtml('#E8EDDF')
  $avoid = [System.Drawing.ColorTranslator]::FromHtml('#F2E1D8')
  $cover = New-Object System.Drawing.SolidBrush($surface)
  $g.FillRectangle($cover,390,0,1196,224)
  $cover.Dispose()

  Draw-Label $g 'OVERLAY HEADER · DO' 426 48 $fontTitle $olive
  Draw-Label $g 'LOGO와 UTILITY는 배경 없이, 중앙 MENU만 낮고 긴 SURFACE' 426 75 $fontBody $ink
  Draw-Label $g 'DAMORI' 442 119 $fontTitle $ink
  Fill-RoundRect $g 720 105 470 48 16 $soft
  Draw-Label $g '방식 찾기     비교     템플릿     기록 가이드' 776 121 $fontBody $ink
  Draw-Label $g '로그인   ○' 1380 119 $fontBody $ink

  Draw-Label $g 'AVOID' 52 758 $fontTitle $olive
  Fill-RoundRect $g 52 790 300 70 18 $avoid
  Draw-Label $g 'DAMORI  MENU  LOGIN' 104 812 $fontBody $ink
  Draw-Label $g 'HEADER 전체 BOX 금지' 93 874 $fontBody $ink
}

function Draw-SafeArea($g) {
  $surface = [System.Drawing.ColorTranslator]::FromHtml('#F7F3E8')
  $soft = [System.Drawing.ColorTranslator]::FromHtml('#E8EDDF')
  $cover = New-Object System.Drawing.SolidBrush($surface)
  $g.FillRectangle($cover,1200,500,386,430)
  $cover.Dispose()
  Draw-Label $g 'OVERLAY HEADER SAFE AREA' 1225 528 $fontTitle $olive
  Draw-Label $g 'DESKTOP · 24 / HERO · 64' 1225 558 $fontBody $ink
  $pen = New-Object System.Drawing.Pen($olive,2)
  $dash = New-Object System.Drawing.Pen($sage,1)
  $dash.DashStyle = [System.Drawing.Drawing2D.DashStyle]::Dash
  $g.DrawRectangle($pen,1230,603,310,215)
  $g.DrawLine($dash,1230,663,1540,663)
  Fill-RoundRect $g 1315 618 145 30 12 $soft
  Draw-Label $g 'CENTER MENU' 1344 626 $fontMicro $olive
  Draw-Label $g 'HEADER 24' 1242 617 $fontMicro $ink
  Draw-Label $g 'HERO QUIET AREA 64' 1242 682 $fontMicro $ink
  Draw-Label $g 'OBJECT GAP 32–64' 1242 786 $fontMicro $ink
  Draw-Label $g 'MOBILE: MENU 제거 · HIT AREA 44' 1225 850 $fontBody $ink
  $pen.Dispose(); $dash.Dispose()
}

function Draw-PagePattern($g) {
  $surface = [System.Drawing.ColorTranslator]::FromHtml('#FFFCF5')
  $soft = [System.Drawing.ColorTranslator]::FromHtml('#E8EDDF')
  $clay = [System.Drawing.ColorTranslator]::FromHtml('#F2E1D8')
  $dark = [System.Drawing.ColorTranslator]::FromHtml('#25281F')
  $cover = New-Object System.Drawing.SolidBrush($surface)
  $g.FillRectangle($cover,950,175,586,680)
  $cover.Dispose()
  Draw-Label $g 'PAGE PATTERN · FINAL V3' 980 194 $fontTitle $olive

  $hero = New-Object System.Drawing.SolidBrush($dark)
  $g.FillRectangle($hero,980,228,526,232)
  $hero.Dispose()
  Draw-Label $g 'DAMORI' 999 246 $fontMicro ([System.Drawing.Color]::White)
  Fill-RoundRect $g 1135 238 235 30 12 ([System.Drawing.Color]::FromArgb(65,255,255,255))
  Draw-Label $g '방식 찾기   비교   템플릿' 1170 246 $fontMicro ([System.Drawing.Color]::White)
  Draw-Label $g '로그인' 1450 246 $fontMicro ([System.Drawing.Color]::White)
  Draw-Label $g '기록은 남고,' 1002 302 $fontTitle ([System.Drawing.Color]::White)
  Draw-Label $g '방식은 달라져도 돼요.' 1002 331 $fontTitle ([System.Drawing.Color]::White)

  Fill-RoundRect $g 1260 286 125 145 18 $sage
  $diary = New-Object System.Drawing.Pen($olive,2)
  $g.DrawLine($diary,1278,322,1368,322)
  $g.DrawLine($diary,1278,350,1368,350)
  $g.DrawLine($diary,1278,378,1368,378)
  $diary.Dispose()
  Fill-RoundRect $g 1372 326 105 92 14 $surface
  Draw-Label $g 'DIGITAL' 1394 343 $fontMicro $olive
  Draw-Label $g '오늘 한 줄' 1390 372 $fontMicro $ink

  Draw-Label $g 'ANALOG / DIGITAL' 980 485 $fontMicro $olive
  Fill-RoundRect $g 980 510 252 102 12 $soft
  Fill-RoundRect $g 1254 510 252 102 12 ([System.Drawing.ColorTranslator]::FromHtml('#E7EDF7'))
  Draw-Label $g '쿠션 다이어리 · 제본 · 내지' 1000 548 $fontBody $ink
  Draw-Label $g '노트북 · APP · 실제 기록 UI' 1273 548 $fontBody $ink

  Draw-Label $g 'TEMPLATE GALLERY' 980 635 $fontMicro $olive
  for($n=0;$n -lt 4;$n++) {
    Fill-RoundRect $g (980 + $n*132) 660 116 92 10 $(if($n%2 -eq 0){$clay}else{$soft})
    Draw-Label $g @('여행','학습','취향','노트')[$n] (1018 + $n*132) 692 $fontBody $ink
  }
  Draw-Label $g 'LOGIN / RESUME' 980 779 $fontMicro $olive
  Fill-RoundRect $g 980 800 256 38 10 $soft
  Fill-RoundRect $g 1250 800 256 38 10 $clay
  Draw-Label $g '이 기기의 기록 이어가기' 1010 811 $fontMicro $ink
  Draw-Label $g 'PROTOTYPE · 로그인' 1295 811 $fontMicro $ink
}

for($i=1; $i -le 13; $i++) {
  $src = Join-Path $V2Dir ("브랜드-선호디자인기반-스타일가이드{0}_v2.png" -f $i)
  $dst = Join-Path $OutputDir ("브랜드기반_스타일가이드_최종안{0}.png" -f $i)
  $img = [System.Drawing.Bitmap]::FromFile($src)
  $canvas = New-Object System.Drawing.Bitmap($img.Width,$img.Height,[System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
  $g = [System.Drawing.Graphics]::FromImage($canvas)
  $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
  $g.DrawImage($img,0,0,$img.Width,$img.Height)
  if($i -eq 1) { Draw-Pill $g 1370 44 155 'FINAL V3 · 05 SPEC' $sage $ink }
  if($i -eq 5) { Draw-SafeArea $g }
  if($i -eq 6) { Draw-HeaderAnatomy $g }
  if($i -eq 13) { Draw-PagePattern $g }
  if($i -gt 1) { Draw-Pill $g 1430 930 96 'V3' $olive ([System.Drawing.Color]::White) }
  $g.Dispose(); $img.Dispose()
  $canvas.Save($dst,[System.Drawing.Imaging.ImageFormat]::Png)
  $canvas.Dispose()
}

$fontTitle.Dispose(); $fontBody.Dispose(); $fontMicro.Dispose()

$thumbW = 397
$thumbH = 248
$sheet = New-Object System.Drawing.Bitmap(1588,992,[System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$sg = [System.Drawing.Graphics]::FromImage($sheet)
$sg.Clear([System.Drawing.ColorTranslator]::FromHtml('#25281F'))
$sg.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
for($i=1; $i -le 13; $i++) {
  $src = Join-Path $OutputDir ("브랜드기반_스타일가이드_최종안{0}.png" -f $i)
  $thumb = [System.Drawing.Bitmap]::FromFile($src)
  $col = ($i - 1) % 4
  $row = [Math]::Floor(($i - 1) / 4)
  $sg.DrawImage($thumb,$col*$thumbW,$row*$thumbH,$thumbW,$thumbH)
  $thumb.Dispose()
}
$sg.Dispose()
$sheet.Save((Join-Path $OutputDir '브랜드기반_스타일가이드_최종안_컨택트시트.png'),[System.Drawing.Imaging.ImageFormat]::Png)
$sheet.Dispose()
