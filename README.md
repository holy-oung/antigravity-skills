# 🗃️ Antigravity 개인 스킬 보관소 (Skill Vault) & 1-2-3-4 거버넌스

> **Antigravity Official Skill Vault & Universal Multi-Agent Engineering Governance**  
> 145선 통합 색인표 + 4대 코어 엔지니어링 헌법(`GEMINI.md`) + ECC 292종 + Google 137종 공식 스킬을 탑재한 개인 스킬 보관소입니다.

---

## 🛡️ 1-2-3-4 Core Engineering Protocol (기본 헌법)

이 저장소를 사용하는 모든 환경 및 프로젝트에서는 아래 4대 코어 엔지니어링 거버넌스가 무조건 강제 적용됩니다:

1. **Pillar 1 (Addy Osmani)**: 코드를 즉시 작성하지 않고, 반드시 `/spec`과 `/plan` 명세 및 계획을 선행합니다.
2. **Pillar 4 (Claude Scaffold)**: 단일 파일 덤프를 지양하고 모듈형 클린 아키텍처 폴더/파일 구조를 유지합니다.
3. **Pillar 2 (Matt Pocock)**: Zero-any 정책, 엄격한 도메인 모델링과 타입 무결성을 사전에 정의합니다.
4. **Pillar 3 (Ponytail)**: 극단적 YAGNI 미니멀리즘, 불필요한 의존성 0개, 표준 라이브러리 우선으로 코드를 70% 가볍게 유지합니다.
5. **Skill Vault Gateway**: 특수 역량(HWP 파싱, 3D, SEO, 스크래핑 등)이 필요할 때 이 보관소에서 온디맨드로 인출합니다.

* **지원 규격**: `GEMINI.md` (Antigravity), `AGENTS.md` (Universal AI Agent), `CLAUDE.md` (Claude Code)

---

## 💻 다른 기기(새 PC / 노트북 / Mac)에서 1초 만에 설정하기

새로운 컴퓨터나 노트북에서 이 보관소와 4대 규칙을 그대로 사용하려면:

```bash
# 1. 비공개 저장소 클론
git clone https://github.com/holy-oung/antigravity-skills.git

# 2. 저장소 디렉토리로 이동
cd antigravity-skills

# 3. 원클릭 셋업 스크립트 실행
# Windows (PowerShell):
.\install.ps1

# macOS / Linux (Bash):
chmod +x install.sh && ./install.sh
```

설치 스크립트를 실행하면 해당 기기의 글로벌 설정(`~/.gemini/GEMINI.md`)에 4대 헌법이 자동 등록되어, **어떤 폴더나 프로젝트를 열어도 안티그래비티가 자동으로 최상위 엔지니어링 헌법을 준수**합니다.

---

## 📌 폴더 구조 및 가이드

```
antigravity-skills/
├── 📄 GEMINI.md                 # Antigravity 4대 코어 헌법 (최우선 사용자 규칙)
├── 📄 AGENTS.md / CLAUDE.md     # 타 AI 에이전트 호환용 헌법 파일
├── 📄 skills-index.md           # 145종 엄선 스킬 통합 색인표 (핵심 카탈로그)
├── 📄 ecc-catalog.md            # ECC 292종 실전 프로덕션 스킬 카탈로그
├── 📄 google-skills-catalog.md   # Google 공식 137종 클라우드/AI/광고 스킬 카탈로그
├── ⚡ install.ps1 / install.sh   # 다른 기기 원클릭 글로벌 셋업 스크립트
│
├── 📁 01-core-skills/           # 핵심 코딩 & 아키텍처 (ECC, Google, Superpowers, Gstack, Game-Studios 등)
├── 📁 02-korean-doc-automation/ # 한국 공문서 & HWP 자동화 (Kordoc, Auto-HWP, Opendataloader-PDF 등)
├── 📁 03-media-creative/        # 미디어 & 디자인 (Taste-Skill, OpenDesign, AutoClip, Hypit, UI UX Pro Max 등)
├── 📁 04-browser-scraping/      # 웹 브라우징 & 스크래핑 (Agent-Reach, Playwright CLI, Scrapling 등)
├── 📁 05-agent-memory-harness/  # 메모리 & 인프라 (Headroom 토큰압축, Archify 아키맵, Dream-RSI 등)
└── 📁 06-developer-tools-mcp/   # MCP & 개발자 생산성 (Artemis 안드로이드제어, Fire-Your-SEO, Trail of Bits 보안 등)
```

---

## 🚀 개별 프로젝트에 특정 스킬 가져오는 방법

특정 프로젝트(예: `my-web-app`)에서 안티그래비티와 작업할 때:

```markdown
"내 스킬 보관소(antigravity-skills)에서 [스킬이름] 스킬을 현재 프로젝트로 가져와줘."
```

라고 요청하시면 해당 스킬만 현재 작업 폴더(`.agents/skills/`)로 복사되어 가볍고 안전하게 동작합니다.
