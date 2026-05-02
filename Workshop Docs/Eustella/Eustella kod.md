## 1. Repository Struktura

```
docs-as-code-fakultet/
├── .github/
│   └── workflows/
│       ├── build-pdf.yml          # CI/CD za automatski PDF build
│       └── spell-check.yml        # Provjera pravopisa
├── templates/
│   ├── eu-proposal/
│   │   ├── template.md            # Markdown template
│   │   ├── template.tex           # LaTeX template za Pandoc
│   │   ├── csl/                   # Citation styles
│   │   │   └── vancouver.csl
│   │   └── pandoc.yml             # Pandoc konfiguracija
│   ├── scientific-paper/
│   │   ├── template.md
│   │   ├── template.tex
│   │   └── pandoc.yml
│   └── project-documentation/
│       ├── template.md
│       └── pandoc.yml
├── projects/
│   └── example-eu-proposal/
│       ├── src/
│       │   ├── 00-abstract.md
│       │   ├── 01-introduction.md
│       │   ├── 02-objectives.md
│       │   ├── 03-methodology.md
│       │   ├── 04-work-packages.md
│       │   ├── 05-budget.md
│       │   ├── 06-team.md
│       │   └── references.bib
│       ├── assets/
│       │   ├── figures/
│       │   ├── tables/
│       │   └── diagrams/
│       ├── output/
│       │   └── (auto-generated PDF)
│       └── config.yml
├── docs/
│   ├── setup-guide.md             # Upute za postavku
│   ├── workflow-guide.md          # Timski rad workflow
│   └── troubleshooting.md
├── .gitignore
├── README.md
└── quarto.yml                     # Quarto konfiguracija (ako koristiš Quarto)
```

---

## 2. GitHub Actions Workflow (`build-pdf.yml`)

```yaml
name: Build PDF

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  build-pdf:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Install Pandoc
        run: |
          sudo apt-get update
          sudo apt-get install -y pandoc pandoc-latex
      
      - name: Install LaTeX
        run: |
          sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-xetex
      
      - name: Build EU Proposal PDF
        run: |
          pandoc projects/example-eu-proposal/src/*.md \
            --bibliography=projects/example-eu-proposal/src/references.bib \
            --csl=templates/eu-proposal/csl/vancouver.csl \
            --template=templates/eu-proposal/template.tex \
            --output=projects/example-eu-proposal/output/proposal.pdf \
            --pdf-engine=xelatex
      
      - name: Upload PDF Artifact
        uses: actions/upload-artifact@v4
        with:
          name: proposal-pdf
          path: projects/example-eu-proposal/output/proposal.pdf
```

---

## 3. Template za EU Pripravu (`templates/eu-proposal/template.md`)

```markdown
---
title: "Naziv Projekta"
subtitle: "EU Proposal"
author:
  - Ime Prezime¹
  - Ime Prezime²
affiliations:
  - "¹Građevinski fakultet, Sveučilište u Zagrebu"
  - "²Institut XYZ"
date: "{{ date() }}"
grant_number: "HORIZON-CL4-2024-XXX"
budget: "€ 2,500,000"
duration: "36 months"
---

## Sažetak

<!-- 300 riječi max -->

## 1. Uvod

### 1.1 Kontekst

### 1.2 Problem

### 1.3 Ciljevi

## 2. Metodologija

## 3. Radni paketi

| WP | Naziv | Voditelj | Trajanje (mjeseci) |
|----|-------|----------|-------------------|
| WP1 | Management | Partner 1 | 1-36 |
| WP2 | Research | Partner 2 | 1-18 |

## 4. Proračun

## 5. Tim

## Reference
```

---

## 4. Pandoc Konfiguracija (`templates/eu-proposal/pandoc.yml`)

```yaml
input-format: markdown
output-format: pdf
pdf-engine: xelatex
template: template.tex
csl: csl/vancouver.csl
bibliography: references.bib
metadata-file: config.yml
variables:
  geometry: margin=2.5cm
  fontsize: 11pt
  mainfont: Arial
  line-spacing: 1.5
toc: true
toc-depth: 3
number-sections: true
```

---

## 5. Quarto Konfiguracija (`quarto.yml`)

