# 🗂️ Antigravity 개인 스킬 보관소 색인표 (145선)

> **이 색인표의 목적**:  
> 수많은 스킬과 도구를 Antigravity에 한꺼번에 전부 등록하면 **컨텍스트 토큰이 과도하게 낭비되고 성능이 저하**됩니다.  
> 따라서 모든 고급 도구/스킬을 이곳 **스킬 색인표(Index)**에 분류해 두고, **필요한 순간에만 프로젝트 폴더(`.agents/skills/`)로 가져와(복사하여) 가볍고 완벽하게 활용**합니다.

---

## 🧭 카테고리별 빠른 이동
1. [🛠️ 핵심 코딩 & 아키텍처 스킬](#1-️-핵심-코딩--아키텍처-스킬-core-agent-skills)
2. [🇰🇷 한국형 문서 & 오피스 자동화](#2--한국형-문서--오피스-자동화-korean-doc--publishing)
3. [🎬 미디어, 영상 & 시각 디자인](#3--미디어-영상--시각-디자인-media--visual-design)
4. [🌐 웹 브라우징 & 스텔스 크롤링](#4--웹-브라우징--스텔스-크롤링-web-browsing--scraping)
5. [🧠 에이전트 메모리 & 오케스트레이션](#5--에이전트-메모리--오케스트레이션-memory--harness)
6. [💻 개발자 생산성, 보안 & MCP](#6--개발자-생산성-보안--mcp-devtools--security)
7. [🔍 글로벌 스킬·MCP 통합 검색 허브](#7--글로벌-스킬mcp-통합-검색-허브-skill--mcp-hubs)

---
### 1. 🛠️ 핵심 코딩 & 아키텍처 스킬 (Core Agent Skills)
> 프로젝트에 바로 주입하여 코드 품질을 높이고 버그를 줄이는 순수 지침/규칙 팩, 거버넌스 팩 및 게임 스튜디오 하네스

| 번호 | 스킬/프로젝트 | 유형 | 주요 용도 및 추천 사용 시점 |
| :---: | :--- | :---: | :--- |
| 1 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `[Skill]` | **(스타 9.9만) 구글 크롬 리드 애디 오스마니**의 프로덕션급 개발 순서 스킬 25개 (`/spec → /plan → /build → /test → /review → /ship`), 웹 표준·성능·클린 코드 강제 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | `[Skill]` | **타입스크립트 마스터**의 실전 스킬. any 남발 방지, React 19/Next.js 엄격한 타입 안정성 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | `[Skill]` | **[전역 설치됨]** YAGNI & 미니멀리즘 시니어 개발자 사다리 원칙. 코드량 70% 감소 및 토큰 절약 |
| 4 | [LeeYudok/claude-scaffold](https://github.com/LeeYudok/claude-scaffold) | `[Skill]` | 프로젝트 초기 구조 설계 및 아키텍처 스캐폴딩 자동화 |
| 5 | [calmtiger86/senpai-ask](https://github.com/calmtiger86/senpai-ask) | `[Skill]` | 개발자에게 날카로운 질문/인터뷰를 진행하여 애매한 요구사항을 명확히 뽑아내는 질문 스킬 |
| 6 | [jongwony/epistemic-protocols](https://github.com/jongwony/epistemic-protocols) | `[Skill]` | 의사결정 시 AI 환각과 확증 편향을 통제하는 품질 관리 프로토콜 |
| 7 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | `[Skill]` | AI가 코드를 생략(`// TODO...`)하지 않고 끝까지 완벽히 구현하도록 강제 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | `[Tool]` | 기술 문서나 PDF 책을 에이전트가 읽을 수 있는 `SKILL.md` 포맷으로 자동 변환 |
| 9 | [alamops/skills](https://github.com/alamops/skills) | `[Skill]` | 앱스토어 SEO 최적화 및 메타데이터 자동 작성 스킬 (`#appstore-seo`) |
| 10 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | `[Skill/Harness]` | **[보관소 복제됨 / 스타 25.7만]** Claude Code·Codex·커서 하네스 최적화 및 292종 프로덕션 스킬, 인스팅트 지속 학습, 보안 감사 ([292종 전체 카탈로그](./ecc-catalog.md)) |
| 11 | [google/skills](https://github.com/google/skills) | `[Skill/Cloud]` | **[보관소 복제됨 / 스타 19.8k]** 구글 공식 Agent Skills (137종). Google Ads·GA4·GCP 클라우드(118종)·Firebase·Gemini 공식 플레이북 ([137종 전체 카탈로그](./google-skills-catalog.md)) |
| 12 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | `[Skill]` | **[보관소 복제됨 / 스타 21.3만]** 안드레이 카파시(Karpathy)의 AI 코딩 관찰에 기반한 `CLAUDE.md` 행동 제어 및 LLM 코딩 함정 방지 룰 |
| 13 | [github/spec-kit](https://github.com/github/spec-kit) | `[Tool/Framework]` | **깃허브 공식 Spec-Kit**: 바이브 코딩을 방지하는 명세 주도 개발(SDD). 명세(Specify) → 계획 → 작업 분해 → 구현 자동화 |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | `[Skill/Framework]` | **[보관소 복제됨]** 에이전트를 규율 있는 다단계 엔지니어링 팀으로 격상시키는 컴포저블 스킬 프레임워크 & 개발 방법론 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | `[Skill/Pack]` | **[보관소 복제됨]** YC 대표 개리 탄의 Claude Code 전용 20+ 전문 인지 역할별(/ceo, /eng-manager, /qa, /security) 스킬 팩토리 |
| 16 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | `[Harness/Game]` | **[보관소 복제됨 / 스타 2.5만]** 49개 전문 AI 에이전트, 72개 워크플로우 스킬을 갖춘 실제 게임 스튜디오 계층 구조 오케스트레이션 |
| 17 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | `[Agent/Platform]` | **(스타 8.9만)** 개발자의 지시를 받아 소프트웨어 개발 작업을 완전히 자율 수행하는 오픈소스 AI 개발자 (구 OpenDevin) |
| 18 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | `[Curated/Apps]` | **(스타 14.0만)** 100+개 오픈소스 AI 비즈니스 에이전트(영업·제품 런칭·채용·데이터 분석·딥리서치) 및 RAG 실전 앱 모음 |
| 19 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | `[Skill/Course]` | **(스타 5.8만)** 에이전트·MCP 서버·프롬프트·강화학습·스웜까지 523개 프로젝트를 직접 코딩하며 배우는 20단계(342시간, 한국어 포함 12개 언어) AI 엔지니어링 실전 커리큘럼 스킬 ([공식 사이트](https://aiengineeringfromscratch.com/)) |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | `[Skill/Pack]` | **(스타 15.8만)** 프론트엔드 마법사부터 레딧 커뮤니티 닌자, 현실성 체커까지 18개 전문 부서, 230여 명의 개별 AI 직원을 즉시 업무에 투입하는 에이전시 스킬 모음 |
| 21 | [trailhq/Graft](https://github.com/trailhq/Graft) | `[Tool/Visual]` | **(스타 9.6k)** AI 자동화 폴더와 코드베이스를 시각적 지도로 구조화하여 Claude Code, Cursor, Codex 등 코딩 에이전트의 컨텍스트 이해를 가속화하고 비용을 절감하는 도구 |
| 22 | [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) | `[Skill/Game]` | **(스타 2.4k)** Three.js 브라우저 3D 게임 제작 에이전트 스킬: 게임플레이 루프, AAA 스타일 그래픽, UI/UX, QA 테스트 및 AI 3D·오디오 에셋 파이프라인 |
| 23 | [vesperchant & vibepackr / BT-OS](https://www.threads.com/share/BAC4dLvcQt/) | `[Rule/Governance]` | **Gemini & Antigravity 조련술**: `00-instinct.md` 본능 통제, PreInvocation 훅 현실 접지(git status 주입), intent-guard 위험 차단, 온디맨드 3단계 지연 로딩, `.harness/` 지식 영구 자산화 거버넌스 팩 |

---

### 2. 🇰🇷 한국형 문서 & 오피스 자동화 (Korean Doc & Publishing)
> 한국 관공서, 기업의 HWP/HWPX 문서 처리, 신구대조, 양식 자동 채우기, 네이버 메일 자동화 및 전자책 출판

| 번호 | 스킬/프로젝트 | 유형 | 주요 용도 및 추천 사용 시점 |
| :---: | :--- | :---: | :--- |
| 24 | [kwakseongjae/auto-hwp](https://github.com/kwakseongjae/auto-hwp) | `[Tool/MCP]` | **오토한글**: Rust/Wasm 기반 HWP/HWPX 파싱, 렌더링, 편집 및 PDF 변환 엔진 |
| 25 | [DoHyun468/claw-hwp](https://github.com/DoHyun468/claw-hwp) | `[Tool]` | AI 에이전트와 한글(HWP) 오피스를 연동하여 문서를 직접 다루는 툴 |
| 26 | [gongnyang/bookforge](https://github.com/gongnyang/bookforge) | `[Skill/Tool]` | 주제 한 줄 입력 시 상업 출판 품질의 국문 전자책 PDF를 자동 생성 (스타일 6종) |
| 27 | [deusyu/translate-book](https://github.com/deusyu/translate-book) | `[Tool]` | 외국어 전문 서적 번역 및 교정 자동화 파이프라인 |
| 28 | [chrisryugj/kordoc](https://github.com/chrisryugj/kordoc) | `[Skill/MCP]` | **[보관소 복제됨 / 스타 1.9k]** HWP 3/5/HWPX/PDF/Office/이미지 등 대한민국 모든 관공서 문서 파싱, 신구대조, 양식 자동 채우기 CLI/MCP (Antigravity 공식 지원) |
| 29 | [changh95/latex_resume_template_kor](https://github.com/changh95/latex_resume_template_kor) | `[Template]` | 한국형 모던 LaTeX 국문 이력서/포트폴리오 템플릿 |
| 30 | [seungyeon980808-pixel/exam_pool](https://github.com/seungyeon980808-pixel/exam_pool) | `[Tool]` | 시험 문제 은행 관리 및 HWP 문서 변환기 |
| 31 | [jungkeun-lee/SAJDMathNote-Release](https://github.com/jungkeun-lee/SAJDMathNote-Release) | `[Tool]` | 수학 공식 및 수식 기반 문제 풀이 노트 정리 도구 |
| 32 | [kjh0523/kayatext](https://github.com/kjh0523/kayatext) | `[Tool]` | 한국어 텍스트 정제 및 문서 처리 유틸리티 |
| 33 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | `[Tool/Parser]` | **(스타 2.9만)** AI/LLM 파이프라인에 최적화된 초고속 오픈소스 PDF 파서 (복잡한 서식, 표, 수식 완벽 추출) |
| 34 | [golbin/hop](https://github.com/golbin/hop) | `[App/Editor]` | **(스타 1.8k) HOP (HOP is Open HWP)**: Rust/rhwp 기반 오픈소스 크로스플랫폼(macOS, Windows, Linux) HWP/HWPX 데스크톱 문서 뷰어·편집기 및 PDF 내보내기 앱 ([공식 사이트](https://golbin.github.io/hop/)) |
| 35 | [chanmuzi/naver-mail-mcp](https://github.com/chanmuzi/naver-mail-mcp) | `[MCP/Mail]` | **Naver Mail MCP 서버**: 네이버 메일 검색, 스레드/본문 열람, 첨부파일 다운로드, 초안 작성 및 발송을 에이전트와 연동하는 Python/uvx 기반 공식 규격 MCP (`uvx naver-mail-mcp`) |
| 36 | [eziwork/naver-mail](https://github.com/eziwork/naver-mail) | `[Plugin/Mail]` | **Eziwork 네이버 메일**: Claude Code 및 Codex 터미널에서 네이버 업무 메일을 직접 검색·요약하고 답장을 작성·발송하는 한국형 로컬 오피스 플러그인 |

---

### 3. 🎬 미디어, 영상 & 시각 디자인 (Media & Visual Design)
> 숏폼/릴스 바이럴 복제, 영상 하이라이트 자동 추출(AutoClip), React 영상 렌더링(Remotion), 실시간 아바타, Anti-Slop UI, 디자인 시스템, 건축 대지분석 및 HTML 시각화

| 번호 | 스킬/프로젝트 | 유형 | 주요 용도 및 추천 사용 시점 |
| :---: | :--- | :---: | :--- |
| 37 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | `[Tool]` | **(스타 12만)** 키워드 하나로 쇼츠/릴스/틱톡 고화질 AI 영상을 전자동 생성 |
| 38 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | `[Skill/Tool]` | AI 에이전트에 비디오 이해 능력 부여 (`/watch` 영상 프레임 분석 및 전사) |
| 39 | [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) | `[Skill/Tool]` | 자막(SRT)을 따뜻한 종이 질감의 손글씨 화이트보드 애니메이션으로 렌더링 |
| 40 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | `[Skill]` | 38종의 잡지/출판물급 고품질 HTML+SVG 다이어그램 생성 (Mermaid 대체) |
| 41 | [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) | `[Skill]` | 캐릭터/IP 마스코트 기반 귀엽고 정교한 네오-스큐어모피즘 로고 디자인 |
| 42 | [Audio8-AI/Audio8_TTS](https://github.com/Audio8-AI/Audio8_TTS) | `[Tool/Model]` | 자연스러운 음성 합성을 위한 고품질 TTS 엔진 |
| 43 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | `[Tool]` | 이미지에서 워터마크를 깔끔하게 자동 제거하는 유틸리티 |
| 44 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | `[Tool]` | 2D 이미지나 UI 디자인을 인터랙티브 3D Three.js 코드로 변환 |
| 45 | [OpenMOSS/MOSS-VL](https://github.com/OpenMOSS/MOSS-VL) | `[Model]` | 장문 영상 및 실시간 비디오 이해를 위한 오픈 비전-언어 모델 |
| 46 | [jkf87/murmur](https://github.com/jkf87/murmur) | `[App/Tool]` | 맥 실리콘 기반 실시간 고속 음성 전사(STT) 및 번역 도구 |
| 47 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | `[Tool]` | 대용량 및 다양한 폰트의 문서를 인식하는 고성능 OCR 엔진 |
| 48 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `[Skill]` | **[보관소 복제됨 / 스타 12.8만]** 프로덕션급 UI/UX 설계를 위한 고도화된 디자인 인텔리전스 가이드 팩 |
| 49 | [amaancoderx/skillui](https://github.com/amaancoderx/skillui) | `[Tool/Skill]` | **SkillUI**: 웹사이트 URL에서 색상·폰트·간격·컴포넌트를 뜯어내 에이전트가 쓸 `.skill` 디자인 파일로 자동 추출 |
| 50 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | `[Skill/Video]` | **[보관소 복제됨 / 스타 7.4k]** AI 에이전트 기반 바이럴 영상 복제 & 프로덕션 DSL. 단어 앵커링 편집, B-roll·음성·얼굴 교체 및 100개 변형 영상 원커맨드 자동 렌더링 |
| 51 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `[Skill/Design]` | **[보관소 복제됨 / 스타 8.9만]** Anti-Slop 프론트엔드 디자인 스킬. AI의 밋밋한 기본값 대신 미니멀·브루탈리스트·하이엔드 비주얼 톤 자동 주입 |
| 52 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | `[Workspace]` | **OpenDesign**: 오픈소스 로컬 퍼스트 AI 디자인 워크스페이스. DESIGN.md 표준 규격과 250+ 스킬로 코딩 에이전트에 디자인 엔진 권한 부여 |
| 53 | [zhouxiaoka/autoclip_mvp](https://github.com/zhouxiaoka/autoclip_mvp) | `[Tool/Video]` | **[보관소 복제됨 / 스타 1.1k]** AutoClip: 긴 영상에서 AI가 하이라이트 구간을 자동 추출 및 9:16 인물 추적 컷 편집하는 쇼츠 제작 도구 |
| 54 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | `[Framework]` | **(스타 6.0만)** React 코드로 프로그래밍 방식 영상을 렌더링하는 오픈소스 표준 프레임워크 (reborn-motion-skills 모션그래픽 팩 연동) |
| 55 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | `[Model/Video]` | **(CVPR 2026 / 스타 3.8k)** 사진 한 장으로 실시간 라이브 스트리밍용 말하는 아바타 애니메이션을 고화질로 구동 |
| 56 | [HisMax/RedInk](https://github.com/HisMax/RedInk) | `[Tool/App]` | **(스타 5.6k)** 한 문장 입력으로 샤오홍슈/SNS 감성 글과 카드뉴스 이미지를 원스톱 자동 생성하는 툴 |
| 57 | [xiamuceer-j/MuMuAINovel](https://github.com/xiamuceer-j/MuMuAINovel) | `[Tool/Writing]` | **(스타 3.1k)** 줄거리 기획, 인물 설정부터 본문 집필까지 AI와 함께 완성하는 지능형 소설 창작 도구 |
| 58 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | `[Tool/Video]` | **(스타 6.4만)** 주제 하나로 대본 기획, 이미지 생성, 자막 렌더링, 컷 편집까지 12개 파이프라인과 700+ 스킬로 전자동 완결하는 오픈소스 AI 영상 제작 스튜디오 시스템 |
| 59 | [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) | `[Skill/Design]` | **(스타 2.2k)** 1,400+개 실제 브랜드 로고 레퍼런스 라이브러리와 SVG 제작·검수 원칙을 담은 Claude Code & Gemini 공식 로고 디자인 스킬 (`/logo-design`) |
| 60 | [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) | `[Skill/Visual]` | **(스타 1.1k)** 복잡한 설명이나 비교 분석 질문의 답을 장문의 텍스트 대신 단일 반응형 HTML 시각화 페이지로 응답 (출력 토큰 7.4배 절감, 시간 3.6배 단축) |
| 61 | [leeuc10/blurssism](https://github.com/leeuc10/blurssism) | `[Design System]` | **(스타 37)** 글래스모피즘(Glassmorphism)과 정교한 블러 효과를 결합한 모던 웹·앱 공용 오픈소스 디자인 시스템 (React/Svelte 지원) |
| 62 | [sitedia.app](https://sitedia.app/) | `[Platform/Arch]` | **(Sitedia / 대지분석 AI)**: 전국 지번 클릭 시 용도지역·건폐율·용적률 산출, 3D 매스 모델링, 일조·그림자·바람 시뮬레이션 및 24종 건축 다이어그램·단면도를 자동 생성하는 공간 설계 AI |

---

### 4. 🌐 웹 브라우징 & 스텔스 크롤링 (Web Browsing & Scraping)
> AI 에이전트를 위한 초경량 브라우저, 안티봇 우회 스크래핑 및 전 웹 트렌드 리서치

| 번호 | 스킬/프로젝트 | 유형 | 주요 용도 및 추천 사용 시점 |
| :---: | :--- | :---: | :--- |
| 63 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | `[Library]` | 차단 및 안티봇을 지능적으로 우회하는 고속 스텔스 웹 스크래퍼 |
| 64 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | `[Tool]` | AI 에이전트를 위해 Rust로 밑바닥부터 만든 초경량/초고속 헤드리스 브라우저 |
| 65 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | `[Browser]` | 핑거프린트 추적을 방지하는 보안 스텔스 브라우징 환경 |
| 66 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | `[Agent]` | 웹 페이지 요소를 인식하고 사람처럼 클릭/입력하는 알리바바 웹 에이전트 |
| 67 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | `[Tool]` | 여러 검색 엔진을 조합하여 최적의 개발 정보를 긁어오는 심층 검색 툴 |
| 68 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | `[Dataset]` | 개발에 즉시 쓸 수 있는 전 세계 무료 공개 API 총집합 목록 |
| 69 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | `[Tool/Skill]` | **(스타 7.9만)** AI 에이전트 전 웹(Twitter/X, Reddit, YouTube, GitHub 등 15개 플랫폼) 검색·리딩 권한 부여 (무과금 연동) |
| 70 | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | `[Tool/CLI]` | **(스타 1.3만)** 마이크로소프트 공식 Playwright CLI. AI가 브라우저를 직접 열어 클릭·입력하고 스크린샷 검증 수행 |
| 71 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | `[Skill/Research]` | **(스타 6.3만)** 레딧·X·유튜브·틱톡·HN·Polymarket 등 최근 30일간 전 웹의 실시간 반응과 여론을 조사·합성하는 트렌드 리서치 스킬 |

---

### 5. 🧠 에이전트 메모리 & 오케스트레이션 (Memory & Harness)
> 에이전트 세션 간 장기 기억 유지, 멀티에이전트 스웜, 컨텍스트 압축(Headroom), 아키텍처 맵(Archify), 자가 개선(Dream-RSI), 초고속 의사결정(Laya), 실시간 게임 하네스(JEV-Star) 및 학술 연구 에이전트(Paper2Agent)

| 번호 | 스킬/프로젝트 | 유형 | 주요 용도 및 추천 사용 시점 |
| :---: | :--- | :---: | :--- |
| 72 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | `[Tool/MCP]` | **[핵심]** 에이전트 CLI 간 영구 장기 기억(Memory) 보관 및 Handoff 세션 공유 |
| 73 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | `[Harness]` | DeepSeek 모델 기반 플러그인 에이전트 오케스트레이션 하네스 |
| 74 | [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) | `[Index]` | DeepSeek Harness용 15,000+개 플러그인 검증 및 추천 레이더 |
| 75 | [Prism-Shadow/penguin-harness](https://github.com/Prism-Shadow/penguin-harness) | `[Harness]` | 경량 에이전트 실행 및 모니터링 하네스 |
| 76 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | `[Agent]` | Nous Research의 강력한 오픈 가중치 자율 에이전트 프레임워크 |
| 77 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | `[Agent]` | 분산 컴퓨팅 기반 자율 학습 및 코딩 에이전트 (중복 1건 제거) |
| 78 | [falcons-eyes/agent-fabric-dispatch](https://github.com/falcons-eyes/agent-fabric-dispatch) | `[Orchestrator]` | 여러 세부 에이전트에게 업무를 분배하고 취합하는 디스패치 시스템 |
| 79 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | `[Tool]` | 터미널 에이전트 환경 및 플러그인 관리 도구 |
| 80 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | `[Tool]` | 오픈소스 모델 기반 코딩 에이전트 실행 환경 |
| 81 | [12errh/zen-proxy](https://github.com/12errh/zen-proxy) | `[Proxy]` | 다중 LLM API 호출 라우팅, 캐싱 및 장애 복구 프록시 레이어 |
| 82 | [CopilotKit/openbot](https://github.com/CopilotKit/openbot) | `[Framework]` | 웹 앱 내부에 에이전트 기능을 직접 임베드하는 챗봇 프레임워크 |
| 83 | [yoheinakajima/activegraph](https://github.com/yoheinakajima/activegraph) | `[Framework]` | 지식 그래프를 활용한 자율 작업 실행 에이전트 |
| 84 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | `[Infrastructure]` | 그래프 기반 컨텍스트 엔지니어링 및 지식 추적 인프라 (중복 1건 제거) |
| 85 | [webfuse-com/awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | `[Curated]` | 스스로 코드를 수정하고 개선하는 자율 연구 에이전트 모음 |
| 86 | [Ranteck/graph-engineer](https://github.com/Ranteck/graph-engineer) | `[Tool]` | 그래프 구조 기반 코드 분석 및 리팩토링 엔지니어링 툴 |
| 87 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | `[Harness/Swarm]` | **(스타 1.4만)** Claude Code 전용 멀티에이전트 스웜 오케스트레이션 메타 하네스 & 공유 벡터 메모리 |
| 88 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | `[Tool/Graph]` | **Task Master**: PRD 요구사항을 의존성 트리 기반 `tasks.json`으로 구조화하여 AI의 단계별 완수를 보장 |
| 89 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | `[Tool/Graph]` | 낯선 대규모 코드베이스를 인터랙티브 지식 그래프로 변환하여 에이전트 구조 이해 및 온보딩 지원 |
| 90 | [zhengkid/Dream-RSI](https://github.com/zhengkid/Dream-RSI) | `[Framework/RSI]` | **[보관소 복제됨]** 구글&딥마인드 발표. 탐색 이력(Tree)을 리플레이 시뮬레이터로 재활용하여 0의 실행 비용으로 탐색 정책을 자가 개선(RSI)하는 프레임워크 (Lasso 호출 162배 절감, GPU 커널 개선) |
| 91 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | `[MCP/Proxy]` | **[보관소 복제됨 / 스타 7.4만]** 도구 출력, 대용량 로그, JSON, RAG 청크를 60~95% 무손실 압축하여 토큰 비용과 컨텍스트 오버플로우를 해결하는 MCP |
| 92 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | `[Skill/Graph]` | **[보관소 복제됨 / 스타 5.8만]** 아키맵: 코드베이스를 분석해 인터랙티브 대화형 시스템 맵(아키텍처·시퀀스·데이터 흐름)을 HTML로 자동 생성 |
| 93 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | `[Research/Agent]` | **(스타 6.6k)** 인간 개입 없이 스스로 존재 가치를 증명(수익/연산자원 확보)하고 복제 및 진화하는 최초의 자율 생존 AI 에이전트 |
| 94 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | `[Tool/MCP]` | **(스타 4.5만)** 코드베이스 전체를 영구 지식 그래프로 초고속 색인하여 AI 비서가 엉뚱한 코드를 건드리는 오류를 방지하고 토큰을 99% 절약하는 고성능 MCP 서버 (158개 언어) |
| 95 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | `[Engine/Decision]` | **(스타 3.1만)** 텍스트 생성 대신 1회 순전파(33ms)로 고객 문의의 의도·긴급도·이탈 위험 등 구조화된 '결정(Choice/Score)'만 초고속 반환하는 비자기회귀 System 1 의사결정 엔진 (`pip install laya`) |
| 96 | [sc2musa/Jev_Star](https://github.com/sc2musa/Jev_Star) | `[Research/Game]` | **(arXiv:2609.27331)** 서브세컨드(0.42초) 실행기 System 1(JEV)과 거대 전략 플래너 System 2(GPT-6) 2단계 분업으로 스타크래프트 2 최고 난이도 AI(Lv7)를 전승 격파한 실시간 하네스 아키텍처 |
| 97 | [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | `[Skill/Compaction]` | **(스타 7.4k)** 긴 작업 중 컨텍스트 컴팩트(대화 요약) 시 파일 경로·에러 로그 소실 없이, 불필요한 도구 호출·결과만 선택 정리하여 원문을 정밀 보존하는 지능형 압축 스킬 |
| 98 | [jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent) | `[Research/MCP]` | **(Nature 게재 / 스타 3.7k)** 스탠퍼드대 연구: 논문의 알고리즘, 코드, 데이터를 MCP 실행 도구로 자동 패키징하여 질문에 답하고 실험을 재현하는 대화형 가상 연구원 멀티에이전트 시스템 |

---

### 6. 💻 개발자 생산성, 보안 & MCP (DevTools & Security)
> 실무 취업 지원, 보안 모의해킹, 모바일 안드로이드 제어(Artemis), Computer-Use OS 플릿(CUA), SEO/NEO 최적화, 자동 배포, 주식 매매 MCP 및 로컬 LLM 추론

| 번호 | 스킬/프로젝트 | 유형 | 주요 용도 및 추천 사용 시점 |
| :---: | :--- | :---: | :--- |
| 99 | [usestrix/strix](https://github.com/usestrix/strix) | `[Security]` | **(스타 6.1만)** 진짜 침투 테스터처럼 내 웹앱의 취약점을 직접 모의해킹하고 보안 패치 제안 |
| 100 | [santifer/career-ops](https://github.com/santifer/career-ops) | `[Tool]` | **(스타 7.0만)** 로컬 CLI 기반 AI 구직 어시스턴트 (공고 평가 A~H 등급, 이력서 최적화) |
| 101 | [gugu9999gu/PC-CONTROL-MCP](https://github.com/gugu9999gu/PC-CONTROL-MCP) | `[MCP]` | AI 에이전트가 PC 마우스 클릭, 키보드 입력, 화면 캡처를 직접 수행하는 MCP 서버 |
| 102 | [google/artemis](https://github.com/google/artemis) | `[Agent/MCP]` | **[보관소 복제됨 / 스타 7.4k]** 구글 픽셀 팀의 안드로이드 모바일 자동화 & E2E 테스팅 AI. 자연어로 스마트폰 앱 제어, Antigravity 네이티브 MCP 연동 및 AndroidWorld 99%+ SOTA |
| 103 | [trycua/cua](https://github.com/trycua/cua) | `[Framework/OS]` | **(스타 2.6만)** Computer-Use 2.0을 지원하는 오픈소스 OS 드라이버, 크로스 OS(맥/윈도우/리눅스) 플릿 제어 및 벤치마크 프레임워크 |
| 104 | [leopard627/fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) | `[Skill/SEO]` | **[보관소 복제됨]** SEO, AEO, GEO, LLMO 및 네이버 검색(NEO)까지 사이트의 검색 가시성을 자동 진단·개선하는 AI 최적화 스킬 |
| 105 | [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | `[Agent/Trading]` | **(스타 2.2k)** Monad 블록체인 상에서 매 블록마다 AI가 온체인 거래 결정을 내리는 실시간 자율 트레이딩 에이전트 (Jev Trader 가이드) |
| 106 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | `[Tool/Career]` | **(스타 4.5만)** Claude Code 기반 로컬 구직 자동화 프레임워크. 채용 공고 스크래핑/분석, 맞춤 이력서(CV)·자기소개서 작성, 에이전트 검토, 인터뷰 대비, 연봉 벤치마킹까지 지원하는 14개 특화 명령어 (`/setup`, `/scrape`, `/apply`) |
| 107 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | `[Skill/Tool]` | 로컬 옵시디언(Obsidian) 지식 볼트와 AI 에이전트를 실시간 연동 |
| 108 | [alclssna33/codex_to_telegram](https://github.com/alclssna33/codex_to_telegram) | `[Tool]` | 긴 코딩 작업 완료 시 텔레그램으로 완료 알림 및 원격 명령어 전송 |
| 109 | [coder/code-server](https://github.com/coder/code-server) | `[Server]` | 웹 브라우저에서 원격으로 실행하는 풀 VS Code 환경 |
| 110 | [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) | `[Tool]` | M시리즈 맥북에서 RAM 2GB만으로 Gemma 4 모델 초고속 로컬 구동 |
| 111 | [goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant) | `[Library]` | 골드만삭스의 금융 파생상품 및 퀀트 리스크 분석 오픈소스 툴킷 |
| 112 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | `[Skill/Korean]` | **(Humanize KR v2.3.2)** 한국어 AI 글에서 번역투, 기계적 병렬 구조, 상투적 접속사를 찾아내 자연스러운 한국어 문체로 다듬어주는 Agent Skill |
| 113 | [blader/humanizer](https://github.com/blader/humanizer) | `[Skill/Writing]` | **(스타 5.4만)** AI 글의 반복적 리듬, 기계적 수사, 챗봇 상투어를 제거하고 작성자 본연의 목소리를 복원하는 글로벌 대표 De-AI 글쓰기 스킬 |
| 114 | [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | `[Skill/Writing]` | **(스타 3.0k)** 소설, 기술 문서, 릴리즈 노트 등 서사 구조와 장르 문체를 심층 분석하여 기계적인 AI 톤을 사람다운 유려한 필체로 복원하는 De-AI Writing Skill (Antigravity 네이티브 지원) |
| 115 | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | `[Skill/Writing]` | **(스타 1.9만)** 중국어 AI 글의 템플릿화된 상투구와 기계적 번역투를 정밀 제거하고 자연스러운 모국어 필체로 윤문하는 De-AI 스킬 |
| 116 | [undefined-ui/second-brain-os](https://github.com/undefined-ui/second-brain-os) | `[Skill/Notes]` | **(스타 1.0k)** 저장해 둔 글, 영상, 노트를 AI(Claude Code)가 옵시디언(Obsidian) 위키 및 자가 유지형 지식 베이스로 자동 구조화해 주는 세컨드 브레인 OS |
| 117 | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | `[Tool]` | GUI 작업 자동화를 위한 마우스 이동 및 매크로 제어 봇 |
| 118 | [Dongkyu-ES/persona-lightsim](https://github.com/Dongkyu-ES/persona-lightsim) | `[Simulation]` | 사용자 페르소나 행동 시뮬레이션 및 데이터 테스트 환경 |
| 119 | [jaeseok614/llm-gpu-checker-ko](https://github.com/jaeseok614/llm-gpu-checker-ko) | `[Tool]` | 모델 파라미터/양자화에 따른 로컬 GPU VRAM 요구량 실시간 계산기 |
| 120 | [leeryong/NELLA](https://github.com/leeryong/NELLA) | `[Tool]` | 한국어 자연어 분석 및 온톨로지 지식 추출 도구 |
| 121 | [reqover-labs/reqover](https://github.com/reqover-labs/reqover) | `[Tool]` | 스프링(Spring) 백엔드 요청 단위 런타임 테스트 커버리지 분석 |
| 122 | [LilMGenius/paperthin](https://github.com/LilMGenius/paperthin) | `[Tool]` | 프롬프트 토큰 압축 및 초경량 LLM 파이프라인 최적화 |
| 123 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | `[Tool]` | 작업 목적(코딩, 작문, 번역 등)에 가장 가성비 좋은 최적 모델 추천기 |
| 124 | [LilMGenius/polysona](https://github.com/LilMGenius/polysona) | `[Framework]` | 여러 가상 인격(페르소나) 간의 토론 및 협업 시뮬레이터 |
| 125 | [yazzang-homelab/colab-fleet](https://github.com/yazzang-homelab/colab-fleet) | `[Tool]` | 여러 구글 코랩 인스턴스를 하나의 클러스터처럼 묶어 원격 실행하는 툴 |
| 126 | [zulip/zulip](https://github.com/zulip/zulip) | `[Platform]` | 스레드 기반 대규모 팀 협업 오픈소스 커뮤니케이션 서버 |
| 127 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | `[Curated]` | **(스타 13.7만)** 개발자·데브옵스를 위한 무료 티어(Free tier) SaaS, PaaS, IaaS 클라우드 및 개발 인프라 서비스 총정리 |
| 128 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | `[Framework]` | **(스타 4.9만)** 홍콩대 개발: 모든 데스크톱/웹/GUI 소프트웨어를 에이전트 네이티브 CLI 도구로 변환하여 AI 제어권 부여 |
| 129 | [Shaivpidadi/FreeRideV3](https://github.com/Shaivpidadi/FreeRideV3) | `[Gateway]` | Groq, OpenRouter, NVIDIA NIM, Cloudflare AI 등 무료 AI 티어를 자동 페일오버로 묶는 로컬 OpenAI 호환 게이트웨이 |
| 130 | [supabase/mcp](https://github.com/supabase/mcp) | `[MCP]` | **(스타 2.9k)** SQL 없이 자연어 대화만으로 DB 생성, 스키마 마이그레이션, 테이블 관리 수행 |
| 131 | [upstash/context7](https://github.com/upstash/context7) | `[Platform/Docs]` | **(스타 6.2만)** 최신 공식 라이브러리 문서를 AI 코딩 어시스턴트에 실시간 주입하여 구버전 코드 생성 방지 |
| 132 | [oraios/serena](https://github.com/oraios/serena) | `[Tool/MCP]` | **Serena**: 단순 문자열 검색을 넘어 심볼/AST 단위 코드 참조와 안전한 크로스파일 리팩토링을 부여하는 IDE급 시맨틱 MCP |
| 133 | [trailofbits/skills](https://github.com/trailofbits/skills) | `[Skill/Security]` | **[보관소 복제됨 / 스타 7.2k]** 최고 권위 보안 연구소 Trail of Bits 공식 보안 플러그인 44개: 스마트 컨트랙트 감사, CodeQL 정적 분석, 취약점 탐지 |
| 134 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | `[Skill/Security]` | **(스타 3.3만)** MITRE ATT&CK, NIST CSF 2.0 등 6대 보안 프레임워크·29개 도메인에 매핑된 818개 AI 에이전트 사이버보안 스킬 팩 (`npx skills add`) |
| 135 | [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | `[Skill/Security]` | **(스타 6.3k)** 앤트로픽 공식 보안 리뷰 스킬 & GitHub Action (`/security-review`). 코드 변경 사항의 SQL 인젝션 등 보안 취약점 정밀 감사 |
| 136 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | `[Skill/Notes]` | **(스타 4.9만)** 옵시디언 대표(kepano)가 직접 만든 공식 에이전트 노트 스킬. Obsidian CLI, Markdown, Bases, JSON Canvas 완벽 제어 |
| 137 | [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | `[Engine/LLM]` | **(스타 8.7k)** GPU 0장·순수 C99 엔진(176KB)과 RAM 8.24GB만으로 2.78조 파라미터 초대형 모델(Kimi K3)을 단일 CPU에서 로컬 추론 구동 (디스크 1.7TB·AVX2 필요) |
| 138 | [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | `[Skill/Game]` | **(스타 4.9k)** Claude Code와 fal MCP를 연동하여 PC 게임 분석, 역공학, 3D/아트 생성, 인게임 테스트를 거쳐 게임 모드(Mod)를 전자동 제작하는 스킬 |
| 139 | [mikehasa/golive-skill](https://github.com/mikehasa/golive-skill) | `[Skill/Deploy]` | **(스타 1.2k)** AI가 개발한 웹 서비스의 호스팅(Vercel), DB(Supabase/Neon), 커스텀 도메인, 이메일, 결제(Stripe)까지 계획→승인→적용 단계로 자동 인프라 배포하는 론칭 스킬 |
| 140 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | `[Engine/LLM]` | **(스타 16.5k)** VRAM 12GB 일반 게이밍 PC에서 1,250억(125B) 파라미터 Qwen3.8-Flash-Next 모델을 로컬 구동(대화·코딩·이미지 인식 지원, 로컬 OpenAI/Anthropic 호환 API)하는 고속 로컬 추론 엔진 |
| 141 | [koreainvestment/open-trading-api](https://github.com/koreainvestment/open-trading-api) | `[MCP/Finance]` | **(스타 1.6k)** 한국투자증권(KIS) 공식 오픈 트레이딩 API: AI 주식 매매, 실시간 시세, 전략 백테스팅, LLM 퀀트 파이프라인을 지원하는 공식 전용 MCP 서버 및 예제 팩 |

---

### 7. 🔍 글로벌 스킬·MCP 통합 검색 허브 (Skill & MCP Hubs)
> 로컬 보관소에 없는 새로운 스킬·MCP·플러그인을 탐색하고 즉시 설치할 수 있는 글로벌 통합 디렉토리 및 레지스트리

| 번호 | 스킬/프로젝트 | 유형 | 주요 용도 및 추천 사용 시점 |
| :---: | :--- | :---: | :--- |
| 142 | [skills.sh](https://skills.sh/) | `[Skill Hub]` | **(스타 1.2만 / 스킬 9만 개)** `find-skills`로 가장 유명한 대표 스킬 허브. `npx skills add` 명령어 한 줄로 즉시 설치 지원 |
| 143 | [skillsmp.com](https://skillsmp.com/) | `[Skill DB]` | **(스킬 63만 개)** 최대 규모 스킬 데이터베이스 보유. 자연어 검색 매칭이 뛰어나 특수 도메인 스킬 탐색에 최적 |
| 144 | [vibeindex.ai](https://vibeindex.ai/) | `[All-in-One Hub]` | **(스킬 10만 / MCP 6천 / 플러그인 1.4만)** 스킬·MCP·플러그인을 한 번에 통합 검색할 수 있는 올인원 인덱스 |
| 145 | [smithery.ai](https://smithery.ai/) | `[MCP/Skill Hub]` | **(스킬 13만 / MCP 3천)** 스킬 및 MCP 서버의 실제 이용자 수와 품질 점수를 함께 제공하여 검증된 도구 선별에 유용 |

---

## 🚀 프로젝트에 스킬 가져오는 방법 (복사 가이드)

특정 프로젝트 폴더(예: `C:\dev\my-app`)에서 작업할 때 안티그래비티에게 이렇게 말씀하시면 됩니다:

```markdown
"내 skill-vault 색인표(skills-index.md)를 참고해서,
[스킬이름] 스킬을 현재 프로젝트 폴더의 .agents/skills/ 에 복사해서 세팅해줘."
```

이렇게 하면 전체 안티그래비티가 꼬이지 않고, **오직 해당 프로젝트 내에서만 100% 안전하게 동작**합니다.
