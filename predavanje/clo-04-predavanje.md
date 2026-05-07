# Poglavlje 4 – Kloniranje repozitorija i kreiranje Obsidian vaulta

---

> ⏱️ **Procijenjeno vrijeme:** 15–20 minuta
> 📋 **Preduvjeti:** Git instaliran (Pogl. 2.1), GitHub račun s prihvaćenom pozivnicom (Pogl. 2.4), PAT token kreiran (Pogl. 2.5)

---

## 4.1 Što je repozitorij i što znači kloniranje?

### Repozitorij

**Repozitorij** (skraćeno: *repo*) je folder projekta koji Git prati. Nije to samo folder s datotekama — uz datoteke, Git pohranjuje i **kompletnu povijest** svake promjene koja je ikad napravljena.

Projektni repozitorij živi na dva mjesta istovremeno:

```
┌─────────────────────┐          ┌─────────────────────┐
│  GitHub (online)    │          │  Tvoje računalo     │
│                     │          │  (lokalno)          │
│  FGAG-docs/         │◄────────►│  EU-Project-Template│
│  EU-Project-Template│  sinkrono│  (klonirana kopija) │
└─────────────────────┘          └─────────────────────┘
```

Ono što vidiš na GitHubu i ono što imaš na računalu je **ista stvar** — samo sinkronizirana. Kada radiš lokalno i pushaš promjene, GitHub se ažurira. Kada kolega pusha promjene, ti ih preuzimeš (pull).

### Kloniranje

**Kloniranje** je jednokratni postupak kojim preuzimamo kompletni repozitorij s GitHuba na svoje računalo — sa svim datotekama i kompletnom poviješću promjena.

> ℹ️ **Analogija:** Kloniranje je kao "checkout" knjige iz knjižnice. Knjiga (repozitorij) postoji u knjižnici (GitHub), a ti preuzimeš svoju kopiju. Kada napraviš bilješke (promjene) i "vratiš" ih (push), knjižnica ažurira svoju verziju.

---

## 4.2 Odabir lokacije za kloniranje

Prije kloniranja, odluči **gdje** na svom računalu želiš pohraniti projektni folder.

**Preporuke:**

✅ Dobra lokacija:
- `C:\Projekti\EU-Project-Template`
- `C:\Users\ImeKorisnika\Documents\Projekti\EU-Project-Template`

