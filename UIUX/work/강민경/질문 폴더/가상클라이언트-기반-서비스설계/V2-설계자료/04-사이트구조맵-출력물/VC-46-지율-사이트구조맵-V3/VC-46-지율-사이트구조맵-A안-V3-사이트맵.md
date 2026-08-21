# VC-46 지율 사이트구조맵 A안 V3 — Section·Skip 탐색형

## 1. Client·REQ 추적
- Client: VC-46 지율(긴 페이지의 스크린리더 탐색), REQ-046.
- 요구: 반복 콘텐츠 Skip, 의미 있는 Section 제목, 레일 범위와 현재 위치를 제공한다.
- 연결 제품: PROD-021 — 레일 탐색 보조 라벨 세트 / PROD-049 — Heading 탐색 제품 목록 / PROD-085 — 제품 Section 요약 카드 / PROD-087 — 포커스 순서 제품 카드.

## 2. 구조 전략
- 시각 순서와 DOM 순서를 일치시키고 반복 카드에 Skip을 제공한다.
- 중복 대체 텍스트를 제거하고 Section·Heading으로 이동한다.

## 3. 페이지·콘텐츠·기능 계약
- PAGE-001 랜딩, PAGE-020 Section, PAGE-021 제품 레일.
- Heading, Skip, 현재 위치, 레일 범위, 복귀를 제공한다.

## 4. 사용자 흐름·상태
- 랜딩 → Section 선택 → 제품군 레일 → 카드 상세 → 원래 위치 복귀.
- 상태: 현재 Section, 레일 범위, 포커스 이동, Skip, 오류·복귀.

## 5. 중복·끊김·가정 검증
- 요약 카드는 반복 음성 낭독을 줄이고 상세 카드로 연결한다.
- 포커스 순서와 시각 순서를 동일하게 유지한다.

## 6. Mermaid
```mermaid
flowchart LR
 A[랜딩]-->B[Section Heading]
 B-->C[Skip·레일 범위]
 C-->D[제품 카드]
 D-->E[상세·복귀]
```

## 7. 판정
- MERGE / INFERENCE: 접근성 탐색과 제품 레일 구조를 하나의 이동 체계로 통합한다.

