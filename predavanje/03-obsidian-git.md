---
title: "Poglavlje 3 - Obsidian Git plugin: instalacija i konfiguracija"
---

> **Procijenjeno vrijeme:** 15–20 minuta
> **Preduvjet:** Git instaliran (Poglavlje 2.1), PAT token kreiran i negdje pohranjen (Poglavlje 2.5)

> **Važno:** Ovo poglavlje radi **bez kloniranog repozitorija** — plugin instaliramo dok Obsidian radi na privremenom vaultu. U Poglavlju 4 otvorit ćemo pravi projektni repozitorij.

***

## 3.1 Pokretanje Obsidiana i privremeni vault

Obsidian ne može raditi bez **vaulta** (hrv. *trezor*) — foldera koji je postavljen kao radni prostor. Budući da još nismo klonirali repozitorij, koristit ćemo privremeni vault samo za instalaciju plugina.

1. Pokreni **Obsidian**
2. Na početnom ekranu klikni **"Create new vault"**
3. Daj mu bilo koji naziv (npr. `privremeni`) i odaberi lokaciju (npr. Desktop)
4. Klikni **"Create"**

Obsidian se otvara s praznim vaultom. Sad možemo instalirati plugin.

***

## 3.2 Omogućavanje Community plugina

Obsidian dolazi s ugrađenim pluginima, ali **Obsidian Git** je *community plugin* — plugin kojeg su razvili vanjski developeri, nije dio službenog Obsidiana.

Da bi koristili community plugine, moramo ih najprije omogućiti:

1. Klikni na ikonu **zupčanika** ⚙️ u donjem lijevom kutu (Settings / Postavke)
2. U lijevom izborniku klikni na **"Community plugins"**
3. Vidjet ćeš upozorenje: *"Community plugins can execute arbitrary code..."*

> **O sigurnosnom upozorenju:** Ovo upozorenje postoji jer community plugine pišu vanjski developeri. **Obsidian Git** je jedan od najpopularnijih i najprovjerenijih plugina s desetcima tisuća korisnika i otvorenim izvornim kodom. Prihvati upozorenje.

4. Klikni na **"Turn on community plugins"**
5. Potvrdi klikom na **"Turn on"**

***

## 3.3 Instalacija Obsidian Git plugina

1. U istom ekranu (Community plugins), klikni na gumb **"Browse"** (Pregledaj)
2. U polje za pretraživanje upiši: `Obsidian Git`
3. U rezultatima klikni na **"Obsidian Git"** (autor: Vinzent03)
4. Klikni na gumb **"Install"**
5. Nakon instalacije klikni na **"Enable"** (Omogući)

**Provjera uspjeha:** U lijevom izborniku Settings-a trebala bi se pojaviti nova stavka **"Obsidian Git"** pod sekcijom *Plugin Options*.

***

## 3.4 Konfiguracija plugina – autentikacija

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

> **Savjet:** Polje za token izgleda kao obično tekstualno polje — token upisuješ ili lijepiš (Ctrl+V) direktno u njega. Ne skrivaj ga u lozinkovnom manageru sada — Obsidian ga sam sigurno pohranjuje.

> **Upozorenje:** Author name i Author email moraju biti **isti** kao oni koje si postavio/la u Git konfiguraciji (Poglavlje 2.1, Korak 4). Inače će tvoje promjene biti pripisane drugom identitetu.

***

## 3.5 Konfiguracija plugina – automatizacija

Ostale postavke koje preporučujemo za svakodnevni rad:

### Automatski pull

Skrolaj do sekcije **"Automatic"**:

| Postavka | Preporučena vrijednost | Objašnjenje |
|----------|----------------------|-------------|
| **Pull updates on startup** | Uključeno | Svaki put kad otvoriš Obsidian, automatski preuzme najnovije promjene kolega |
| **Pull interval (minutes)** | `0` (isključeno) | Automatski pull svakih N minuta — za početnike isključi, radi ručno |
| **Push on commit** | Uključeno | Nakon svakog commita, automatski šalje promjene na GitHub |

> **Zašto isključiti automatski pull interval?** Automatski pull može prekinuti pisanje u neočekivanom trenutku. Bolja navika za početnike je: ručno povuci promjene ujutro kada sjedneš raditi.

### Commit poruke

Skrolaj do sekcije **"Commit"**:

| Postavka | Preporučena vrijednost |
|----------|----------------------|
| **Commit message** | `{{date}} - {{hostname}}: {{numFiles}} datoteka izmijenjeno` |
| **Date format** | `YYYY-MM-DD HH:mm` |

> **Objašnjenje commit poruke:** `{{date}}` automatski upiše datum i vrijeme, `{{hostname}}` ime tvog računala, `{{numFiles}}` broj izmijenjenih datoteka. Rezultat izgleda ovako: `2024-03-15 09:30 - ANA-LAPTOP: 2 datoteke izmijenjeno`.

***

## 3.6 Pregled sučelja plugina

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
- **Current branch:** na kojoj si grani (više o granama u Poglavlju 6)
- **v0** — nema novih promjena za preuzeti s GitHuba
- **^2** — imaš 2 commita koja još nisu poslana na GitHub

***

## 3.7 Što plugin radi automatski, a što ručno

| Radnja | Automatski | Ručno |
|--------|-----------|-------|
| Pull pri pokretanju Obsidiana | (ako je uključeno) | Gumb v Pull |
| Praćenje izmjena datoteka | uvijek | — |
| Stage promjena | Ne | Gumb "Stage All" |
| Commit | Ne | Gumb "Commit" |
| Push na GitHub | (nakon commita, ako je uključeno) | Gumb ^ Push |
| Kreiranje novog brancha | Ne | Command Palette (objašnjeno u Poglavlju 6) |

> **Preporučeni dnevni ritam:**
> 1. Otvori Obsidian -> automatski pull preuzima novosti
> 2. Piši dokument
> 3. Kada završiš logičnu cjelinu -> Stage All -> Commit
> 4. Na kraju radnog dana (ili češće) -> Push

***

## Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Community plugin** | Plugin razvijen od strane zajednice, nije dio službenog Obsidiana |
| **Autentikacija** | Obsidian Git koristi PAT token za slanje promjena na GitHub |
| **Source Control panel** | Pregled izmijenjenih datoteka i gumbi za commit/push |
| **Push on commit** | Automatsko slanje na GitHub nakon svakog commita |
| **Pull on startup** | Automatsko preuzimanje izmjena kolega pri pokretanju Obsidiana |

> **Napomena:** Plugin si konfigurirao/la u privremenom vaultu. Kada u Poglavlju 4 otvorimo pravi repozitorij kao novi vault, **morat ćeš ponoviti instalaciju i konfiguraciju plugina** — postavke se pohranjuju po vaultu, ne globalno. Proces je isti, a ovaj put znaš točno što radiš.

***

**<- Prethodno poglavlje:** [Poglavlje 2 – Instalacija](02-instalacija.md)
**Sljedeće poglavlje:** [Poglavlje 4 – Kloniranje repozitorija i kreiranje Obsidian vaulta ->](04-kloniranje-repozitorija.md)







