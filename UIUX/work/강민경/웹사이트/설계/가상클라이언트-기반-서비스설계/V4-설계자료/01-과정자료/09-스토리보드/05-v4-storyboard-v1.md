# 05. DAMORI V4 공식 통합 스토리보드 V1 (Storyboard Baseline)

- **단계**: `05-설계 (V4 파이프라인 Storyboard Baseline V1)`
- **버전**: `V1`
- **프로젝트 브랜드명**: `DAMORI / 다모리`
- **상태**: `CURRENT_WORKING_MASTER_BASELINE`
- **저장 위치**: `V4-설계자료/05-v4-storyboard-v1.md`

---

## 1. 문서 개요

### 1.1 최종 경험 목표
본 명세서는 **"브랜드를 소개하면서 제품군까지 설득력 있게 보여주는 포트폴리오형 랜딩 경험"**을 구현하기 위하여, 확정된 **Client Baseline V3**, **Site Map Baseline V3**, **Service Flow Baseline V1**, **Screen Specification Baseline V1**을 바탕으로 3대 공식 Page (`0.0 HOME / MAIN`, `1.0 PRODUCTS / CATEGORY-SUB`, `2.0 BRAND`)의 화면별 콘텐츠 순서, 시각적 역할, 서사적 리듬 및 사용자 행동 경로를 구체화한 DAMORI 공식 통합 스토리보드 V1 명세 문서이다.

### 1.2 스토리보드 역할 및 범위 정의
스토리보드는 화면설계서(Screen Specification)의 정보 요구사항(WHAT)을 구체적인 화면 콘텐츠 전개 순서와 visual 스토리텔링 시각(HOW)으로 번역하는 단계이다. 와이어프레임(Wireframe)보다 상위의 시각적 뼈대 구성을 정의하며, 특정 px, exact Grid 수, exact Gray HEX, 애니메이션 시간, 확정 컴포넌트 형태가 아닌 **콘텐츠의 시각적 역할과 흐름(Rhythm & Sequence)**을 정의한다.

---

## 2. 설계 기준 및 Source

- **Primary Source**:
  - `Client Baseline V3`: 7인 대표 클라이언트(`V4-C01` ~ `V4-C07`), 10개 Pure DN(`DN-01~08, 12, 13`), 8개 RG(`RG-01~08`).
  - `Site Map Baseline V3`: 3대 공식 Page Anchor (`0.0`, `1.0`, `2.0`) 및 16개 서브 섹션.
  - `Service Flow Baseline V1`: 3대 멀티 진입 경로(`PATH A`, `PATH B`, `PATH C`).
  - `Screen Spec Baseline V1`: 3대 화면의 공식 정보 및 기능 목적.
- **Brand Source**: `04-기획/브랜드-기획/BRAND-PLAN.md` (DAMORI 존재 이유, 기록 철학, 핵심 가치 3종).
- **Product Source**: `products-200-v6.json` (약 200개 Raw Product Source Pool).
- **디자인 참고자료**: `V4-설계자료/웹디자인-레퍼런스/` (`DESIGN_REFERENCE_ONLY`).

---

## 3. Storyboard 공통 원칙

1. **비판매 포트폴리오 아카이브 원칙**: 결제, 장바구니, 가격, 수량 선택 등 쇼핑몰 상업적 UI 요소를 전면 배제하며, 하이브리드 도구 포트폴리오 탐색에 집중한다.
2. **비실행 경험 가이드 원칙**: 실제 작성/저장/동기화 등 앱 기능을 배제하고, 저부담 회고, 글 보존, 편안한 복귀 등 사용자 기록 경험 안내로 한정한다.
3. **미니멀 GNB 고정**: 전역 상단 내비게이션은 `[LOGO / HOME] | PRODUCTS | BRAND` 3대 앵커만 유지하며, `SEARCH`는 `HOLD_DESIGN_OPPORTUNITY` 상태로 관리한다.
4. **Grayscale 와이어프레임 전환성 원칙**: 브랜드 색상을 확정하지 않고 Dark Gray, Medium Gray, Light Gray, Black, White의 무채색 톤 대조만으로 정보 위계가 구분되도록 설계한다.

---

## 4. 공식 화면 목록

