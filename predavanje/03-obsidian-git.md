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

> ℹ️ **Napomena o prijavi:** Ako repozitorij nije javno dostupan, Git/Windows će pri prvom preuzimanju ili slanju (Push/Pull) prikazati prozor za prijavu. Odaberi prijavu putem Tokena i zalijepi svoj PAT token. Tvoj sustav (npr. Git Credential Manager na Windowsima) će ga zapamtiti i više te neće tražiti.

> ⚠️ **Ako kloniranje ne radi — provjeri ove 3 stvari:**
> 1. Jesi li primio/la pozivnicu za repozitorij i prihvatio/la je? (Poglavlje 2.4)
> 2. Jesi li unio/la **PAT token** (ne GitHub lozinku) kada je terminal to zatražio?
> 3. Je li PAT token još uvijek važeći? Provjeri u GitHub Settings → Developer settings.

✅ **Provjera uspjeha:** Smanji sve prozore i pogledaj svoju Radnu površinu. Tamo bi se sada trebao nalaziti novi folder pod nazivom `EU-Project-Template`.

***

## 3.3 Otvaranje kloniranog repozitorija kao Obsidian vault

Sada imamo datoteke na računalu. Otvorimo ih u Obsidianu.

> 💡 **Savjet:** U Obsidianu se svaki projektni folder naziva **Vault** (trezor). Svaki projekt koji otvoriš u Obsidianu je zasebni vault s vlastitim postavkama i pluginovima.

### Korak po korak

1. Pokreni **Obsidian**
2. Na početnom ekranu klikni na **"Open folder as vault"** (Otvori mapu kao trezor)
3. Otvorit će se prozor za odabir foldera. Pronađi Radnu površinu (Desktop), klikni na folder `EU-Project-Template` i pritisni **Select Folder**
4. Ako Obsidian pita `"Do you trust the authors of the files in this folder?"`, odaberi **"Trust author and enable plugins"**

> ⚠️ **Važno:** Klik na "Trust author and enable plugins" je obavezan — bez toga Obsidian Git plugin neće raditi. Ova poruka se pojavljuje samo jednom, pri prvom otvaranju vaulta.

✅ **Provjera uspjeha:** S lijeve strane Obsidian ekrana sada vidiš popis datoteka i foldera tvog projekta. (Napomena: Nakon odabira “Trust author and enable plugins”, u nekim se slučajevima mogu automatski otvoriti postavke aplikacije ili Community plugins sekcija).

***

## 3.4 Aktivacija predinstaliranog Git plugina

U našem projektu `EU-Project-Template`, najvažniji plugini su **već unaprijed instalirani**. Kada si u prethodnom koraku kliknuo/la na **"Trust author and enable plugins"**, Obsidian je automatski omogućio rad tih plugina. Zato ne moraš samostalno pretraživati niti instalirati plugin — on je već spreman!

### Korak 1: Kako provjeriti je li uključen

1. Klikni na ikonu **zupčanika** ⚙️ u donjem lijevom kutu (Settings / Postavke / Options).
2. U lijevom izborniku, na samom dnu pod sekcijom **"Community plugins"**, potraži stavku **"Git"**.
3. Ako je nema ili je isključena, klikni na **"Community plugins"** u lijevom izborniku i provjeri je li sklopka pored plugina **"Git"** (autor: Vinzent) uključena (zelena).

> ℹ️ **Napomena:** Budući da je projektni predložak postavljen tako da vjeruješ autorima, Obsidian je već omogućio community plugine i instalirao plugin **Git**. Neće se prikazati nikakva sigurnosna upozorenja jer si odobrenje dao/la pri otvaranju foldera.

✅ **Provjera uspjeha:** U lijevom izborniku Options-a, na dnu u sekciji **"Community plugins"** trebala bi se pojaviti nova stavka **"Git"**.

***

## 3.5 Konfiguracija plugina – autentikacija

Ovo je najvažniji korak — ovdje unosimo podatke o autoru da Git zna tko radi izmjene.

1. U Options izborniku klikni na **"Git"**
2. Skrolaj do sekcije **"Commit Author"**
3. Ispuni sljedeća polja u sekciji **"Commit Author"**:

| Polje | Što upisati | Primjer |
|-------|------------|---------|
| **Author name** | Tvoje ime i prezime | `Ana Kovač` |
| **Author email** | E-mail vezan uz GitHub račun | `ana@primjer.com` |

> ⚠️ **Upozorenje:** Author name i Author email moraju biti **isti** kao oni koje si postavio/la u Git konfiguraciji (Poglavlje 2.1, Korak 4). Inače će tvoje promjene biti pripisane drugom identitetu.

