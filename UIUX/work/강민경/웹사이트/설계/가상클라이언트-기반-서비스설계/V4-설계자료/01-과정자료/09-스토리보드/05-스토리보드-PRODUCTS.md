# DAMORI PRODUCTS Storyboard

- 프로젝트 브랜드명: `DAMORI / 다모리`
- Screen ID: `PAGE-01`
- 상태: `CURRENT_WORKING_PAGE_STORYBOARD`
- 기준: `05-v4-storyboard-v1.md` Master에서 PRODUCTS만 분리 도출

## 1. Page Name

`PRODUCTS / CATEGORY-SUB`

## 2. Page Purpose

약 200개 Raw Product Source Pool을 유연하게 수용하며 제품군, 소재, 제본, 사양과 탐색 기준 정보를 비교·확인하게 한다.

## 3. User Goal

가입이나 진단 없이 제품 정보를 살펴보고, 자신이 중요하게 보는 기준과 소재·사양 차이를 이해한다.

## 4. 관련 Client / DN / RG 근거

- Client: `V4-C01`, `V4-C02`, `V4-C04`, `V4-C07`
- DN: `DN-01`, `DN-02`, `DN-04`, `DN-07`, `DN-08`, `DN-13`
- RG: `RG-01`, `RG-02`, `RG-04`, `RG-07`, `RG-08`
- `DN-05`는 원본 서비스 요구로만 추적하며 현재 Page 기능 범위 밖이다.
- 경로: `PATH B`, `PATH C`

## 5. Section Structure

`1.1 → 1.2 → 1.3 → 필요 시 1.4`

## 6. Section별 Storyboard

| Section | 목적 | 핵심 콘텐츠 | Visual 영역 | Text 영역 | 사용자 행동 | 다음 연결 |
|---|---|---|---|---|---|---|
| `1.1` Visual Hero | 제품 포트폴리오 첫인상 제공 | DAMORI Products Portfolio | Product Hero Visual 예정 영역 | 제품 탐색 맥락 요약 | 제품군 영역으로 이동 | `1.2` |
| `1.2` Product Group Exploration | Raw Source Pool 탐색 구조 제시 | `GROUP 01~06` 구조 검증용 임시 그룹 | Group Visual Placeholder | Group Description Placeholder, 수·명칭 미확정 안내 | 제품군 정보 확인 | `1.3` |
| `1.3` Product Feature & Specification | 소재와 사양을 균형 있게 비교 | Source 확인: `120gsm`, `180도`, `Smyth Sewn`; 나머지는 Generic Info Slot | Material Detail과 Specification의 Balanced 영역 | 필기 적합성 정보, 사용 방식 참고 정보, 치수·페이지 등 Placeholder | 제품 정보 비교 | `1.4`, `BRAND 2.6` |
| `1.4` User-led Exploration | 탐색에 참고할 기준 안내 | Exploration Criteria와 Related Product Range의 비실행형 정보 구조 | Criteria Guide와 Product Placeholder 영역 | 기준 예시와 관련 정보 범위 안내 | 기준을 참고하고 1.3 정보 재확인 | `1.3`, `BRAND 2.6` |

## 7. Page Flow

- PATH B: `PRODUCTS 1.1 → 1.2 → 1.3 → 필요 시 1.4`
- PATH C: `HOME 0.3 → HOME 0.4 → PRODUCTS 1.2 → PRODUCTS 1.3`
- `1.4`는 실제 동적 필터·추천·알고리즘 결과 기능이 아니라, 사용자가 가입이나 진단 없이 제품 정보를 비교·탐색할 때 참고할 수 있는 탐색 기준과 관련 정보 범위를 안내하는 비실행형 정보 구조이다.

## 8. Reference Insight

Portfolio Density, Product Information Grouping, Material/Specification Balance와 Section Contrast의 구조 원리만 참고한다. Reference의 색상과 고유 Component는 적용하지 않는다.

## 9. Wireframe Handoff

- Wireframe: `06-통합-와이어프레임-V3-PRODUCTS.svg`
- 1.2/1.3/1.4의 역할 차이와 1.3 Balanced Layout을 유지한다.
- Category 수·명칭과 대표 Product는 아직 확정하지 않는다.

## 10. 미확정 사항

- Category 체계와 명칭
- 대표 Product 15개 실제 선정
- Generic Info Slot에 들어갈 최종 Source 확인 콘텐츠
- 최종 Typography, Color, Component Visual과 이미지

