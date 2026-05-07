---
title: "Poglavlje 4 - Kloniranje repozitorija i kreiranje Obsidian vaulta"
---



**Procijenjeno vrijeme:** 10–15 minuta

**Cilj:** Preuzeti projekt s GitHuba na računalo i otvoriti ga u Obsidianu.

Sada kada su svi alati instalirani, vrijeme je da na svoje računalo preuzmemo stvarni projekt (dokumentaciju) na kojem ćemo raditi. Ovaj proces nazivamo **kloniranje**.

## **4.1 Što je repozitorij i što znači "kloniranje"?**

Prije nego što upišemo naredbu, važno je razumjeti što točno radimo.

**Repozitorij (ili skraćeno "repo")** je glavni direktorij (folder) tvog projekta koji se nalazi na internetu (na GitHubu). On sadrži sve datoteke, slike i kompletnu povijest svih promjena. Zamisli ga kao glavni, zajednički folder na Google Driveu.

**Kloniranje (Cloning)** nije obično preuzimanje (Download). Kada "skidaš" običnu datoteku s interneta, ona gubi vezu sa svojim izvorom. Kada **kloniraš** Git repozitorij, ti na svoje računalo preuzimaš identičnu, radnu kopiju koja trajno pamti odakle je došla i ostaje povezana s glavnim repozitorijem na GitHubu. To nam omogućuje kasnije slanje i preuzimanje novih promjena.

## **4.2 Kloniranje repozitorija na računalo**

Sada ćemo klonirati testni repozitorij na tvoju Radnu površinu (Desktop).

### **Korak po korak:**

1. Otvori **Command Prompt** (Pritisni tipku Windows \+ R, upiši cmd i pritisni Enter).

**macOS:** Otvori aplikaciju **Terminal**.

2. Prvo moramo reći terminalu u koji folder želimo spremiti projekt. Upiši sljedeću naredbu i pritisni Enter:  
   cd Desktop

   *(Ova naredba znači "Change Directory to Desktop" \- prebaci me na Radnu površinu).*  
3. Sada upiši naredbu za kloniranje (ili je kopiraj i zalijepi) i pritisni Enter:  
   git clone \[https://github.com/FGAG-docs/EU-Project-Template\](https://github.com/FGAG-docs/EU-Project-Template)

4. **Što se događa sada?**  
   Vidjet ćeš tekst koji ispisuje postotke (Receiving objects: 100%...). Git preuzima sve datoteke i cijelu povijest projekta s GitHuba na tvoje računalo.

ℹ️ **Napomena o prijavi:** Ako repozitorij nije javno dostupan, u ovom trenutku iskočit će prozor ili će terminal tražiti tvoje GitHub korisničko ime i lozinku. Kao lozinku **obavezno upiši onaj PAT token** koji si kreirao/la i spremio/la u Poglavlju 2\! (Ako si u Poglavlju 2 uspješno podesio/la Credential Manager, ovaj korak će se možda odraditi potpuno automatski).

✅ **Provjera uspjeha:** Smanji sve prozore i pogledaj svoju Radnu površinu. Tamo bi se sada trebao nalaziti novi folder pod nazivom EU-Project-Template.

## **4.3 Otvaranje kloniranog foldera kao Obsidian "Vault"**

Sada imamo datoteke na računalu, ali ih želimo uređivati u našem pametnom editoru. U Obsidianu se svaki projektni folder naziva **Vault** (trezor).

### **Korak po korak:**

1. Otvori program **Obsidian**.  
2. Ako ti se otvori onaj probni Vault iz Poglavlja 3, klikni na ikonu "Vault" u donjem lijevom kutu (izgleda kao sef s otvorenim vratima) kako bi otvorio/la glavni izbornik.  
3. U glavnom izborniku Obsidiana, pored opcije **"Open folder as vault"** (Otvori mapu kao trezor), klikni na gumb **Open**.  
4. Otvorit će se prozor za odabir foldera. Navigiraj na svoju Radnu površinu (Desktop), klikni na folder EU-Project-Template i pritisni **Select Folder** (ili Odaberi mapu).  
5. Ako te Obsidian pita "Do you trust the authors of the files in this folder?" (Vjeruješ li autorima...), klikni **"Trust author and enable plugins"**. Ovo je važno jer omogućava rad našem Obsidian Git pluginu.

✅ **Provjera uspjeha:** S lijeve strane Obsidian ekrana sada vidiš popis datoteka i foldera tvog projekta.

## **4.4 Razumijevanje strukture repozitorija**

Kada pogledaš lijevi izbornik u Obsidianu, vidjet ćeš razne foldere i datoteke. Ovdje je objašnjenje što oni znače i koje smiješ dirati:

| Ime foldera/datoteke | Namjena | Što ti radiš s tim? |
| :---- | :---- | :---- |
| .obsidian | Ovdje Obsidian čuva svoje postavke i plugine. | **Ne diraj.** Git je uglavnom podešen da ignorira tvoje lokalne promjene ovdje. |
| .github | Ovdje se nalaze upute za "robote" (GitHub Actions) koji automatski generiraju tvoj Word/PDF dokument. | **Ne diraj.** Ovo je posao administratora sustava. |
| Slike (ili images) | Folder u koji ubacujemo sve vizualne materijale. | **Koristiš.** Tu spremaš slike koje želiš umetnuti u dokument. |
| \*.md ili \*.qmd datoteke | Ovo su tvoji stvarni tekstualni dokumenti (npr. 01-Uvod.md, 02-Metodologija.qmd). | **Ovdje pišeš.** Ovo su datoteke na kojima ćeš raditi svaki dan. |
| \_quarto.yml | Konfiguracijska datoteka koja govori Quartu kako da spoji sve Markdown datoteke u jednu Word knjigu. | **Oprezno.** Mijenjaš samo kada dodaješ novo poglavlje u strukturu knjige. |
| reference-doc.docx | Prazan Word dokument koji služi kao vizualni predložak (definira fontove, veličine naslova, boje). | **Ne diraj** osim ako nisi zadužen/a za vizualni identitet dokumenta. |

: Struktura repozitorija {tbl-colwidths="[25,35,40]"}

**Savjet:** Markdown datoteke obično imaju nastavak .md, a u našem sustavu mogu imati i nastavak .qmd (Quarto Markdown). Za tebe kao pisca nema nikakve razlike – obje vrste otvaraš i uređuješ u Obsidianu na potpuno identičan način.

## ✅ Što smo naučili u ovom poglavlju

| Koncept / Korak | Status |
| :---- | :---- |
| Razumijem razliku između običnog "Downloada" i "Kloniranja" | [ ] |
| Znam pozicionirati terminal na Desktop pomoću komande cd Desktop | [ ] |
| Uspješno sam pokrenuo/la naredbu git clone ... | [ ] |
| Novi folder EU-Project-Template nalazi se na mom računalu | [ ] |
| Projekt je uspješno otvoren u Obsidianu (Open folder as vault) | [ ] |
| Znam u kojim folderima pišem, a koje sistemske foldere ne diram | [ ] |









