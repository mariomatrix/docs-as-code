---
title: "Poglavlje 2 - Instalacija i postavljanje okruzenja"
---

> **Procijenjeno vrijeme:** 60–90 minuta (jednokratno)
> **Primarno za:** Windows 10/11
> **Korisnici macOS-a:** Tamo gdje se postupak razlikuje, označeno je posebnom napomenom.

U ovom poglavlju instaliramo sve alate i kreiramo račune koje ćeš koristiti svaki dan. Ovo radiš **samo jednom** — nakon postavljanja, svakodnevni rad ne zahtijeva ponovnu instalaciju.


## 2.1 Git – instalacija

### Što je Git i zašto ga instaliramo?

Git je program koji radi u pozadini i **prati sve promjene** u tvojim datotekama. Obsidian Git plugin (kojeg instaliramo u Poglavlju 3) koristi Git ispod haube — bez njega plugin ne može raditi.

### Korak 1: Preuzimanje

1. Otvori preglednik i idi na: **https://git-scm.com/download/win**
2. Preuzimanje će se automatski pokrenuti za tvoj Windows
3. Sačekaj da se preuzme datoteka (npr. `Git-2.44.0-64-bit.exe`)

> **macOS:** Idi na https://git-scm.com/download/mac i slijedi upute za instalaciju putem Homebrew-a, ili jednostavno otvori Terminal i upiši `git --version` — macOS će ponuditi automatsku instalaciju.

### Korak 2: Instalacija (Windows)

1. Pokreni preuzetu `.exe` datoteku dvostrukim klikom
2. Prihvati sve zadane opcije klikom na **Next** kroz cijeli instalacijski čarobnjak
3. Na ekranu **"Choosing the default editor used by Git"** — ostavi zadanu opciju (Vim) ili odaberi **Notepad** ako se osjećaš nelagodno s Vimom. Za naš rad, ovo nije važno jer editor koristimo samo u Obsidianu.
4. Na ekranu **"Adjusting your PATH environment"** — obavezno odaberi **"Git from the command line and also from 3rd-party software"** (srednja opcija). Ovo omogućava Obsidianu da pronađe Git.
5. Sve ostalo — klikaj **Next** i na kraju **Install**

> **Upozorenje:** Ako instalacijski čarobnjak pita za administratorsku lozinku, upiši ju — instalacija zahtijeva administratorska prava.

### Korak 3: Provjera instalacije

1. Pritisni tipke **Windows + R** na tipkovnici
2. Upiši `cmd` i pritisni Enter — otvara se crni prozor (Command Prompt)
3. Upiši sljedeću naredbu i pritisni Enter:

```cmd
git --version
```

**Provjera uspjeha:** Trebao/la bi vidjeti nešto poput:
```cmd
git version 2.44.0.windows.1
```

> **Ako vidiš grešku** `'git' is not recognized...` — Git nije ispravno instaliran. Ponovi instalaciju i provjeri jesi li na koraku 4 odabrao/la srednju opciju za PATH.

### Korak 4: Konfiguracija identiteta

Git treba znati tko si — ovo ime i e-mail će se prikazivati uz svaku promjenu koju napraviš.

U istom crnom prozoru (Command Prompt) upiši ove dvije naredbe, **zamijeni tekst u navodnicima** s tvojim stvarnim imenom i e-mailom:

```cmd
git config --global user.name "Ime Prezime"
```

```cmd
git config --global user.email "tvoj.email@primjer.com"
```

> **Savjet:** Koristi **isti e-mail koji ćeš koristiti za GitHub račun** (kreiramo ga u koraku 2.4). To pomaže GitHubu da ispravno poveže tvoje doprinose s tvojim profilom.

**Provjera:** Provjeri jesu li podaci ispravno uneseni:
```cmd
git config --global user.name
git config --global user.email
```
Svaka naredba ispisat će vrijednost koju si upravo postavio/la.

***

## 2.2 Obsidian – instalacija

### Što je Obsidian?

Obsidian je editor — program za pisanje teksta. Koristit ćeš ga svaki dan za pisanje dokumentacije. Izgleda kao Word, ali sprema datoteke u jednostavan tekstualni format koji Git može pratiti.

### Korak 1: Preuzimanje

1. Idi na: **https://obsidian.md**
2. Klikni na veliki gumb **"Download"**
3. Odaberi verziju za **Windows** (`.exe` instalacijska datoteka)

> **macOS:** Odaberi `.dmg` verziju i instaliraj kao i svaki drugi Mac program (odvuci u Applications).

### Korak 2: Instalacija

1. Pokreni preuzetu `.exe` datoteku
2. Obsidian se instalira automatski — nema čarobnjaka s opcijama
3. Obsidian će se automatski pokrenuti nakon instalacije