| Canonical ID | Working Alias | 공식 화면명 | Story 역할 및 핵심 방향 | 주 수용 Service Path |
|---|---|---|---|---|
| **0.0** | `PAGE-00` | `HOME / MAIN` | 브랜드 존재 이유 서사 ➔ 기록 경험 발견 ➔ 대표 도구 포트폴리오 쇼케이스 연결 | `PATH A` (Main Narrative), `PATH C` |
| **1.0** | `PAGE-01` | `PRODUCTS / CATEGORY-SUB` | 하이브리드 제품군 비주얼 탐색 ➔ 소재/제본/필기 적합성/치수 대조 ➔ 탐색 기준 안내 | `PATH B` (Product Task), `PATH C` (후속) |
| **2.0** | `PAGE-02` | `BRAND` | DAMORI 존재 이유, 기록 철학, 핵심 가치 및 제품 제작 원칙 에디토리얼 독서 | `PATH A` (서사 심화), `PATH B/C` (Optional) |

---

## 5. 0.0 HOME / MAIN Storyboard

### 5.1 화면 개요
- **화면명**: `0.0 HOME / MAIN (DAMORI Long Scroll Portfolio Landing)`
- **Story Concept**: 브랜드 서사 ➔ 기록 경험 제안 ➔ 제품군 소개 ➔ 대표 포트폴리오 쇼케이스
- **Visual/Text 비중 방향**: Balanced (서사와 시각 비주얼의 조화로운 호흡)
- **Reference Insight**: 서사 중심 스토리텔링과 쇼케이스 사이의 시각적 여백 리듬 참고

### 5.2 섹션별 스토리보드 명세

| 순서 | Section ID | Section 역할 | 핵심 메시지 | 주요 콘텐츠 | Visual 역할 | 사용자 행동 | 연결 | Content Priority | 후속 결정 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | `0.1` | First Impression | 바쁜 일상 속 기록의 쉼표 | DAMORI 브랜드명, 존재 이유 요약, 쉼표 메시지 | Brand Narrative Visual Area | 서사 첫인상 인지 | `0.2` | PRIMARY | `OPEN-01` (Hero Visual 톤) |
| **2** | `0.2` | Brand Core Summary | 편안함, 보존성, 자율성 가치 | 사색의 깊이, 보존성, 자율성 가치 요약 정보 | Core Value Narrative Area | 서사 깊이 읽기 | `0.3` | PRIMARY | 텍스트 배치 및 여백 |
| **3** | `0.3` | Recording Experience | 나에게 맞는 주요 기록 경험 | 저부담 회고, 글 보존, 편안한 복귀 경험 가이드 | Experiential Visual Guide Area | 기록 경험 공감 | `0.4` | SECONDARY | 경험 표현 UI 컴포넌트 |
| **4** | `0.4` | Product Groups Intro | 경험을 돕는 기록 도구들 | 아날로그 & 디지털 하이브리드 결합 소개 | Product Lineup Concept Area | 제품군 관계 파악 | `0.5` / `PRODUCTS` | BRIDGE | 비주얼 표현 방식 |
| **5** | `0.5` | Portfolio Showcase | DAMORI 대표 도구 쇼케이스 | 최소 15개 이상 수용 가능한 대표 Product 영역 | Portfolio Showcase Area | 시각 탐색 & 선택 | `PRODUCTS 1.3` | PRIMARY | 그리드 열 배치 방식 |
| **6** | `0.6` | Navigation & Footer | 전역 내비게이션 & 정보 정돈 | 브랜드 기본 정보, 전역 내비게이션, Copyright | Footer Information Area | 서브 이동/종료 | 전역 앵커 | SUPPORT | 푸터 레이아웃 세부화 |

---

## 6. 1.0 PRODUCTS / CATEGORY-SUB Storyboard

### 6.1 화면 개요
- **화면명**: `1.0 PRODUCTS / CATEGORY-SUB (Product Portfolio & Specification)`
- **Story Concept**: 포트폴리오 제품군 탐색 ➔ 소재/제본/필기 적합성/실측 치수 대조 ➔ 비실행형 탐색 기준 안내
- **Visual/Text 비중 방향**: Visual-led & Information-dense (시각 비주얼과 대조 정보의 균형)
- **Reference Insight**: 소재/제본 및 실측 치수 대조 정보 구획의 직관적 시각 배치 참고

