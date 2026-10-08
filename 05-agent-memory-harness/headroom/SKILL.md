---
name: headroom
description: >
  코딩 에이전트 및 RAG 파이프라인의 토큰 소모를 60~95% 극적으로 압축하는 지능형 MCP 서버 및 프록시.
  도구 실행 결과, 대규모 로그, JSON 데이터, 파일 및 검색 청크를 LLM에 전달하기 직전에 핵심 정보 손실 없이 초고속 압축하여
  컨텍스트 윈도우 오버플로우를 방지하고 API 비용을 대폭 절감합니다.
---

# 🚀 Headroom (LLM Token Compression MCP & Proxy)

> **GitHub ★73.6k+**  
> "Compress tool outputs, logs, files, and RAG chunks before they reach the LLM."

---

## 🌟 핵심 특징
1. **압도적인 토큰 압축률**:
   - JSON 데이터: 60% ~ 95% 토큰 절감
   - 코딩 에이전트 툴 출력 및 로그: 평균 20% ~ 40% 절감
2. **손실 없는 시맨틱 압축**:
   - 단순 요약이 아니라 구조적 스키마와 핵심 키 값을 온전하게 유지하며 군더더기 메타데이터만 지능형 압축
3. **네이티브 MCP 서버 & 투명 프록시 지원**:
   - Antigravity, Claude Code, Cursor 등 모든 에이전트와 MCP 프로토콜로 직접 연동
