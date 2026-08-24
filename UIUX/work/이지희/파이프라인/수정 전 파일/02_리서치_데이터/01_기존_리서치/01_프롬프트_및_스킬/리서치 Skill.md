---
name: research-skill
description: "사용자가 제공한 Skill Template와 리서치 결과 MD를 기반으로 리서치 결과를 생성하기 위한 Claude CLI Skill(SKILL.md)을 생성합니다."
argument-hint: "[Skill Template 또는 리서치 결과 MD]"
disable-model-invocation: true
---

# 리서치 Skill 생성

이 Skill은 사용자가 제공한 Skill Template와 리서치 결과 MD를 분석하여
리서치 결과를 생성하기 위한 Claude CLI Skill(SKILL.md)을 작성합니다.

새로운 리서치를 수행하지 않습니다.

리서치 결과를 분석하거나 분석 리포트를 작성하지 않습니다.

최종 결과물은 Claude CLI에서 사용할 SKILL.md 파일입니다.

---

# 실행 조건

1. `${CLAUDE_PROJECT_DIR}/CLAUDE.md`를 읽습니다.

2. 다음 입력 파일이 존재하는지 확인합니다.

지원 형식

- md
- txt

필수 입력

- Skill Template
- 리서치 결과 MD

3. 입력 파일이 없으면 필요한 파일을 안내한 후 종료합니다.

---

# 입력

사용자 요청

`$ARGUMENTS`

인수가 없으면 다음 위치에서 기본 입력을 찾습니다.

```
input/
template/
references/
```

다음 두 개의 문서를 함께 사용합니다.

- Skill Template
- 리서치 결과 MD

---

# 목적

제공된 Skill Template와 리서치 결과 MD를 분석하여
리서치 결과를 생성하기 위한 Claude CLI Skill을 작성합니다.

다음 내용을 추출하여 Skill에 반영합니다.

- 리서치 진행 목적
- 입력 구조
- 작업 절차
- 작성 규칙
- 출력 형식
- 저장 방식
- 검증 절차
- 완료 보고 방식

Template의 구조는 유지하며
리서치 결과 MD의 작성 방식을 Skill에 반영합니다.

---

# 작업 절차

## 1단계

Skill Template의 구조를 분석합니다.

- YAML Header
- 섹션 구성
- 작성 방식
- 문체
- Workflow 구조

---

## 2단계

리서치 결과 MD의 구조를 분석합니다.

- 문서 구성
- 목차
- 작성 순서
- 분석 항목
- 출력 형식

---

## 3단계

리서치 결과 MD를 생성하기 위한 작업 절차를 추출합니다.

분석 항목

- 입력
- 처리 과정
- 출력
- 검증
- 저장

---

## 4단계

Template 구조에 맞게 각 항목을 작성합니다.

다음을 포함합니다.

- 목적
- 실행 조건
- 입력
- 작업 절차
- 작성 규칙
- 저장
- 완료 보고

---

## 5단계

Claude CLI에서 사용할 수 있는 SKILL.md 파일을 생성합니다.

Template의 구조는 유지하고
내용만 리서치 결과 생성 목적에 맞게 작성합니다.

---

# 출력 형식

다음 순서의 Markdown 문서를 생성합니다.

- YAML Header
- Skill 제목
- 실행 조건
- 입력
- 목적
- 작업 절차
- 작성 규칙
- 저장 및 상태
- 완료 전 확인
- 완료

최종 결과물은 Claude CLI에서 사용할 SKILL.md 파일입니다.

---

# 작성 규칙

제공된 Template의 구조를 유지합니다.

리서치 결과 MD의 구조를 반영합니다.

새로운 섹션을 임의로 추가하지 않습니다.

기존 섹션을 삭제하지 않습니다.

리서치를 수행하지 않습니다.

리서치 결과를 분석하지 않습니다.

분석 리포트를 생성하지 않습니다.

최종 결과물은 반드시 리서치 SKILL.md 파일이어야 합니다.

---

# 완료 전 확인

다음을 확인합니다.

- Template 구조를 유지했는가
- 리서치 결과 MD의 구조가 반영되었는가
- 모든 필수 항목이 작성되었는가
- 불필요한 분석 내용이 포함되지 않았는가
- Antigravity CLI에서 바로 사용할 수 있는 형식인가

---

# 완료

결과를 다음 파일명으로 저장합니다.

```
리서치 Skill.md
```

완료 후 다음 내용을 보고합니다.

- 생성된 Skill 이름
- 반영된 Template 구조
- 반영된 리서치 결과 구조
- 생성된 SKILL.md 저장 위치