### 6.2 섹션별 스토리보드 명세

| 순서 | Section ID | Section 역할 | 핵심 메시지 | 주요 콘텐츠 | Visual 역할 | 사용자 행동 | 연결 | Content Priority | 후속 결정 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | `1.1` | Visual Hero | 포트폴리오 탐색 뷰 | 카테고리/제품군 시각 아이덴티티 표현 | Category Hero Visual Area | 카테고리 확인 | `1.2` | PRIMARY | 히로 시각 톤 |
| **2** | `1.2` | Product Group Exploration | 약 200개 인벤토리 유연 탐색 | 유연한 제품군 탐색 정보 갤러리 | Group Exploration Gallery Area | 제품군 둘러보기 | `1.3` | SECONDARY | 갤러리 배치 방식 |
| **3** | `1.3` | Product Feature & Spec | 소재, 제본, 필기 적합성, 실측 치수 대조 | 소재, 평면 펼침, 필기 적합성 정보, 실측 치수 대조 정보 및 사용 맥락 | Spec & Material Detail Area | 스펙/치수 대조 | `1.4` / `BRAND 2.6` | PRIMARY | `RESOLVED_AT_WIREFRAME` (Material + Specification Balanced) |
| **4** | `1.4` | User-led Exploration | 내 기준 탐색 참고 | 가입·진단 없이 참고하는 탐색 기준과 관련 정보 범위 | User-led Exploration Area | 탐색 기준 확인 | `BRAND 2.6` | SUPPORT | `NON_EXECUTABLE_INFORMATION_STRUCTURE` |

---

## 7. 2.0 BRAND Storyboard

### 7.1 화면 개요
- **화면명**: `2.0 BRAND (Brand Philosophy & Storytelling)`
- **Story Concept**: 브랜드 시작 ➔ 존재 이유 ➔ "기록은 쉼표" 철학 ➔ 상위 가치 ➔ 제품 제작 원칙
- **Visual/Text 비중 방향**: Text-led Editorial (에디토리얼 스토리텔링 및 수필 독서 감성)
- **Reference Insight**: 에디토리얼 브랜드 수필 스토리텔링 및 인용구 강조 구조 참고

### 7.2 섹션별 스토리보드 명세

| 순서 | Section ID | Section 역할 | 핵심 메시지 | 주요 콘텐츠 | Visual 역할 | 사용자 행동 | 연결 | Content Priority | 후속 결정 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | `2.1` | DAMORI Introduction | 브랜드의 시작과 미션 | DAMORI 브랜드명 의미 및 비전 서사 | Essay Cover Visual Area | 서사 입문 | `2.2` | PRIMARY | 대형 헤딩 타이포 |
| **2** | `2.2` | Brand Existence & Purpose | 왜 쉼표가 필요한가 | 일상 속 기록의 쉼표 메시지 서사 | Purpose Story Display Area | 존재 이유 독서 | `2.3` | PRIMARY | 인용구 배치 |
| **3** | `2.3` | Recording Philosophy | 기록은 의무가 아닌 쉼표 | 스트릭 죄책감 차단 미안함 없는 철학 서사 | Philosophy Essay Area | 기록 철학 공감 | `2.4` | PRIMARY | 텍스트 단락 여백 |
| **4** | `2.4` | Core Values & User Value | 당신에게 전달되는 가치 | Zero Strain, Data Integrity, Autonomy | Core Value Display Area | 가치 체계 파악 | `2.5` | SECONDARY | 가치 시각화 방식 |
| **5** | `2.5` | Analog & Digital Principle | 손의 감성과 디지털의 편의 | 아날로그 물성과 디지털 보완 관계 서사 | Hybrid Balance Visual Area | 결합 관점 공감 | `2.6` | SECONDARY | 이미지-텍스트 교차 |
| **6** | `2.6` | Product Principle | DAMORI 제품 제작 원칙 | 도구를 과시하지 않는 담백한 제품 기준 정보 | Product Principle Info Area | 제품 원칙 확인 | `PRODUCTS` | BRIDGE | 원칙 정보 구획 스타일 |

---

## 8. Page 간 Story 연결