### Korak 3: Početni ekran

Kada se Obsidian prvi put pokrene, prikazuje se ekran dobrodošlice s opcijama. **Nemoj još ništa birati** — vault (projektni folder) kreirat ćemo u Poglavlju 4, kada kloniramo repozitorij.

Možeš zatvoriti Obsidian za sada.

**Provjera uspjeha:** Obsidian se pokrenuo i prikazuje početni ekran.

***

## 2.3 Quarto – instalacija

### Što je Quarto?

Quarto je alat koji radi u pozadini — pretvara tvoje tekstualne datoteke u finalne Word dokumente. Nećeš ga koristiti direktno svaki dan, ali mora biti instaliran da bi automatizacija (GitHub Actions) i lokalni pregled funkcionirali.

### Korak 1: Preuzimanje

1. Idi na: **https://quarto.org/docs/get-started/**
2. Klikni na gumb za preuzimanje za **Windows** (`.msi` datoteka)

> **macOS:** Preuzmi `.pkg` verziju.

### Korak 2: Instalacija

1. Pokreni preuzetu `.msi` datoteku
2. Prihvati sve zadane opcije i klikaj **Next** do kraja
3. Klikni **Finish**

### Korak 3: Provjera instalacije

1. Zatvori i ponovo otvori Command Prompt (Windows + R -> `cmd`)
2. Upiši:

```cmd
quarto check
```

**Provjera uspjeha:** Nakon nekoliko sekundi vidjet ćeš popis provjera. Važno je da nema crvenih grešaka za osnovne komponente. Upozorenja (žuta) su u redu.

> **Ako naredba nije prepoznata:** Restart računala i pokušaj ponovo — instalacija Quarta ponekad zahtijeva ponovno pokretanje računala da bi se PATH ažurirao.

***

## 2.4 GitHub – kreiranje računa

### Što je GitHub?

GitHub je online platforma gdje se pohranjuje sva dokumentacija projekta. Svaki član tima ima vlastiti račun. Kroz GitHub koordiniramo tko radi što i pregledavamo tuđi rad.

### Korak 1: Registracija

1. Idi na: **https://github.com**
2. Klikni na **"Sign up"** u gornjem desnom kutu
3. Upiši svoju **e-mail adresu** (isti e-mail koji si koristio/la u Git konfiguraciji!)
4. Kreiraj **lozinku** — GitHub traži minimalnu duljinu i složenost
5. Odaberi **korisničko ime** (username) — ovo će biti vidljivo svim članovima tima. Preporuka: `ime-prezime` ili varijanta

> **Savjet za korisničko ime:** Odaberi nešto profesionalno jer će biti vidljivo u svim pull requestima i komentarima. Primjeri: `ana-kovac`, `pero-novak`, `mj-horvat`

6. Dovrši verifikaciju (puzzle ili slično)
7. GitHub će poslati **verifikacijski e-mail** — otvori ga i klikni na link za potvrdu

### Korak 2: Traženje pristupa repozitoriju

Samo kreiranje računa nije dovoljno — administrator projekta mora te **dodati u tim** koji ima pristup repozitoriju.

Nakon kreiranja računa, pošalji administratoru projekta:
- Svoje GitHub **korisničko ime**
- Svoju **e-mail adresu** vezanu uz GitHub

Administrator će ti poslati pozivnicu na e-mail. **Klikni na link u e-mailu** da prihvatiš pozivnicu. Tek tada ćeš imati pristup repozitoriju.

***

## 2.5 Personal Access Token (PAT) – postavljanje autentikacije

### Zašto nam treba PAT?

Kada Obsidian šalje tvoje promjene na GitHub, GitHub mora znati da si zaista ti — a ne netko tko se lažno predstavlja. Umjesto lozinke, GitHub koristi **Personal Access Token** (PAT) — poseban ključ koji koristimo samo za ovaj tip pristupa.

> ℹ️ **Za razumijevanje:** PAT je poput privremene propusnice — možeš ga poništiti u bilo kojem trenutku ako sumnjaš da ga je netko drugi dobio.

### Korak 1: Kreiranje PAT-a na GitHubu

1. Prijavi se na **https://github.com**
2. Klikni na svoju **profilnu sliku** u gornjem desnom kutu
3. Odaberi **Settings** (Postavke)
4. U lijevom izborniku skrolaj do dna i klikni na **Developer settings**
5. Klikni na **Personal access tokens** -> **Tokens (classic)**
6. Klikni na gumb **"Generate new token"** -> **"Generate new token (classic)"**

### Korak 2: Konfiguracija tokena

Na ekranu za kreiranje tokena:

