---
title: "Poglavlje 3 - Postavljanje radnog okruženja"
---



> ⏱️ **Procijenjeno vrijeme:** 25–35 minuta
> 📋 **Preduvjet:** Git instaliran (Poglavlje 2.1), PAT token kreiran i negdje pohranjen (Poglavlje 2.5)

***

## 3.1 Što je repozitorij i što znači "kloniranje"?

Prije nego što upišemo naredbu, važno je razumjeti što točno radimo.

**Repozitorij (ili skraćeno "repo")** je glavni direktorij (folder) tvog projekta koji se nalazi na internetu (na GitHubu). On sadrži sve datoteke, slike i kompletnu povijest svih promjena. Zamisli ga kao glavni, zajednički folder na Google Driveu.

**Kloniranje (Cloning)** nije obično preuzimanje (Download). Kada "skidaš" običnu datoteku s interneta, ona gubi vezu sa svojim izvorom. Kada **kloniraš** Git repozitorij, ti na svoje računalo preuzimaš identičnu, radnu kopiju koja trajno pamti odakle je došla i ostaje povezana s glavnim repozitorijem na GitHubu. To nam omogućuje kasnije slanje i preuzimanje novih promjena.

***

## 3.2 Kloniranje repozitorija na računalo

Sada ćemo klonirati projektni repozitorij na tvoju Radnu površinu (Desktop).

### Korak po korak

1. Otvori **Command Prompt** (Pritisni tipku Windows + R, upiši `cmd` i pritisni Enter).

> 🍎 **macOS:** Otvori aplikaciju **Terminal**.

2. Prebaci se u folder Desktop:

```cmd
cd Desktop
```

*(Ova naredba znači "Change Directory to Desktop" — prebaci me na Radnu površinu.)*

3. Upiši naredbu za kloniranje i pritisni Enter:

```cmd
git clone https://github.com/FGAG-docs/EU-Project-Template
```

4. Vidjet ćeš tekst koji ispisuje postotke (`Receiving objects: 100%...`). Git preuzima sve datoteke i cijelu povijest projekta s GitHuba na tvoje računalo.

> ℹ️ **Napomena o prijavi:** Ako repozitorij nije javno dostupan, terminal će tražiti tvoje GitHub korisničko ime i PAT token. Upiši ih kada se to zatraži. Ako si u Poglavlju 2 postavio/la Windows Credential Manager, ovaj korak će se odraditi automatski.

> ⚠️ **Ako kloniranje ne radi — provjeri ove 3 stvari:**
> 1. Jesi li primio/la pozivnicu za repozitorij i prihvatio/la je? (Poglavlje 2.4)
> 2. Jesi li unio/la **PAT token** (ne GitHub lozinku) kada je terminal to zatražio?
> 3. Je li PAT token još uvijek važeći? Provjeri u GitHub Settings → Developer settings.

✅ **Provjera uspjeha:** Smanji sve prozore i pogledaj svoju Radnu površinu. Tamo bi se sada trebao nalaziti novi folder pod nazivom `EU-Project-Template`.

***

## 3.3 Otvaranje kloniranog repozitorija kao Obsidian vault

Sada imamo datoteke na računalu. Otvorimo ih u Obsidianu.

> 💡 **Savjet:** U Obsidianu se svaki projektni folder naziva **Vault** (trezor). Svaki projekt koji otvoriš u Obsidianu je zasebni vault s vlastitim postavkama i pluginima.

### Korak po korak

1. Pokreni **Obsidian**
2. Na početnom ekranu klikni na **"Open folder as vault"** (Otvori mapu kao trezor)
3. Otvorit će se prozor za odabir foldera. Navigiraj na Radnu površinu (Desktop), klikni na folder `EU-Project-Template` i pritisni **Select Folder**
4. Ako Obsidian pita `"Do you trust the authors of the files in this folder?"`, klikni **"Trust author and enable plugins"**

> ⚠️ **Važno:** Klik na "Trust author and enable plugins" je obavezan — bez toga Obsidian Git plugin neće raditi. Ova poruka se pojavljuje samo jednom, pri prvom otvaranju vaulta.

✅ **Provjera uspjeha:** S lijeve strane Obsidian ekrana sada vidiš popis datoteka i foldera tvog projekta.

***

## 3.4 Instalacija Obsidian Git plugin

Obsidian dolazi s ugrađenim pluginima, ali **Obsidian Git** je *community plugin* — plugin razvijen od strane zajednice, nije dio službenog Obsidiana. Instaliramo ga direktno u ovaj vault, na pravi projekt.

### Korak 1: Omogući community plugine

1. Klikni na ikonu **zupčanika** ⚙️ u donjem lijevom kutu (Settings / Postavke)
2. U lijevom izborniku klikni na **"Community plugins"**
3. Vidjet ćeš upozorenje: *"Community plugins can execute arbitrary code..."*