- **`HOME ➔ PRODUCTS`**: `HOME 0.4` (Product Groups Intro) 및 `0.5` (Portfolio Showcase)에서 제품/제품군 탐색 선택 시 `PRODUCTS 1.2/1.3`으로 연결.
- **`HOME ➔ BRAND`**: `HOME 0.2` (Brand Core Summary)에서 미션 서사를 깊이 독서하기 위해 `BRAND 2.1`로 연결.
- **`PRODUCTS ➔ BRAND`**: `PRODUCTS 1.3` (Feature & Spec)에서 스펙 확인 후 DAMORI 제작 기준이 궁금해질 때 `BRAND 2.6` (Product Principle)으로 연결.
- **`BRAND ➔ PRODUCTS`**: `BRAND 2.6`에서 제품 원칙 확인 후 관련 도구 포트폴리오를 둘러보기 위해 `PRODUCTS 1.0`으로 연결.

---

## 9. Client Coverage (7/7 수용)

| Client ID | Client 성명 | 핵심 Site-level Need | Storyboard 수용 Section | Coverage Type | Coverage 판정 |
|---|---|---|---|:---:|:---:|
| **V4-C01** | 은재 | 제본/지질 사양 대조 & 제품 원칙 | `PRODUCTS 1.3`, `BRAND 2.6` | `DIRECT` | **COVERED** |
| **V4-C02** | 지안 | 세로 타임라인 서식 특성 파악 | `PRODUCTS 1.2`, `1.3` | `INFORMATIONAL` | **COVERED** |
| **V4-C03** | 하람 | 짧고 부담 없는 회고 방식 이해 | `HOME 0.3`, `PRODUCTS 1.2` | `EXPERIENCE_PREVIEW` | **COVERED** |
| **V4-C04** | 소담 | 글 보존 서식 구조 정보 파악 | `PRODUCTS 1.3`, `HOME 0.3` | `INFORMATIONAL` | **COVERED** |
| **V4-C05** | 태오 | 오프라인·로컬 소장 원본 서비스 요구 | 현재 Page 직접 수용 없음 | `OUT_OF_CURRENT_SCOPE_REFERENCE` | **TRACEABLE** |
| **V4-C06** | 이준 | 죄책감 차단 미안함 없는 복귀 철학 | `HOME 0.3`, `BRAND 2.3` | `EXPERIENCE_PREVIEW` | **COVERED** |
| **V4-C07** | 다온 | 사용자 기준 자율 좁히기 & 치수 대조 | `PRODUCTS 1.4`, `1.3` | `DIRECT` | **COVERED** |

---

## 10. DN / RG Traceability (10 Pure DNs & 8 RGs)

| Pure DN ID | 관련 RG ID | 대표 Client | 수용 화면 및 섹션 | Service Flow 반영 형태 | Traceability 판정 |
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

- **`PATH A`**: `HOME 0.1 ➔ 0.5` 메인 서사 랜딩 콘텐츠 순서에 대응됨.
- **`PATH B`**: `PRODUCTS 1.1 ➔ 1.3 (1.4)` 태스크/스펙 대조 콘텐츠 순서에 대응됨.
- **`PATH C`**: `HOME 0.3 ➔ 0.4 ➔ PRODUCTS 1.2 ➔ 1.3` 경험 발견 콘텐츠 순서에 대응됨.

---

## 12. Screen Specification 정합성

- Screen Spec V1의 3대 화면 9개 필수 양식 대응을 확인했으며, 정보 역할(WHAT)을 시각적 콘텐츠 순서(HOW)로 확장함.

---

## 13. Responsive 전달사항

- **Desktop**: 에디토리얼 다열 텍스트-이미지 믹스 및 스펙 정보 영역 표현.
- **Mobile**: 1컬럼 수직 Reading Order 배치 및 스펙 대조 정보 가독성 보장. (정확한 Column 수 및 Breakpoint는 Wireframe 단계로 이관).

---

## 14. Accessibility 전달사항

- H1~H3 헤딩 위계 준수, 스크린 리더용 레이아웃 순서 유지, 키보드 Tab Focus Ring 설계 적용.
- 색상 미확정에 따라 명도 대비는 후속 Style Guide 단계에서 실측 검증 후 확정함.

---

## 15. Design Reference 활용 (`DESIGN_REFERENCE_ONLY`)

