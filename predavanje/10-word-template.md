---
title: "Poglavlje 10 - Word DOCX template: koncept"
---

> **Procijenjeno vrijeme čitanja:** 10 minuta
> **Preduvjet:** Razumijevanje osnovnog toka rada (Poglavlja 1–9)

***

## 10.1 Problem koji template rješava

Zamisli da pet osoba piše pet poglavlja u Obsidianu. Svako poglavlje je Markdown tekst — bez fontova, bez boja, bez margina. Kada Quarto spoji sve u jedan Word dokument, tko odlučuje kako će izgledati finalni dokument?

**Odgovor: Word template.**

Bez predloška, Quarto bi primijenio generički izgled koji ne odgovara standardima projekta. S predloškom, svaki put dobivaš identičan, profesionalno formatiran dokument — bez obzira tko je pisao koje poglavlje i s kojeg računala je pokrenut render.

***

## 10.2 Kako funkcionira reference-doc mehanizam

Quarto ne čita template kao "uzorak koji treba kopirati" — on čita **stilove** definirane u predlošku i primjenjuje ih na generirani dokument.

```text
+-------------------------------------------------------------+
|               KAKO QUARTO KORISTI TEMPLATE                  |
+-------------------------------------------------------------+

  Tvoj Markdown tekst          Word template
  ------------------           -------------
  # Naslov poglavlja    +      Stil "Heading 1":
                               * Font: Calibri 16pt Bold
                               * Boja: Plava #003399
                               * Razmak prije: 12pt
                                       |
                                       v
                              Finalni Word dokument:
                              Naslov poglavlja u Calibri
                              16pt Bold, plavi, s razmakom
```

Quarto čita oznake iz Markdowna (`#`, `##`, `**`, tablice...) i za svaku oznaku pronalazi odgovarajući stil u predlošku. **Sadržaj dolazi iz Markdowna, oblik dolazi iz predloška.**

***

## 10.3 Gdje se template nalazi

U repozitoriju, template se nalazi na lokaciji:

```text
EU-Project-Template/
└── templates/
    └── EU-dokument-template.docx    <- Word predložak
```

Quarto zna gdje je template jer je putanja definirana u `_quarto.yml` konfiguracijskoj datoteci:

```yaml
format:
  docx:
    reference-doc: templates/EU-dokument-template.docx
```

Ova veza je već postavljena — **ne trebaš ništa mijenjati** da bi template bio primijenjen. Svaki put kada pokreneš render, Quarto automatski koristi ovaj predložak.

***

## 10.4 Koje stilove template definira

Word predložak definira izgled svakog elementa dokumenta:

| Markdown element | Word stil u predlošku |
|-----------------|----------------------|
| `# Naslov` | Heading 1 |
| `## Podnaslov` | Heading 2 |
| `### Sekcija` | Heading 3 |
| Normalni tekst | Normal / Body Text |
| `**podebljano**` | Bold (unutar stila) |
| Tablice | Table Grid ili prilagođeni stil |
| Slike | Figure |
| Numeracija stranica | Footer stil |
| Zaglavlje dokumenta | Header stil |

> **Važna implikacija:** Ako u Obsidianu pišeš `# Poglavlje 1` i u predlošku stil Heading 1 ima definiranu automatsku numeraciju, finalni dokument će automatski ispisati `1. Poglavlje 1` — bez da si ti ručno upisivao/la broj. Formatiranje i numeracija su potpuno automatski.

***

## 10.5 Kako modificirati template

> **Upozorenje:** Modificiranje predloška mijenja izgled **svakog budućeg dokumenta** generiranog iz ovog repozitorija. Ovu promjenu radi isključivo **maintainer projekta**, po dogovoru s timom ili naručiteljem.

Ako ipak trebaš promijeniti izgled:

### Korak 1: Otvori template u Wordu

Dvostruki klik na `templates/EU-dokument-template.docx` — otvara se u Microsoft Wordu.

### Korak 2: Uredi stilove, ne sadržaj

Template ne sadrži pravi sadržaj dokumenta — sadrži samo ogledne primjere teksta koji pokazuju kako svaki stil izgleda.

**Što mijenjati:**
- Otvori **Home -> Styles panel** (ili `Alt+Ctrl+Shift+S`)
- Desni klik na stil koji želiš promijeniti (npr. `Heading 1`)
- Odaberi **"Modify..."**
- Promijeni font, veličinu, boju, razmak...

**Što ne mijenjati:**
- Naziv stila (npr. `Heading 1` mora ostati `Heading 1` — Quarto ga traži po imenu)
- Strukturu dokumenta

### Korak 3: Spremi i commitaj

1. Spremi datoteku u Wordu (`Ctrl+S`)
2. U Obsidianu: Stage All -> Commit -> Push
3. Otvori PR kao i za svaku drugu promjenu

> **Savjet:** Kada modificiraš template, u commit poruci napiši točno što si promijenio/la: npr. `Template: promjena fonta naslova na Arial 14pt`. Ovo je važno jer svaka promjena predloška utječe na sve buduće renderove.

***

## 10.6 Što se dogodi ako template nedostaje

Ako Quarto ne pronađe template na definiranoj putanji, render će i dalje raditi — ali s generičkim Word stilovima. Finalni dokument neće izgledati prema standardima projekta.

GitHub Actions će u logu prikazati upozorenje:
```text
Warning: reference-doc 'templates/EU-dokument-template.docx' not found.
Using default styles.
```

Ako vidiš ovo upozorenje — provjeri je li datoteka na ispravnoj lokaciji i je li commitana u repozitorij.

***

## 10.7 Veza između template i finalnog dokumenta — sažetak

```text
+--------------+    +--------------+    +----------------------+
|   Markdown   |    |    Word      |    |   Finalni Word       |
|   sadržaj    | +  |   template   | =  |   dokument           |
|              |    |              |    |                      |
| # Naslov     |    | Heading 1:   |    | NASLOV               |
| Tekst...     |    | Calibri 16pt |    | (Calibri 16pt Blue)  |
| - stavka     |    | Blue         |    |                      |
|              |    |              |    | Tekst u Body Text    |
|              |    | Normal:      |    | stilu...             |
|              |    | Times 11pt   |    |                      |
+--------------+    +--------------+    +----------------------+
     Pišeš              Ne diraš             Automatski rezultat
```

Kao autor, tvoj jedini posao je **ispravno koristiti Markdown oznake**. Sve ostalo — fontovi, boje, margine, numeracija stranica, zaglavlja i podnožja — dolazi automatski iz predloška.

***

## Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Word template** | `.docx` datoteka koja definira stilove finalnog dokumenta |
| **reference-doc** | Quarto mehanizam kojim se template primjenjuje na output |
| **Stilovi** | Definirani u predlošku — Heading 1, Normal, Table Grid itd. |
| **Sadržaj vs. oblik** | Markdown = sadržaj; template = oblik. Nikad se ne miješaju |
| **Tko mijenja template** | Isključivo maintainer, po dogovoru, s commit porukom |

> **Ključna poruka ovog poglavlja:** Kao autor, ne brineš se za formatiranje. Pišeš ispravne Markdown oznake, a predložak se brine za sve ostalo. Konzistentnost između poglavlja različitih autora je zajamčena.

***

**<- Prethodno poglavlje:** [Poglavlje 9 – Merge u main](09-merge-u-main.md)
**Sljedeće poglavlje:** [Poglavlje 11 – GitHub Actions: pregled automatizacije ->](11-github-actions.md)







