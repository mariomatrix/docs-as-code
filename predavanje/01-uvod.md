---
title: "Poglavlje 1 - Uvod: Nova paradigma rada s dokumentacijom"
---

{{< pagebreak >}}

### Preduvjeti za cijeli priručnik

Prije nego počneš, provjeri imaš li:

- Računalo s pristupom internetu
- Administratorska prava na računalu (za instalaciju softvera)
- E-mail adresu (za kreiranje GitHub računa)
- Oko **2–3 sata** za postavljanje kompletnog okruženja

### Alati koje ćemo instalirati

| Alat | Verzija | Namjena |
|------|---------|---------|
| Git | 2.44+ | Praćenje promjena i suradnja |
| Obsidian | 1.5+ | Editor za pisanje dokumentacije |
| Quarto | 1.4+ | Pretvorba teksta u Word/PDF/HTML |
| GitHub račun | — | Pohrana i dijeljenje dokumentacije |

> ⏱️ **Procijenjeno vrijeme postavljanja:** 2–3 sata (jednokratno)
> ⏱️ **Procijenjeno vrijeme učenja toka rada:** 1 dan aktivne prakse

***

## 1.1 Stari način rada – i zašto više ne funkcionira

Zamisli ovaj scenarij koji se događa u svakom timu koji piše dokumentaciju:

1. Ana napiše prvu verziju projektnog izvješća u Wordu i pošalje ga e-mailom
2. Pero napravi izmjene i pošalje `izvjesce_v2_FINAL.docx`
3. Marija doda komentare i pošalje `izvjesce_v2_FINAL_komentari_MJ.docx`
4. Ana integrira sve izmjene i šalje `izvjesce_v3_FINAL_zapravo_final.docx`
5. Tjedan dana kasnije, nitko ne zna koja je verzija ispravna

Ovo nije greška pojedinca — **ovo je greška alata i procesa.**

Problemi starog načina rada:

- Nema jasne evidencije tko je što promijenio i kada
- Verzije se gube, miješaju ili dupliraju
- Paralelni rad na istom dokumentu stvara konflikte
- Nema automatske provjere konzistentnosti formatiranja
- Svaki put kada se mijenja sadržaj, netko mora ručno renovirati cijeli dokument

***

## 1.2 Novi način rada – Docs-as-Code

**Docs-as-code** (hrv. *dokumentacija kao kôd*) je pristup u kojem dokumentaciju pišemo, pratimo i objavljujemo **istim alatima i procesima kojima programeri prate softverski kôd.**

Umjesto Word datoteka i e-maila, koristimo:

- **Markdown** – jednostavan format za pisanje teksta
- **Git** – sustav koji pamti svaku promjenu, tko ju je napravio i kada
- **GitHub** – online pohrana i suradnički prostor
- **Obsidian** – ugodan editor za pisanje u Markdownu
- **Quarto** – alat koji pretvara Markdown u lijepo formatiran Word/PDF/HTML

Ključna razlika: **sadržaj je odvojen od oblika.**

Ti pišeš samo tekst. Oblikovanje (fontovi, stilovi, numeracija) se primjenjuje automatski i konzistentno pri svakom generiranju dokumenta.

***

## 1.3 Usporedba starog i novog načina

| Značajka | Stari način (Word + e-mail) | Novi način (Docs-as-code) |
|---|---|---|
| **Verzioniranje** | Ručno (`_v2_FINAL`) | Automatsko, svaka promjena zabilježena |
| **Suradnja** | Slanje datoteka e-mailom | Paralelni rad, bez e-maila |
| **Praćenje promjena** | Komentari u Wordu | Potpuna povijest tko je što promijenio |
| **Formatiranje** | Svaki put iznova | Jednom definirano, uvijek konzistentno |
| **Objavljivanje** | Ručno generiranje PDF-a | Automatski pri svakom ažuriranju |
| **Pohrana** | Lokalno + e-mail privitak | Centralna pohrana, dostupno svima |
| **Greška** | "Koja je verzija ispravna?" | Uvijek jasno koja je zadnja verzija |

***

## 1.4 Tijek rada – kako to izgleda u praksi

```text
+-----------------------------------------------------------------+
|                     DOCS-AS-CODE TIJEK RADA                     |
+-----------------------------------------------------------------+

  [ ] Preuzmi zadnju verziju         [ ] Piši dokument
      s GitHuba (Pull)                   u Obsidianu (.md)
         |                                  |
         v                                  v
  +-------------+                   +---------------+
  |   GitHub    |<------------------|   Obsidian    |
  | repozitorij |   Spremi promjene |   (lokalno)   |
  |  (online)   |   na GitHub       +---------------+
  +-------------+   (Commit+Push)
         |
         v
  [ ] GitHub Actions automatski pokreće Quarto
         |
         v
  [ ] Generirani dokumenti (Word, PDF, HTML)
      dostupni za preuzimanje
```

**Korak po korak u svakodnevnom radu:**

