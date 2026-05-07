---
title: "Poglavlje 5 - Podjela rada i timska suradnja"
---

> **Procijenjeno vrijeme čitanja:** 10–15 minuta
> **Preduvjet:** Repozitorij kloniran i vault otvoren (Poglavlje 4)

***

## 5.1 Noćna mora zvana "Merge Conflict"

U klasičnom načinu rada (Word datoteka na dijeljenom disku ili slanje mailom), najveći strah tima je "pregaziti" tuđi rad. U Git svijetu, tvoj rad je uvijek siguran jer radiš u izoliranom okruženju. Međutim, problem može nastati u trenutku spajanja (Merge).

**Zamisli ovu situaciju:**
1. Ti i kolega radite na istoj datoteci (`01-uvod.md`).
2. Ti izmijeniš prvu rečenicu u *"Ovaj projekt je izvrstan."*
3. Kolega izmijeni **potpuno istu rečenicu** u *"Ovaj projekt je sjajan."*
4. Oboje pošaljete promjene na GitHub.

Kada pokušate spojiti te dvije grane, Git će stati, podići "ručnu kočnicu" i reći:
*"Čekaj malo! Imam dvije različite verzije iste rečenice. Ne znam koja je točna. Ljudi, riješite ovo sami."*

To se zove **Merge Conflict (Konflikt pri spajanju)**. Sustav će u dokument ubaciti čudne oznake (`<<<<<<<`, `=======`) i tražiti od tebe da ručno odabereš verziju koju želiš zadržati.

> **Utješna činjenica:** Konflikt **nije** katastrofa! Git ne briše podatke, ništa nije izgubljeno i nikome nisi obrisao/la tekst. Sustav samo traži ljudsku odluku. Ipak, za početnike su konflikti stresni, pa ih želimo izbjeći u potpunosti.

***

## 5.2 Rješenje: Modularnost i konvencija vlasništva

Kako bismo u startu eliminirali 99% mogućnosti za konflikte, koristimo dva jednostavna principa Docs-as-Code metodologije: **Modularnost** i **Vlasništvo**.

### 1. Modularnost (Knjiga od Lego kockica)
U Wordu obično imamo jednu divovsku datoteku od 100 stranica. U našem repozitoriju, projekt je "razbijen" na mnogo malih datoteka (modula). 

```
Klasični pristup:                   Docs-as-Code pristup:
Glavni_Dokument_v7_final.docx    ├── 01-uvod.qmd
                                    ├── 02-metodologija.qmd
                                    ├── 03-budzet.qmd
                                    └── 04-zakljucak.qmd
```

Naš "printer" (Quarto alat) će na kraju samostalno uzeti sve ove male datoteke i savršeno ih slijepiti u jedan veliki Word dokument.

### 2. Vlasništvo (Jedna osoba = Jedna datoteka)
Budući da je projekt razbijen na module, tim se može dogovoriti tko je "vlasnik" kojeg modula. 
Ako je Ana zadužena za *Uvod*, nitko drugi u timu **ne smije otvarati niti uređivati** datoteku `01-uvod.qmd` dok je Ana na njoj.

Kada odvojimo ljude u zasebne datoteke, Git može savršeno i potpuno automatski spojiti njihov rad bez ikakvih konflikata!

***

## 5.3 Praktičan primjer: Tijek suradnje i zaduženja

Ovako izgleda kompletan životni ciklus jednog dokumenta kroz timsku suradnju:

```text
+-------------------------------------------------------------+
|                    TIJEK SURADNJE TIMA                      |
+-------------------------------------------------------------+

  VODITELJ                    AUTOR                  RECENZENT
  --------                    ------                 ---------
  Kreira repozitorij
  Postavi strukturu
  Pozove članove
         |
         v
                         Klonira repozitorij
                         Kreira vlastitu granu
                         Piše dokument
                         Commit + Push
                         Otvori Pull Request
                                |
                                v
                                              Pregledava PR
                                              Dodaje komentare
                                |
                                v
                         Ispravlja prema
                         komentarima
                         Push novih izmjena
                                |
                                v
  Odobrava i mergea <-----------+
  u main
         |
         v
  GitHub Actions
  automatski renderira
  finalni dokument
```

### Tablica podjele rada
Prije početka pisanja, projektni menadžer kreira ovakvu tablicu zaduženja (obično u `README.md` datoteci na GitHubu):

