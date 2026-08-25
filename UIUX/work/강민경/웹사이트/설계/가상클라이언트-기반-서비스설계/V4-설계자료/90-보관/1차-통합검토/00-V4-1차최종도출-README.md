# DAMORI V4 1차 최종 도출 검토본

- 상태: `V4_FIRST_INTEGRATED_REVIEW_DRAFT`
- 프로젝트 브랜드명: `DAMORI / 다모리` (working name)
- 범위: `HOME / PRODUCTS / BRAND`, 3 Pages, 16 Sections
- 목적: 기존 V1~V4의 유효 근거를 현재 V4 범위로 연결하여 사용자가 전체 설계를 한 번에 검토할 수 있게 한다.

## 전체 작업 흐름

가상 클라이언트 → 사이트 분석 → 사이트맵 → 사이트 구조맵 → 사이트 흐름도 → 서비스 흐름도 → 화면설계서 → 상세 Wireframe → Storyboard

## 추천 열람 순서

1. `09-스토리보드-HOME.html`, `09-스토리보드-PRODUCTS.html`, `09-스토리보드-BRAND.html`
2. `08-와이어프레임-HOME.svg`, `08-와이어프레임-PRODUCTS.svg`, `08-와이어프레임-BRAND.svg`
3. `07-와이어프레임-통합.html`
4. `03`~`06` Diagram SVG
5. 각 단계 MD와 `07-화면목록.json`

## 파일 역할

| Prefix | 산출물 | 역할 |
|---|---|---|
| 01 | 가상 클라이언트 통합 | 51 Source와 7 Representative, DN/RG 및 과거 개별 산출물 Coverage 연결 |
| 02 | 사이트 분석 | Client Need를 메뉴·콘텐츠·기능으로 번역 |
| 03 | 사이트맵 | 3 Page와 16 Section 계층 |
| 04 | 사이트 구조맵 | 메뉴·콘텐츠·정보 구조·Page 관계 |
| 05 | 사이트 흐름도 | Page 간 이동 방향 |
| 06 | 서비스 흐름도 | PATH A/B/C 사용자 목표 흐름 |
| 07 | 화면설계서·Registry·HTML | 화면 단위 명세 및 브라우저 저충실도 확인 |
| 08 | 상세 Wireframe | Content Fidelity가 보강된 Grayscale 구조 검토 |
| 09 | Storyboard | Page별 이야기·시각·행동·연결 검토 |

## 기존 V4와의 차이

- 기존 V4 원본은 수정하지 않았다.
- 사이트맵과 사이트 구조맵, 사이트 흐름도와 서비스 흐름도를 별도 산출물로 분리했다.
- 51 Client별 과거 산출물 Coverage를 명시했다.
- HOME에는 Source Pool에서 가져온 15개 Working Display Set을 넣어 밀도와 문장 길이를 검토할 수 있게 했다.
- PRODUCTS 1.4를 비실행형 정보 구조로 고정했다.
- Wireframe은 V3의 구조 원리를 승계하되 실제 콘텐츠 역할을 읽을 수 있도록 상세화했다.

## 아직 확정되지 않은 것

- 프로젝트 브랜드명의 최종 승인
- 공식 Product Category와 Category 수
- 대표 판매 Product 15개
- 실제 이미지, 최종 카피, 가격·판매 정보
- 색상, 타이포그래피, 컴포넌트 스타일, 모션

## 먼저 확인하면 좋은 파일

1. HOME Storyboard HTML: Long Scroll 서사와 15개 Portfolio 밀도
2. PRODUCTS Wireframe SVG: 1.2/1.3/1.4의 역할 분리
3. BRAND Storyboard HTML: 브랜드 서사 순서
4. 통합 Wireframe HTML: 3 Page와 반응형 구조

> 이 폴더는 사용자 검토용 도출본이며 `최종-기준본`이나 사용자 승인본이 아니다.
