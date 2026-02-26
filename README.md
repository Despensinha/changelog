# Despensinha - Changelog Público

Changelog unificado e traduzido automaticamente para os usuários da plataforma.

## Como funciona

1. Uma release é publicada no repo de **frontend** ou **backend**
2. O workflow `notify-changelog` dispara um evento para este repo
3. O workflow `update-changelog` busca todas as releases dos dois repos
4. A API do Claude traduz e unifica o changelog em português
5. O `CHANGELOG.md` é atualizado automaticamente

## Setup

### 1. Criar este repo

```bash
# Crie o repo Despensinha/despensinha-changelog (público)
# Copie o workflow para .github/workflows/update-changelog.yml
```

### 2. Configurar secrets neste repo

| Secret | Descrição |
|--------|-----------|
| `ANTHROPIC_API_KEY` | Chave da API do Claude |

### 3. Configurar secrets nos repos de front e back

| Secret | Descrição |
|--------|-----------|
| `CHANGELOG_PAT` | PAT com permissão `repo` (para disparar o workflow neste repo) |

Adicione o workflow `notify-changelog.yml` em ambos os repos:
- `Despensinha/despensinha-admin-app/.github/workflows/notify-changelog.yml`
- `Despensinha/despensinha-main-api-modular/.github/workflows/notify-changelog.yml`

### 4. Testar manualmente

Vá em **Actions → Update Changelog → Run workflow** neste repo para testar.

## Teste local

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
chmod +x test-local.sh
./test-local.sh
```

## Uso no frontend

```typescript
const CHANGELOG_URL = 'https://raw.githubusercontent.com/Despensinha/despensinha-changelog/main/CHANGELOG.md';

const res = await fetch(CHANGELOG_URL);
const markdown = await res.text();
// Renderize com react-markdown, marked, etc.
```