| Član tima | Datoteka | Poglavlje | Status |
|-----------|----------|-----------|--------|
| Ana Kovač | `01-uvod.qmd` | 1. Uvod i kontekst | (U izradi) |
| Pero Novak | `02-metodologija.qmd`| 2. Metodologija provedbe | (Nije poceto) |
| Marija Horvat | `03-rezultati.qmd` | 3. Rezultati i pokazatelji | Gotovo |
| *Tim* | `index.md` | Naslovnica i meta-podaci | Zaključano |

: Tablica podjele rada {tbl-colwidths="[20,25,35,20]"}

***

## 5.4 Oprez: Što je `index.md` i tko je njegov vlasnik?

U tablici iznad vidiš da je datoteka `index.md` "zaključana". Ako ju otvoriš, na samom vrhu vidjet ćeš blok koda oivičen s tri crtice:

```yaml
***
title: "Prijava EU Projekta"
author: "Tim za razvoj"
date: "2023-10-25"  
***
```

Ovo se zovu **metapodaci (YAML)**. Quarto će automatski uzeti ove informacije i pozicionirati ih na naslovnicu tvog gotovog Word/PDF dokumenta.

> **Najčešća početnička greška u Docs-as-Code!**
> U praksi, ovu datoteku uređuje isključivo **Voditelj projekta**. Ostali članovi tima je NE bi trebali dirati! Ako dvije osobe iz tima istovremeno promijene datum u YAML bloku, nastat će Merge Conflict koji će prekinuti automatsko generiranje Word dokumenta za cijeli tim!

***

## 5.5 Zlatna pravila za miran san (Bez konflikata!)

Evo konkretnih navika koje konflikte svode na nulu:

| Navika | Zašto pomaže |
|--------|-------------|
| **Pull svako jutro** (Preuzimanje) | Kad otvoriš Obsidian, prvo napravi *Git: Pull*. Uvijek moraš imati najnoviju verziju rada tvojih kolega. |
| **Poštuj granice datoteka** | Radi samo u datotekama koje su ti dodijeljene. Ne ispravljaj tipfelere u tuđem tekstu dok on radi! |
| **Commit često** | Najgora navika je pisanje 4 sata bez ijednog Commita. Što su Commiti manji i češći, konflikti se teže događaju. |
| **Komunikacija spašava** | Nemaš strpljenja i moraš hitno nešto promijeniti u tuđoj datoteci? Pošalji poruku na Teams/Slack: *"Hej Pero, planiram dodati odlomak u tvoju 02-metodologija.qmd. Mogu li napraviti push?"* |

*(Napomena: Konačna i najviša zaštita od konflikata je rad na vlastitoj **grani**, što detaljno učimo u sljedećem poglavlju!)*

***

## 5.6 Test – Simulacija dodjele vlasništva

Da bismo tehnički potvrdili ovaj koncept, napravimo kratku vježbu.

1. Ti preuzmi odgovornost za poglavlje Uvod.
2. U Obsidianu, klikni na ikonu "Nova bilješka" (New note) ili pritisni `Ctrl+N`.
3. Preimenuj bilješku u `01-uvod` (Obsidian će automatski dodati `.md`).
4. Upiši naslov (`# Uvod`) i par rečenica teksta.
5. Napravi Commit i Push.

Sve dok pišeš isključivo unutar svog `01-uvod` dokumenta, tehnički si apsolutno siguran/na od konflikata s ostalim članovima tima!

***

## Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Merge Conflict** | Nastaje kada dvije osobe mijenjaju isti redak u istoj datoteci. Rješava se ručno. |
| **Podjela po datotekama** | Projekt je "knjiga od Lego kockica" - svaki član zadužen je za određene datoteke. |
| **Vlasništvo nad datotekama** | Timski dogovor (1 osoba = 1 datoteka), a ne tehničko ograničenje Git-a. |
| **YAML metapodaci (`index.md`)** | Podaci za naslovnicu knjige. **Smije ih mijenjati isključivo voditelj!** |
| **Prevencija konflikata** | *Pull* svako jutro + česti, mali *Commitovi* + poštivanje tuđih datoteka. |

***

**<- Prethodno poglavlje:** [Poglavlje 4 – Kloniranje repozitorija](04-kloniranje-repozitorija.md)
**Sljedeće poglavlje:** [Poglavlje 6 – Branching: Tvoj izolirani prostor za rad ->](06-branching.md)







