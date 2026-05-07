---
title: "Poglavlje 11 - GitHub Actions: pregled automatizacije"
---

> **Procijenjeno vrijeme čitanja:** 10 minuta
> **Preduvjet:** Razumijevanje toka rada (Poglavlja 1–10)

***

## 11.1 Što su GitHub Actions?

**GitHub Actions** je sustav automatizacije ugrađen direktno u GitHub. Kada se nešto dogodi u repozitoriju — primjerice netko pusha promjene — GitHub Actions automatski pokreće unaprijed definirane zadatke.

### Analogija

Zamisli automatsku praonicu rublja u praonici samousluge:
- Ti staviš rublje i pritisneš gumb (= push na GitHub)
- Stroj automatski pere, ispire i centrifugira (= GitHub Actions pokreće korake)
- Na kraju izvadi čisto rublje (= generiran Word dokument)

Ti ne moraš znati kako stroj radi iznutra — samo koristiš rezultat.

### Što Actions radi u ovom projektu

Svaki put kada se promjene mergaju u `main` granu:

```text
+--------------------------------------------------------------+
|                AUTOMATSKI TOK GITHUB ACTIONS                 |
+--------------------------------------------------------------+

  Push/Merge -> main
       |
       v
  GitHub prepoznaje događaj
       |
       v
  Pokreće "runner" (privremeno virtualno računalo)
       |
       v
  +-----------------------------+
  |  Koraci koji se izvršavaju: |
  |                             |
  |  1. Preuzmi repozitorij     |
  |  2. Instaliraj Quarto       |
  |  3. Pokreni quarto render   |
  |  4. Spremi generirane       |
  |     dokumente               |
  +-----------------------------+
       |
       v
  Generirani dokumenti dostupni
  za preuzimanje na GitHubu
```

**Rezultat:** Svaki push na `main` automatski producira svježu verziju finalnog dokumenta — bez da itko ručno pokreće Quarto na svom računalu.

***

## 11.2 Gdje se nalazi konfiguracija

Konfiguracija GitHub Actions nalazi se u posebnom folderu repozitorija:

```text
EU-Project-Template/
└── .github/
    └── workflows/
        └── render.yml     <- datoteka koja definira automatizaciju
```

> **Ne dirati:** Cijeli `.github/` folder je isključiva odgovornost maintainera. Greška u YAML konfiguraciji može onemogućiti cijelu automatizaciju. Ako misliš da nešto treba promijeniti — javi maintaineru.

### Kako izgleda workflow datoteka (samo za razumijevanje)

```yaml
name: Render Quarto Documents

on:
  push:
    branches: [main]        # <- pokreće se samo na main grani

jobs:
  render:
    runs-on: ubuntu-latest  # <- GitHub koristi Linux virtualno računalo
    steps:
      - uses: actions/checkout@v4          # preuzima repozitorij
      - uses: quarto-dev/quarto-actions/setup@v2  # instalira Quarto
      - run: quarto render                 # pokreće render
      - uses: actions/upload-artifact@v4  # sprema generirane dokumente
```

Ne trebaš razumjeti svaki redak — dovoljno je znati da ova datoteka postoji i što radi u cjelini.

***

## 11.3 Praćenje statusa Actions — gdje gledati

### Zelena kvačica / Crveni X na GitHubu

Nakon svakog pusha na `main`, pored commit poruke na GitHubu pojavljuje se ikona:

| Ikona | Značenje |
|-------|----------|
| Zuta tocka | Action je pokrenut, u tijeku |
| | Action završio uspješno, dokumenti su generirani |
| Ne | Action nije uspio — nešto je krenulo naopako |

### Kako otvoriti Actions log

1. Na GitHubu, klikni na karticu **"Actions"** u gornjem izborniku repozitorija
2. Vidiš popis svih pokretanja — svaki push na main je jedan unos
3. Klikni na posljednje pokretanje

```text
+--------------------------------------------------------+
|  Actions / Render Quarto Documents                     |
|                                                        |
|  [V]  Render Quarto Documents    #42   3 min ago       |
|  [V]  Render Quarto Documents    #41   2 hours ago     |
|  Ne  Render Quarto Documents    #40   yesterday       |
+--------------------------------------------------------+
```

4. Klikni na pokretanje da vidiš detalje
5. Klikni na **"render"** u lijevom izborniku da vidiš log koraka

***

## 11.4 Čitanje loga — što tražiti

Log izgleda kao dugačak ispis teksta. Ne moraš čitati sve — traži **crvene linije s greškama**.

### Uspješan log

