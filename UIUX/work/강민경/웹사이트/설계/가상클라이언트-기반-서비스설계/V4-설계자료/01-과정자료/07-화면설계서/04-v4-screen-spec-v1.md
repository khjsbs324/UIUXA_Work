# 04. DAMORI V4 공식 화면설계서 V1 (Screen Specification Baseline)

- **단계**: `05-설계 (V4 파이프라인 Screen Specification Baseline V1)`
- **버전**: `V1`
- **프로젝트 브랜드명**: `DAMORI / 다모리`
- **상태**: `CURRENT_WORKING_BASELINE`
- **저장 위치**: `V4-설계자료/04-v4-screen-spec-v1.md`

---

## 1. 문서 개요

### 1.1 최종 경험 목표
본 명세서는 **"브랜드를 소개하면서 제품군까지 설득력 있게 보여주는 포트폴리오형 랜딩 경험"**을 구현하기 위하여, 확정된 **Client Baseline V3**, **Site Map Baseline V3**, **Service Flow Baseline V1**을 바탕으로 3대 공식 Page Anchor (`0.0 HOME / MAIN`, `1.0 PRODUCTS / CATEGORY-SUB`, `2.0 BRAND`)의 화면 레이아웃, 콘텐츠, 인터페이스, 작동 및 연결을 정의한 DAMORI 공식 화면설계서 V1 명세 문서이다.

### 1.2 위계 및 수용 범위 정의
화면설계서는 사이트맵의 공간 구조와 서비스 흐름도의 이동 경로를 구체적인 화면 정보 영역으로 번역한 문서이다. 스토리보드나 와이어프레임보다 상위 수율의 개념적 정보 배치를 다루며, 특정 브랜드 색상, exact px, 구체 UI Component 형태, 필터/탭/카드가 아닌 **정보의 역할과 위계(WHAT)**를 정의하는 데 집중한다.

---

## 2. 설계 기준 및 Source

- **Primary Source**:
  - `Client Baseline V3`: 7인 대표 클라이언트(`V4-C01` ~ `V4-C07`) 요구사항, 10개 Pure DN(`DN-01~08, 12, 13`), 8개 RG(`RG-01~08`).
  - `Site Map Baseline V3`: 3대 공식 Page Anchor (`0.0`, `1.0`, `2.0`) 및 16개 서브 섹션.
  - `Service Flow Baseline V1`: 3대 멀티 진입 경로(`PATH A`, `PATH B`, `PATH C`).
- **Brand Source**: `04-기획/브랜드-기획/BRAND-PLAN.md` (DAMORI 존재 이유, 기록 철학, 핵심 가치 3종).
- **Product Source**: `products-200-v6.json` (약 200개 Raw Product Source Pool).
- **디자인 참고자료**: `V4-설계자료/웹디자인-레퍼런스/` (`DESIGN_REFERENCE_ONLY`).

---

## 3. 화면설계 공통 원칙

1. **비판매 포트폴리오 랜딩 원칙**: 결제, 장바구니, 구매하기, 가격, 수량 선택 등 쇼핑몰 UI 요소를 전면 배제하며, 탐색·이해·비교·브랜드 연결에 집중한다.
2. **비실행 정보형 원칙**: 실제 기록 작성, 파일 저장, IndexedDB 로컬 캐시 실행 등 모바일/웹앱 동작을 배제하고, 서비스 특성 안내 및 경험 미리보기 형태로 정보를 제공한다.
3. **미니멀 GNB 고정**: 전역 상단 내비게이션은 `[LOGO / HOME] | PRODUCTS | BRAND` 3대 앵커만 유지하며, `SEARCH`는 `HOLD_DESIGN_OPPORTUNITY` 상태로 관리한다.
4. **Grayscale 와이어프레임 대비성**: 색상에 의존하지 않고 정보의 크기, 여백, 대비, 그룹핑만으로 정보 위계가 성립하도록 설계한다.

---

## 4. 화면 목록

