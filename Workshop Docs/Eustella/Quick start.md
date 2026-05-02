## Quick Start

1. Kloniraj repository: `git clone https://github.com/fakultet/docs-as-code.git`
2. Otvori u Obsidianu
3. Instaliraj preporučene pluginove
4. Kopiraj template iz `templates/` u svoj projekt
5. Piši u Markdownu
6. Commit & Push → automatski PDF

## Struktura

- `templates/` - Templatei za različite vrste dokumenata
- `projects/` - Aktivni projekti
- `docs/` - Dokumentacija i upute

## Workflow

1. Kreiraj branch: `git checkout -b feature/ime-projekta`
2. Piši dokumente u `projects/ime-projekta/src/`
3. Commitaj promjene
4. Otvori Pull Request za review
5. Nakon mergea, CI/CD gradi PDF

## Alati

- Obsidian - Editor
- Git - Version control
- Pandoc/Quarto - Konverzija u PDF
- GitHub Actions - Automatizacija