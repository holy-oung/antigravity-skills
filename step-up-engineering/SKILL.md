---
name: step-up-engineering
description: >
  스텝업 엔지니어링 거버넌스 (Step Up Engineering: 1번 Addy Osmani + 2번 Matt Pocock + 3번 Ponytail + 4번 Claude Scaffold).
  모든 코딩, 리팩토링, 아키텍처 설계 작업 시 자동으로 활성화됩니다.
  1) /spec → /plan 명세와 계획 선행 (Addy), 2) Zero-any 도메인 모델링 및 엄격한 타입 무결성 (Matt),
  3) YAGNI 원칙에 따른 70% 코드 삭감 및 불필요한 의존성 0개 차단 (Ponytail),
  4) 클린 아키텍처 폴더/파일 스캐폴딩 표준 (Scaffold)을 강제하여 주니어 AI의 오버엔지니어링을 차단하고
  시니어 테크 리드 수준의 견고하고 가벼운 프로덕션 코드를 보장합니다.
argument-hint: "[spec|plan|model|scaffold|audit]"
license: MIT
---

# 🚀 Step Up Engineering Protocol (스텝업 엔지니어링 거버넌스)

본 스킬은 Antigravity의 모든 개발 작업에서 **오버엔지니어링(Over-engineering)과 즉흥적 바이브 코딩을 원천 차단**하고, 구글/빅테크 시니어 테크 리드 수준의 규율로 코드를 스텝업(Step Up)시키는 통합 엔지니어링 거버넌스입니다.

---

## 🏛️ 4대 기둥 (The 4 Pillars of Engineering)

```
[1. Addy Osmani] ────> [4. Claude Scaffold] ────> [2. Matt Pocock] ────> [3. Ponytail]
  명세/계획 선행           단정한 폴더 골격          Zero-any 타입 안전        YAGNI 코드 70% 절삭
```

### 1. Pillar 1: Addy Osmani (프로세스 규율)
- **절대 즉흥적으로 코드부터 치지 않습니다.**
- 반드시 6단계 라이프사이클을 준수합니다:
  - `/spec`: 사용자의 모호한 요구사항에서 핵심 요구조건, 제약사항, 입출력 정의.
  - `/plan`: 의존성 및 파일별 구현 순서를 1, 2, 3 단계로 분해.
  - `/build`: 계획된 순서대로 최소 단위 구현.
  - `/test`: 핵심 엣지케이스 검증.
  - `/review`: 불필요한 코드 및 가독성 점검.
  - `/ship`: 배포 및 사용자 인도.

### 2. Pillar 4: Claude Scaffold (아키텍처 스캐폴딩)
- 코드를 한 파일에 무질서하게 누적하거나 폴더를 난잡하게 만들지 않습니다.
- 새 프로젝트나 모듈 생성 시 가장 단정한 클린 구조를 표준으로 잡습니다:
  ```
  project-root/
  ├── .agents/skills/      # [Skill Vault] 필요한 특수 스킬만 온디맨드 복사
  ├── src/
  │   ├── types/           # [Matt Pocock] 도메인 모델 및 타입 정의
  │   ├── core/            # 순수 비즈니스 로직 (의존성 제로)
  │   └── ui/ 또는 api/    # 입출력 인터페이스 레이어
  └── tests/               # 검증 테스트 케이스
  ```

### 3. Pillar 2: Matt Pocock (타입 무결성 & 도메인 모델링)
- `any` 타입 사용을 100% 금지합니다 (`no-explicit-any`).
- 로직을 작성하기 전에 **데이터의 형태(Domain Model)**를 먼저 정의합니다.
- `interface` 및 `type`을 정확히 설계하여 런타임에 발생할 수 있는 `undefined` / `null` 에러를 컴파일 타임에 100% 방어합니다.
- 타입 좁히기(Type Narrowing), 판별 유니온(Discriminated Unions)을 활용하여 상태의 모호성을 제거합니다.

### 4. Pillar 3: Ponytail (YAGNI & 미니멀리즘 브레이크)
- **최고의 코드는 작성하지 않은 코드입니다.**
- Matt과 Addy의 규율이 자칫 "과도한 타입 체조(Type Gymnastics)"나 "거대한 프레임워크 도입"으로 변질되지 않도록 강력한 브레이크를 겁니다.
- **사다리 원칙(The Ladder)**:
  1. 지금 당장 필요한가? (추측성 기능 금지, YAGNI)
  2. 표준 라이브러리(Stdlib)로 해결 가능한가? → 무조건 표준 라이브러리 우선.
  3. 플랫폼 네이티브 기능(Browser DOM, HTML5 등)으로 되는가? → 외부 npm/pip 설치 금지.
  4. 200줄로 쓸 코드를 50줄로 압축할 수 있는가? → 즉시 단순화.

---

## ⚡ 스킬 보관소(Skill Vault)와의 온디맨드 연동

- 본 Step Up Engineering 거버넌스는 상시 기본으로 작동하여 프로젝트의 뼈대와 코드 품질을 지킵니다.
- 특정 도메인 작업(예: HWP 공문서, 3D 게임, SEO 진단, 모바일 제어 등)이 필요할 때는:
  - 145선 스킬 보관소(`C:\Users\Han\Documents\antigravity\skills\`)에서 필요한 스킬만 해당 프로젝트의 `.agents/skills/`로 가져와 결합합니다.
  - 이를 통해 전역 컨텍스트 오염 없이 가장 가볍고 날카로운 에이전트 성능을 유지합니다.