| Canonical ID | Working Alias | 공식 화면명 | 핵심 목적 | 주요 수용 Service Path |
|---|---|---|---|---|
| **0.0** | `PAGE-00` | `HOME / MAIN` | DAMORI 브랜드 소개, 기록 경험 제안, 쇼케이스 통합 포트폴리오 랜딩 | `PATH A` (Main Narrative), `PATH C` |
| **1.0** | `PAGE-01` | `PRODUCTS / CATEGORY-SUB` | 제품군 비주얼 탐색, 소재/제본/필기 적합성/실측 치수 대조 및 탐색 기준 안내 | `PATH B` (Product Task), `PATH C` (후속) |
| **2.0** | `PAGE-02` | `BRAND` | DAMORI 존재 이유, 기록 철학, 가치 및 제품 원칙 서사 전달 | `PATH A` (서사 심화), `PATH B/C` (Optional) |

---

## 5. 0.0 HOME / MAIN 화면설계

### 5.1 선생님 9개 공식 작성 양식

1. **화면명**: `0.0 HOME / MAIN (DAMORI Long Scroll Portfolio Landing)`
2. **목적**: DAMORI의 존재 이유, 브랜드 철학, 기록 경험을 서사적으로 전달하고 대표 제품 쇼케이스를 통해 포트폴리오를 총체적으로 경험하게 함.
3. **주요 콘텐츠**:
   - `0.1 First Impression`: DAMORI 브랜드명, 존재 이유 요약, 일상 속 쉼표 메시지, 대표 비주얼 영역.
   - `0.2 Brand Core Summary`: 사색의 깊이, 보존성, 자율성 상위 가치 요약 정보.
   - `0.3 Recording Experience`: 저부담 회고, 글 보존, 편안한 복귀 3대 주요 기록 경험 소개.
   - `0.4 Product Groups Intro`: 아날로그 & 디지털 하이브리드 결합 제품군 소개 및 제품 탐색 연결 정보.
   - `0.5 Portfolio Showcase`: 대표 Product 최소 15개 이상을 설득력 있게 수용하는 시각 포트폴리오 영역.
   - `0.6 Navigation & Footer`: 서브페이지 보조 연결 및 DAMORI 전역 푸터 정보.
4. **인터페이스**: GNB 상단 내비게이션(`[LOGO / HOME] | PRODUCTS | BRAND`), 스크롤 탐색 가이드, 섹션 이동 링크, 쇼케이스 정보 확인 선택 인터랙션.
5. **레이아웃**: 상단 비주얼 히로 ➔ 중단 에디토리얼 텍스트-이미지 믹스 ➔ 하단 반복형 다열 쇼케이스 배치 ➔ 전역 푸터.
6. **작동**: 스크롤에 따른 섹션 순차 탐색, 쇼케이스 제품/제품군 선택 시 `PRODUCTS 1.3` 관련 특징 및 사양 정보 뷰로 이동.
7. **연결**: `PRODUCTS (1.2/1.3)`, `BRAND (2.1/2.3)`
8. **사용자 경로**: `PATH A` (Main Narrative: Step A-1 ~ A-6), `PATH C` (Need-based Discovery: Step C-1 ~ C-2)
9. **비고**: 결제 중심 쇼핑몰 메인이 아니며, 대표 Product 최소 15개 이상을 유연하게 수용할 수 있는 포트폴리오 랜딩 구조를 유지함. (실제 15개 대표 제품은 후속 검증 단계에서 확정).

### 5.2 보조 QA 및 정합성 항목
- **관련 Client**: `V4-C03 (하람)`, `V4-C06 (이준)`, `V4-C01 (은재 보조)`
- **관련 DN / RG**: `DN-03, 06, 12` / `RG-03, 06`
- **상태 및 예외**: 정상 랜딩 서사 탐색 / 콘텐츠 또는 이미지 로드 실패 시 대체 정보 및 비주얼 그레이박스 제공 (`IMAGE_LOAD_ERROR`, `CONTENT_LOAD_ERROR`).
- **Responsive 고려사항**: Desktop 다열 구조 ➔ Mobile 수직 1컬럼 에디토리얼 흐름으로 손실 없이 전환.
- **Accessibility 고려사항**: H1~H3 헤딩 위계 준수, 키보드 Tab Focus Ring 적용, 이미지 Alt Text 제공.
- **Reference Insight**: 서사 중심 브랜드 스토리텔링 및 쇼케이스 연결 레이아웃 여백 리듬 참고.
- **Design Opportunity**: 저부담 회고 미리보기 UI, 복귀 응원 안내 UI.
- **확정 / 미확정 / 후속 결정**:
  - `CONFIRMED`: 0.1~0.6 섹션 역할 및 포트폴리오 랜딩 성격.
  - `UNCONFIRMED`: exact px, Column 수, 애니메이션 종류/시간.
  - `NEXT_STAGE_DECISION`: Storyboard / Wireframe 단계에서 시각적 구체화.

