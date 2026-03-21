import json
import os
import re
from datetime import datetime

CHANGELOG_FILE = "CHANGELOG.md"
TITLE_LINE = "# Histórico de Atualizações (RAW - sem tradução)"
WARNING_LINE = "> ⚠️ Este é o changelog bruto sem tradução. Defina ANTHROPIC_API_KEY para gerar a versão traduzida.\n"


def load_releases(filepath):
    with open(filepath) as f:
        return json.load(f)


def parse_last_update_date(changelog_path):
    """Extrai a data mais recente do CHANGELOG.md existente."""
    if not os.path.exists(changelog_path):
        return None
    with open(changelog_path) as f:
        for line in f:
            # Formato raw: ## [Frontend] v1.0.0 (2026-03-20)
            m = re.match(r"^## \[.+\] .+ \((\d{4}-\d{2}-\d{2})\)", line)
            if m:
                return datetime.strptime(m.group(1), "%Y-%m-%d")
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


def read_existing_entries(changelog_path):
    """Lê as entradas existentes do changelog, sem título e warning."""
    if not os.path.exists(changelog_path):
        return ""
    with open(changelog_path) as f:
        content = f.read()
    # Remove título e warning
    content = re.sub(r"^# Histórico de Atualizações.*\n*", "", content)
    content = re.sub(r"^> ⚠️.*\n*", "", content)
    return content.strip()


def main():
    front = load_releases("/tmp/front-releases.json")
    back = load_releases("/tmp/back-releases.json")

    last_date = parse_last_update_date(CHANGELOG_FILE)
    if last_date:
        print(f"   Última atualização no changelog: {last_date.strftime('%Y-%m-%d')}")

    front_new = filter_new_releases(front, last_date)
    back_new = filter_new_releases(back, last_date)

    all_new = []
    for r in front_new:
        all_new.append({**r, "source": "Frontend"})
    for r in back_new:
        all_new.append({**r, "source": "Backend"})

    print(f"   Releases novas: {len(front_new)} frontend, {len(back_new)} backend")

    if not all_new:
        print("   ✅ Changelog já está atualizado, nenhuma release nova.")
        return

    # Ordena por data desc
    all_new.sort(key=lambda x: x.get("date") or "", reverse=True)

    new_lines = []
    for r in all_new:
        date = r["date"][:10] if r["date"] else "sem data"
        body = r["body"] or "(sem conteúdo)"
        new_lines.append(f"## [{r['source']}] {r['tag']} ({date})\n")
        new_lines.append(f"{body}\n")

    new_entries = "\n".join(new_lines).strip()
    existing = read_existing_entries(CHANGELOG_FILE)

    with open(CHANGELOG_FILE, "w") as f:
        f.write(f"{TITLE_LINE}\n\n{WARNING_LINE}\n")
        f.write(new_entries)
        if existing:
            f.write(f"\n\n{existing}")
        f.write("\n")

    print("   ✅ CHANGELOG.md (raw) atualizado!")


if __name__ == "__main__":
    main()
