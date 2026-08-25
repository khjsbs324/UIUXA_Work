# 01. V4 대표 가상 클라이언트 명세 V2

- **단계**: `05-설계 (V4 파이프라인 Client Baseline V2)`
- **버전**: `V2`
- **공식 브랜드명**: `DAMORI / 다모리`
- **상태**: `APPROVED_CLIENT_BASELINE_V2` (사용자 승인 공식 기준본)
- **저장 위치**: `V4-설계자료/01-v4-client-baseline-v2.md`

---

## 1. Baseline 개요

본 문서는 기존 51명 Source Client Master(`clients-51-v6.json`)를 바탕으로 검증된 Pure User Need와 Requirement Pattern을 추출하고, 이를 7인의 대표 가상 클라이언트(`V4-C01` ~ `V4-C07`) 세트로 체계화한 V4 공식 클라이언트 기준본 V2 명세서이다.

## 2. V1 ➔ V2 주요 정정사항

1. **Source Role 4종 완전 분리**: `PRIMARY_PERSONA_SOURCE` (20명), `SECONDARY_PERSONA_SOURCE` (2명), `PRODUCT_COMPARISON_POOL_SOURCE` (38명), `INSUFFICIENT_EVIDENCE` (0명)로 역할을 계층화함.
2. **C07 다온 인원수 논리 모순 정정**: C07의 진성 Primary Persona Source는 `VC-08`, `VC-09` (2명)이며, 31명 인벤토리 대조 소스는 `PRODUCT_COMPARISON_POOL_SOURCE`로 분리하여 C07 Persona 인원수에 포함하지 않음.
3. **Site Scope Translation 수립**: 원래 서비스 요구(`originalServiceNeed`)와 현재 DAMORI 포트폴리오 웹사이트 요구(`siteLevelNeed`)를 구분하고 5대 `siteCoverageType`(`DIRECT`, `INFORMATIONAL`, `EXPERIENCE_PREVIEW`, `OUT_OF_CURRENT_SCOPE`, `HOLD`)을 부여함.
4. **Legacy Metadata & 단정어 정제**: Project Constraint의 과거 '제본 철학' 구문을 완벽히 제거하고 Product Requirement로 격하함. 근거 없는 절대 수치 26건에 `sourceValueStatus` 속성을 부여함.

## 3. Source Role 정의

- **`PRIMARY_PERSONA_SOURCE`**: Source Client의 본질적 Pure Need가 특정 V4 대표 Client를 직접 구성하는 핵심 근거 (VC당 최대 1개).
- **`SECONDARY_PERSONA_SOURCE`**: Source Client가 독립적인 두 번째 Pure Need를 실제로 가져 다른 대표 Client에도 정당하게 매핑되는 경우.
- **`PRODUCT_COMPARISON_POOL_SOURCE`**: 제품/인벤토리/실측 대조 설계의 참고 소스로 쓰인 경우 (Persona 인원수에 합산 금지).
- **`INSUFFICIENT_EVIDENCE`**: 현 Source Master만으로 매핑 근거가 불충분한 경우.

## 4. V4 대표 Client 7인 세부 명세

### V4-C01 은재 (장문 사색 & 필기 물성 중시 클라이언트)