---

## 6. 1.0 PRODUCTS / CATEGORY-SUB 화면설계

### 6.1 선생님 9개 공식 작성 양식

1. **화면명**: `1.0 PRODUCTS / CATEGORY-SUB (Product Portfolio & Specification)`
2. **목적**: DAMORI 하이브리드 제품군을 포트폴리오 형태로 탐색하고, 소재/제본/필기 적합성/실측 치수 대조 및 사용자 기준 탐색 정보를 제공함.
3. **주요 콘텐츠**:
   - `1.1 Visual Hero`: 카테고리/제품군 시각 아이덴티티 표현 영역.
   - `1.2 Product Group Exploration`: 약 200개 Raw Product Pool을 유연하게 수용하는 제품군 탐색 정보 영역.
   - `1.3 Product Feature & Specification`: 소재, 평면 펼침 제본, 필기 적합성 정보, 실측 치수 1:1 대조 정보 및 사용 맥락(Usage Context) 안내.
   - `1.4 User-led Exploration`: 회원가입/진단 강요 없이 비교·탐색에 참고할 기준과 관련 정보 범위를 안내하는 비실행형 정보 영역.
4. **인터페이스**: GNB, 제품군 정보 확인, 사양 대조 정보 확인, 탐색 기준 안내 확인, `BRAND 2.6` 연결 링크.
5. **레이아웃**: 상단 비주얼 히로 ➔ 중단 제품군 탐색 갤러리 ➔ 하단 탐색 기준 안내 및 실측 치수 대조 정보 병렬 배치.
6. **작동**: 제품군 정보와 소재·치수 대조 정보를 순차 확인하고, 1.4의 비실행형 탐색 기준과 관련 정보 범위를 참고하며, 제품 원칙 링크 선택 시 `BRAND 2.6`으로 이동함.
7. **연결**: `HOME (0.0)`, `BRAND (2.6)`
8. **사용자 경로**: `PATH B` (Product Task Flow: Step B-1 ~ B-5), `PATH C` (후속 단계)
9. **비고**: 결제, 장바구니, 가격, 수량 선택 등 쇼핑몰 UI 요소 배제. 약 200개 Raw Product Pool을 수용하되 Category 수 및 이름은 미확정 유지함.

### 6.2 보조 QA 및 정합성 항목
- **관련 Client**: `V4-C01 (은재)`, `V4-C02 (지안)`, `V4-C04 (소담)`, `V4-C07 (다온)`
- **관련 DN / RG**: `DN-01, 02, 04, 07, 08, 13` / `RG-01, 02, 04, 07, 08`. `DN-05/RG-05`는 원본 서비스 요구 추적용이며 현재 Page 직접 수용 범위 밖임.
- **상태 및 예외**: 정상 정보 대조 / 관련 제품 정보 범위를 참고하며, 개별 정보 누락 시 Generic Placeholder 안내 (`PRODUCT_INFO_MISSING`).
- **Responsive 고려사항**: Desktop 병렬 Layout ➔ Mobile 상하 순차 배치 및 대조 정보 가로 스크롤 전환.
- **Accessibility 고려사항**: 표 헤더(`<th>`) 구조 제공, 명도 대비 검증 대상, 키보드 접근성 준수.
- **Reference Insight**: 소재/제본 및 실측 치수 대조 정보 구획의 직관적 시각 배치 참고.
- **Design Opportunity**: 소재 & 치수 1:1 대조 정보 구획. 1.4는 `NON_EXECUTABLE_INFORMATION_STRUCTURE`로 해결됨.
- **확정 / 미확정 / 후속 결정**:
  - `CONFIRMED`: 1.1~1.4 섹션 역할, 비판매 포트폴리오 성격.
  - `UNCONFIRMED`: Category 수/이름, 대표 15개 선정, exact Grid px.
  - `NEXT_STAGE_DECISION`: Storyboard / Wireframe 단계에서 컴포넌트 형태 결정.

