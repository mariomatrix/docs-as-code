---
title: "Poglavlje 6 - Pisanje dokumenta"
---



> ⏱️ **Procijenjeno vrijeme:** 20–30 minuta
> 📋 **Preduvjet:** Vault otvoren, vlastiti branch kreiran (Poglavlje 3)

***

## 7.1 Markdown – format u kojemu pišemo

### Što je Markdown?

Markdown je način pisanja teksta gdje **formatiranje opisuješ jednostavnim znakovima** unutar samog teksta — bez klikanja na gumbe kao u Wordu.

Zašto? Jer je tekst bez skrivenih kodova format koji Git može pratiti, uspoređivati i spajati. Word `.docx` datoteke su iznutra kompleksni XML — Git ih ne može čitati smisleno.

### Kako to izgleda u praksi

Pišeš ovo:
```markdown
## Uvod projekta

Projekt se provodi u **tri faze** tijekom **2024. godine**.

Ciljevi su:
- Smanjenje potrošnje energije za 30%
- Ugradnja obnovljivih izvora
- Edukacija korisnika
```

Obsidian ti prikazuje ovo (Reading View):

***
## Uvod projekta

Projekt se provodi u **tri faze** tijekom **2024. godine**.

Ciljevi su:
- Smanjenje potrošnje energije za 30%
- Ugradnja obnovljivih izvora
- Edukacija korisnika

***

A Quarto od toga generira lijepo formatirani Word dokument s automatski primijenjenim stilovima.

***

## 7.2 Markdown osnove – sve što trebaš znati

### Naslovi

```markdown
# Naslov razine 1  (Heading 1 u Wordu)
## Naslov razine 2  (Heading 2 u Wordu)
### Naslov razine 3  (Heading 3 u Wordu)
```

> ⚠️ **Važno:** Između `#` i teksta naslova mora biti **razmak**. `#Naslov` ne funkcionira, `# Naslov` funkcionira.

***

### Isticanje teksta

```markdown
**podebljani tekst**
*kurziv*
***podebljani kurziv***
```

Prikazuje se kao: **podebljani tekst**, *kurziv*, ***podebljani kurziv***

***

### Nabrajanje – liste

**Nenumerirana lista** (bullet points):
```markdown
- Prva stavka
- Druga stavka
  - Podstavka (uvučena s 2 razmaka)
  - Još jedna podstavka
- Treća stavka
```

**Numerirana lista:**
```markdown
1. Prva stavka
2. Druga stavka
3. Treća stavka
```

> 💡 **Savjet:** Kod numerirane liste ne moraš paziti na redoslijed brojeva — možeš pisati sve `1.` i Quarto će automatski ispravno numerirati pri renderiranju.

***

### Tablice

```markdown
| Stupac 1     | Stupac 2     | Stupac 3     |
|--------------|--------------|--------------|
| Sadržaj ćelije | Sadržaj ćelije | Sadržaj ćelije |
| Drugi redak  | Drugi redak  | Drugi redak  |
```

Prikazuje se kao:

| Stupac 1 | Stupac 2 | Stupac 3 |
|----------|----------|----------|
| Sadržaj ćelije | Sadržaj ćelije | Sadržaj ćelije |
| Drugi redak | Drugi redak | Drugi redak |

> 💡 **Savjet:** Ne moraš ručno poravnavati crtice i stupce — Obsidian to radi automatski kada pritisneš Tab unutar tablice. Možeš i koristiti plugin **"Advanced Tables"** koji olakšava rad s tablicama.

***

### Linkovi i slike

**Link:**
```markdown
[tekst koji se prikazuje](https://www.primjer.com)
```

**Slika:**
```markdown
![opis slike](putanja/do/slike.png)
```

> **Savjet za slike:** Slike povuci i ispusti (drag & drop) direktno u Obsidian editor. Plugin će automatski kopirati datoteku na ispravnu lokaciju i umetnuti Markdown kod.

***

### Blokovi koda i napomene

**Inline kod** (za kratke naredbe unutar teksta):
```markdown
Pokreni naredbu `quarto render` u terminalu.
```