```text
[V]  Set up job
[V]  Checkout repository
[V]  Setup Quarto
[V]  Run quarto render
    Rendering docs/01-uvod.md
    Rendering docs/02-metodologija.md
    Output created: output/EU-izvjesce.docx
[V]  Upload artifacts
[V]  Complete job
```

### Log s greškom

```text
[V]  Set up job
[V]  Checkout repository
[V]  Setup Quarto
Ne  Run quarto render
    Rendering docs/01-uvod.md
    ERROR: YAMLException: bad indentation of a mapping entry
    at line 3, column 5
    Execution halted
Ne  Upload artifacts (skipped)
Ne  Complete job
```

### Kako čitati poruku greške

Poruka greške obično sadrži:
- **Vrstu greške** (`YAMLException`, `FileNotFoundException`, `ParseError`...)
- **Datoteku** gdje je greška (`docs/01-uvod.md`)
- **Redak i stupac** (`at line 3, column 5`)

Ove informacije su dovoljne da lociraš i popraviš problem.

***

## 11.5 Najčešće greške i kako ih prepoznati

| Poruka greške | Uzrok | Rješenje |
|--------------|-------|----------|
| `YAMLException: bad indentation` | Razmaci u YAML zaglavlju nisu ispravni | Provjeri zaglavlje `.md` datoteke — ne koristi Tab, samo razmake |
| `FileNotFoundException: template not found` | Predložak nije na ispravnoj putanji | Provjeri je li `templates/EU-dokument-template.docx` commitana |
| `ParseError: unexpected character` | Poseban znak u Markdownu koji Quarto ne može parsirati | Pronađi redak naveden u grešci, provjeri znakove |
| `Error: Process completed with exit code 1` | Generička greška — gledaj prethodne linije loga | Skrolaj gore u logu — greška je opisana nekoliko redaka iznad |

> **Savjet:** Kopiraj poruku greške i pošalji je maintaineru — s imenom datoteke i brojem retka. To je sve što je potrebno za dijagnozu.

***

## 11.6 Preuzimanje generiranih dokumenata

Kada je Action uspješno završio, generirani dokumenti su dostupni kao **Artifacts** (privremene datoteke koje GitHub čuva određeni broj dana).

### Kako preuzeti dokument

1. Na GitHubu, klikni karticu **"Actions"**
2. Klikni na posljednje uspješno pokretanje (zelena kvačica)
3. Skrolaj do dna stranice — sekcija **"Artifacts"**

```text
+--------------------------------------------+
|  Artifacts                                 |
|                                            |
|  [ ] EU-izvjesce-output    45.2 MB    v    |
+--------------------------------------------+
```

4. Klikni na naziv Artifacta za preuzimanje ZIP datoteke
5. Raspakiraj ZIP — unutra je finalni `.docx` dokument

> ℹ️ **Napomena:** GitHub čuva Artifacts određeni broj dana (obično 90). Ako projekt ima duži vijek, maintainer može podesiti automatsko objavljivanje dokumenata na GitHub Pages ili drugoj lokaciji — ali to je naprednija konfiguracija.

***

## 11.7 Što korisnik treba znati, a što ne

### Trebaš znati

- Gdje gledati status Actions (kartica "Actions")
- Razliku između zelene kvačice i crvenog X-a
- Kako otvoriti log i pronaći poruku greške
- Kako preuzeti generirani dokument iz Artifacts

### Ne trebaš znati (to je posao maintainera)

- Kako pisati ili mijenjati YAML workflow datoteke
- Kako konfigurirati GitHub runners
- Kako postavljati environment varijable i secrets
- Kako mijenjati trigger uvjete (kada se Action pokreće)

***

## Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **GitHub Actions** | Sustav automatizacije koji se pokreće na svaki push u main |
| **Workflow** | YAML datoteka koja definira što se automatski radi |
| **Runner** | Privremeno virtualno računalo koje izvršava korake |
| **Artifact** | Generirani dokument dostupan za preuzimanje na GitHubu |
| **Log** | Ispis svih koraka — tražimo crvene linije za dijagnozu |
| **Zelena/crvena ikona** | Brzi vizualni signal o uspjehu ili neuspjehu rendera |

> **Ključna poruka:** GitHub Actions radi u pozadini, automatski, bez tvoje intervencije. Tvoj jedini zadatak je prepoznati kada nešto nije prošlo (crveni X), pročitati poruku greške i javiti maintaineru — ili popraviti svoju `.md` datoteku ako greška pokazuje na nju.

***

**<- Prethodno poglavlje:** [Poglavlje 10 – Word DOCX template](10-word-template.md)
**Sljedeće poglavlje:** [Poglavlje 12 – Quarto render: lokalni pregled dokumenta ->](12-lokalni-pregled.md)







