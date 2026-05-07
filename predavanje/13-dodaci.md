---
title: "Poglavlje 13 - Dodaci: Cheat Sheet, Rjecnik i Rjesavanje gresaka"
---

{{< pagebreak >}}

Ovo poglavlje služi kao tvoja "prva pomoć". Ne moraš ga čitati od početka do kraja. Spremi ga (ili isprintaj) kako bi mu se mogao/la brzo vratiti kada zaboraviš neku naredbu, kada čuješ nepoznat izraz ili kada sustav javi grešku.

## **13.1 Brzi referentni karton (Cheat Sheet)**

Sve najvažnije akcije koje radiš svaki dan, sažete na jednom mjestu.

| Akcija | Obsidian Git (Paleta: Ctrl+P) | Terminal (Git CLI) |
| :---- | :---- | :---- |
| **Preuzmi najnovije stanje** | Git: Pull | git pull origin main |
| **Napravi svoju radnu kopiju** | Git: Create branch | git checkout \-b ime/zadatak |
| **Provjeri gdje se nalaziš** | Pogledaj u donji desni kut Obsidiana | git branch |
| **Zabilježi promjenu** | Panel desno -> + -> Upiši poruku -> Commit | git add . git commit \-m "Poruka" |
| **Pošalji na GitHub** | Git: Push | git push origin ime-grane |
| **Živi pregled dokumenta** | *(Nema u Obsidianu)* | quarto preview |
| **Generiraj Word na računalu** | *(Nema u Obsidianu)* | quarto render |

: Cheat Sheet {tbl-colwidths="[30,35,35]"}

## **13.2 Rječnik pojmova (Što znači ta riječ?)**

IT industrija prepuna je engleskih izraza. Evo jednostavnih prijevoda onoga što znače u našem svakodnevnom radu:

* **Branch (Grana):** Tvoja izolirana, sigurna radna kopija projekta. Mjesto gdje slobodno pišeš i griješiš bez utjecaja na službeni dokument.  
* **Commit:** Čin trajnog spremanja (bilježenja) jedne logične cjeline teksta, uvijek popraćen kratkom porukom koja objašnjava što si napravio/la.  
* **Docs-as-Code:** Pristup u kojem dokumentaciju pišemo istim alatima kojima programeri pišu računalne programe (tekst, verzije, automatizacija).  
* **Git:** Softver koji radi u pozadini na tvom računalu i pamti cijelu povijest svake izmjene u tvojim datotekama (tvoj "vremenski stroj").  
* **GitHub:** Web stranica na kojoj se čuva glavna, zajednička kopija tvog projekta i gdje odobravaš tuđi rad.  
* **Main (Glavna grana):** Službena, finalna verzija tvog dokumenta. Nikada ne pišemo direktno u nju.  
* **Merge (Spajanje):** Čin prepisivanja tvog odobrenog rada s tvoje radne grane u službenu main granu.  
* **Pull Request / PR:** Službena molba kolegama koja kaže: "Završio sam, molim vas pregledajte moj rad i spojite ga u glavnu verziju."  
* **Pull (Povlačenje):** Preuzimanje najnovijih izmjena s GitHuba na tvoje računalo. (Radi to svako jutro\!)  
* **Push (Guranje/Slanje):** Slanje tvojih zabilježenih (commit) promjena s računala na GitHub.  
* **Render:** Proces u kojem Quarto uzima tvoj običan tekst, provlači ga kroz Word predložak i "isprinta" gotov dokument.  
* **Vault (Trezor):** Obsidianov naziv za glavni folder na tvom računalu u kojem se nalazi cijeli tvoj projekt.  
* **YAML (Metapodaci):** Blok teksta na samom vrhu index.md datoteke (ili u \_quarto.yml) koji sadrži podatke o dokumentu (naslov, autor, datum).

## **13.3 Top 10 najčešćih grešaka (Troubleshooting)**

Svi griješe, posebno na početku. Ovdje je popis 10 najčešćih problema i kako ih riješiti.

### **1\. "Nema mog novog poglavlja u Wordu\!"**

* **Simptom:** Napisao/la si predivan tekst u datoteku 04-zakljucak.md, ali Quarto ga nije ubacio u gotov Word.  
* **Rješenje:** Zaboravio/la si reći Quartu da to poglavlje postoji. Otvori datoteku \_quarto.yml i dodajte 04-zakljucak.md na popis pod sekcijom chapters.

### **2\. Slike se ne prikazuju (crveni križić u Quarto logu)**

* **Simptom:** Quarto javlja grešku File not found.  
* **Rješenje:** Provjeri jesi li zaista ubacio/la sliku u mapu Slike/ u Obsidianu. Zatim provjeri velika i mala slova. Git razlikuje velika i mala slova\! Slike/Graf.png nije isto što i Slike/graf.png.

### **3\. "GitHub ne prihvaća moju lozinku" (Authentication failed)**