> 🔑 **Gdje upisati PAT token i korisničko ime?**
> U modernoj verziji plugina u postavkama **nema polja za Username i Password/Token**. To je zbog sigurnosti. Umjesto toga, kada prvi put napraviš Commit i pokušaš poslati rad (Push), otvorit će se prozor za prijavu na GitHub. Tamo odaberi opciju **"Token"** i zalijepi svoj PAT token. Nakon toga će tvoj sustav zapamtiti prijavu i više te neće tražiti!

***

## 3.6 Konfiguracija plugina – automatizacija

Ostale postavke koje preporučujemo za svakodnevni rad:

### Automatski pull

Skrolaj do sekcije **"Automatic"**:

Postavi sljedeće opcije automatizacije:

- U sekciji **"Pull"** postavi **Pull on startup** na uključeno.
- U sekciji **"Automatic"** postavi **Auto pull interval (minutes)** na `0` (isključeno).

> ℹ️ **Napomena za Push:** Ako ne vidiš postavku "Push on commit" ili "Auto push", to znači da ćeš promjene slati ručno klikom na gumb za Push ili kroz Command Palette. To je i sigurnije jer imaš kontrolu nad time kada šalješ svoj rad.

> 💡 **Zašto isključiti automatski pull interval?** Automatski pull može prekinuti pisanje u neočekivanom trenutku. Bolja navika za početnike: ručno povuci promjene ujutro kada sjedneš raditi.

### Commit poruke

Skrolaj do sekcije **"Commit message"**:

| Postavka | Preporučena vrijednost |
|----------|----------------------|
| **Commit message on manual commit** | `{{date}} - {{hostname}}: {{numFiles}} datoteka izmijenjeno` |
| **Date format** | `YYYY-MM-DD HH:mm` |

> 💡 **Objašnjenje commit poruke:** `{{date}}` automatski upiše datum i vrijeme, `{{hostname}}` ime tvog računala, `{{numFiles}}` broj izmijenjenih datoteka. Rezultat izgleda ovako: `2024-03-15 09:30 - ANA-LAPTOP: 2 datoteke izmijenjeno`.

***

## 3.7 Pregled sučelja plugina

Nakon konfiguracije, plugin dodaje nekoliko elemenata u Obsidian sučelje:

### Source Control panel (bočna traka)

Klikni na Git ikonu (izgleda kao grananje ili Git simbol) u bočnoj traci (kod tebe je na lijevoj traci). Pritisak na prečac `Ctrl+Shift+G` radi samo ako je ta kratica ručno podešena u Obsidian postavkama.

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
| **↓ Pull** | Preuzima najnovije promjene s GitHuba |
| **⊕ Stage All** | Označava sve promjene kao "spremne za commit" |
| **✓ Commit** | Sprema promjene s opisnom porukom |
| **↑ Push** | Šalje commitove na GitHub |

### Status bar (statusna traka)

Na dnu Obsidian prozora (dolje desno) vidjet ćeš informacije o trenutnom stanju:

- Statusne podatke poput broja backlinks, riječi i znakova (npr. `0 backlinks | </> | 7 words | 51 characters`).
- Ikonu za sinkronizaciju (npr. prekriženu ikonu Obsidian Sync ako je isključen).
- Kvačicu `✓` (koja na prijelaz miša / hover prikazuje kada je napravljen zadnji commit, npr. "Last commit: 7 days ago").
- Naziv trenutne grane (npr. `main` ili `sime/uvod`). Klikom na naziv grane otvara se izbornik za brzo prebacivanje na druge grane!

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

Kada pogledaš lijevi izbornik u Obsidianu, vidjet ćeš popis datoteka i mapa tvog projekta. Primijeti da su neke mape i datoteke skrivene u Obsidianu i vidljive su samo u Windows Exploreru jer ih Obsidian ne podržava ili započinju s točkom.

| Ime foldera/datoteke | Vidljivost u Obsidianu | Namjena | Što ti radiš s tim? |
| :---- | :---- | :---- | :---- |
| `.obsidian` | ❌ Skriven | Postavke i plugini Obsidiana. | **Ne diraj** bez razloga. |
| `.github` | ❌ Skriven | Postavke za GitHub Actions (automatski render). | **Ne diraj.** |
| `Slike` (ili `images`) | ✅ Vidljiv | Mapa za vizualne materijale. (Ako ne postoji u projektu, slobodno je sam/a kreiraj). | **Koristiš.** Tu spremaš slike. |
| `*.md` ili `*.qmd` | ✅ Vidljiv | Tvoji tekstualni dokumenti. Ekstenzije (`.md`/`.qmd`) su sakrivene u Obsidianu, vidi se samo naziv. | **Ovdje pišeš.** |
| `_quarto.yml` | ❌ Skriven | Konfiguracija knjige. | **Oprezno.** |
| `template.docx` | ❌ Skriven | Word predložak za oblikovanje dokumenta. | **Ne diraj.** |

: Struktura repozitorija {tbl-colwidths="[20,20,30,30]"}

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