---

## 7. 2.0 BRAND 화면설계

### 7.1 선생님 9개 공식 작성 양식

1. **화면명**: `2.0 BRAND (Brand Philosophy & Storytelling)`
2. **목적**: DAMORI가 왜 존재하는가, 기록을 어떻게 바라보는가, 어떤 핵심 가치와 아날로그/디지털 결합 관점 및 제품 원칙을 갖는지 전달함.
3. **주요 콘텐츠**:
   - `2.1 DAMORI Introduction`: 브랜드 명칭의 의미와 비전 서사.
   - `2.2 Brand Existence & Purpose`: 일상 속 기록의 쉼표 메시지 및 존재 이유.
   - `2.3 Recording Philosophy`: "의무가 아닌 쉼표" 기록 철학 및 죄책감 차단 메시지.
   - `2.4 Core Values & User Value`: Zero Strain, Data Integrity, Autonomy 3대 상위 가치.
   - `2.5 Analog & Digital Principle`: 아날로그 물성과 디지털 편의성의 상호 보완 관계.
   - `2.6 Product Principle`: 도구를 과시하지 않고 담백하게 바라보는 DAMORI 제품 원칙.
4. **인터페이스**: GNB, 서사 목차 안내, `PRODUCTS` 연결 링크(2.6 하단), `HOME` 이동 링크.
5. **레이아웃**: 중앙 텍스트 중심 에디토리얼 스토리텔링 Layout + 2.6 하단 제품 원칙 안내 구획.
6. **작동**: 스크롤에 따른 서사 읽기 전개, 2.6 제품 원칙 확인 후 관련 `PRODUCTS` 탐색 영역으로 이관 가능.
7. **연결**: `HOME (0.0)`, `PRODUCTS (1.0)`
8. **사용자 경로**: `PATH A` (서사 심화), `PATH B/C` (Optional Branch)
9. **비고**: 연혁 나열이나 기술 스펙 설명 페이지가 아니며, 순수 브랜드 서사 독서 공간 성격을 유지함.

### 7.2 보조 QA 및 정합성 항목
- **관련 Client**: `V4-C06 (이준)`, `V4-C01 (은재 보조)`, `V4-C03 (하람 보조)`
- **관련 DN / RG**: `DN-06, 12` / `RG-06`
- **상태 및 예외**: 정상 서사 독서 / 텍스트 및 이미지 로드 오류 시 대체 안내 제공.
- **Responsive 고려사항**: 가독성 중심 텍스트 폭 유지 및 모바일 글자 크기 최적화.
- **Accessibility 고려사항**: 스크린 리더용 서사 헤딩 구조 제공, 명도 대비 검증 대상.
- **Reference Insight**: 에디토리얼 브랜드 수필 스토리텔링 구조 참고.
- **Design Opportunity**: 기록 철학 인용구 비주얼 표현.
- **확정 / 미확정 / 후속 결정**:
  - `CONFIRMED`: 2.1~2.6 서사 섹션 구성 및 존재 이유 전달 목적.
  - `UNCONFIRMED`: 최종 브랜드 Copywriting, 이미지 수량, 애니메이션.
  - `NEXT_STAGE_DECISION`: Wireframe 및 Style Guide 단계에서 시각화.

---

## 8. 화면 간 연결 관계

- **`HOME ↔ PRODUCTS`**: `HOME 0.4/0.5`에서 제품군 또는 쇼케이스 선택 시 `PRODUCTS 1.2/1.3`으로 직행 연결.
- **`HOME ↔ BRAND`**: `HOME 0.2`에서 브랜드 서사 심화를 위해 `BRAND 2.1`로 연결.
- **`PRODUCTS ↔ BRAND`**: `PRODUCTS 1.3`에서 스펙 대조 후 제품 제작 원칙이 궁금해질 때 `BRAND 2.6`으로 연결.
- **`GNB 전역 연결`**: 상단 `[LOGO / HOME] | PRODUCTS | BRAND`를 통해 모든 화면에서 1-클릭 상시 이동 보장.

---

## 9. Client Coverage (7/7 매핑)

