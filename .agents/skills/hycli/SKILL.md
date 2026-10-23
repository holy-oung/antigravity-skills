---
name: hycli
description: >
  임의의 웹사이트를 타입 안전한 CLI 및 MCP 도구 세트로 변환하는 Hycli 공식 스킬.
  사용자가 '웹사이트 도구화', '웹사이트 CLI 변환', '웹사이트 자동화', 'Hycli', 'hycli'를 언급하거나
  브라우저 로그인 세션을 재활용하여 웹사이트의 Read/Write 작업을 자동화하고자 할 때 사용합니다.
---

# 🌐 Hycli (Turn Any Website into Typed CLI & MCP)

Hycli는 임의의 웹사이트 URL을 입력받아 3단계 AI 워커가 문서(Docs), 프론트엔드 번들, 브라우저 네트워크 트래픽을 분석하여 타입이 완벽히 정의된 **CLI 및 MCP(Model Context Protocol) 서버**로 자동 변환해주는 네이티브 오픈소스 엔진입니다.

* **GitHub 공식 저장소**: [https://github.com/Hybirdss/Hycli](https://github.com/Hybirdss/Hycli)
* **대시보드 로컬 URL**: `http://127.0.0.1:4318`
* **주요 특징**:
  - **Zero Cookie Leaks**: 브라우저(Chrome, Edge, Whale 등)의 로그인 세션을 로컬 암호화 볼트에만 보관하며 LLM에게 원시 쿠키를 일절 노출하지 않음
  - **안전한 쓰기 통제(Safe Write Gate)**: 초기 셋업 시 계정 변조 0건 보장, 쓰기(Write) 작업 실행 전 반드시 사용자 승인 필요 (`hycli writes <site> allow`)
  - **단일 바이너리(Rust)**: Node.js나 Rust 컴파일 환경 없이도 단일 바이너리로 CLI, 로컬 대시보드, MCP 서버 내장 구동

---

## ⚡ 빠른 시작 (30-Second Quickstart)

```bash
# 1. 대상 웹사이트 준비 (의도 전달, Read/Write 액션 추출, 계정 변조 없음)
hycli prepare https://your-website.example --intent "Search posts, save drafts, and publish articles"

# 2. 준비된 액션 및 워크플로우 확인
hycli describe your-website

# 3. 안전한 읽기(Read) 작업 즉시 실행
hycli your-website search-posts --query "release notes"

# 4. 쓰기(Write) 권한 승인 후 생성/수정/삭제 작업 실행
hycli writes your-website allow
hycli your-website create-draft --title "Hello from Hycli" --body "Automated from my terminal."
```

---

## 🔌 Antigravity & AI 에이전트 MCP 연동 설정

Antigravity, Claude Code, Cursor, Windsurf 등의 에이전트 환경에서 Hycli를 MCP 서버로 직접 연동할 수 있습니다.

### MCP 설정 (`mcp.json` 또는 에이전트 설정)
```json
{
  "mcpServers": {
    "hycli": {
      "command": "hycli",
      "args": ["mcp"]
    }
  }
}
```

### 자연어 프롬프트 예시
> *"Hycli를 사용해서 `https://example.com` 사이트를 분석해줘. 어떤 액션들을 쓸 수 있는지 목록을 보여주고, 새 글 초안을 작성해줘."*

---

## 🛠️ 핵심 명령어 가이드

| 명령어 | 설명 | 예시 |
| :--- | :--- | :--- |
| `hycli open` | Hycli 로컬 웹 대시보드 실행 (`http://127.0.0.1:4318`) | `hycli open` |
| `hycli prepare <URL> --intent "<목적>"` | 웹사이트를 분석하여 CLI/MCP 액션 세트 생성 | `hycli prepare https://velog.io --intent "글 목록 조회 및 포스팅"` |
| `hycli describe <site>` | 해당 사이트에서 사용 가능한 액션 스키마 열람 | `hycli describe velog` |
| `hycli <site> <action> --help` | 특정 액션의 입력 파라미터 확인 | `hycli velog create-draft --help` |
| `hycli <site> <action> [인자]` | 액션 직접 실행 | `hycli velog search-posts --query "React"` |
| `hycli writes <site> allow` | 해당 사이트에 대한 쓰기/변경 액션 실행 권한 활성화 | `hycli writes velog allow` |
| `hycli check <site>` | 저장된 액션 상태 점검 (로그아웃/사이트 변경 감지) | `hycli check velog` |
| `hycli request <site> "<추가기능>"` | 기존 등록 사이트에 새로운 액션 확장/추가 분석 | `hycli request velog "태그별 통계 조회 기능 추가"` |
| `hycli accounts --site <site>` | 연결된 로컬 계정 목록 확인 | `hycli accounts --site velog` |

---

## 🛡️ 에이전트 거버넌스 & 안전 수칙

1. **쓰기(Write) 작업 사전 질문 필수**:
   - 웹사이트 CLI는 기본적으로 `writes: false` 상태로 시작됩니다.
   - 쓰기 액션을 처음 수행하기 전, 에이전트는 **반드시 사용자에게 명시적으로 확인**("`SITE` 사이트에 대한 쓰기 권한을 승인하시겠습니까?")을 구해야 합니다.
   - 사용자가 승인한 후에만 `hycli writes SITE allow`를 실행합니다.
2. **불확실한 결과 재시도 금지**:
   - 쓰기 작업 중 `action_outcome_unknown` 오류가 발생한 경우, 서버에 이미 반영되었을 수 있으므로 즉시 재시도하지 말고 먼저 `hycli check` 또는 사이트 상태 조회를 수행합니다.
3. **자격 증명 비노출 원칙**:
   - 대화창(채팅)에 쿠키, 세션 토큰, 비밀번호 입력을 절대 요구하지 않습니다.
   - 세션 연동은 Hycli 대시보드의 **Accounts → Connect an account** 또는 로컬 브라우저 세션 자동 감지를 통해서만 처리합니다.
4. **다운로드 파일 목록 및 목적 안내**:
   - 파일 다운로드 액션 완료 후, 로컬 경로(`local_path`), 파일명, MIME 타입, 바이트 수, 목적을 사용자에게 명확히 보고합니다.
