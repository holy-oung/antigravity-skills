# 🛡️ Antigravity Core Engineering Rules (1-2-3-4 Protocol)

All AI-assisted coding, modifications, and code suggestions in this repository must strictly adhere to the following 1-2-3-4 Core Engineering Protocol:

1. **Pillar 1 (Addy Osmani - Spec & Plan First)**:
   - Always state a concise `/spec` and `/plan` before writing or modifying code.
   - Clarify edge cases, constraints, and requirements first.

2. **Pillar 4 (Claude Scaffold - Clean Architecture)**:
   - Maintain modular structure and clear separation of concerns.
   - Avoid monolithic file dumps. Keep functions and modules focused.

3. **Pillar 2 (Matt Pocock - Strict Type Safety & Domain Modeling)**:
   - Zero `any` policy. Provide strict type hints (Python `typing`, TypeScript strict).
   - Define domain models and data interfaces before implementing execution logic.

4. **Pillar 3 (Ponytail - YAGNI Minimalism)**:
   - Enforce extreme YAGNI (You Aren't Gonna Need It). Keep solutions as simple and short as possible.
   - Prefer standard library utilities over third-party dependencies.
   - Aim for 70% lighter code, cutting speculative abstractions and boilerplate.

5. **Skill Vault Integration**:
   - For specialized capabilities (scraping, automation, browser testing, Korean doc, 3D, SEO), pull proven patterns from the personal Skill Vault.
