#!/usr/bin/env bash
# ==============================================================================
# Antigravity Skill Vault & 1-2-3-4 Core Governance Installer (macOS / Linux)
# ==============================================================================

set -e

echo "============================================================"
echo "🛡️  Antigravity Skill Vault & 1-2-3-4 Core Rules Installer"
echo "============================================================"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GEMINI_GLOBAL_DIR="$HOME/.gemini"
GLOBAL_RULES_FILE="$GEMINI_GLOBAL_DIR/GEMINI.md"

mkdir -p "$GEMINI_GLOBAL_DIR"
cp "$SCRIPT_DIR/GEMINI.md" "$GLOBAL_RULES_FILE"

echo "✔ 1-2-3-4 Core Engineering Protocol successfully registered to: $GLOBAL_RULES_FILE"
echo ""
echo "🎉 Setup Complete!"
echo "Any project opened with Antigravity on this machine will now enforce:"
echo "  1. Addy Osmani   : Specification & Plan first (/spec, /plan)"
echo "  2. Matt Pocock   : Zero-any strict domain modeling & type safety"
echo "  3. Ponytail      : YAGNI minimalism, 70% lighter code, stdlib first"
echo "  4. Claude Scaffold: Modular clean architecture"
echo ""
echo "📚 Skill Vault Index: $SCRIPT_DIR/skills-index.md"
echo "============================================================"
