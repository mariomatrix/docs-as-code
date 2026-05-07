---
title: "Poglavlje 7 - Pull Request: predaja rada na pregled"
---



> ⏱️ **Procijenjeno vrijeme:** 15–20 minuta
> 📋 **Preduvjet:** Završeno pisanje na vlastitom branchu, barem jedan commit pushean na GitHub (Poglavlje 3)

***

## 8.1 Što je Pull Request i zašto je važan?

### Definicija

**Pull Request** (skraćeno: PR) je formalni zahtjev da se tvoje promjene s radnog brancha **spoje u main granu**.

Naziv može zbuniti — ne radi se o tome da ti nešto "povlačiš" (pull), nego da **tražiš od tima da povuče tvoje promjene** u glavnu verziju.

### Zašto ne spajamo direktno?

Jer svaka promjena koja ulazi u `main` mora biti:

- Pregledana od bar jedne druge osobe
- Bez tehničkih grešaka (ispravan Markdown, YAML zaglavlje)
- Sadržajno odobrena (točnost, stil, konzistentnost s ostatkom dokumenta)

PR je **kapija kontrole kvalitete** — ništa ne ulazi u službenu verziju bez pregleda.

### Analogija

Zamisli PR kao **predaju zadaće profesoru**:
- Ti predaješ (otvaraš PR)
- Profesor pregledava i komentira (Review)
- Ti ispravljaš prema komentarima (novi commits na isti branch)
- Profesor odobrava i "zaključuje" (Merge)

Razlika od klasičnog pregleda dokumenta: sve je vidljivo, sve je zabilježeno, nema e-mail pingponga.

***

## 8.2 Uloge u procesu pregleda

| Uloga | Tko | Što radi |
|-------|-----|----------|
| **Autor** | Onaj tko je pisao dokument | Otvara PR, odgovara na komentare, ispravlja |
| **Recenzent** | Kolega iz tima ili voditelj | Pregledava, komentira, odobrava ili traži izmjene |
| **Maintainer** | Voditelj projekta | Ima pravo mergati u main — može biti ista osoba kao recenzent |

> 💡 **Savjet:** Dogovorite u timu tko je maintainer — ta osoba ima finalnu odgovornost za kvalitetu `main` grane. Obično je to voditelj dokumentacije.

***

## 8.3 Kada otvoriti Pull Request?

PR otvori kada:
- Završiš poglavlje ili logičnu cjelinu (ne čekaj da bude "savršeno")
- Sve promjene su pushane na GitHub
- Lokalno si provjerio/la da Markdown izgleda ispravno (Reading View u Obsidianu)

Ne čekaj da bude sto posto gotovo — PR je i alat za **rano dobivanje povratnih informacija**. Bolje kratki PR s jednim poglavljem nego jedan veliki PR s cijelim dokumentom.

***

## 8.4 Otvaranje Pull Requesta na GitHubu

### Korak 1: Idi na GitHub repozitorij

1. Otvori preglednik i idi na:
   `https://github.com/FGAG-docs/EU-Project-Template`
2. Prijavi se ako nisi prijavljen/a

### Korak 2: GitHub primijeti tvoj branch

Kada pushaš branch na GitHub, stranica repozitorija automatski prikazuje žuti banner:

```text
+----------------------------------------------------------------+
|  [!] ana-kovac/uvod had recent pushes 2 minutes ago            |
|                              [ Compare & pull request ]        |
+----------------------------------------------------------------+
```

Klikni na **"Compare & pull request"**.

> **Ako bannera nema:** Klikni na karticu **"Pull requests"** -> zeleni gumb **"New pull request"** -> u padajućem izborniku "compare" odaberi svoj branch -> klikni **"Create pull request"**.

### Korak 3: Ispuni obrazac Pull Requesta

Otvara se obrazac s nekoliko polja:

***

**Title (Naslov)**

Naslov PR-a treba jasno opisati što si napravio/la:

| Dobro | Loše |
|---------|--------|
| `Poglavlje 1 - Uvod i kontekst projekta` | `moje izmjene` |
| `Ispravak tablice projektnog tima (Pogl. 2)` | `update` |
| `Dodano poglavlje Metodologija - prva verzija` | `PR` |

***

**Description (Opis)**

Opis je prostor gdje objašnjavaš recenzentu što treba pregledati. Preporučeni format:

```markdown
## Što je napravljeno
- Napisano poglavlje 1.1 Kontekst projekta
- Napisano poglavlje 1.2 Ciljevi
- Dodana tablica projektnog tima

## Što treba pregledati
- Jesu li ciljevi usklađeni s projektnim prijedlogom?
- Provjeri tablicu - nisam siguran/na za nazive organizacija

## Što još nije gotovo (ako je primjenjivo)
- Poglavlje 1.3 (Dionici) - dolazi u sljedećem PR-u
```

