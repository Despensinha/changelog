import json

def load_releases(filepath):
    with open(filepath) as f:
        return json.load(f)

def main():
    front = load_releases("/tmp/front-releases.json")
    back = load_releases("/tmp/back-releases.json")

    lines = ["# Histórico de Atualizações (RAW - sem tradução)\n"]
    lines.append("> ⚠️ Este é o changelog bruto sem tradução. Defina ANTHROPIC_API_KEY para gerar a versão traduzida.\n\n")

    all_releases = []
    for r in front:
        all_releases.append({**r, "source": "Frontend"})
    for r in back:
        all_releases.append({**r, "source": "Backend"})

    # Ordena por data desc
    all_releases.sort(key=lambda x: x.get("date") or "", reverse=True)

    for r in all_releases:
        date = r["date"][:10] if r["date"] else "sem data"
        body = r["body"] or "(sem conteúdo)"
        lines.append(f"## [{r['source']}] {r['tag']} ({date})\n")
        lines.append(f"{body}\n\n")

    with open("CHANGELOG.md", "w") as f:
        f.write("\n".join(lines))

    print("   ✅ CHANGELOG.md (raw) gerado!")

if __name__ == "__main__":
    main()
