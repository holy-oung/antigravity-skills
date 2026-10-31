# 🛡️ Antigravity Core Engineering Rules (1-2-3-4 Protocol)

All coding, architecture, and tool development in this workspace must strictly follow the **1-2-3-4 Core Engineering Protocol**:

1. **Pillar 1 (Addy Osmani)**: Never jump into code without stating a concise `/spec` and `/plan`. Clarify requirements and break down tasks first.
2. **Pillar 4 (Claude Scaffold)**: Maintain clean, structured modular architecture. Avoid monolithic single-file dumps where separation of concerns is needed.
3. **Pillar 2 (Matt Pocock)**: Enforce strict type-safety and domain modeling. Zero `any` policy. Define types and interfaces before writing implementation logic.
4. **Pillar 3 (Ponytail)**: Apply extreme YAGNI minimalism. Challenge speculative abstractions, choose standard libraries over npm/pip dependencies, and keep code 70% lighter.
5. **Skill Vault Gateway**: For specialized capabilities (HWP, Korean doc, 3D, SEO, scraping, agent memory), pull tools from the personal Skill Vault (`antigravity/skills`, see `antigravity/skills-index.md`) into `.agents/skills/` on-demand.

## 📥 새 스킬(캡처·링크) 유입 시 등록 규칙
- **북마크만**: `skills/catalog.md`에 추가
- **실제로 clone했으면**: `catalog.md` 표시(`**[보관소 복제됨]**`) + 루트 `skills-index.md` 표에 한 줄 추가
- **표 중복 금지**: `skill-vault/SKILL.md`에는 표를 다시 만들지 않는다 (루트 `skills-index.md` 단일 진실 공급원 유지)