***

**Reviewers (Recenzenti)**

Na desnoj strani obrasca, pod "Reviewers":
1. Klikni na zupčanik ⚙️ pored "Reviewers"
2. Upiši GitHub korisničko ime kolege koji treba pregledati
3. Odaberi ga s popisa

> 💡 **Savjet:** Recenzent dobiva e-mail obavijest. Ako žuriš, dodatno ga obavijesti porukama — GitHub notifikacije ponekad završe u spamu.

***

**Labels (Oznake) — opcionalno**

Labels pomažu organizirati PR-ove u većim projektima. Uobičajene oznake:
- `in-review` — čeka pregled
- `needs-revision` — treba ispravke
- `ready-to-merge` — odobreno

Ako tim nije postavio labels, preskoči ovaj korak.

***

### Korak 4: Pošalji Pull Request

Klikni zeleni gumb **"Create pull request"**.

✅ **Provjera uspjeha:** PR je otvoren i vidljiv pod karticom "Pull requests" repozitorija. Recenzent je dobio obavijest.

***

## 8.5 Što se događa nakon otvaranja PR-a?

```text
+-----------------------------------------------------+
|              ZIVOT JEDNOG PULL REQUESTA             |
+-----------------------------------------------------+

  AUTOR                          RECENZENT
  -----                          ---------
  Otvori PR
                                 Dobiva e-mail obavijest
                                 Pregledava promjene
                                 (Files changed tab)
                                         |
                            +------------+-----------+
                            |                        |
                     Komentira i traži        Odobrava
                     izmjene                 (Approve)
                            |                        |
  Prima komentare           |                        |
  Ispravlja u Obsidianu     |               MAINTAINER
  Commit + Push             |               mergea u main
  (PR se automatski         |
   azurira)                 |
            |               |
            +---------------+
          (ciklus se ponavlja
           dok nije odobreno)
```

***

## 8.6 Kako reagirati na komentare recenzenta

### Gdje vidiš komentare

1. Na GitHubu, otvori PR
2. Klikni na karticu **"Files changed"** — vidiš točno koje linije su komentirane
3. Klikni na karticu **"Conversation"** — vidiš sve komentare kronološki

### Kako ispraviti prema komentarima

1. Vrati se u **Obsidian**
2. Otvori datoteku koja je komentirana
3. Napravi tražene izmjene
4. **Stage All -> Commit -> Push**

> ℹ️ **Automatsko ažuriranje PR-a:** Ne moraš otvarati novi PR. Svaki novi commit na isti branch automatski se pojavljuje u otvorenom PR-u. Recenzent vidi sve promjene u realnom vremenu.

5. Na GitHubu, odgovori na komentar: klikni **"Resolve conversation"** kada si riješio/la tu točku

### Bonton PR komunikacije

| Situacija | Preporučeni odgovor |
|-----------|-------------------|
| Slažeš se s komentarom | Napravi izmjenu, klikni "Resolve conversation" |
| Ne razumiješ komentar | Odgovori pitanjem u komentaru, ne pretpostavljaj |
| Ne slažeš se | Objasni razlog u komentaru — odluku donosi maintainer |
| Komentar je zastario | Napiši "Riješeno u commitu abc123" i zatvori |

***

## 8.7 Provjera prije nego pushaš PR na recenziju

Kratka kontrolna lista koju prođeš sam/a prije nego tražiš pregled:

```text
[ ] Sve datoteke su commitane i pushane
[ ] Naslov PR-a je jasan i opisuje sadržaj
[ ] Opis objašnjava što treba pregledati
[ ] Odabran je recenzent
[ ] Otvorio/la sam "Files changed" i pregledao/la vlastite promjene
[ ] Nema slučajno dodanih testnih redaka ili komentara tipa "TODO"
[ ] YAML zaglavlje je ispravno (naslov, autor, datum)
```

***

## ✅ Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Pull Request (PR)** | Formalni zahtjev za spajanje brancha u main, s procesom pregleda |
| **Reviewer** | Osoba koja pregledava i komentira PR |
| **Maintainer** | Osoba s pravom merganja u main |
| **Files changed** | GitHub prikaz točno što se promijenilo, redak po redak |
| **Resolve conversation** | Označavanje komentara kao riješenog |
| **PR se ažurira automatski** | Svaki novi commit na branch pojavljuje se u otvorenom PR-u |

***