- **상황 (Context)**: 카페 및 서재에서 1시간 이상 몰입하여 장문 필기와 아이디어 구상을 진행하며 손목 피로와 잉크 번짐에 민감함.
- **목표 (Goal)**: 손목 부담 없이 평평하게 펼쳐지는 제본과 만년필 잉크 번짐이 적은 고품질 아날로그 기록 도구를 탐색하고 비교함.
- **Original Service Need (원본 서비스 요구)**: 손목 통증 없는 180도 평면 펼침 Smyth Sewn 실제본 및 EF/F 만년필 잉크 번짐 0% 지질 노트 원함.
- **Normalized Pure Need (정제된 본질 요구)**: 장시간 필기 시 손목에 부담이 적고 글씨가 번지지 않는 고품질 아날로그 기록 경험
- **Site-level Need (웹사이트 수용 요구)**: DAMORI가 제공하는 제품의 제본 특성(평면 펼침), 종이 사양(잉크 번짐 저감), 브랜드의 제품 원칙을 탐색하고 실측 스펙을 대조함.
- **Site Coverage Type**: `DIRECT`
- **Site Relevant Pages**: PRODUCTS (주 수용), BRAND (보조적 제품 원칙 이해)
- **Scope Note**: 웹사이트에서 제본/지질 사양 정보와 실측 치수를 직접 대조할 수 있어 DIRECT 수용 가능. 구체 Smyth Sewn, 120gsm은 Product Requirement로 관리.
- **Primary Persona Sources**: VC-01, VC-06, VC-17, VC-29 (총 4명)
- **Secondary Persona Sources**: 없음
- **Product Pool Sources**: 1개 소스 연계
- **Product Requirements**: 180도 평면 펼침 제본 사양 검토, EF/F 잉크 번짐 저감 지질 검토, 두께 및 치수 실측 정보
- **Design Opportunities**: 제품 스펙 및 치수 1:1 대조 비교표 UI 후보
- **Global Rules**: ACCESSIBILITY_RULE, RESPONSIVE_RULE

### V4-C02 지안 (수치적 시간축 통제 & 타임라인 클라이언트)

- **상황 (Context)**: 직장 및 프리랜서 업무 중 바쁜 일정 겹침과 계획 수립에 대한 스트레스를 직관적 타임라인으로 통제하길 원함.
- **목표 (Goal)**: 하루의 시간을 24시간 세로 축으로 직관적으로 파악하고 계획과 실적을 명확히 대조하는 기록 서식과 제품을 탐색함.
- **Original Service Need (원본 서비스 요구)**: 24시간 세로 타임라인에서 일정 겹침을 실시간 파악하고 직접 조절하는 앱 기능 원함.
- **Normalized Pure Need (정제된 본질 요구)**: 복잡한 일정을 직관적으로 시각화하고 시간을 유연하게 통제하는 경험
- **Site-level Need (웹사이트 수용 요구)**: DAMORI의 디지털/아날로그 플래너 및 세로 타임라인 서식의 지원 특성과 시간 관리 방식을 파악함.
- **Site Coverage Type**: `INFORMATIONAL`
- **Site Relevant Pages**: PRODUCTS (1.2 서식 탐색)
- **Scope Note**: 실제 일정 조절 앱 기능이 아닌, 관련 플래너 서식 및 디지털 템플릿의 지원 특성과 사용 방식을 확인하는 정보 수용.
- **Primary Persona Sources**: VC-02, VC-05, VC-16 (총 3명)
- **Secondary Persona Sources**: 없음
- **Product Pool Sources**: 1개 소스 연계
- **Product Requirements**: 24시간 세로 타임라인 레이아웃 검토, 일정-실적 대조 구획 서식 검토
- **Design Opportunities**: 시간축 플래너 템플릿 구조 시각화 UI 후보
- **Global Rules**: ACCESSIBILITY_RULE, RESPONSIVE_RULE

### V4-C03 하람 (저부담 시각 회고 & 1줄 스냅 클라이언트)