| Client ID | Client 성명 | 핵심 Site-level Need | Primary 화면 & 섹션 | Optional 화면 | Coverage 상태 |
|---|---|---|---|---|:---:|
| **V4-C01** | 은재 | 제본/지질 사양 대조 & 제품 원칙 | `PRODUCTS 1.3` | `BRAND 2.6` | **COVERED (`DIRECT`)** |
| **V4-C02** | 지안 | 세로 타임라인 서식 특성 파악 | `PRODUCTS 1.2` | `PRODUCTS 1.3` | **COVERED (`INFORMATIONAL`)** |
| **V4-C03** | 하람 | 짧고 부담 없는 회고 방식 이해 | `HOME 0.3` | `PRODUCTS 1.2` | **COVERED (`EXPERIENCE_PREVIEW`)** |
| **V4-C04** | 소담 | 글 보존 서식 구조 정보 파악 | `PRODUCTS 1.3` | `HOME 0.3` | **COVERED (`INFORMATIONAL`)** |
| **V4-C05** | 태오 | 오프라인·로컬 소장 원본 서비스 요구 | 현재 Page 직접 수용 없음 | - | **OUT_OF_CURRENT_SCOPE_REFERENCE** |
| **V4-C06** | 이준 | 죄책감 차단 미안함 없는 복귀 철학 | `HOME 0.3` | `BRAND 2.3` | **COVERED (`EXPERIENCE_PREVIEW`)** |
| **V4-C07** | 다온 | 사용자 기준 자율 좁히기 & 치수 대조 | `PRODUCTS 1.4` | `PRODUCTS 1.3` | **COVERED (`DIRECT`)** |

---

## 10. DN / RG Traceability (10 Pure DNs & 8 RGs)

| Pure DN ID | 관련 RG ID | 대표 Client | 수용 화면 및 섹션 | 수용 방식 | Traceability 판정 |
|---|---|---|---|---|:---:|
| **DN-01** | `RG-01` | `V4-C01` | `PRODUCTS 1.3`, `BRAND 2.6` | 평면 펼침 제본 & 지질 스펙 대조 정보 제공 | **TRACEABLE** |
| **DN-02** | `RG-02` | `V4-C02` | `PRODUCTS 1.2`, `1.3` | 세로 타임라인 서식 특성 파악 안내 제공 | **TRACEABLE** |
| **DN-03** | `RG-03` | `V4-C03` | `HOME 0.3`, `PRODUCTS 1.2` | 저부담 회고 경험 미리보기 및 양식 안내 | **TRACEABLE** |
| **DN-04** | `RG-04` | `V4-C04` | `PRODUCTS 1.3`, `HOME 0.3` | 글 원본 데이터 보존 서식 구조 정보 제공 | **TRACEABLE** |
| **DN-05** | `RG-05` | `V4-C05` | 현재 Page 직접 수용 없음 | 원본 서비스 요구 보존 · 현재 범위 밖 참고 | **TRACEABLE** |
| **DN-06** | `RG-06` | `V4-C06` | `HOME 0.3`, `BRAND 2.3` | 죄책감 없는 기록 복귀 철학 전달 | **TRACEABLE** |
| **DN-07** | `RG-07` | `V4-C07` | `PRODUCTS 1.4` | 비실행형 탐색 기준 및 관련 정보 범위 안내 | **TRACEABLE** |
| **DN-08** | `RG-08` | `V4-C07` | `PRODUCTS 1.3` | 소재/제본/치수 1:1 대조 정보 제공 | **TRACEABLE** |
| **DN-12** | `RG-06관련` | `V4-C06` | `HOME 0.3`, `BRAND 2.3` | 스트릭 파기 죄책감 차단 미안함 없는 철학 | **TRACEABLE** |
| **DN-13** | `RG-04관련` | `V4-C04` | `HOME 0.3` | 원본 서비스 요구로 추적하며 글 원본 보존 상위 메시지로 현재 범위 수용 | **OUT_OF_CURRENT_SCOPE_REFERENCE** |

---

## 11. Service Flow 반영