* **Simptom:** Kada pokušaš napraviti Push ili Clone, terminal uporno traži lozinku i javlja grešku iako si upisao/la točnu lozinku tvog GitHub računa.  
* **Rješenje:** GitHub više ne dopušta obične lozinke. Moraš koristiti onaj dugi kod (PAT \- Personal Access Token) koji smo kreirali u Poglavlju 2\.

### **4\. "Ovaj dokument ima konflikte\!" (Merge Conflict)**

* **Simptom:** Prilikom pokušaja spajanja (Merge) na GitHubu gumb je siv i sustav prijavljuje konflikte.  
* **Rješenje:** Ti i kolega mijenjali ste isti redak teksta istovremeno. Klikni "Resolve conflicts" na GitHubu, obriši linije s \<\<\<\<\<\<\< i ostavi samo onaj tekst koji treba preživjeti.

### **5\. Gubitak Word formatiranja**

* **Simptom:** Ručno si popravio/la marginu i font u gotovom Word dokumentu, ali sljedeći dan je sve opet po starom.  
* **Rješenje:** Sjeti se zlatnog pravila iz Poglavlja 10: Gotov Word se **nikada** ne uređuje ručno. Sve vizualne promjene moraš napraviti u praznoj template.docx datoteci.

### **6\. Kolege ne vide moje promjene**

* **Simptom:** Ti vidiš tekst u Obsidianu, ali tvoj voditelj na GitHubu ne vidi ništa novo.  
* **Rješenje:** Vjerojatno si zaboravio/la odraditi **Push**. Ako si samo kliknuo/la "Commit" (spremi), promjene su sigurne, ali su i dalje samo na tvom računalu. Moraš napraviti Push.

### **7\. "Ne mogu napraviti Push na main\!"**

* **Simptom:** Pokušavaš poslati promjene, ali Git javlja grešku "Protected branch" ili "Permission denied".  
* **Rješenje:** Slučajno si počeo/la pisati tekst na glavnoj (main) grani, a ona je zaštićena. Otvori paletu (Ctrl+P), upiši Git: Create branch, napravi novu granu i Git će automatski prebaciti tvoj novi tekst na nju. Zatim napravi Push.

### **8\. Quarto javlja "Invalid YAML" grešku**

* **Simptom:** Crveni križić na GitHub Actions ili crveni tekst u terminalu koji spominje YAML.  
* **Rješenje:** YAML je jako osjetljiv na razmake. Provjeri index.md i \_quarto.yml. Jesi li slučajno obrisao/la dvotočku (:)? Jesi li koristio/la "Tab" tipku umjesto razmaka? YAML koristi isključivo obične razmake\!

### **9\. Obsidian Git panel je nestao**

* **Simptom:** Nema "Source Control" ikone na desnoj strani Obsidiana.  
* **Rješenje:** Obsidian je vjerojatno iz sigurnosnih razloga blokirao plugine. Idi u Settings \-\> Community Plugins, isključi "Safe Mode" i provjeri je li "Obsidian Git" omogućen (Enabled).

### **10\. Ne razumijem zašto se Quarto ruši**

* **Simptom:** Crveni križić, čudna greška koja nema smisla, panika.  
* **Rješenje:**  
  1. Duboko udahni.  
  2. Izgovori tri puta na glas: *"GIT\! GIT\! GIT\!"*.  
  3. Ne činite ništa  
  4. Učinite nešto  
  5. Kopiraj grešku iz loga i pošalji je svom administratoru.

## **13.4 Korištenje AI alata (Tvoj osobni Git asistent)**

Ako se nađeš u problemu koji nije pokriven u "Top 10 grešaka", tvoj najbolji prijatelj može biti umjetna inteligencija.

Alati poput **ChatGPT-a, Google Gemini-a ili Claude-a** iznimno su vješti i precizni u rješavanju problema s Gitom. Budući da je Git globalni industrijski standard, AI alati poznaju sve njegove naredbe do u detalj.

Ne moraš biti stručnjak da bi ih pitao/la za pomoć. Dovoljno je objasniti što želiš postići na običnom jeziku.

**Primjer tvog pitanja (Prompt):**

*"Završio sam s pisanjem uvodnog poglavlja u svom editoru. Sada želim sve to spremiti. Kako ću točno napraviti commit i poslati to na GitHub preko terminala?"*

**Primjer AI odgovora koji ćeš dobiti:**



1. Pripremi sve izmijenjene datoteke za spremanje:  
   git add .  
2. Zabilježi promjene (commit) uz kratku opisnu poruku:  
   git commit \-m "Završeno uvodno poglavlje"  
3. Pošalji promjene na tvoju radnu granu na GitHubu (zamijeni ime-vase-grane stvarnim imenom):  
   git push origin ime-vase-grane

**Savjet za greške:** Ako ti terminal izbaci crveni tekst s greškom koju ne razumiješ, samo je **označi, kopiraj i zalijepi u AI alat** uz pitanje: *"Dobio sam ovu grešku u Gitu, kako da je riješim korak po korak?"*. AI će ti gotovo uvijek dati precizno rješenje unutar par sekundi.



**Kraj priručnika\!** Želimo ti ugodan i produktivan rad u novom okruženju\!