- **상황 (Context)**: 피곤한 퇴근 후 길고 거창한 일기를 쓸 엄두가 나지 않아 부담 없이 10초 만에 하루를 기록하길 원함.
- **목표 (Goal)**: 사진 1장이나 감정 스티커, 짧은 1줄 글만으로도 부담 없이 하루를 돌아보고 회고하는 기록 방식을 발견함.
- **Original Service Need (원본 서비스 요구)**: 10초 만에 폼 작성 없이 사진 1장과 1줄 텍스트로 회고를 완료하고 저장하는 서비스 원함.
- **Normalized Pure Need (정제된 본질 요구)**: 복잡한 폼이나 압박 없이 짧고 부담 없이 회고하는 경험
- **Site-level Need (웹사이트 수용 요구)**: DAMORI가 지향하는 저부담 회고 경험과 관련 서식/도구 샘플 및 양식 갤러리를 미리 봄.
- **Site Coverage Type**: `EXPERIENCE_PREVIEW`
- **Site Relevant Pages**: HOME (0.3 회고 경험 섹션), PRODUCTS (서식 탐색)
- **Scope Note**: 실제 회고 데이터를 저장하는 기능이 아니라, 부담 없는 회고 방식 및 관련 양식을 시각적으로 설명/미리보기함.
- **Primary Persona Sources**: VC-03, VC-14, VC-32 (총 3명)
- **Secondary Persona Sources**: 없음
- **Product Pool Sources**: 2개 소스 연계
- **Product Requirements**: 1줄 회고 전용 간결 레이아웃 검토, 사진-텍스트 결합 서식 검토
- **Design Opportunities**: 짧은 회고 입력 UI 후보, 무설정 원터치 팝업 폼 UI 후보
- **Global Rules**: ACCESSIBILITY_RULE, RESPONSIVE_RULE

### V4-C04 소담 (글-서식 분리 & 레이어 보존 클라이언트)

- **상황 (Context)**: 다이어리 꾸미기와 스티커 사용을 즐기지만, 배경 서식이나 스티커 때문에 본문 글이 훼손되거나 가려지는 것을 싫어함.
- **목표 (Goal)**: 내가 적은 소중한 글 원본과 꾸미기 레이어가 분리되어 언제든 깨끗하게 글만 보존되는 제품 구조를 확인함.
- **Original Service Need (원본 서비스 요구)**: 글 데이터(Structure)와 배경 서식/스티커(Asset)를 100% 독립 레이어로 분리 작성하고 추출하는 앱 원함.
- **Normalized Pure Need (정제된 본질 요구)**: 내가 적은 글 원본 데이터가 다른 요소에 의해 훼손되지 않고 보존되는 경험
- **Site-level Need (웹사이트 수용 요구)**: DAMORI 제품 및 템플릿에 적용된 글 원본 보존 원칙과 서식 분리 구조의 특징을 확인함.
- **Site Coverage Type**: `INFORMATIONAL`
- **Site Relevant Pages**: PRODUCTS (1.3 제품 특징), HOME (0.3 경험 섹션)
- **Scope Note**: 실제 레이어 편집 기능을 실행하는 웹앱이 아닌, 글 원본 보존 원칙과 관련 서식의 구조적 특징을 정보로 제공함.
- **Primary Persona Sources**: VC-04, VC-30, VC-50 (총 3명)
- **Secondary Persona Sources**: VC-06
- **Product Pool Sources**: 0개 소스 연계
- **Product Requirements**: 글-서식 분리 프레임 레이아웃 검토, 텍스트 보호 투명도 가이드 검토
- **Design Opportunities**: 글-서식 분리 구조 시각 설명 UI 후보
- **Global Rules**: ACCESSIBILITY_RULE, RESPONSIVE_RULE

### V4-C05 태오 (오프라인 캐시 & 로컬 소장 클라이언트)

- **상황 (Context)**: 인터넷이 불안정한 장소에서도 안심하고 기록하고 싶고, 개인적 기록이 외부 서버에만 남는 것에 보안상 불안감을 느낌.
- **목표 (Goal)**: 네트워크 연결 없이도 기록할 수 있고 내 기록 데이터를 로컬 파일(PDF/CSV)로 안전하게 소장할 수 있는 제품 특성을 확인함.
- **Original Service Need (원본 서비스 요구)**: Offline-First 작성, IndexedDB 로컬 저장 및 PDF/CSV 사본 백업 다운로드 서비스 원함.
- **Normalized Pure Need (정제된 본질 요구)**: 내 기록과 데이터에 대한 완전한 소유권과 오프라인 안전성을 확보하는 경험
- **Site-level Need (웹사이트 수용 요구)**: DAMORI의 로컬 데이터 소장 및 오프라인 우호적 제품/시스템 지원 특성을 정보를 통해 확인함.
- **Site Coverage Type**: `INFORMATIONAL`
- **Site Relevant Pages**: PRODUCTS (지원 사양 안내), HOME (0.6 정보 섹션)
- **Scope Note**: 현재 웹사이트가 실제 오프라인 백업 도구가 아니므로, 로컬 소장 우호적 특성을 정보 및 지원 가이드로 수용.
- **Primary Persona Sources**: VC-18, VC-42 (총 2명)
- **Secondary Persona Sources**: VC-05
- **Product Pool Sources**: 2개 소스 연계
- **Product Requirements**: 표준 PDF/CSV 추출 상환성 검토, 오프라인 백업 안내 가이드 검토
- **Design Opportunities**: 로컬 백업 안내 모듈 UI 후보
- **Global Rules**: ACCESSIBILITY_RULE, RESPONSIVE_RULE