> ℹ️ **O sigurnosnom upozorenju:** Ovo upozorenje postoji jer community plugine pišu vanjski developeri. **Obsidian Git** je jedan od najpopularnijih i najprovjerenijih plugina s desetcima tisuća korisnika i otvorenim izvornim kodom. Prihvati upozorenje.

4. Klikni na **"Turn on community plugins"**
5. Potvrdi klikom na **"Turn on"**

### Korak 2: Pronađi i instaliraj plugin

1. U istom ekranu (Community plugins), klikni na gumb **"Browse"** (Pregledaj)
2. U polje za pretraživanje upiši: `Obsidian Git`
3. U rezultatima klikni na **"Obsidian Git"** (autor: Vinzent03)
4. Klikni na gumb **"Install"**
5. Nakon instalacije klikni na **"Enable"** (Omogući)

✅ **Provjera uspjeha:** U lijevom izborniku Settings-a trebala bi se pojaviti nova stavka **"Obsidian Git"** pod sekcijom *Plugin Options*.

***

## 3.5 Konfiguracija plugina – autentikacija

Ovo je najvažniji korak — ovdje unosimo naš PAT token da Obsidian može komunicirati s GitHubom.

1. U Settings izborniku klikni na **"Obsidian Git"**
2. Skrolaj do sekcije **"Authentication/Commit Author"**
3. Ispuni sljedeća polja:

| Polje | Što upisati | Primjer |
|-------|------------|---------|
| **Username** | Tvoje GitHub korisničko ime | `ana-kovac` |
| **Password/Token** | PAT token koji si kreirao/la u Poglavlju 2.5 | `ghp_ABC...` |
| **Author name** | Tvoje ime i prezime | `Ana Kovač` |
| **Author email** | E-mail vezan uz GitHub račun | `ana@primjer.com` |

> 💡 **Savjet:** Polje za token izgleda kao obično tekstualno polje — token upisuješ ili lijepiš (Ctrl+V) direktno u njega. Obsidian ga sam sigurno pohranjuje.

> ⚠️ **Upozorenje:** Author name i Author email moraju biti **isti** kao oni koje si postavio/la u Git konfiguraciji (Poglavlje 2.1, Korak 4). Inače će tvoje promjene biti pripisane drugom identitetu.

***

## 3.6 Konfiguracija plugina – automatizacija

Ostale postavke koje preporučujemo za svakodnevni rad:

### Automatski pull

Skrolaj do sekcije **"Automatic"**:

| Postavka | Preporučena vrijednost | Objašnjenje |
|----------|----------------------|-------------|
| **Pull updates on startup** | Uključeno | Svaki put kad otvoriš Obsidian, automatski preuzme najnovije promjene kolega |
| **Pull interval (minutes)** | `0` (isključeno) | Automatski pull svakih N minuta — za početnike isključi, radi ručno |
| **Push on commit** | Uključeno | Nakon svakog commita, automatski šalje promjene na GitHub |

> 💡 **Zašto isključiti automatski pull interval?** Automatski pull može prekinuti pisanje u neočekivanom trenutku. Bolja navika za početnike: ručno povuci promjene ujutro kada sjedneš raditi.

### Commit poruke

Skrolaj do sekcije **"Commit"**:

| Postavka | Preporučena vrijednost |
|----------|----------------------|
| **Commit message** | `{{date}} - {{hostname}}: {{numFiles}} datoteka izmijenjeno` |
| **Date format** | `YYYY-MM-DD HH:mm` |

> 💡 **Objašnjenje commit poruke:** `{{date}}` automatski upiše datum i vrijeme, `{{hostname}}` ime tvog računala, `{{numFiles}}` broj izmijenjenih datoteka. Rezultat izgleda ovako: `2024-03-15 09:30 - ANA-LAPTOP: 2 datoteke izmijenjeno`.

***

## 3.7 Pregled sučelja plugina

Nakon konfiguracije, plugin dodaje nekoliko elemenata u Obsidian sučelje:

### Source Control panel (bočna traka)

Klikni na ikonu **grananja** (<) u desnoj bočnoj traci (ili pritisni `Ctrl+Shift+G`).

Otvara se **Source Control** panel s:

```text
+---------------------------------+
|  SOURCE CONTROL          R  ^   |
+---------------------------------+
|  Changes (Promjene)             |
|  |-- dokument1.md       [M]     |  <- M = Modified
|  |-- novi-dokument.md   [U]     |  <- U = Untracked
|  |-- obrisan.md         [D]     |  <- D = Deleted
+---------------------------------+
|  [Stage All]  [Commit]  [Push]  |
+---------------------------------+
```

### Gumbi koje ćeš koristiti svaki dan