**Blok koda** (za dulje isječke):
````markdown
```
git commit -m "opis promjene"
git push origin naziv-brancha
```
````

**Horizontalna crta** (za vizualno odvajanje sekcija):
```markdown
***
```

***

### Quarto specifične napomene (callouts)

Quarto dodaje posebne blokove koji se lijepo renderiraju u finalnom dokumentu:

```markdown
::: {.callout-note}
Ovo je informativna napomena.
:::

::: {.callout-warning}
Ovo je upozorenje.
:::

::: {.callout-important}
Ovo je važna informacija.
:::
```

***

### Matematičke formule i izrazi

> ⚠️ **Napredno — preskoči ako tek učiš osnove Markdowna**
> Sljedeći odjeljak pokriva pisanje matematičkih formula u LaTeX notaciji. Potrebno je samo ako tvoj EU projekt uključuje statičke izračune, financijske formule ili metodološke jednadžbe. Ako to nije slučaj, slobodno priđi na Poglavlje 7.3.

Quarto podržava pisanje matematičkih formula u **LaTeX notaciji**. Ovo je korisno za EU projektne dokumente koji uključuju statističke pokazatelje, financijske formule ili metodološke izračune.

#### Inline formula (unutar teksta)

Za formulu unutar rečenice koristi **jednu dolarsku oznaku** (`$...$`):

```markdown
Stopa apsorpcije izračunava se kao $A = \frac{I}{P} \times 100\%$, gdje je $I$ iznos isplaćenih sredstava, a $P$ ukupni proračun projekta.
```

Prikazuje se kao:

Stopa apsorpcije izračunava se kao $A = \frac{I}{P} \times 100\%$, gdje je $I$ 
iznos isplaćenih sredstava, a $P$ ukupni proračun projekta.

***

#### Izdvojena formula (u zasebnom retku)

Za formulu koja stoji samostalno, na sredini stranice, koristi **dvostruku dolarsku oznaku** (`$$...$$`):

```markdown
$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$
```

Prikazuje se kao:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

***

#### Primjeri iz EU projektne dokumentacije

| Što izračunavaš | Markdown kod |
|---|---|
| Postotni udio | `$p = \frac{a}{b} \times 100$` |
| Prosjek | `$\bar{x} = \frac{\sum x_i}{n}$` |
| Standardna devijacija | `$\sigma = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n}}$` |
| Složena kamatna stopa | `$A = P(1 + r)^t$` |
| Energetska učinkovitost | `$\eta = \frac{W_{korisni}}{W_{ukupni}} \times 100\%$` |

: Primjeri matematičkih formula za EU projekte {tbl-colwidths="[40,60]"}

***

#### Česti LaTeX simboli

| Simbol | Kod | Primjer |
|--------|-----|---------|
| Razlomak | `\frac{a}{b}` | $\frac{a}{b}$ |
| Suma | `\sum_{i=1}^{n}` | $\sum_{i=1}^{n}$ |
| Kvadratni korijen | `\sqrt{x}` | $\sqrt{x}$ |
| Eksponent | `x^{2}` | $x^{2}$ |
| Indeks | `x_{i}` | $x_{i}$ |
| Postotak | `\%` | $\%$ |
| Srednja vrijednost | `\bar{x}` | $\bar{x}$ |
| Delta (promjena) | `\Delta` | $\Delta$ |
| Veće/manje | `\geq`, `\leq` | $\geq$, $\leq$ |
| Priblizno | `\approx` | $\approx$ |

: Česti LaTeX simboli {tbl-colwidths="[30,35,35]"}

> 💡 **Savjet:** Obsidian u Reading View prikazuje formule renderiranjem u stvarnom vremenu — vidiš rezultat dok pišeš. Ako formula ne izgleda ispravno, najčešći uzrok je pogrešna sintaksa u LaTeX kodu (nedostaje `}` ili `{`).

> **Napomena za Word output:** Quarto pri renderiranju u `.docx` pretvara LaTeX formule u Word-ove native matematičke objekte (OMath). Ne moraš ništa posebno raditi — formula u Markdownu automatski postaje ispravna formula u Wordu.

***

