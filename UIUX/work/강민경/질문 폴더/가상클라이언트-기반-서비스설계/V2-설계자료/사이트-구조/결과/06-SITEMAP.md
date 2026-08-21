# 06 사이트맵

## 전체 수량

- 전체 Page: 20
- HOME: 1
- 1Depth: 5
- 2Depth: 13
- 3Depth: 1
- 최대 Depth: 3

## GNB

1. 기록 방식 찾기
2. 아날로그 기록
3. 디지털 기록
4. 템플릿과 꾸미기
5. 기록 가이드

브랜드 소개는 Footer로 이동한다. 검색·로그인·마이페이지는 활성 근거가 없어 추가하지 않는다.

## 사이트맵 Tree

```text
HOME / PAGE-001
├─ 기록 방식 찾기 / PAGE-002 [CORE_PAGE]
│  └─ 맞춤 기록 추천 / PAGE-003 [CORE_PAGE]
├─ 아날로그 기록 / PAGE-004 [CORE_PAGE]
│  ├─ 노트·속지 선택 / PAGE-005 [REQUIRED_PAGE]
│  ├─ 장문 기록 가이드 / PAGE-006 [REQUIRED_PAGE]
│  └─ 제품과 구성 / PAGE-007 [CORE_PAGE]
│     └─ 제품 상세·비교 / PAGE-008 [REQUIRED_PAGE]
├─ 디지털 기록 / PAGE-009 [CORE_PAGE]
│  ├─ 빠른 기록 / PAGE-010 [REQUIRED_PAGE]
│  ├─ 일정과 시간 흐름 / PAGE-011 [REQUIRED_PAGE]
│  └─ 장문·보존 도구 / PAGE-012 [REQUIRED_PAGE]
├─ 템플릿과 꾸미기 / PAGE-013 [CORE_PAGE]
│  ├─ 템플릿 탐색·비교 / PAGE-014 [REQUIRED_PAGE]
│  └─ 꾸미기 자산 / PAGE-015 [REQUIRED_PAGE]
└─ 기록 가이드 / PAGE-016 [SUPPORT_PAGE]
   ├─ 작게 시작하기 / PAGE-017 [SUPPORT_PAGE]
   ├─ 중단 후 다시 시작 / PAGE-018 [CONDITIONAL_PAGE]
   └─ 이동·보존·도움말 / PAGE-019 [SUPPORT_PAGE]

FOOTER
└─ 브랜드 소개 / PAGE-020 [REQUIRED_PAGE]
```

## 전체 Page Table

| ID | Page | Depth | Parent | 상태 | 핵심 SR |
|---|---|---:|---|---|---|
| PAGE-001 | 홈 | 0 | SITE | CORE_PAGE | SR-001·019·020 |
| PAGE-002 | 기록 방식 찾기 | 1 | PAGE-001 | CORE_PAGE | SR-001·002 |
| PAGE-003 | 맞춤 기록 추천 | 2 | PAGE-002 | CORE_PAGE | SR-001·002·019·020 |
| PAGE-004 | 아날로그 기록 | 1 | PAGE-001 | CORE_PAGE | SR-003~005 |
| PAGE-005 | 노트·속지 선택 | 2 | PAGE-004 | REQUIRED_PAGE | SR-003·004·011·012 |
| PAGE-006 | 장문 기록 가이드 | 2 | PAGE-004 | REQUIRED_PAGE | SR-001·002·004 |
| PAGE-007 | 제품과 구성 | 2 | PAGE-004 | CORE_PAGE | SR-003~005 |
| PAGE-008 | 제품 상세·비교 | 3 | PAGE-007 | REQUIRED_PAGE | SR-002·005·019 |
| PAGE-009 | 디지털 기록 | 1 | PAGE-001 | CORE_PAGE | SR-006~008 |
| PAGE-010 | 빠른 기록 | 2 | PAGE-009 | REQUIRED_PAGE | SR-008·018 |
| PAGE-011 | 일정과 시간 흐름 | 2 | PAGE-009 | REQUIRED_PAGE | SR-006·007·015(HOLD) |
| PAGE-012 | 장문·보존 도구 | 2 | PAGE-009 | REQUIRED_PAGE | SR-002·014·016(HOLD)·019 |
| PAGE-013 | 템플릿과 꾸미기 | 1 | PAGE-001 | CORE_PAGE | SR-009~012 |
| PAGE-014 | 템플릿 탐색·비교 | 2 | PAGE-013 | REQUIRED_PAGE | SR-011·012 |
| PAGE-015 | 꾸미기 자산 | 2 | PAGE-013 | REQUIRED_PAGE | SR-009·010 |
| PAGE-016 | 기록 가이드 | 1 | PAGE-001 | SUPPORT_PAGE | SR-018~020 |
| PAGE-017 | 작게 시작하기 | 2 | PAGE-016 | SUPPORT_PAGE | SR-008·018·020 |
| PAGE-018 | 중단 후 다시 시작 | 2 | PAGE-016 | CONDITIONAL_PAGE | SR-017(HOLD)·018·020 |
| PAGE-019 | 이동·보존·도움말 | 2 | PAGE-016 | SUPPORT_PAGE | SR-014~016(HOLD)·019·020 |
| PAGE-020 | 브랜드 소개 | 1 | FOOTER | REQUIRED_PAGE | SR-019 |

## 검토 결과

- 1Depth 폭 5개: `WITHIN_GUIDE`
- 최대 3Depth: `WITHIN_GUIDE`
- Parent 없는 활성 Page 0
- 중복 Page 0
- 고립 Page 0
- 핵심 요구는 2~3Depth 이내 접근
- 서비스 흐름·화면 배치·와이어프레임은 이 문서 범위에 포함하지 않음
