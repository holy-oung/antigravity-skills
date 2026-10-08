---
name: skill-vault
description: >
  개인 스킬 보관소(Skill Vault) 및 JIT 스킬 버틀러(Just-in-Time Skill Butler) 가이드.
  사용자가 '스킬 인덱스', '스킬 색인', '스킬 보관소', '스킬 추천', '스킬 가져와줘'를 언급할 때뿐만 아니라,
  특화 도메인(HWP/공문서, 안티슬롭 UI, 영상/유튜브, 보안 감사, SEO, 토큰 압축, 아키맵 등) 작업이 감지되면
  "잠깐! ✋ [스킬명]을 장착합니다"를 선언하고 온디맨드로 스킬을 로드·수행 후 자동 언마운트합니다.
  일상 잡담 및 일반 코딩에는 침묵하여 피로도를 0으로 유지합니다.
---

# 📚 Antigravity 개인 스킬 보관소 & JIT 스킬 버틀러 가이드

개인 스킬 보관소(Skill Vault, 145선)를 총괄하며, 사용자 요청 시 스마트하게 개입·수행·복귀하는 **JIT 스킬 버틀러(Skill Butler)** 운영 지침입니다.

---

## 🎩 JIT 스킬 버틀러(Skill Butler) 3단계 프로토콜

### 1단계: 상황 인지 필터 (3-Tier Context Filtering)
* **Tier 1 (일상/잡담/일반 질문)**:
  - 예: *"쿠팡 의자가 덜컹거리는데 어떡해?"*, *"오늘 날씨 어때?"*, *"파이썬 리스트 슬라이싱 문법 알려줘"*
  - **버틀러 행동: 100% 완전 침묵.** 일반 대화/지식 답변을 즉시 제공하며 스킬 인덱스를 전혀 탐색하지 않습니다.
* **Tier 2 (일반 코딩/단순 수정)**:
  - 예: *"버그 수정해줘"*, *"API 엔드포인트 하나 추가해줘"*, *"타입 선언해줘"*
  - **버틀러 행동: 기본 1-2-3-4 엔지니어링 규칙(Addy-Matt-Ponytail-Scaffold)으로 직접 해결.** 스킬을 끼어들지 않습니다.
* **Tier 3 (전문 도메인 / 복합 프로젝트)**:
  - 예: HWP 공문서 처리, 안티슬롭 UI/디자인 시스템, 바이럴 쇼츠/영상 제작, 보안 침투 감사, 검색엔진(SEO/GEO) 최적화 등.
  - **버틀러 행동: "잠깐! ✋ [스킬명]을 장착합니다" 선언 후 즉시 최적화 스킬 로드.**

---

### 2단계: 초경량 20대 도메인 라우팅 맵 (Fast-Path Routing Map)
전체 145종 색인 파일을 매번 읽지 않고, 아래 20개 대표 스킬 맵으로 0.1초 만에 즉시 라우팅합니다:

| 도메인 | 대표 추천 스킬 | 보관소 위치 | 주요 용도 |
| :--- | :--- | :--- | :--- |
| **🇰🇷 관공서/HWP/PDF** | `kordoc` (#28), `auto-hwp` (#24) | `02-korean-doc-automation/` | HWP/HWPX/PDF 파싱, 신구대조, 공문서 양식 채우기 |
| **🎨 안티슬롭 UI/디자인** | `taste-skill` (#51), `ui-ux-pro-max` (#48) | `03-media-creative/` | AI 특유의 밋밋한 UI 제거, 미니멀/하이엔드 비주얼 톤 주입 |
| **🎬 영상/쇼츠/유튜브** | `autoclip` (#53), `hypit` (#50), `agent-reach` (#68) | `03-media-creative/`, `04-browser-scraping/` | 쇼츠 컷편집, 영상 스크립트 복제, 자막·댓글 스크래핑 |
| **🛡️ 보안/모의해킹** | `strix` (#99), `ECC/security` (#10) | `06-developer-tools-mcp/`, `01-core-skills/` | 침투 테스트, 취약점 패치, 스마트 컨트랙트 감사 |
| **🔍 검색 최적화 (SEO/AEO)** | `fire-your-seo-agency` (#104) | `06-developer-tools-mcp/` | 네이버(NEO), 구글(SEO), AI 검색(GEO/LLMO) 가시성 극대화 |
| **🧠 토큰 압축 & 아키맵** | `headroom` (#91), `archify` (#92) | `05-agent-memory-harness/` | 컨텍스트 60~95% 무손실 압축, 코드베이스 대화형 지도 생성 |
| **📱 모바일/PC OS 제어** | `artemis` (#102), `PC-CONTROL-MCP` (#101) | `06-developer-tools-mcp/` | 스마트폰 앱 자동 제어, OS 마우스/키보드 자동화 |
| **🎮 게임 스튜디오/3D** | `claude-code-game-studios` (#16), `threejs-game-skills` (#22) | `01-core-skills/` | 49개 에이전트 게임 개발 루프, Three.js 3D 파이프라인 |
| **📚 전자책/출판 자동화** | `bookforge` (#26), `translate-book` (#27) | `02-korean-doc-automation/` | 상업 출판급 국문 PDF 생성, 외국 전문 서적 번역 |
| **🤖 대규모 에이전트 팩** | `agency-agents` (#20), `gstack` (#15) | `01-core-skills/` | 18개 부서 230명 전문 AI 직원 투입, 역할별 인지 모드 |

> **희귀 전문 작업 안내**: 위 20개 매핑에 없는 특수 작업일 때만 `C:\Users\Han\Documents\antigravity\skills\skills-index.md` 전체 색인을 1회 열람하여 최적 스킬을 찾습니다.

---

### 3단계: 하이브리드 격리 & 생명주기 (Lifecycle Management)

1. **가벼운 단발성 작업 (1~2개 파일, 즉시 수정)**:
   - 현재 세션에서 해당 스킬의 `SKILL.md`를 `view_file`로 열람하여 지침 흡수.
   - 선언: `💡 잠깐! ✋ 보관소의 [스킬명]을 일시 장착합니다.`
   - 작업 완결 후 명시적 종료: `✅ [스킬명] 작업 완료. 해당 스킬 세션을 언마운트하고 기본 모드로 복귀했습니다.`
2. **다단계 대형 작업 (시스템 전면 개편, 대규모 에셋 생성 등)**:
   - 메인 대화창의 컨텍스트 오염을 100% 방지하기 위해 **서브에이전트(`invoke_subagent`)**를 호출.
   - 서브에이전트에게 해당 스킬 지침을 주입하여 독립된 작업 공간에서 완결.
   - 작업 결과만 메인 대화창에 가져오고 서브에이전트 즉시 소멸 (메인 컨텍스트 잔류 오염 0%).

---

## 📍 핵심 파일 및 보관소 디렉토리

1. **전체 145종 스킬 색인표**: `C:\Users\Han\Documents\antigravity\skills\skills-index.md`
2. **로컬 스킬 보관소**: `C:\Users\Han\Documents\antigravity\skills\`
3. **글로벌 외부 스킬 허브**:
   - [skills.sh](https://skills.sh/) (`npx skills add`)
   - [skillsmp.com](https://skillsmp.com/) (63만 스킬 DB)
   - [vibeindex.ai](https://vibeindex.ai/) (스킬·MCP 통합 검색)
   - [smithery.ai](https://smithery.ai/) (품질 점수 랭킹)
