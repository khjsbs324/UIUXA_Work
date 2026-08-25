# 05. DAMORI V4 스토리보드 후보 C (User Need & Recording Experience)

- **단계**: `05-설계 (V4 파이프라인 Storyboard Candidate C)`
- **버전**: `V1`
- **공식 브랜드명**: `DAMORI / 다모리`
- **후보 컨셉**: `User Need & Recording Experience (기록 습관 및 경험 발견 중심)`
- **저장 위치**: `V4-설계자료/05-v4-storyboard-candidate-c.md`

---

## 1. Candidate Concept

후보 C는 "나는 어떤 방식으로 기록하고 싶은가?"라는 사용자의 일상적 고민과 기록 습관에 먼저 공감하고, 저부담 회고, 글 원본 보존, 미안함 없는 복귀 경험을 제안한 뒤 관련 도구로 안내하는 스토리보드 세트이다. 사용자 중심의 경험 발견 경로를 제공한다. (단, 실제 글 작성/저장 등 Web App 기능은 배제됨).

---

## 2. 공식 기준

- **기반 Baseline**: `Client Baseline V3`, `Site Map Baseline V3`, `Service Flow Baseline V1`, `Screen Spec Baseline V1`
- **공식 3대 Page**: `0.0 HOME / MAIN`, `1.0 PRODUCTS / CATEGORY-SUB`, `2.0 BRAND`
- **Design Reference**: `DESIGN_REFERENCE_ONLY` (사용자 경험 중심 컨텐츠 위계, 카드 뉴스형 서사 가이드 참고)

---

## 3. HOME Storyboard C (Recording Experience-Centric Main)

### 3.1 HOME C 요약
- **화면명**: `0.0 HOME / MAIN (Recording Experience Baseline C)`
- **Concept**: 쉼표 첫인상 ➔ 기록 경험 제안 비중 강화 ➔ 관련 도구 연결 ➔ 쇼케이스
- **Visual/Text 비중**: Visual 60% / Text 40%
- **Reference Insight**: 사용자의 생활 습관과 고민에 맞춘 회고/보존/복귀 경험 시각화

### 3.2 HOME C 섹션 스토리보드

| 순서 | Section ID | Section 역할 | 핵심 메시지 | 주요 콘텐츠 | Visual 역할 | 사용자 행동 | 연결 | Reference Insight | 비고 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | `0.1` | First Impression | 당신의 기록은 어떤 모습인가요 | 브랜드명, 쉼표 미션, 기록 고민 던지기 | Experiential Hero Visual | 기록 고민 공감 | `0.2` | 공감형 질의 히로 | PRIMARY |
| **2** | `0.2` | Brand Core Summary | 의무를 벗어난 기록의 가치 | 편안함, 보존성, 자율성 가치 소개 | Value Summary Card Block | 가치 이해 | `0.3` | 카드형 가치 전달 | SECONDARY |
| **3** | `0.3` | Recording Experience | 나에게 맞는 3대 기록 경험 | 저부담 회고, 글 보존, 편안한 복귀 경험 | 3-Experience Interactive Block | 경험 선택 | `0.4` | 3대 경험 선택 시각화 | PRIMARY |
| **4** | `0.4` | Product Groups Intro | 경험을 돕는 기록 도구들 | 선택한 경험과 제품군의 결합 안내 | Hybrid Tools Concept Visual | 제품군 연결 | `0.5` | 도구 연결 가이드 | BRIDGE |
| **5** | `0.5` | Portfolio Showcase | 기록 도구 쇼케이스 (15+) | 최소 15개 이상 수용 가능한 대표 Product 영역 | Showcase Portfolio Grid | 시각 탐색 | `PRODUCTS` | 쇼케이스 갤러리 | SECONDARY |
| **6** | `0.6` | Navigation & Footer | 전역 정보 및 안내 | 푸터 정보, 전역 링크, Copyright | Footer Information Block | 서브 이동 | 전역 | 푸터 정돈 | SUPPORT |

---

## 4. PRODUCTS Storyboard C (Usage Context-Centric Category)

### 4.1 PRODUCTS C 요약
- **화면명**: `1.0 PRODUCTS / CATEGORY-SUB (Usage Context Baseline C)`
- **Concept**: 제품 종류 자체보다 사용 목적과 맥락(장시간 사색, 시간축, 회고, 보존 등)에 맞는 도구 안내
- **Visual/Text 비중**: Visual 50% / Text 50%
- **Reference Insight**: 사용 맥락별 서식 및 템플릿 정보의 카드형 안내

### 4.2 PRODUCTS C 섹션 스토리보드

| 순서 | Section ID | Section 역할 | 핵심 메시지 | 주요 콘텐츠 | Visual 역할 | 사용자 행동 | 연결 | Reference Insight | 비고 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | `1.1` | Visual Hero | 기록 목적별 도구 안내 | 카테고리/경험 중심 비주얼 표현 | Usage Context Hero Visual | 목적 확인 | `1.2` | 목적 안내 히로 | PRIMARY |
| **2** | `1.2` | Product Group Exploration | 사용 목적과 맞물린 제품군 | 유연한 제품군 탐색 및 서식 안내 | Context-based Group Gallery | 서식/제품 탐색 | `1.3` | 사용 맥락 갤러리 | PRIMARY |
| **3** | `1.3` | Product Feature & Spec | 기록을 돕는 소재와 사양 | 소재, 평면 펼침, 번짐 저감, 치수 대조표 | Spec & Feature Info Block | 스펙/치수 대조 | `1.4` | 스펙 안내 블록 | SECONDARY |
| **4** | `1.4` | User-led Exploration | 내 경험에 맞는 기준 자율 좁히기 | 가입 없는 자율 조건 탐색 정보 | User Need Criteria Block | 조건 좁히기 | `BRAND 2.3` | 자율 조건 좁히기 구획 | SUPPORT |