### V4-C06 이준 (미안함 없는 복귀 & 죄책감 차단 클라이언트)

- **상황 (Context)**: 며칠 동안 바빠서 기록을 멈추었을 때, 출석 파기 경고나 미완성 빈자리를 보면 죄책감이 들어 완전히 포기하게 됨.
- **목표 (Goal)**: 한참 동안 쉬었다 돌아와도 미안함이나 압박 없이 언제든 편안하게 다시 기록을 시작할 수 있는 브랜드를 발견함.
- **Original Service Need (원본 서비스 요구)**: 연속 작성 경고를 지우고 마지막 작성 위치로 1-클릭 자동 복귀시켜 주는 앱 서비스 원함.
- **Normalized Pure Need (정제된 본질 요구)**: 기록 중단에 대한 죄책감이나 스트릭 강요 없이 언제든 자유롭게 돌아오는 경험
- **Site-level Need (웹사이트 수용 요구)**: DAMORI의 '기록은 의무가 아닌 쉼표'라는 철학 및 미안함 없는 복귀 가이드를 경험하고 이해함.
- **Site Coverage Type**: `EXPERIENCE_PREVIEW`
- **Site Relevant Pages**: HOME (0.3 기록 경험), BRAND (2.2 기록 철학)
- **Scope Note**: 실제 개인 작성 위치 복귀 포커스 앱이 아니라, 죄책감을 주지 않는 DAMORI의 브랜드 철학과 복귀 경험을 설명/미리보기함.
- **Primary Persona Sources**: VC-07, VC-20, VC-51 (총 3명)
- **Secondary Persona Sources**: 없음
- **Product Pool Sources**: 1개 소스 연계
- **Product Requirements**: 날짜 강요 없는 날짜 자율 서식 검토, 복귀 응원 안내 문구 검토
- **Design Opportunities**: 부담 없는 복귀 표현 UI 후보, 복귀 포커스 가이드 UI 후보
- **Global Rules**: ACCESSIBILITY_RULE, RESPONSIVE_RULE

### V4-C07 다온 (자율 조건 탐색 & 실측 대조 클라이언트)

- **상황 (Context)**: 복잡한 회원가입이나 개인정보 입력, 취향 진단 퀴즈에 피로감을 느끼며 자신만의 명확한 기준으로 제품을 탐색하길 원함.
- **목표 (Goal)**: 가입이나 진단 강요 없이 내 기준(용도, 제본, 종이, 규격)에 따라 제품 후보를 자율적으로 좁히고 사양 차이를 직접 비교함.
- **Original Service Need (원본 서비스 요구)**: 회원가입 없이 4개 칩 필터로 제품을 좁히고 소재/치수 1:1 비교표를 제공하는 기능 원함.
- **Normalized Pure Need (정제된 본질 요구)**: 강요나 진단 없이 스스로의 기준에 따라 제품 정보를 자율 탐색하고 실측 차이를 비교하는 경험
- **Site-level Need (웹사이트 수용 요구)**: DAMORI 제품군을 사용자 자율 기준에 따라 좁혀 탐색하고, 소재 및 실측 치수 대조 정보를 직접 확인함.
- **Site Coverage Type**: `DIRECT`
- **Site Relevant Pages**: PRODUCTS (1.3 스펙 대조 & 1.4 자율 탐색)
- **Scope Note**: 웹사이트 내에서 자율 조건 좁히기 및 실측 치수 대조표를 직접 이용할 수 있어 DIRECT 수용 가능.
- **Primary Persona Sources**: VC-08, VC-09 (총 2명)
- **Secondary Persona Sources**: 없음
- **Product Pool Sources**: 38개 소스 연계
- **Product Requirements**: 실측 치수 대조표 구조 검토, 소재 및 제본 사양 표기 검토
- **Design Opportunities**: 사용자 기준 조건 탐색 UI 후보, 소재 & 치수 1:1 대조 비교표 UI 후보
- **Global Rules**: ACCESSIBILITY_RULE, RESPONSIVE_RULE