| Gumb | Što radi |
|------|----------|
| **v Pull** | Preuzima najnovije promjene s GitHuba |
| **Stage All** | Označava sve promjene kao "spremne za commit" |
| **Commit** | Sprema promjene s opisnom porukom |
| **^ Push** | Šalje commitove na GitHub |

### Status bar (statusna traka)

Na dnu Obsidian prozora vidjet ćeš informacije o trenutnom stanju:

```text
Current branch: main  |  v0  ^2
```

Što znači:
- **Current branch:** na kojoj si grani (više o granama u Poglavlju 3)
- **v0** — nema novih promjena za preuzeti s GitHuba
- **^2** — imaš 2 commita koja još nisu poslana na GitHub

***

## 3.8 Što plugin radi automatski, a što ručno

| Radnja | Automatski | Ručno |
|--------|-----------|-------|
| Pull pri pokretanju Obsidiana | (ako je uključeno) | Gumb v Pull |
| Praćenje izmjena datoteka | uvijek | — |
| Stage promjena | Ne | Gumb "Stage All" |
| Commit | Ne | Gumb "Commit" |
| Push na GitHub | (nakon commita, ako je uključeno) | Gumb ^ Push |
| Kreiranje novog brancha | Ne | Command Palette (objašnjeno u Poglavlju 3) |

> 💡 **Preporučeni dnevni ritam:**
> 1. Otvori Obsidian -> automatski pull preuzima novosti
> 2. Piši dokument
> 3. Kada završiš logičnu cjelinu -> Stage All -> Commit
> 4. Na kraju radnog dana (ili češće) -> Push

***

## 3.9 Razumijevanje strukture repozitorija

Kada pogledaš lijevi izbornik u Obsidianu, vidjet ćeš razne foldere i datoteke. Evo što svaki znači i što smiješ dirati:

| Ime foldera/datoteke | Namjena | Što ti radiš s tim? |
| :---- | :---- | :---- |
| `.obsidian` | Ovdje Obsidian čuva svoje postavke i plugine. | **Ne diraj** bez razloga. |
| `.github` | Upute za "robote" (GitHub Actions) koji automatski generiraju Word/PDF dokument. | **Ne diraj.** Ovo je posao administratora. |
| `Slike` (ili `images`) | Folder za sve vizualne materijale. | **Koristiš.** Tu spremaš slike za dokument. |
| `*.md` ili `*.qmd` datoteke | Tvoji tekstualni dokumenti (npr. `01-Uvod.md`). | **Ovdje pišeš.** |
| `_quarto.yml` | Konfiguracijska datoteka koja spaja sva poglavlja u jednu Word knjigu. | **Oprezno.** Mijenjaš samo kada dodaješ novo poglavlje. |
| `reference-doc.docx` | Word predložak koji definira fontove, naslove i boje. | **Ne diraj** osim ako nisi zadužen/a za vizualni identitet. |

: Struktura repozitorija {tbl-colwidths="[25,35,40]"}

> ℹ️ **Napomena o `.obsidian` folderu:** Sadrži i dijeljene postavke (plugini koje svi koriste) i osobne postavke (raspored prozora, koji se razlikuje po računalu). `.gitignore` je već podešen tako da se dijeljene postavke sinkroniziraju, a osobne ignoriraju.

> 💡 **Savjet:** Datoteke s nastavkom `.md` i `.qmd` su funkcionalno iste — obje otvaraš i uređuješ u Obsidianu na potpuno identičan način.

***

## ✅ Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Repozitorij** | Centralni folder projekta na GitHubu — zajednički izvor istine za cijeli tim |
| **Kloniranje** | Preuzimanje repozitorija na lokalno računalo uz zadržavanje veze s GitHubom |
| **Vault** | Obsidianov naziv za projektni folder koji se koristi kao radni prostor |
| **Community plugin** | Plugin razvijen od strane zajednice, nije dio službenog Obsidiana |
| **Autentikacija** | Obsidian Git koristi PAT token za slanje promjena na GitHub |
| **Source Control panel** | Pregled izmijenjenih datoteka i gumbi za commit/push |
| **Push on commit** | Automatsko slanje na GitHub nakon svakog commita |
| **Pull on startup** | Automatsko preuzimanje izmjena kolega pri pokretanju Obsidiana |

### Checklista

| Korak | Status |
|-------|--------|
| Razumijem razliku između "Downloada" i "Kloniranja" | [ ] |
| Uspješno sam pokrenuo/la naredbu `git clone` | [ ] |
| Folder `EU-Project-Template` nalazi se na mom Desktop-u | [ ] |
| Projekt je otvoren u Obsidianu kao vault | [ ] |
| Obsidian Git plugin je instaliran i omogućen | [ ] |
| PAT token je unesen u plugin postavke | [ ] |
| Znam koristiti Source Control panel (Stage All, Commit, Push) | [ ] |
| Znam u kojim folderima pišem, a koje sistemske foldere ne diram | [ ] |

***




