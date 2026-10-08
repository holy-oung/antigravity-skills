# 🛡️ Antigravity Core Engineering Rules (1-2-3-4 Protocol)

All coding, architecture, and tool development in this workspace must strictly follow the **1-2-3-4 Core Engineering Protocol**:

1. **Pillar 1 (Addy Osmani)**: Never jump into code without stating a concise `/spec` and `/plan`. Clarify requirements and break down tasks first.
2. **Pillar 4 (Claude Scaffold)**: Maintain clean, structured modular architecture. Avoid monolithic single-file dumps where separation of concerns is needed.
3. **Pillar 2 (Matt Pocock)**: Enforce strict type-safety and domain modeling. Zero `any` policy. Define types and interfaces before writing implementation logic.
4. **Pillar 3 (Ponytail)**: Apply extreme YAGNI minimalism. Challenge speculative abstractions, choose standard libraries over npm/pip dependencies, and keep code 70% lighter.
5. **Skill Vault Gateway**: For specialized capabilities (HWP, Korean doc, 3D, SEO, scraping, agent memory), pull tools from the personal Skill Vault (`antigravity/skills` or `skills-index.md`) into `.agents/skills/` on-demand.