- **`HOME`**: 에디토리얼 글 호흡과 쇼케이스 사이의 시각적 여백 리듬 반영.
- **`PRODUCTS`**: 스펙 정보 및 대조 구획의 깔끔한 시각 정보 위계 반영.
- **`BRAND`**: 인용구 중심 에세이 및 명료한 원칙 정보 구획 반영.

---

## 16. Design Candidate / Open Visual Decision

| Candidate / Decision ID | 대상 Section | 디자인 아이디어 및 비교 내용 | 상태 | 후속 결정 단계 |
|---|---|---|:---:|---|
| **`OPEN-01`** | `HOME 0.1` | Editorial Brand Narrative Visual vs Product Object Visual 우선순위 | `RESOLVED_AT_WIREFRAME` (Balanced Direction) | Wireframe V3 반영 |
| **`OPEN-02`** | `PRODUCTS 1.3` | Material Detail 강조 vs Specification Data 강조 vs Balanced 균형 | `RESOLVED_AT_WIREFRAME` (Material + Specification Balanced) | Wireframe V3 반영 |
| **`CANDIDATE-01`** | `PRODUCTS 1.3` | 소재/제본/치수 1:1 대조 비교표 시각 구획 방식 | `DESIGN_CANDIDATE` | Wireframe / Visual 단계 |
| **`CANDIDATE-02`** | `PRODUCTS 1.4` | 사용자 기준 탐색 정보 구조 | `NON_EXECUTABLE_INFORMATION_STRUCTURE` | Wireframe V3 반영 |
| **`CANDIDATE-03`** | 전역 | 섹션 간 페이드/슬라이드 시각적 전환 연출 아이디어 | `DESIGN_CANDIDATE` | Visual / Style Guide 단계 |

---

## 17. Wireframe 전달사항 (Grayscale Constraint)

- **와이어프레임 무채색 제약**: 후속 와이어프레임은 **WHITE, GRAY, BLACK Grayscale만 사용**하며, 브랜드 색상에 의존하지 않고 정보의 크기, 위치, 여백, 대비, 그룹핑만으로 정보 위계가 표현되도록 설계함.
  - Primary Visual ➔ Dark Gray Area
  - Secondary Content ➔ Medium Gray Area
  - Card/Table Container ➔ Light Gray Area
  - Text ➔ Black Text / Background ➔ White

---

## 18. 범위 밖 요소 (Out of Scope)

- **쇼핑몰 커머스 UI**: 가격, 장바구니, 구매하기, 결제, 수량, 할인 CTA (전면 배제).
- **웹앱 실행 기능**: 실제 글 작성/저장, 동기화, 캘린더 조작, 오프라인 파일 추출 실행, 계정 로그인 (전면 배제).

---

## 19. 확정 / 미확정 / 후속 결정

| 구분 | **Confirmed (확정 사항)** | **Unconfirmed / Next Stage (미확정/후속 이관)** |
|---|---|---|
| **0.0 HOME** | 0.1~0.6 섹션 역할, 포트폴리오 랜딩 성격, 대표 제품 최소 15개 수용 구조, `OPEN-01` Balanced Direction | exact px, 애니메이션 시간 ➔ 후속 단계 이관 |
| **1.0 PRODUCTS**| 1.1~1.4 섹션 역할, 스펙/치수 대조 및 비실행형 탐색 기준 안내, `OPEN-02` Balanced | Category 수/이름, 대표 15개 선정 ➔ 후속 Content 결정 |
| **2.0 BRAND** | 2.1~2.6 서사 섹션 구성, 존재 이유 및 기록 철학 전달 목적 | 최종 브랜드 Copywriting, 이미지 수량, 브랜드 공식 색상 ➔ Style Guide 이관 |

---

## 20. 검토 결과

- **파일 생성 검증**: `V4-설계자료/05-v4-storyboard-v1.md` 현재 작업용 Master 문서 유지.
- **Traceability 검증**: 7/7 Client, 10/10 Pure DN, 8/8 RG 매핑 확인.
- **과설계 배제 검증**: exact Gray HEX 0건, exact Column 수 0건, 1:1 표/컴포넌트 강제 0건 준수.
- **현재 문서 상태**: **`CURRENT_WORKING_MASTER_BASELINE`**