## 5. Source VC 51명 Traceability 전수 명세 (51 UNIQUE IDs)

| VC ID | Source Client 성명 | 원본 핵심 Title 요약 | Primary V4 Persona | Secondary V4 Persona | Product Pool Role | 최종 Source Role |
|---|---|---|:---:|:---:|:---:|:---:|
| **VC-01** | 은재 | 아날로그 장문 기록 | V4-C01 (은재) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-02** | 지안 | 미래 일정 흐름 통제 | V4-C02 (지안) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-03** | 하람 | 저부담 시각 회고 | V4-C03 (하람) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-04** | 소담 | 주제별 기록 탐색 | V4-C04 (소담) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-05** | 태오 | 다기기 연속성 검증 | V4-C02 (지안) | V4-C05 (태오) | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-06** | 나린 | 꾸미기 자산 재사용 | V4-C01 (은재) | V4-C04 (소담) | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-07** | 이준 | 중단 후 재시작 | V4-C06 (이준) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-08** | 다온 | 첫 선택 부담 | V4-C07 (다온) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-09** | 윤슬 | 카테고리·제품 비교 | V4-C07 (다온) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-10** | 온유 | 선물 패키지 선택 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-11** | 가람 | 브랜드 신뢰 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-12** | 해솔 | 개인정보·보존 통제 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-13** | 여울 | 접근성 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-14** | 마루 | 탐색 재개 | V4-C03 (하람) | NONE | C07-Product-Pool | `PRIMARY_PERSONA_SOURCE` |
| **VC-15** | 새봄 | 재료·지속가능성 정보 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-16** | 한결 | 반복 설정 피로 | V4-C02 (지안) | NONE | C07-Product-Pool | `PRIMARY_PERSONA_SOURCE` |
| **VC-17** | 채운 | 아날로그 정보 부족 | V4-C01 (은재) | NONE | C07-Product-Pool | `PRIMARY_PERSONA_SOURCE` |
| **VC-18** | 서우 | 디지털 내보내기 판단 | V4-C05 (태오) | NONE | C07-Product-Pool | `PRIMARY_PERSONA_SOURCE` |
| **VC-19** | 초아 | 가족 공동 기록 경계 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-20** | 주원 | 기록 방식 전환 | V4-C06 (이준) | NONE | C07-Product-Pool | `PRIMARY_PERSONA_SOURCE` |
| **VC-21** | 민서 | 예산 미정 탐색 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-22** | 선율 | 기록 공개 부담 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-23** | 도윤 | 복잡한 필터 회피 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-24** | 아라 | 근거 시점 확인 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-25** | 재희 | 선물 실패 회피 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-26** | 지후 | 중단 후 비교 맥락 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-27** | 예린 | 브랜드 주장 검증 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-28** | 수현 | 오래된 기록 재탐색 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-29** | 건우 | 실물 보관 공간 제약 | V4-C01 (은재) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-30** | 서진 | 커스터마이징 후회 방지 | V4-C04 (소담) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-31** | 지민 | 알림 피로 회피 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-32** | 유진 | 빠른 기록의 의미 선택 | V4-C03 (하람) | NONE | C07-Product-Pool | `PRIMARY_PERSONA_SOURCE` |
| **VC-33** | 연우 | 기존 기록 이전 판단 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-34** | 하윤 | 선물 수령자의 접근성 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-35** | 시온 | 생활 변화에 따른 방식 수정 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-36** | 나윤 | 리필·수리 가능성 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-37** | 태윤 | 콘텐츠와 제품 탐색 구분 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-38** | 라온 | 가칭 브랜드 인지 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-39** | 은호 | 포트폴리오 과정 검증 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-40** | 세아 | 긴 랜딩 서사 탐색 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-41** | 유나 | 200개 후보군 전체 방향 감각 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-42** | 현서 | 시각적 Hero와 탐색 균형 | V4-C05 (태오) | NONE | C07-Product-Pool | `PRIMARY_PERSONA_SOURCE` |
| **VC-43** | 다빈 | 비판매 포트폴리오 인지 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-44** | 로운 | 이미지 실패 상황의 제품 판단 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-45** | 해나 | 한국적 정서의 진정성 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-46** | 지율 | 긴 페이지의 스크린리더 탐색 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-47** | 주하 | 모바일 제품 레일 발견 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-48** | 태린 | 대표 15개 선정 이유 확인 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-49** | 윤재 | 브랜드와 제품의 일관성 | NONE | NONE | C07-Product-Pool | `PRODUCT_COMPARISON_POOL_SOURCE` |
| **VC-50** | 아인 | 카테고리 경계 이해 | V4-C04 (소담) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |
| **VC-51** | 이솔 | 저연결성 긴 페이지 복귀 | V4-C06 (이준) | NONE | NONE | `PRIMARY_PERSONA_SOURCE` |