- **`PATH A (Main Narrative)`**: `HOME 0.1 ➔ 0.5` 브랜드 발견 및 서사 랜딩 화면 정보에 대응됨.
- **`PATH B (Product Task)`**: `PRODUCTS 1.1 ➔ 1.3 (1.4)` 스펙 및 치수 대조 화면 정보에 대응됨.
- **`PATH C (Need-based Discovery)`**: `HOME 0.3 ➔ HOME 0.4 ➔ PRODUCTS 1.2 ➔ PRODUCTS 1.3` 기록 경험 발견과 제품 정보 연결 순서로 대응됨.

---

## 12. 상태 및 예외

- **`HOME`**: `NORMAL` (정상 서사 랜딩), `IMAGE_LOAD_ERROR` / `CONTENT_LOAD_ERROR` (대체 정보 제공).
- **`PRODUCTS`**: `NORMAL` (정상 스펙 대조), `NO_RELEVANT_PRODUCT_INFORMATION` (전체 제품군 안내), `PRODUCT_INFO_MISSING` (대체 스펙 안내).
- **`BRAND`**: `NORMAL` (정상 서사 독서), `CONTENT_LOAD_ERROR` (대체 서사 안내).

---

## 13. Responsive 고려사항

- **`Desktop`**: 서사 텍스트-이미지 믹스 및 스펙 대조 정보 병렬 Layout 표현.
- **`Tablet`**: 마진 축소 및 2컬럼 레이아웃 유지.
- **`Mobile`**: 1컬럼 수직 Reading Order 배치 및 스펙 대조표 정보 정돈.

---

## 14. Accessibility 고려사항

- Heading Tag 위계(H1~H3) 제공, 스크린 리더 가독성 준수, 키보드 Tab Focus Ring 설계.
- `#6B7F5E`/White 명도 대비(`4.3546:1`) 미달 참고치에 따라, 실제 본문용 색상은 후속 Style Guide 단계에서 실측 검증 후 결정함.

---

## 15. Design Reference 활용사항 (`DESIGN_REFERENCE_ONLY`)

- **`HOME`**: 에디토리얼 글 호흡과 쇼케이스 사이의 시각적 여백 리듬 참고.
- **`PRODUCTS`**: 스펙 정보 및 1:1 대조 구획의 깔끔한 정보 위계 참고.
- **`BRAND`**: 미션 서사의 가독성 높은 에디토리얼 수필 전개 방식 참고.

---

## 16. 확정 / 미확정 / 후속 결정

| 구분 | **Confirmed (확정 사항)** | **Unconfirmed / Next Stage (미확정/후속 이관)** |
|---|---|---|
| **0.0 HOME** | 0.1~0.6 섹션 역할, 비판매 포트폴리오 랜딩 성격, 대표 제품 최소 15개 수용 구조 | exact px, Column 수, 애니메이션 효과 ➔ Wireframe/Storyboard 이관 |
| **1.0 PRODUCTS**| 1.1~1.4 섹션 역할, 스펙/치수 대조 및 비실행형 탐색 기준 안내 목적 | Category 수/이름, 대표 15개 선정. 1.4는 `NON_EXECUTABLE_INFORMATION_STRUCTURE`로 Wireframe에서 해결됨 |
| **2.0 BRAND** | 2.1~2.6 서사 섹션 구성, 존재 이유 및 기록 철학 전달 목적 | 최종 브랜드 Copywriting, 이미지 수량 ➔ Style Guide/Visual 이관 |

---

## 17. Storyboard 전달사항

- 스토리보드 단계에서는 확정된 3대 Page 화면 정보 역할을 유지하며, 각 섹션별 씬(Scene) 흐름과 화면 전환 가이드를 구체화함.

---

## 18. Wireframe 전달사항 (Grayscale Constraint)

- **와이어프레임 제작 제약**: 후속 와이어프레임은 **WHITE, GRAY, BLACK Grayscale만 사용**하며, 브랜드 색상에 의존하지 않고 크기, 위치, 여백, 대비, 그룹핑만으로 정보 위계를 표현함.

---

## 19. 검토 결과

- **파일 생성 검증**: `V4-설계자료/04-v4-screen-spec-v1.md` 현재 작업용 Master 문서 유지.
- **선생님 9개 양식**: 3개 화면 모두 9/9 항목 확인.
- **Traceability 검증**: 7/7 Client, 10/10 Pure DN, 8/8 RG 매핑 확인.
- **과설계 검증**: exact px, Column 수, 애니메이션, 브랜드 색상 0건 확정 준수.