```yaml
project:
  type: book
  output-dir: output

book:
  title: "EU Proposal Template"
  author: "Građevinski fakultet"
  chapters:
    - src/00-abstract.md
    - src/01-introduction.md
    - src/02-objectives.md
    - src/03-methodology.md
    - src/04-work-packages.md
    - src/05-budget.md
    - src/06-team.md

format:
  pdf:
    documentclass: article
    papersize: a4
    fontsize: 11pt
    geometry: margin=2.5cm
    mainfont: Arial
    toc: true
    number-sections: true
    cite-method: natbib
  docx:
    toc: true
    reference-doc: templates/eu-proposal-reference.docx
```

---

## 6. Obsidian Postavke

**Preporučeni pluginovi:**

```
1. Git                 - Git integracija unutar Obsidiana
2. Pandoc Plugin       - Direktni export iz Obsidiana
3. Citation            - BibTeX/CSL podrška
4. Dataview            - Dinamičke tablice i upiti
5. Templater           - Automatski templatei
6. QuickAdd            - Brzo kreiranje dokumenata
7.Various Complements  - Auto-complete za reference
```

**Struktura vaulta:**

```
Obsidian Vault/
├── .git/
├── Templates/
│   ├── EU Proposal.md
│   ├── Scientific Paper.md
│   └── Project Doc.md
├── Projects/
│   └── (aktivni projekti)
├── References/
│   └── references.bib
├── Assets/
│   ├── Figures/
│   └── Tables/
└── Output/
    └── (generirani PDF)
```

---

## 7. Git Workflow za Timski Rad

```bash
# Inicijalizacija repositorya
git init
git remote add origin https://github.com/fakultet/docs-as-code.git

# Kreiranje nove dokumentacije
git checkout -b feature/nova-prijava
# Radi u Obsidianu...
git add .
git commit -m "Dodana sekcija Metodologija"
git push origin feature/nova-prijava

# Pull request za review
# (na GitHub/GitLab sučelju)

# Nakon odobravanja
git checkout main
git merge feature/nova-prijava
git push origin main
# → Triggera CI/CD i automatski PDF build
```

---

## 8. Spell Check Workflow (`spell-check.yml`)

```yaml
name: Spell Check

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  spell-check:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Install Codespell
        run: pip install codespell
      
      - name: Run Spell Check
        run: codespell src/ --ignore-words=.codespell-ignore
      
      - name: Install LanguageTool
        run: |
          sudo apt-get install -y languagetool
          
      - name: Run Grammar Check (Croatian)
        run: |
          languagetool --language hr --enabledOnly src/*.md
```

---

## 9. `.gitignore` za Obsidian + Pandoc

```gitignore
# Obsidian
.obsidian/app.json
.obsidian/appearance.json
.obsidian/core.json
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/graph.json
.obsidian/backlink.json

# Output (generirani fileovi)
output/*.pdf
output/*.docx
*.aux
*.log
*.out
*.toc
*.lof
*.lot

# Temporary
*.tmp
*.bak
.DS_Store
Thumbs.db

# Quarto
_quarto/
```

---

## 10. README.md za Repository

```markdown
# Docs-as-Code - Građevinski Fakultet

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
```

---

## 11. Demo Script za Predavanje

```
1. Otvori Obsidian vault s primjerom projekta (5 min)
2. Pokaži strukturu foldera i linkove između dokumenata (3 min)
3. Napravi promjenu u dokumentu i commitaj (3 min)
4. Pokaži GitHub Actions build u stvarnom vremenu (5 min)
5. Otvori Pull Request i dodaj komentar (4 min)
6. Mergeaj i pokaži generirani PDF (5 min)
```

---

## 12. Implementacijski Timeline

| Faza | Trajanje | Aktivnosti |
|------|----------|------------|
| 1. Pilot | 2 mjeseca | 1 katedra, 5-10 korisnika, 1-2 projekta |
| 2. Template | 1 mjesec | Finalizacija templatea, dokumentacija |
| 3. Obuka | 1 mjesec | Radionice za 20-30 korisnika |
| 4. Rollout | 3 mjeseca | Širenje na sve katedre |
| 5. Optimizacija | Kontinuirano | Feedback, poboljšanja |

---

Želiš li da dodam još nešto specifično — npr. konkretan LaTeX template za EU formate, detaljnije upute za Obsidian pluginove, ili primjer references.bib datoteke s pravim citatima?