---

## 5. BRAND Storyboard C (User Value & Philosophy Brand)

### 5.1 BRAND C 요약
- **화면명**: `2.0 BRAND (Philosophy Baseline C)`
- **Concept**: DAMORI의 브랜드 철학이 사용자의 실제 마음과 일상에 전달하는 평안과 가치 강조
- **Visual/Text 비중**: Visual 50% / Text 50%
- **Reference Insight**: 인용문과 일상 시각 이미지를 결합한 공감형 에세이 구조

### 5.2 BRAND C 섹션 스토리보드

| 순서 | Section ID | Section 역할 | 핵심 메시지 | 주요 콘텐츠 | Visual 역할 | 사용자 행동 | 연결 | Reference Insight | 비고 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | `2.1` | DAMORI Introduction | 쉼표를 전하는 브랜드 | DAMORI 명칭의 의미와 비전 서사 | Emotional Intro Visual | 브랜드 접하기 | `2.2` | 감성 소개 비주얼 | PRIMARY |
| **2** | `2.2` | Brand Existence & Purpose | 왜 쉼표가 필요한가 | 현대인의 일상과 DAMORI 존재 이유 | Purpose Story Graphic | 미션 읽기 | `2.3` | 스토리 그래픽 | PRIMARY |
| **3** | `2.3` | Recording Philosophy | 기록은 의무가 아닌 쉼표 | 스트릭 파기 죄책감 차단 철학 메시지 | Quote & Essay Image Block | 철학 깊이 공감 | `2.4` | 인용구 강조 에세이 | PRIMARY |
| **4** | `2.4` | Core Values & User Value | 당신에게 전달되는 가치 | Zero Strain, Integrity, Autonomy 이점 | User Value Diagram | 가치 체계 이해 | `2.5` | 사용자 이점 다이어그램 | SECONDARY |
| **5** | `2.5` | Analog & Digital Principle | 손의 감성과 디지털의 편의 | 아날로그 물성과 디지털 보완 관계 | Hybrid Balance Visual | 결합 관점 공감 | `2.6` | 밸런스 디스플레이 | SECONDARY |
| **6** | `2.6` | Product Principle | 검증된 도구의 표준 | 도구를 과시하지 않는 제품 제작 원칙 | Product Principle Display | 원칙 확인 | `PRODUCTS` | 제품 원칙 디스플레이 | BRIDGE |

---

## 6. Client / DN / RG Coverage

- **주 수용 Client**: `V4-C03 (하람 - 회고)`, `V4-C06 (이준 - 복귀)`, `V4-C02 (지안 - 시간축)`, `V4-C04 (소담 - 글 보존)`
- **커버 DN / RG**: `DN-02, 03, 04, 06, 12, 13` / `RG-02, 03, 04, 06` (사용자 경험 및 맥락 밀착형)

---

## 7. Service Flow 연결

- `PATH C` (Need-based Discovery)를 가장 자연스럽게 지원하며, `HOME 0.3 ➔ 0.4 ➔ PRODUCTS 1.2` 경험 발견 및 도구 연결 흐름이 매끄럽게 성립함.

---

## 8. Reference Insight

- `웹디자인-레퍼런스` 내 스토리 카드 뉴스 및 사용자 인터뷰 에세이 형식을 참고하여, 사용자 생활 습관 중심의 친근한 브랜딩 가이드를 구축함.

---

## 9. Responsive / Accessibility

- **Responsive**: Desktop(3컬럼 경험 카드 및 믹스 뷰) ➔ Mobile(1컬럼 카드 아코디언 배치) 전환.
- **Accessibility**: 텍스트 단락 명도 대비 검증 대상, 스크린 리더용 가이드 구조 제공.

---

## 10. Wireframe Translation Note (Grayscale Constraint)

- **Primary Visual**: Medium Gray (`#555555`) 경험 가이드 시각 블록.
- **Experience Cards**: Light Gray (`#F0F0F0`) 배경 구획 카드.
- **Text & Heading**: Black (`#111111`) / Background: White (`#FFFFFF`).

---

## 11. 장점

- 사용자의 일상 고민과 기록 습관에 가장 깊은 공감대를 형성함 (`C03, C06` 만족도 최상).

---

## 12. 약점

- 제품 실측 치수 및 소재 대조만을 신속히 수행하려는 목적형 사용자(`C01, C07`)에게는 1단계 경험 선택 탐색이 필요함.

---

## 13. 검토사항

- 후속 5-B 통합 단계에서 후보 B의 소재/제본 실측 치수 대조표 및 자율 탐색 뷰를 보조 결합할 필요가 있음.
