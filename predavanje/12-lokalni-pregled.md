---
title: "Poglavlje 11 - Quarto render: lokalni pregled dokumenta"
---



> ⏱️ **Procijenjeno vrijeme:** 15–20 minuta
> 📋 **Preduvjet:** Quarto instaliran i provjeren (Poglavlje 2.3), repozitorij kloniran (Poglavlje 3)

***

## 12.1 Zašto renderirati lokalno?

GitHub Actions automatski renderira dokument svaki put kada se pusha na `main` — to smo vidjeli u Poglavlju 3. Zašto bi onda uopće pokretao/la Quarto lokalno na svom računalu?

**Tri razloga:**

1. **Brza provjera prije pusha** — vidiš kako će finalni dokument izgledati *prije* nego pošalješ promjene kolegama. Bolje uhvatiti grešku lokalno nego čekati da Actions javi problem na GitHubu.

2. **Rad bez interneta** — lokalni render ne zahtijeva GitHub. Možeš raditi i pregledavati rezultate i bez veze s mrežom.

3. **Brže iteracije** — lokalni render je trenutan. GitHub Actions treba 2–5 minuta. Ako testiraš izgled tablice ili slike, puno je brže renderirati lokalno.

> 💡 **Pravilo palca:** Lokalni render je za **osobnu provjeru**. GitHub Actions je za **službeni output** koji ide timu.

***

## 12.2 Otvaranje terminala u folderu repozitorija

Sve Quarto naredbe pokrećemo iz **Command Prompta** unutar foldera repozitorija.

### Windows

1. Otvori **File Explorer**
2. Navigiraj do `C:\Projekti\EU-Project-Template`
3. U adresnoj traci klikni jednom, upiši `cmd`, pritisni **Enter**

Otvara se Command Prompt s ispravnom lokacijom:
```cmd
C:\Projekti\EU-Project-Template>
```

> 💡 **Alternativa:** U Obsidianu možeš otvoriti terminal direktno — `Ctrl+P` -> upiši `terminal` -> "Open terminal here". Ako plugin nije instaliran, koristi File Explorer metodu iznad.

### macOS

1. Otvori **Finder**
2. Navigiraj do foldera repozitorija
3. Desni klik na folder -> **"New Terminal at Folder"**

***

## 12.3 Osnovne Quarto naredbe

### Render jedne datoteke

Renderira jednu `.md` datoteku u sve formate definirane u `_quarto.yml`:

```cmd
quarto render docs/01-uvod.md
```

### Render jedne datoteke u specifičan format

Renderira samo u Word dokument, bez obzira na ostale formate u konfiguraciji:

```cmd
quarto render docs/01-uvod.md --to docx
```

Ostali dostupni formati:
```cmd
quarto render docs/01-uvod.md --to html
quarto render docs/01-uvod.md --to pdf
```

> ⚠️ **PDF napomena:** Render u PDF zahtijeva instaliran LaTeX (`tinytex`). Ako ti PDF nije potreban, koristi docx ili html. Instalacija tinytex-a: `quarto install tinytex`

### Render cijelog projekta

Renderira sve datoteke definirane u `_quarto.yml` odjednom:

```cmd
quarto render
```

> 💡 **Savjet:** Za svakodnevnu provjeru vlastitog poglavlja koristi render jedne datoteke — brže je. Render cijelog projekta koristi samo kada trebaš vidjeti kako sve zajedno izgleda.

### Preview — pregled u pregledniku

Preview pokreće lokalni web server i otvara dokument u pregledniku. Automatski se ažurira svaki put kada spremiš datoteku:

```cmd
quarto preview docs/01-uvod.md
```

```text
Preparing to preview
  [✓] docs/01-uvod.md
Watching files for changes
Browse at http://localhost:4848/
```

Otvori preglednik na adresi `http://localhost:4848/` — vidiš live pregled dokumenta.

Za zaustavljanje pregleda pritisni `Ctrl+C` u Command Promptu.

> ⚠️ **Zaustavljanje previewa:** `quarto preview` pokreće lokalni web server koji ostaje aktivan u pozadini sve dok ga ručno ne zaustaviš. Za zaustavljanje **uvijek pritisni `Ctrl+C` u Command Promptu**. Ako zatvoriš terminal prozor direktno (bez Ctrl+C), sljedeći puta možeš dobiti grešku `Error: Port 4848 is already in use`. Rješenje: restart Command Prompta.

> 💡 **Kada koristiti preview vs. render?**
> - **Preview** — dok pišeš i hoćeš vidjeti promjene odmah (HTML prikaz)
> - **Render** — kada hoćeš finalnu `.docx` datoteku za provjeru izgleda u Wordu

***

## 12.4 Gdje se nalaze generirani dokumenti

Nakon lokalnog rendera, Quarto sprema output u folder definiran u `_quarto.yml`. Najčešće:

```text
EU-Project-Template/
└── output/               <- generirani dokumenti idu ovdje
    ├── 01-uvod.docx
    ├── 02-metodologija.docx
    └── EU-projekt-kompletno.docx
```

Otvori `.docx` datoteku dvostrukim klikom — otvara se u Microsoft Wordu s primijenjenim stilovima iz predloška.

> ⚠️ **Važno:** Folder `output/` je naveden u `.gitignore` — generirani dokumenti se **ne commitaju** u repozitorij. Svaki put se generiraju iznova iz izvora. Ovo je namjerno: jedini "izvor istine" su `.md` datoteke, ne generirani outputi.