- **Note** (naziv): Upiši npr. `Obsidian-Git-token` — da znaš čemu služi
- **Expiration** (trajanje): Odaberi **90 days** ili **1 year** ovisno o preferenciji tima

> **Savjet:** Kada token istekne, moraš kreirati novi i ponoviti korake 3 i 4 iz ovog poglavlja. Postavi podsjetnik u kalendar.

- **Odaberi ovlasti (scopes):** Stavi kvačicu samo na **`repo`** — ovo je sve što trebaš za rad s repozitorijem

7. Skrolaj do dna i klikni **"Generate token"**

### Korak 3: Kopiranje i pohrana tokena

> **VAŽNO:** Token ćeš vidjeti **samo jednom**. Kada zatvoriš ovu stranicu, više ga nećeš moći vidjeti. GitHub pokazuje token samo u trenutku kreiranja.

1. Klikni na ikonu kopiranja pored tokena (ili označi tekst i kopiraj Ctrl+C)
2. Odmah ga spremi na **sigurno mjesto** — primjeri:
   - Privatna bilješka u password manageru (preporuka)
   - Zaštićena tekstualna datoteka na računalu
   - Privremeno: nalijepi ga u Notepad dok ga ne postaviš u Obsidian

Token izgleda otprilike ovako (ovo je primjer, ne koristi ga):
```text
ghp_ABCDEFGHijklmnopQRSTUVWXYZ123456789
```

### Korak 4: Pohrana tokena

Token ćeš upisati direktno u **Obsidian Git plugin** u sljedećem poglavlju — nema potrebe za dodatnim koracima ovdje.

> **Savjet:** Ostavi token kopiran u Notepadu ili na sigurnom mjestu dok ne završiš postavljanje plugina u Poglavlju 3 — tamo ćeš ga unijeti na točno određeno mjesto u postavkama.

**Provjera uspjeha:** Token je kreiran i pohranjen na sigurnom mjestu, spreman za unos u Obsidian.

***

## 2.6 .gitignore – što dijelimo, a što ne

### Što je .gitignore?

`.gitignore` je tekstualna datoteka koja Git-u govori koje datoteke i foldere treba **ignorirati** — tj. nikada ih ne pratiti niti slati na GitHub.

### Zašto je to važno za Obsidian?

Obsidian pohranjuje svoje postavke u skriveni folder `.obsidian/`. Taj folder sadrži:

| Sadržaj | Treba dijeliti? | Razlog |
|---------|----------------|--------|
| `plugins/` | **Da** | Da svi imaju iste plugine |
| `app.json` | **Da** | Zajedničke postavke aplikacije |
| `workspace.json` | Ne | Osobne postavke prozora — razlikuju se po računalu |
| `cache` | Ne | Privremene datoteke — automatski se kreiraju |

### Primjer .gitignore za ovaj projekt

Datoteka `.gitignore` već postoji u repozitoriju. Ovako izgleda relevantni dio za Obsidian:

```gitignore
# Obsidian – osobne postavke koje NE dijelimo
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache

# Obsidian – ove datoteke DIJELIMO (plugin konfiguracija)
# (nisu navedene u .gitignore, što znači da Git ih prati)
# .obsidian/plugins/
# .obsidian/app.json
# .obsidian/community-plugins.json

# Sistemske datoteke
.DS_Store          # macOS metapodaci
Thumbs.db          # Windows metapodaci
desktop.ini        # Windows postavke foldera

# Quarto output (generirani dokumenti)
/_site/
/.quarto/
```

> **Savjet:** Ne moraš mijenjati `.gitignore` datoteku. Administrator projekta već je postavio ispravne postavke u repozitoriju koji ćeš klonirati. Ovo je samo objašnjenje zašto neke datoteke vidiš, a neke ne.

***

## Što smo naučili u ovom poglavlju

| Alat/Korak | Status |
|------------|--------|
| Git instaliran i konfiguriran s imenom i e-mailom | [ ] |
| Obsidian instaliran | [ ] |
| Quarto instaliran i provjeren | [ ] |
| GitHub račun kreiran i verificiran | [ ] |
| Pozivnica za repozitorij prihvaćena | [ ] |
| PAT kreiran i sigurno spremljen | [ ] |

> **Savjet:** Iskoristi gornju tablicu kao checklistu — označi svaki korak koji si dovršio/la. Ako nešto nije funkcioniralo, ne prelazi na sljedeće poglavlje — svaki alat ovisi o prethodnom.

***

**<- Prethodno poglavlje:** [Poglavlje 1 – Uvod](01-uvod.md)
**Sljedeće poglavlje:** [Poglavlje 3 – Obsidian Git plugin ->](03-obsidian-git.md)