1. **Pull** — Jutarnji ritual: preuzmi sve izmjene koje su napravili kolege
2. **Branch** — Kreiraj svoju "radnu granu" (vlastitu kopiju projekta)
3. **Piši** — Piši u Obsidianu kao u bilo kojem editoru teksta
4. **Commit** — Spremi promjenu s kratkim opisom što si napravio/la
5. **Push** — Pošalji promjene na GitHub
6. **Pull Request** — Predaj rad na pregled kolegi
7. **Merge** — Nakon pregleda, promjene se spajaju s glavnom verzijom
8. **Automatski render** — GitHub automatski generira finalni dokument

***

## 1.5 Uloga svakog alata

### Git

**Što je:** Sustav za praćenje promjena u datotekama.

**Analogija:** Zamisli Git kao napredni "Track Changes" u Wordu, ali koji radi za sve datoteke odjednom i pamti **kompletnu povijest** svih promjena od samog početka projekta.

**Što radi za tebe:**
- Pamti tko je što promijenio i kada
- Omogućava vraćanje na bilo koju prethodnu verziju
- Omogućava paralelni rad više osoba bez konflikata

**Gdje živi:** Na tvom računalu (lokalno)

***

### GitHub

**Što je:** Online platforma koja pohranjuje Git repozitorije.

**Analogija:** GitHub je kao Google Drive, ali za kod i dokumentaciju — s ugrađenim sustavom pregleda, komentiranja i odobravanja promjena.

**Što radi za tebe:**
- Centralna pohrana svih datoteka projekta
- Pregled i odobravanje tuđih izmjena (Pull Request)
- Automatsko pokretanje alata (GitHub Actions)
- Evidencija svih promjena s imenima autora

**Gdje živi:** Online, na `github.com`

***

### Obsidian

**Što je:** Editor za pisanje tekstualnih datoteka u Markdown formatu.

**Analogija:** Obsidian je kao Word, ali piše u jednostavnom tekstualnom formatu koji Git može pratiti. Nema skrivenih XML datoteka — samo čisti tekst.

**Što radi za tebe:**
- Ugodno sučelje za pisanje dokumentacije
- Pregled Markdown teksta (kako će izgledati)
- Git integracija kroz plugin (commit, push — bez terminala)
- Brza navigacija između datoteka projekta

**Gdje živi:** Na tvom računalu (lokalno)

***

### Quarto

**Što je:** Alat koji pretvara Markdown datoteke u finalne dokumente.

**Analogija:** Quarto je kao printer koji zna i oblikovati dokument. Ti daš čisti tekst, Quarto doda profesionalne stilove i izveze Word, PDF ili web stranicu.

**Što radi za tebe:**
- Pretvara `.qmd` i `.md` datoteke u `.docx`, `.pdf`, `.html`
- Primjenjuje konzistentne stilove (iz Word predloška)
- Automatski numerira naslove, slike, tablice
- Može se pokrenuti ručno ili automatski (GitHub Actions)

**Gdje živi:** Na tvom računalu + automatski na GitHubu

***

## 1.6 Zašto je ovo bolje? – Konkretne prednosti

**Za tebe kao autora:**
- Fokusiraš se na sadržaj, ne na formatiranje
- Znaš točno što si promijenio/la i kada
- Možeš se uvijek vratiti na stariju verziju ako zatreba
- Nema straha od "pokvario/la sam dokument"

**Za tim:**
- Svatko zna na čemu radi tko
- Nema konflikata između verzija
- Svaka promjena je vidljiva i objašnjena
- Pregled rada kolega je strukturiran i dokumentiran

**Za projekt:**
- Kompletna revizijska staza — uvijek se zna što se promijenilo i zašto
- Automatsko generiranje finalnih dokumenata
- Konzistentno formatiranje u svim dokumentima

***

## 1.7 Što ćeš naučiti u ovom priručniku

Do kraja priručnika, moći ćeš **samostalno:**

- Postaviti kompletan radni alat na svom računalu
- Klonirati projektni repozitorij i otvoriti ga u Obsidianu
- Pisati dokumentaciju u Markdown formatu
- Raditi na vlastitoj grani bez ometanja kolega
- Predati rad na pregled putem Pull Requesta
- Generirati finalni Word dokument pomoću Quartoa

***

## ✅ Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Docs-as-code** | Pristup pisanja dokumentacije istim alatima kao softverski kôd |
| **Git** | Lokalni sustav za praćenje svih promjena u datotekama |
| **GitHub** | Online platforma za pohranu i suradnju |
| **Obsidian** | Editor za pisanje u Markdown formatu |
| **Quarto** | Alat za pretvorbu teksta u Word/PDF/HTML |
| **Tijek rada** | Pull -> Branch -> Piši -> Commit -> Push -> PR -> Merge |

***

> 💡 **Savjet:** Ne moraš odmah razumjeti svaki pojam. Svaki korak bit će objašnjen konkretnim primjerima u sljedećim poglavljima. Sada je dovoljno da imaš opću sliku kako dijelovi funkcioniraju zajedno.

***

**Sljedeće poglavlje:** [Poglavlje 2 – Instalacija i postavljanje okruženja ->](02-instalacija.md)










