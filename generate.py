import json
import os
import sys

import httpx

def load_releases(filepath):
    with open(filepath) as f:
        return json.load(f)

def build_prompt(front_releases, back_releases):
    releases_text = "## Frontend Releases\n"
    for r in front_releases[:10]:
        date = r["date"][:10] if r["date"] else "sem data"
        body = r["body"] or "(sem conteúdo)"
        releases_text += f"\n### {r['tag']} ({date})\n{body}\n"

    releases_text += "\n## Backend Releases\n"
    for r in back_releases[:10]:
        date = r["date"][:10] if r["date"] else "sem data"
        body = r["body"] or "(sem conteúdo)"
        releases_text += f"\n### {r['tag']} ({date})\n{body}\n"

    return f"""Você é um redator de changelog para a plataforma Despensinha.
Receba os changelogs técnicos do frontend e backend abaixo e gere UM changelog
unificado em português brasileiro, voltado para usuários finais.

Regras:
- Agrupe por data (mais recente primeiro), unificando front+back do mesmo período
- Use estas categorias quando houver itens: 🚀 Novidades, ✨ Melhorias, 🐛 Correções
- Ignore completamente: refatorações internas, bumps de dependência, mudanças de CI/CD, chores
- Linguagem simples e amigável, sem jargão técnico
- Se um item técnico não tiver impacto visível pro usuário, não inclua
- Formato Markdown limpo
- Título do documento: "# Histórico de Atualizações"
- Cada grupo de data deve ser um ## com formato "## DD/MM/AAAA"
- Se não houver nenhuma mudança relevante pro usuário em uma release, pule ela

Changelogs técnicos:

{releases_text}"""

def generate_changelog(prompt):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY não encontrada no ambiente")
        sys.exit(1)

    print("   Chamando Claude API (claude-sonnet-4-20250514)...")
    resp = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "content-type": "application/json",
            "anthropic-version": "2023-06-01",
        },
        json={
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=120,
    )

    if resp.status_code != 200:
        print(f"❌ Erro na API: {resp.status_code}")
        print(resp.text)
        sys.exit(1)

    data = resp.json()
    return data["content"][0]["text"]

def main():
    front = load_releases("/tmp/front-releases.json")
    back = load_releases("/tmp/back-releases.json")

    if not front and not back:
        print("⚠️  Nenhuma release encontrada nos repos.")
        sys.exit(0)

    prompt = build_prompt(front, back)

    # Salva o prompt pra debug
    with open("debug-prompt.txt", "w") as f:
        f.write(prompt)
    print("   Prompt salvo em debug-prompt.txt")

    md = generate_changelog(prompt)

    with open("CHANGELOG.md", "w") as f:
        f.write(md)

    print("   ✅ CHANGELOG.md gerado com sucesso!")

if __name__ == "__main__":
    main()
