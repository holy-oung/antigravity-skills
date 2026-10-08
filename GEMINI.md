# 🛡️ Antigravity Core Engineering Rules (1-2-3-4 Protocol)

All coding, architecture, and tool development in this workspace must strictly follow the **1-2-3-4 Core Engineering Protocol**:

1. **Pillar 1 (Addy Osmani)**: Never jump into code without stating a concise `/spec` and `/plan`. Clarify requirements and break down tasks first.
2. **Pillar 4 (Claude Scaffold)**: Maintain clean, structured modular architecture. Avoid monolithic single-file dumps where separation of concerns is needed.
3. **Pillar 2 (Matt Pocock)**: Enforce strict type-safety and domain modeling. Zero `any` policy. Define types and interfaces before writing implementation logic.
4. **Pillar 3 (Ponytail)**: Apply extreme YAGNI minimalism. Challenge speculative abstractions, choose standard libraries over npm/pip dependencies, and keep code 70% lighter.
5. **JIT Skill Butler Gateway**: For specialized domains (HWP doc, Anti-slop UI, video/scraping, security audit, SEO, agent memory), the Butler intercepts with *"잠깐! ✋ [스킬명]을 장착합니다"*. Lightweight tasks unmount after single-turn execution; heavy/multi-step tasks run in an ephemeral isolated Subagent to ensure zero main context contamination. Everyday casual questions remain silent.