## 7.3 Struktura .qmd datoteke



### YAML zaglavlje (metadata)

Na samom vrhu svake `.qmd` datoteke nalazi se blok između trojnih crtica:

```yaml
***
title: "Naziv poglavlja"
author: "Ime Prezime"
date: "2024-03-15"
***
```

> ⚠️ **Upozorenje:** YAML zaglavlje mora biti **točno na prvom retku** datoteke, bez ikakvog teksta ispred. Ako pomiješaš format (npr. zaboraviš zatvoriti `---`), Quarto neće moći renderirati dokument.

### Kompletna struktura datoteke

```markdown
***
title: "1. Uvod i kontekst projekta"
author: "Ana Kovač"
date: "2024-03-15"
***

## 1.1 Kontekst projekta

Ovdje počinješ pisati sadržaj...

## 1.2 Ciljevi

- Cilj 1
- Cilj 2

## 1.3 Projektni tim

| Uloga | Ime | Organizacija |
|-------|-----|-------------|
| Voditelj | Ana Kovač | FGAG |
```

***

## 7.4 Korištenje predloška iz repozitorija

Repozitorij sadrži predloške u folderu `templates/` koji definiraju strukturu dokumenta.

### Kako koristiti predložak

1. U Obsidianu desni klik na folder `docs/`
2. Odaberi **"New note"**
3. Daj datoteci naziv prema konvenciji projekta (npr. `01-uvod.qmd`)
4. Na vrh datoteke kopiraj YAML zaglavlje iz predloška
5. Počni pisati sadržaj ispod zaglavlja

> 💡 **Savjet:** Otvori postojeću `.qmd` datoteku iz repozitorija kao referencu — vidiš točan format zaglavlja i strukturu koji projekt koristi.

***

## 7.5 Dva načina prikaza u Obsidianu

Obsidian nudi dva načina rada s datotekom:

### Editing View (uređivanje)

Vidiš sirovi Markdown tekst s oznakama (`**`, `#`, `-`). U ovom modu pišeš.

### Reading View (čitanje)

Vidiš formatiran tekst — naslovi su naslovi, bold je bold, tablice su tablice. Korisno za provjeru izgleda.

**Prebacivanje između modova:**
- Klikni na ikonu **knjige** u gornjem desnom kutu editora
- Ili pritisni `Ctrl + E`

> 💡 **Savjet:** Postoji i **Live Preview** mod koji prikazuje formatiran tekst dok pišeš — kao Word. Uključiš ga u Settings -> Editor -> "Default editing mode" -> "Live Preview". Preporučujemo za početnike.

***

## 7.6 Preporučeni tijek pisanja

Svaki radni dan (ili radna sesija) trebao bi izgledati ovako:

```text
+---------------------------------------------------------+
|              DNEVNI TIJEK PISANJA                       |
+---------------------------------------------------------+

  POCETAK RADA
  ------------
  1. Otvori Obsidian
  2. Provjeri statusnu traku -> jesi li na svom branchu?
  3. Pull (v gumb) -> preuzmi izmjene kolega
  4. Otvori svoju .qmd datoteku i počni pisati

  TIJEKOM PISANJA (svakih 30-60 minuta ili po cjelini)
  ----------------------------------------------------
  5. Stage All -> Commit
     -> poruka: sto si napisao/la? (npr. "Dodao uvod 1.2")

  KRAJ RADNOG DANA
  ----------------
  6. Zadnji Commit
  7. Push (^ gumb) -> pošalji sve na GitHub
  8. Zatvori Obsidian
```

> 💡 **Kada koristiti automatsku, a kada ručnu commit poruku?**
> - **Automatska poruka** (`{{date}} - {{hostname}}: {{numFiles}} datoteka`) — idealna za **česte, kratke commite** u fazi pisanja: draft verzije, male ispravke, svakodnevni ritam pisanja.
> - **Ručna poruka** (npr. `Dodano poglavlje 1.2 - Ciljevi projekta`) — **obavezna** kada commitaš logičku cjelinu koju ćeš poslati na pregled (Pull Request). Recenzent čita poruke da razumije što si napravio/la.

