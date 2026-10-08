---
name: dream-rsi
description: >
  Google & Google DeepMind가 발표한 자가 개선(Recursive Self-Improvement) 프레임워크.
  탐색 이력(Discovery Tree) 자체를 완전한 리플레이 시뮬레이터로 활용하여,
  0의 실행 비용(Zero Execution Cost)으로 수천 개의 새 탐색 정책을 꿈꾸기(Dreaming)로 사전 평가 및 개선합니다.
---

# 🧠 Dream-RSI (Recursive Self-Improvement through Evolving Worlds)

> **Google & Google DeepMind & UMD & UVA 공식 연구**  
> "An agent must dream to recursively self-improve. History is the world it dreams in."

---

## 🌟 핵심 철학 및 개념

1. **이력(History)이 곧 시뮬레이터**:
   - 기존 에이전트는 새 탐색 정책을 평가하기 위해 비싼 온라인 환경에서 수천 번씩 실제로 실행해야 했습니다.
   - Dream-RSI는 이전 실행에서 생성된 탐색 트리(Discovery Tree)가 이미 완전한(Exact) 시뮬레이터임을 간파했습니다.
2. **0의 실행 비용으로 사전 검증 (Dreaming)**:
   - 수천 개의 정책 후보를 기존 트리 위에서 다른 순서/분기로 재배열(Replay)하여 0의 실행 비용으로 점수를 매깁니다.
   - 오프라인에서 검증된 최적의 정책만 선별하여 온라인에 배포합니다.
3. **진화하는 세계 (Evolving Worlds)**:
   - 새로 배포된 정책이 이전에 가보지 못한 새로운 탐색 트리를 기록하면, 이 트리가 다시 시뮬레이터 풀에 축적되어 지속적으로 자가 발전합니다.

---

## 📊 주요 벤치마크 성과
- **알고리즘 엔지니어링 (Lasso)**: SimpleTES 대비 탐색 에이전트 호출 162배 절감, 실행 시간 1.22배 단축
- **GPU 커널 엔지니어링 (KernelBench)**: VGG16, LayerNorm, ConvDiv, ConvMax 4개 커널 전 과제 성능 향상 (동일 예산 대비 2.09배 성능)