❌ Izbjegavaj:
- Desktop (postaje zakrčen)
- Mape koje sinkronizira OneDrive ili Google Drive — može uzrokovati konflikte s Git sinkronizacijom
- Putanje s **naglašenim slovima** (č, ć, š, ž, đ) — npr. `C:\Korisnici\Marković\` može uzrokovati probleme

> ⚠️ **OneDrive upozorenje:** Ako je tvoj `Documents` folder automatski sinkroniziran s OneDriveom (česta situacija na Windows računalima), **ne pohranjuj repo tamo**. Kreiraj folder direktno na `C:\` ili `D:\` disku.

---

## 4.3 Kloniranje putem Command Prompta

### Korak 1: Otvori Command Prompt u željenom folderu

1. Otvori **File Explorer** (Windows Explorer)
2. Navigiraj do foldera gdje želiš pohraniti projekt (npr. `C:\Projekti`)
3. Ako folder `Projekti` ne postoji — kreiraj ga (desni klik → New → Folder)
4. U adresnoj traci File Explorera klikni jednom da je označena, upiši `cmd` i pritisni Enter

```
[ C:\Projekti ]  ← klikni ovdje, upiši cmd, Enter
```

Otvara se Command Prompt direktno u tom folderu.

### Korak 2: Kloniraj repozitorij

U Command Promptu upiši točno ovu naredbu i pritisni Enter:

```
git clone https://github.com/FGAG-docs/EU-Project-Template.git
```

Git će zatražiti autentikaciju:

```
Username for 'https://github.com': ana-kovac
Password for 'https://ana-kovac@github.com':
```

- **Username:** upiši svoje GitHub korisničko ime
- **Password:** upiši (ili nalijepi Ctrl+V) svoj **PAT token** — ekran neće ništa pokazivati dok tipkaš, ali token se unosi

> 💡 **Savjet:** Za lijepljenje u Command Prompt koristi **desni klik miša** umjesto Ctrl+V.

Git preuzima repozitorij:

```
Cloning into 'EU-Project-Template'...
remote: Enumerating objects: 47, done.
remote: Counting objects: 100% (47/47), done.
Receiving objects: 100% (47/47), 1.23 MiB | 2.10 MiB/s, done.
```

✅ **Provjera uspjeha:** U `C:\Projekti\` sada postoji folder `EU-Project-Template` s datotekama projekta.

---

## 4.4 Otvaranje repozitorija kao Obsidian vault

Sada ćemo klonirani folder otvoriti u Obsidianu kao vault — naš radni prostor.

### Korak 1: Pokreni Obsidian

Ako je Obsidian otvoren s privremenim vaultom iz Poglavlja 3, zatvori ga i ponovo pokreni.

### Korak 2: Otvori folder kao vault

Na početnom ekranu Obsidiana:

1. Klikni na **"Open folder as vault"** (Otvori folder kao trezor)
2. U prozoru za odabir foldera navigiraj do `C:\Projekti\EU-Project-Template`
3. Klikni na folder (ne ulazi u njega — samo ga označi)
4. Klikni **"Select Folder"** (ili "Odaberi mapu")

> ⚠️ **Sigurnosni upit:** Obsidian može prikazati poruku *"Do you trust the author of this vault?"* — klikni **"Trust author and enable plugins"**. Ovo je potrebno da bi se automatski aktivirali plugini koji su konfigurirani u repozitoriju.

Obsidian se otvara s projektnim repozitorijem kao vaultom.

### Korak 3: Provjera Obsidian Git plugina

Budući da repozitorij već sadrži konfiguraciju plugina u `.obsidian/` folderu, Obsidian Git plugin trebao bi biti automatski prepoznat.

Provjeri:
1. Klikni na ⚙️ Settings → **Community plugins**
2. U popisu instaliranih plugina trebao bi se vidjeti **Obsidian Git** s toggleom na **ON**

> ⚠️ **Ako plugin nije aktivan:** Vrati se na Poglavlje 3.2 i 3.3 te ponovi instalaciju. Konfiguraciju (postavke) **ne moraš** ponavljati — one su preuzete iz repozitorija — ali **autentikaciju moraš** (korak ispod).

### Korak 4: Unos PAT tokena u novi vault

Postavke autentikacije se **ne pohranjuju u repozitorij** iz sigurnosnih razloga — svaki korisnik mora unijeti vlastiti token.

1. ⚙️ Settings → **Obsidian Git**
2. Skrolaj do sekcije **"Authentication/Commit Author"**
3. Unesi:
   - **Username:** tvoje GitHub korisničko ime
   - **Password/Token:** tvoj PAT token
   - **Author name** i **Author email:** kao u Poglavlju 3.4

✅ **Provjera uspjeha:** U statusnoj traci na dnu Obsidiana vidiš naziv brancha:
```
Current branch: main  |  ↓0  ↑0
```

---

## 4.5 Struktura repozitorija – što se gdje nalazi

Otvori lijevu bočnu traku u Obsidianu — vidiš popis svih datoteka i foldera u projektu.

Ovako izgleda tipična struktura `EU-Project-Template` repozitorija:

```
EU-Project-Template/
│
├── 📁 .github/
│   └── 📁 workflows/          ← GitHub Actions automatizacija (ne dirati)
│       └── render.yml
│
├── 📁 .obsidian/              ← Obsidian postavke (automatski upravljano)
│   ├── plugins/
│   └── app.json
│
├── 📁 docs/                   ← 📝 OVDJE PIŠEMO dokumentaciju
│   ├── 01-uvod.qmd
│   ├── 02-metodologija.qmd
│   └── ...
│
├── 📁 templates/              ← Predlošci dokumenata
│   └── EU-dokument-template.docx
│
├── 📁 output/                 ← Generirani dokumenti (automatski)
│
├── 📄 _quarto.yml             ← Quarto konfiguracija (ne dirati)
├── 📄 .gitignore              ← Popis datoteka koje Git ignorira
└── 📄 README.md               ← Upute za projekt
```

### Što ti kao autor/ica trebaš znati

| Folder/Datoteka | Što radiš s njim |
|----------------|-----------------|
| `docs/` | ✅ Ovdje pišeš. Sve tvoje `.qmd` datoteke idu ovdje |
| `templates/` | 👀 Pogledaj, ali ne mijenjaj bez dogovora s timom |
| `output/` | 👀 Ovdje završavaju generirani dokumenti — samo pregledavaj |
| `README.md` | 👀 Čitaj upute za projekt |
| `.github/` | 🚫 Ne dirati — automatizacija |
| `_quarto.yml` | 🚫 Ne dirati — konfiguracija renderiranja |
| `.obsidian/` | 🚫 Ne dirati ručno — Obsidian upravlja sam |

> 💡 **Savjet:** U Obsidianu možeš desnim klikom na folder `docs/` odabrati **"Set as attachment folder"** — sve što dodaš (slike, tablice) bit će automatski smješteno na pravo mjesto.

---

## 4.6 Test – provjera da sve funkcionira

Napravimo kratki test cijelog lanca prije nego prijeđemo na pravi rad.

### Korak 1: Napravi malu promjenu

1. U Obsidianu otvori `README.md`
2. Na kraju datoteke dodaj jedan prazan redak i upiši:
   ```
   <!-- test kloniranja - možeš obrisati -->
   ```
3. Spremi datoteku (Ctrl+S)

### Korak 2: Napravi commit

1. Otvori **Source Control** panel (Ctrl+Shift+G ili ikona grananja u desnoj traci)
2. Vidiš `README.md` u listi promjena s oznakom `[M]` (Modified)
3. Klikni **"Stage All"**
4. Klikni **"Commit"** — plugin automatski generira poruku s datumom
5. Klikni **"Push"** (ili je Push već automatski pokrenuto)

### Korak 3: Provjeri na GitHubu

1. Otvori preglednik i idi na `https://github.com/FGAG-docs/EU-Project-Template`
2. Klikni na `README.md`
3. Trebao/la bi vidjeti svoju izmjenu i tvoje ime/korisničko ime uz commit

✅ **Provjera uspjeha:** Tvoja promjena je vidljiva na GitHubu. Lokalna instalacija ispravno komunicira s GitHubom.

### Korak 4: Poništi testnu promjenu

Vrati `README.md` u originalno stanje — obriši redak koji si dodao/la, spremi, commit i push.

---

## ✅ Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Repozitorij** | Folder projekta koji Git prati, živi i lokalno i na GitHubu |
| **Kloniranje** | Jednokratno preuzimanje repozitorija s GitHuba na računalo |
| **Vault** | Obsidianov naziv za radni folder — u našem slučaju klonirani repo |
| **Struktura projekta** | `docs/` za pisanje, `output/` za generirane dokumente |
| **Test lanca** | Svaka nova instalacija treba biti testirana malim commit+push ciklusom |

---

**← Prethodno poglavlje:** [Poglavlje 3 – Obsidian Git plugin](03-obsidian-git-plugin.md)
**Sljedeće poglavlje:** [Poglavlje 5 – Podjela rada: koncept i primjer →](05-podjela-rada.md)