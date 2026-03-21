import json
import os
import re
import sys
from datetime import datetime

import httpx

CHANGELOG_FILE = "CHANGELOG.md"
TITLE_LINE = "# Histórico de Atualizações"


def load_releases(filepath):
    with open(filepath) as f:
        return json.load(f)


def parse_last_update_date(changelog_path):
    """Extrai a data mais recente do CHANGELOG.md existente (formato ## DD/MM/AAAA)."""
    if not os.path.exists(changelog_path):
        return None
    with open(changelog_path) as f:
        for line in f:
            m = re.match(r"^## (\d{2}/\d{2}/\d{4})", line)
            if m:
                return datetime.strptime(m.group(1), "%d/%m/%Y")
    return None


def filter_new_releases(releases, since_date):
    """Retorna apenas releases publicadas após since_date."""
    if since_date is None:
        return releases
    new = []
    for r in releases:
        if not r.get("date"):
            continue
        release_date = datetime.fromisoformat(r["date"].replace("Z", "+00:00")).replace(tzinfo=None)
        if release_date > since_date:
            new.append(r)
    return new


def read_existing_content(changelog_path):
    """Lê o conteúdo existente do changelog, sem o título."""
    if not os.path.exists(changelog_path):
        return ""
    with open(changelog_path) as f:
        content = f.read()
    # Remove o título para poder concatenar depois
    content = re.sub(r"^# Histórico de Atualizações\s*\n*", "", content)
    return content.strip()


def build_prompt(front_releases, back_releases):
    releases_text = "## Frontend Releases\n"
    for r in front_releases:
        date = r["date"][:10] if r["date"] else "sem data"
        body = r["body"] or "(sem conteúdo)"
        releases_text += f"\n### {r['tag']} ({date})\n{body}\n"

    releases_text += "\n## Backend Releases\n"
    for r in back_releases:
        date = r["date"][:10] if r["date"] else "sem data"
        body = r["body"] or "(sem conteúdo)"
        releases_text += f"\n### {r['tag']} ({date})\n{body}\n"

    return f"""Você é um redator de changelog para a plataforma Despensinha.
Receba os changelogs técnicos do frontend e backend abaixo e gere APENAS as novas
entradas de changelog em português brasileiro, voltado para usuários finais.

Regras:
- Agrupe por data (mais recente primeiro), unificando front+back do mesmo período
- Use estas categorias quando houver itens: 🚀 Novidades, ✨ Melhorias, 🐛 Correções
- Ignore completamente: refatorações internas, bumps de dependência, mudanças de CI/CD, chores
- Linguagem simples e amigável, sem jargão técnico
- Se um item técnico não tiver impacto visível pro usuário, não inclua
- Formato Markdown limpo
- NÃO inclua título "# Histórico de Atualizações" — retorne apenas as entradas
- Cada grupo de data deve ser um ## com formato "## DD/MM/AAAA"
- Se não houver nenhuma mudança relevante pro usuário em uma release, pule ela

Changelogs técnicos:

{releases_text}"""


def call_claude(prompt):
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

    # Descobre a data da última atualização no changelog existente
    last_date = parse_last_update_date(CHANGELOG_FILE)
    if last_date:
        print(f"   Última atualização no changelog: {last_date.strftime('%d/%m/%Y')}")

    # Filtra apenas releases novas
    front_new = filter_new_releases(front, last_date)
    back_new = filter_new_releases(back, last_date)

    total_new = len(front_new) + len(back_new)
    print(f"   Releases novas: {len(front_new)} frontend, {len(back_new)} backend")

    if total_new == 0:
        print("   ✅ Changelog já está atualizado, nenhuma release nova.")
        sys.exit(0)

    prompt = build_prompt(front_new, back_new)

    # Salva o prompt pra debug
    with open("debug-prompt.txt", "w") as f:
        f.write(prompt)
    print("   Prompt salvo em debug-prompt.txt")

    new_entries = call_claude(prompt).strip()

    # Lê o conteúdo existente e concatena
    existing = read_existing_content(CHANGELOG_FILE)

    with open(CHANGELOG_FILE, "w") as f:
        f.write(f"{TITLE_LINE}\n\n")
        f.write(new_entries)
        if existing:
            f.write(f"\n\n{existing}")
        f.write("\n")

    print("   ✅ CHANGELOG.md atualizado com sucesso!")


if __name__ == "__main__":
    main()
