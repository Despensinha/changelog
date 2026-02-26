#!/bin/bash
set -e

# =============================================================
# Teste local de geração do changelog unificado
#
# Pré-requisitos:
#   - gh CLI instalado e autenticado (gh auth login)
#   - ANTHROPIC_API_KEY exportada no ambiente
#   - Python 3 com httpx (pip install httpx)
#
# Uso:
#   export ANTHROPIC_API_KEY="sk-ant-..."
#   chmod +x test-local.sh
#   ./test-local.sh
# =============================================================

FRONT_REPO="Despensinha/despensinha-admin-app"
BACK_REPO="Despensinha/despensinha-main-api-modular"
OUTPUT_FILE="CHANGELOG.md"

echo "🔍 Buscando releases do backend ($BACK_REPO)..."
gh api "repos/$BACK_REPO/releases?per_page=20" \
  --jq '[.[] | {tag: .tag_name, date: .published_at, body: .body}]' > /tmp/back-releases.json

echo "🔍 Buscando releases do frontend ($FRONT_REPO)..."
gh api "repos/$FRONT_REPO/releases?per_page=20" \
  --jq '[.[] | {tag: .tag_name, date: .published_at, body: .body}]' > /tmp/front-releases.json

echo ""
echo "📋 Releases encontradas:"
echo "   Backend:  $(cat /tmp/back-releases.json | python3 -c "import sys,json; print(len(json.load(sys.stdin)))")"
echo "   Frontend: $(cat /tmp/front-releases.json | python3 -c "import sys,json; print(len(json.load(sys.stdin)))")"
echo ""

# Mostra preview das releases encontradas
echo "--- Preview Backend ---"
cat /tmp/back-releases.json | python3 -c "
import sys, json
releases = json.load(sys.stdin)
for r in releases[:3]:
    print(f\"  {r['tag']} ({r['date'][:10] if r['date'] else 'sem data'})\")"
echo ""

echo "--- Preview Frontend ---"
cat /tmp/front-releases.json | python3 -c "
import sys, json
releases = json.load(sys.stdin)
for r in releases[:3]:
    print(f\"  {r['tag']} ({r['date'][:10] if r['date'] else 'sem data'})\")"
echo ""

if [ -z "$ANTHROPIC_API_KEY" ]; then
  echo "⚠️  ANTHROPIC_API_KEY não definida. Gerando changelog SEM tradução (raw)..."
  python3 generate-raw.py
else
  echo "🤖 Gerando changelog traduzido via Claude API..."
  python3 generate.py
fi

echo ""
echo "✅ Arquivo gerado: $OUTPUT_FILE"
echo ""
echo "--- Primeiras 50 linhas ---"
head -50 "$OUTPUT_FILE"
