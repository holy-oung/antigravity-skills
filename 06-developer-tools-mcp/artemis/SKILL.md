---
name: artemis
description: >
  Google 공식 Pixel Test Engineering 팀이 공개한 안드로이드 모바일 기기 E2E 자동화 및 테스트 AI 에이전트.
  자연어 명령으로 실제 안드로이드 폰/에뮬레이터를 사람처럼 터치, 스와이프, 텍스트 입력하여 앱을 제어하고 테스트합니다.
  Antigravity 네이티브 MCP 서버(mobile_run_task, mobile_diagnose 등)를 지원하며,
  AndroidWorld 벤치마크 99%+ 달성 SOTA 모바일 에이전트입니다.
---

# 📱 ARTEMIS (Android Autonomous Testing & Interaction)

> **Google Pixel Test Engineering 팀 공식 오픈소스** (GitHub ★7.4k+)
> "사람보다 휴대폰을 더 잘 쓰는 AI" (조코딩 유튜브 쇼츠 소개)

---

## 🌟 핵심 특징

1. **사람처럼 앱 제어**: 화면을 보고 직접 클릭, 스크롤, 입력하며 여러 앱을 넘나드는 크로스 앱 자동화 수행.
2. **듀얼 실행 엔진**:
   - **Flash Mode**: 1단계당 3~5초의 초고속 반응형 단일 루프 (경량 UI 작업).
   - **Pro Mode**: Planner -> Operator -> Checker -> Outputter 4단계 멀티에이전트 폐루프 (장기 탐색 및 엄격한 검증).
3. **AndroidWorld 99%+ 성공률**: 100개 이상의 복합 모바일 작업 벤치마크에서 SOTA 달성.
4. **Antigravity 네이티브 MCP 지원**:
   - `mobile_run_task`: 자연어로 모바일 기기에 작업 지시
   - `mobile_manage_task`: 작업 중지, 일시정지, 재개
   - `mobile_get_device_state`: 연결된 디바이스 상태 및 화면 확인
   - `mobile_inspect_trace`: 실행 로그 및 단계별 스크린샷 추적
   - `mobile_diagnose`: ADB 연결, 키 인증, 가상기기(AVD) 자가 진단 및 자동 복구

---

## 🛠️ Antigravity 연동 및 실행 방법

### 1. 전제 조건
- PC에 안드로이드 스마트폰을 USB로 연결하고 **USB 디버깅** 활성화 (또는 Android Studio 에뮬레이터 실행)
- `adb devices` 명령어로 기기 인식 확인

### 2. 실행 (Windows)
```powershell
cd 06-developer-tools-mcp\artemis
.\start.bat
```
또는 uv 명령어 사용:
```powershell
uv run artemis mcp --install antigravity
```

### 3. Antigravity MCP 설정 (~/.gemini/jetski/mcp_config.json)
```json
{
  "mcpServers": {
    "artemis": {
      "command": "python",
      "args": ["-m", "mcp_server"],
      "cwd": "C:\\Users\\Han\\.gemini\\skill-vault\\06-developer-tools-mcp\\artemis",
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```
