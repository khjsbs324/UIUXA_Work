# 수집 레퍼런스 분석 및 Flow 프롬프트 생성 가이드

## Flow 이미지 생성 프롬프트 작성

### 목적

`output/[N번]/` 폴더에 수집된 3장의 로고 레퍼런스를 시각적으로 분석하여 Flow의 이미지 생성 기능에 바로 사용할 수 있는 최적의 영문 프롬프트를 작성한다. 이 단계에서는 이미지를 직접 생성하지 않고 프롬프트만 작성한다.

### 실행 규칙

1. `output/[N번]/` 폴더에서 JPG, JPEG, PNG, WebP 이미지 파일 3장을 확인한다.
2. 각 이미지를 실제로 열어 심볼의 구조, 도형, 선, 구성, 여백, 색상, 질감, 분위기를 분석한다.
3. 분석 내용을 바탕으로 Flow 이미지 생성 기능에 사용할 수 있는 구체적인 프롬프트를 작성한다.
4. 프롬프트 본문은 반드시 **100% 영문(English)**으로 작성한다.
5. 프롬프트에는 다음 내용을 포함한다.
   - 생성할 로고의 핵심 심볼과 구조 (`Minimalist 2D vector logo symbol`, `geometric circular design`)
   - 조형적 요소 및 선의 특징 (`flat line art logo mark`, `interlocking circle grid emblem`)
   - 브랜드 인상과 웰니스/오브제 콘셉트 (`modern aesthetic lifestyle branding identity`)
   - 배경색과 로고 색상 (`pure black logo mark on a solid clean white background`, `monochrome`, `high contrast`)
   - 네거티브 조건 (`no background grid lines`, `no 3D rendering`, `no shadows`, `no mockups`, `no color gradient`)
6. 레퍼런스를 그대로 복제하거나 기존 브랜드·작가·상표명을 모방하도록 지시하지 않는다. 형태적 특징과 디자인 원리만 추출해 새로운 로고를 생성하도록 작성한다.
7. 작성 결과는 `output/[N번]/flow.md`에 저장한다.

### flow.md 작성 형식

각 이미지의 **확장자를 포함한 파일 이름**을 Markdown 대제목(`#`)으로 작성하고, 바로 아래에 영문 프롬프트를 작성한다.

```markdown
# similar_logo_01.jpg

Minimalist 2D vector logo symbol, continuous organic interlocking circles emblem connected with smooth flowing S-curves, pure black logo mark on a solid clean white background, high contrast monochrome flat vector line art, modern object lifestyle branding symbol, pure black and white, vector outline graphic, no background grid lines, no 3D rendering, no shadows, no mockups, no color gradient

# similar_logo_02.jpg

Minimalist 2D vector logo emblem, geometric circular emblem with concentric arc lines, pure black logo mark on a solid clean white background, high contrast monochrome art, modern aesthetic lifestyle branding identity, flat vector line art, no background grid lines, no 3D rendering, no shadows, no mockups, no color gradient

# similar_logo_03.jpg

Minimalist 2D vector logo symbol, geometric emblem featuring interlocking bold circular shapes in balanced composition, pure black logo mark on a solid clean white background, high contrast monochrome flat vector line art, modern object lifestyle branding symbol, pure black and white, vector outline graphic, no background grid lines, no 3D rendering, no shadows, no mockups, no color gradient
```

- 파일명 대제목과 프롬프트 사이에는 빈 줄을 한 줄 넣는다.
- 이미지 하나당 프롬프트 하나만 작성한다.
- 프롬프트 외의 분석 메모, 한국어 설명, 출처 URL은 `flow.md`에 넣지 않는다.

## 완료 보고

분석 작업이 완료되면 다음 정보를 제공한다.

- 지정 초안 번호 (N번)
- 분석 대상 이미지 목록 및 수량 (3장)
- 갱신된 `output/[N번]/flow.md` 파일 경로
- 작성된 영문 프롬프트의 최종 검증 여부 (한글 미포함 확인)
