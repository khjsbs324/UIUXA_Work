---
name: site-structure-designer
description: 승인된 Client 요구와 MENU·CONTENT·FUNCTION 분석을 근거로 정보 그룹, Page, 내비게이션 계층을 설계하고 서로 다른 사이트-구조맵과 사이트맵을 제작한다. 사이트 구조, IA, 페이지 계층, GNB/LNB, sitemap 설계 요청에 사용하며 서비스-흐름도·화면-설계서·와이어프레임은 만들지 않는다.
---

# Site Structure Designer

## 목적과 범위

승인된 분석 결과를 `Client → REQ → MENU/CONTENT/FUNCTION → PAGE → AREA → SITEMAP`으로 변환한다. 사이트-구조맵은 관계 중심, 사이트맵은 페이지 계층 중심으로 분리한다.

## 필수 입력

- 승인 상태와 사용자 실행 승인
- 핵심 Client, 목표, 문제, 요구 및 중요도
- MENU, CONTENT, FUNCTION 결과와 상호 Mapping
- 브랜드 적합성, 충돌, HOLD, 제외 항목
- 이전 단계 추적성 및 구조 설계 입력 파일

입력이 없거나 승인되지 않은 항목은 임의로 확정하지 않는다. HOLD와 후보는 승인 항목과 분리한다.

## 실행 절차

1. 입력의 승인 상태, ID, 수량과 누락을 검증한다.
2. 요구를 사실·개념·절차·과정 정보 단위로 나눈다.
3. 같은 사용자 목적의 정보를 그룹화하고 중복을 통합한다.
4. 독립 목적·정보 묶음·기능·진입점이 있는 경우에만 Page 후보를 만든다.
5. 각 Page에 ID, 목적, Client, REQ, CONTENT, FUNCTION, 상태와 근거를 부여한다.
6. Page를 AREA로 묶고 Parent/Child/Sibling, Depth와 Cross Link를 설정한다.
7. 레이블의 예측 가능성·일관성·중복·추상성을 검토한다.
8. GNB, LNB, Utility, Breadcrumb, Search, Footer, Cross Link는 근거가 있는 항목만 채택한다.
9. 구조맵과 사이트맵을 별도 파일로 작성하고 모든 Mapping과 추적성을 검산한다.
10. 핵심 Client 요구의 반영 상태와 미반영·충돌·경고를 기록한다.

## Page 판단

- 생성: 독립 사용자 목적, 독립 정보 묶음, 핵심 기능, 별도 진입점 또는 명확히 다른 이용 상황이 있다.
- 통합: 목적·정보·행동이 같고 분리하면 탐색 단계만 늘어난다.
- 분리: 목표·기능·콘텐츠 성격·이용 상황이 다르거나 한 Page의 정보량이 과도하다.
- 상태: `CORE_PAGE`, `REQUIRED_PAGE`, `SUPPORT_PAGE`, `UTILITY_PAGE`, `CONDITIONAL_PAGE`, `HOLD_PAGE`, `REJECTED_PAGE`만 사용한다.

## 계층과 내비게이션 검증

- 한 단계 메뉴 폭 5~9개, 최대 5 Depth를 권장 기준으로 검토하되 수치에 맞추기 위한 항목 생성·강제 통합은 하지 않는다.
- 핵심 요구가 과도하게 깊으면 재검토하고 5 Depth 초과는 `DEPTH_WARNING`으로 기록한다.
- 고립 Page는 `ORPHAN_PAGE`, 다음 이동이 없는 구조는 `DEAD_END_WARNING`으로 기록한다.
- GNB와 Utility를 구분하고, 핵심 Client가 예상 가능한 이름을 우선한다.

## 출력 계약

- `06-사이트-구조맵.md`: AREA→PAGE→CONTENT→FUNCTION 및 Client·REQ·Page 관계
- `06-사이트맵.md`: HOME→Depth별 Page 트리와 전체 Page 표
- `06-PAGE-CONTENT-FUNCTION-MAPPING.md`
- `06-CLIENT-PAGE-MAPPING.md`
- `06-STRUCTURE-DECISIONS.md`
- `06-UNMAPPED-ITEMS.md`
- `06-TRACEABILITY.md`
- `06-SERVICE-FLOW-INPUT.md`: 후속 입력만 작성하며 흐름도 자체는 만들지 않음

## 금지

- 근거 없는 Page·로그인·검색·마이페이지 자동 추가
- HOLD·REJECTED 항목 자동 채택
- 레퍼런스 사이트 구조 복제
- 상세 User Flow, 서비스-흐름도, 화면-설계서, UI 배치, 와이어프레임, Figma 작업
- 승인 전 확정본 선언 또는 후속 단계 자동 실행