## 6. Persona Source Coverage 및 통계

| V4 Representative Client | Primary Persona | Secondary Persona | Product Pool | Persona Evidence Total |
|---|---:|---:|---:|---:|
| **V4-C01 은재** | 4명 | 0명 | 1명 (VC-17) | **4명** |
| **V4-C02 지안** | 3명 | 0명 | 1명 (VC-16) | **3명** |
| **V4-C03 하람** | 3명 | 0명 | 2명 (VC-14, 32) | **3명** |
| **V4-C04 소담** | 3명 | 1명 (VC-06) | 0명 | **4명** |
| **V4-C05 태오** | 2명 | 1명 (VC-05) | 2명 (VC-18, 42) | **3명** |
| **V4-C06 이준** | 3명 | 0명 | 1명 (VC-20) | **3명** |
| **V4-C07 다온** | 2명 | 0명 | 38명 (Pool 전량) | **2명** |
| **합계 (Total)** | **20명** | **2명** | **38명 (중복 포함)** | **22명** |

- **TOTAL_SOURCE_ID_COUNT**: `51`
- **UNIQUE_SOURCE_ID_COUNT**: `51` (중복 0, 누락 0)
- **PRIMARY_PERSONA_MAPPED_COUNT**: `20`
- **PRIMARY_PERSONA_UNMAPPED_COUNT**: `31` (Product Pool로 100% 추적)
- **LEGITIMATE_MULTI_NEED_CLIENT_COUNT**: `2` (`VC-05`, `VC-06`)
- **TRACEABILITY_RATE**: `100% Traceable`

## 7. 프로젝트 Constraint (V2 기준)

- **최종 경험 목표**: 브랜드를 소개하면서 제품군까지 설득력 있게 보여주는 포트폴리오형 랜딩 경험
- **3대 대표 Page Anchor**: `0.0 HOME / MAIN`, `1.0 PRODUCTS / CATEGORY-SUB`, `2.0 BRAND`
- **Brand Core 범위**: DAMORI 브랜드 소개, 존재 이유, 기록 철학, 핵심 가치 3종(Zero Strain, Data Integrity, Autonomy), 아날로그/디지털 결합 관점, 제품 원칙
- **Product Requirement 범위**: Smyth Sewn 실제본, 120gsm 지질, 180도 평면 펼침 등 구체 기술 사양 검토 조건