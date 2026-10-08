# ==============================================================================
# Antigravity Skill Vault & 1-2-3-4 Core Governance Installer (Windows PowerShell)
# ==============================================================================

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🛡️  Antigravity Skill Vault & 1-2-3-4 Core Rules Installer" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

$CurrentDir = $PSScriptRoot
$GeminiGlobalDir = Join-Path $HOME ".gemini"
$GlobalRulesFile = Join-Path $GeminiGlobalDir "GEMINI.md"

# 1. ~/.gemini 디렉토리 생성
if (-not (Test-Path $GeminiGlobalDir)) {
    New-Item -ItemType Directory -Path $GeminiGlobalDir -Force | Out-Null
    Write-Host "✔ 글로벌 설정 디렉토리 생성됨: $GeminiGlobalDir" -ForegroundColor Green
}

# 2. 글로벌 GEMINI.md 등록
$RulesContent = Get-Content (Join-Path $CurrentDir "GEMINI.md") -Raw
Set-Content -Path $GlobalRulesFile -Value $RulesContent -Encoding UTF8
Write-Host "✔ 1-2-3-4 코어 엔지니어링 규칙이 글로벌로 등록되었습니다: $GlobalRulesFile" -ForegroundColor Green

Write-Host ""
Write-Host "🎉 설치 완료!" -ForegroundColor Yellow
Write-Host "이제 이 PC의 어떤 프로젝트에서든 Antigravity를 실행하면 아래 4대 코어 규칙이 무조건 자동 적용됩니다:"
Write-Host "  1. Addy Osmani   : /spec, /plan 명세 & 계획 선행"
Write-Host "  2. Matt Pocock   : Zero-any 엄격한 타입 무결성 & 도메인 모델링"
Write-Host "  3. Ponytail      : YAGNI 70% 코드 삭감, 불필요한 의존성 0개"
Write-Host "  4. Claude Scaffold: 모듈형 클린 아키텍처"
Write-Host ""
Write-Host "📚 스킬 인덱스 위치: $CurrentDir\skills-index.md" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