***

## 7.7 Commit i push kroz Obsidian plugin

### Korak po korak

**1. Stage All — označi promjene za commit**

U Source Control panelu (`Ctrl+Shift+G`) klikni **"Stage All"**.

Sve datoteke s oznakom `[M]` (Modified) ili `[U]` (Untracked) prelaze u sekciju "Staged Changes".

> ℹ️ **Što znači "stage"?** Git razlikuje "što si promijenio" od "što šalješ u ovaj commit". Stage je kao stavljanje stvari u kovčeg — odabiraš što ide zajedno.

**2. Commit — spremi s opisom**

Klikni **"Commit"**.

Plugin automatski generira poruku s datumom i brojem datoteka (prema formatu iz Poglavlja 3.5). Ako hoćeš vlastitu poruku, klikni na polje iznad gumba Commit i upiši ju.

### Savjeti za dobre commit poruke

Commit poruka treba odgovoriti na: **"Što sam napravio/la?"**

**Zlatno pravilo:** Zamisli da rečenica počinje s *"Ako primijenim ovaj commit, on će..."*. Tvoja poruka treba biti logičan nastavak te rečenice.

| Dobra poruka (Preporuka) | Loša poruka (Ne raditi) |
|----------------|--------------|
| `Dodati poglavlje 1.2 - Ciljevi projekta` | `izmjene` |
| `Ispraviti tablicu projektnog tima` | `save` |
| `Obrisati stare napomene prema komentarima Marka` | `aaa` |
| `Završiti poglavlje Metodologija` | `update` |

**3. Push — pošalji na GitHub**

Ako je **"Push on commit"** uključen (Poglavlje 3.5), push se dogodi automatski. Ako nije, klikni gumb **^ Push** u Source Control panelu.

✅ **Provjera uspjeha:** U statusnoj traci `^0` znači da nema čekajućih commitova za push — sve je na GitHubu.

***

## 7.8 Git CLI alternativa

Ako preferiraš upisivati naredbe u Command Prompt:

```cmd
# 1. Dodaj sve izmijenjene datoteke
git add .

# 2. Napravi commit s porukom
git commit -m "Dodati poglavlje 1.2 - Ciljevi projekta"

# 3. Pošalji na GitHub
git push origin ana-kovac/uvod
```

> 💡 **Savjet:** `git add .` (s točkom na kraju) dodaje **sve** izmijenjene datoteke odjednom. Točka znači "sve u trenutnom folderu i podfolderima".

***

## 7.9 Što ako nešto pođe po zlu — česte situacije

### Zaboravio/la sam commitati prije zatvaranja Obsidiana
Git prati sve promjene u pozadini — nijedna datoteka nije izgubljena sve dok je Obsidian bio otvoren. Jednostavno otvori Source Control panel (`Ctrl+Shift+G`) i vidiš sve izmjene koje čekaju commit.

### Kolega je pushao izmjene u moju datoteku dok sam pisao/la
Otvori Obsidian, klikni **v Pull**. Ako ste radili na različitim dijelovima datoteke, Git će automatski spojiti promjene. Ako ste radili na istim recima — vidi Poglavlje 8.5 o rješavanju konflikata.

### Slučajno sam commitao/la na `main` umjesto na svoju granu
Nemoj panicirati. Pošalji poruku maintaineru i opiši što se dogodilo. Maintainer može lako poništiti taj commit s GitHuba bez gubljenja sadržaja. Za budućnost: uvijek provjeri statusnu traku (`Current branch:`) prije commita.

***

## ✅ Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Markdown** | Jednostavan tekstualni format za pisanje s oznakama za formatiranje |
| **YAML zaglavlje** | Metadata blok na vrhu svake `.qmd` datoteke |
| **.qmd datoteka** | Quarto Markdown datoteka — naša osnovna jedinica dokumenta |
| **Stage** | Odabir datoteka koje idu u sljedeći commit |
| **Commit** | Snimanje trenutnog stanja s opisnom porukom |
| **Push** | Slanje commitova na GitHub |
| **Dnevni ritam** | Pull -> piši -> commit (često) -> push (kraj dana) |

***