***

## 12.5 Razumijevanje `_quarto.yml` — osnove

Datoteka `_quarto.yml` je "mozak" Quarto projekta — definira što se renderira, kako i kamo. Nalazi se u korijenu repozitorija.

> ℹ️ **Ne mijenjaj ovu datoteku** bez dogovora s maintainerom.

> 💡 **Primjer što se dogodi ako zaboraviš dodati poglavlje:**
> Kreirao/la si `04-zakljucak.md` i napisao/la ga u cijelosti, ali u `_quarto.yml` lista `chapters:` završava s `03-rezultati.md`. Quarto ne zna da tvoja datoteka postoji — u finalnom Wordu nema zaklučka. Rješenje: javi maintaineru da doda tvoju datoteku u listu poglavlja.

Evo što znače ključni dijelovi (samo za razumijevanje):

```yaml
project:
  type: book               # <- tip projekta: book = više datoteka u jedan dokument

book:
  title: "EU Projektno izvješće"
  author: "Projektni tim"
  chapters:
    - docs/01-uvod.md       # <- redoslijed poglavlja u finalnom dokumentu
    - docs/02-metodologija.md
    - docs/03-rezultati.md

format:
  docx:
    reference-doc: templates/EU-dokument-template.docx  # <- Word predložak
  html:
    theme: default          # <- tema za HTML output
```

### Što iz ovoga trebaš znati

| Postavka | Što znači za tebe |
|----------|-----------------|
| `chapters` | Redoslijed u kojem se poglavlja pojavljuju u finalnom dokumentu — ako fali tvoja datoteka, poglavlje neće biti u outputu |
| `reference-doc` | Putanja do Word predloška — mora biti ispravna |
| `format` | Koji formati se generiraju — docx, html, pdf |

> 💡 **Česta situacija:** Napisao/la si novu datoteku, renderiraš — i ne vidiš je u finalnom dokumentu. Razlog: datoteka nije dodana u `chapters` listu u `_quarto.yml`. Javi maintaineru da je doda.

***

## 12.6 Razlika između lokalnog rendera i GitHub Actions

| | Lokalni render | GitHub Actions |
|--|---------------|----------------|
| **Kada se pokreće** | Ručno, po potrebi | Automatski, na svaki push u main |
| **Tko ga pokreće** | Ti, na svom računalu | GitHub, na virtualnom računalu |
| **Rezultat** | Lokalna datoteka u `output/` | Artifact dostupan za preuzimanje |
| **Brzina** | Trenutno (sekunde) | 2–5 minuta |
| **Namjena** | Osobna provjera | Službeni output za tim |
| **Commitanje outputa** | Ne commitaj | GitHub to radi automatski |

***

## 12.7 Tipičan tijek rada s lokalnim renderom

```text
+-----------------------------------------------------------+
|          KAKO UKLOPITI LOKALNI RENDER U RAD               |
+-----------------------------------------------------------+

  1. Piši u Obsidianu
          |
          v
  2. Spremi datoteku (Ctrl+S)
          |
          v
  3. Lokalni render za provjeru:
     quarto render docs/moje-poglavlje.md --to docx
          |
          v
  4. Otvori output/moje-poglavlje.docx u Wordu
     -> Izgleda dobro? Nastavi.
     -> Nešto nije u redu? Vrati se u Obsidian i ispravi.
          |
          v
  5. Commit + Push (Poglavlje 3)
          |
          v
  6. GitHub Actions automatski renderira
     službenu verziju (Poglavlje 3)
```

***

## 12.8 Najčešće greške pri lokalnom renderu

| Greška | Uzrok | Rješenje |
|--------|-------|----------|
| `quarto: command not found` | Quarto nije instaliran ili PATH nije ažuriran | Restart računala, provjeri instalaciju (Pogl. 2.3) |
| `ERROR: YAMLException` | Greška u YAML zaglavlju `.md` datoteke | Provjeri zaglavlje — nema Tab-ova, ima zatvorenu `---` |
| `File not found: templates/...` | Template nije na očekivanoj putanji | Provjeri je li `templates/` folder prisutan i nije li u `.gitignore` |
| `Pandoc not found` | Quarto koristi Pandoc koji nije instaliran | Reinstaliraj Quarto — Pandoc dolazi u paketu |
| Prazan output folder | Render je uspio ali nisi u pravom folderu | Provjeri jesi li pokrenuo/la naredbu iz korijena repozitorija |

***

## ✅ Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Lokalni render** | Ručno pokretanje Quarta na svom računalu za osobnu provjeru |
| **`quarto render`** | Renderira jednu datoteku ili cijeli projekt |
| **`quarto preview`** | Live pregled u pregledniku, ažurira se automatski |
| **`--to docx`** | Zastavica za odabir formata outputa |
| **`_quarto.yml`** | Konfiguracijska datoteka — ne mijenjaj bez maintainera |
| **`output/` folder** | Gdje završavaju lokalno generirani dokumenti — ne commitati |

> 💡 **Ključna poruka:** Lokalni render je tvoj osobni alat za provjeru — koristi ga slobodno i često. Ne commitaj generirane dokumente. Službeni output uvijek dolazi iz GitHub Actions, automatski, nakon mergea u main.

***


**Sljedeće:** [Dodaci – Cheat sheet, Rječnik pojmova, Top 10 grešaka ->](13-dodaci.md)











