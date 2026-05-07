---
title: "Poglavlje 9 - Merge u main: spajanje promjena"
---

{{< pagebreak >}}

> ⏱️ **Procijenjeno vrijeme:** 15–20 minuta
> 📋 **Preduvjet:** Otvoren i pregledan Pull Request (Poglavlje 8)

***

## 9.1 Što znači merge i kada se radi?

**Merge** (hrv. *spajanje*) je postupak kojim se promjene s radnog brancha trajno ugrađuju u `main` granu.

Nakon mergea:
- Sve što si napisao/la postaje dio **službene verzije** dokumenta
- `main` grana sadrži tvoj doprinos zajedno s doprinosima svih ostalih
- GitHub Actions automatski pokreće Quarto render i generira novi finalni dokument

### Kada je pravo vrijeme za merge?

Merge se radi **isključivo** kada su ispunjena sva tri uvjeta:

```text
[ ] Recenzent je pregledao PR i kliknuo "Approve"
[ ] Svi komentari su označeni kao riješeni (Resolve conversation)
[ ] Nema konflikata s main granom (GitHub će jasno javiti ako ih ima)
```

> ⚠️ **Upozorenje:** Nikad ne mergeaj vlastiti PR bez pregleda drugog člana tima — čak i ako si siguran/na da je sve ispravno. Pregled nije samo o greškama, nego i o konzistentnosti cijelog dokumenta.

***

## 9.2 Tko ima pravo mergati?

Pravo merganja ima **maintainer** — osoba s administratorskim ili write pristupom repozitoriju.

U praksi, to znači:

| Veličina tima | Tko mergea |
|--------------|-----------|
| Mali tim (2–3 osobe) | Svaki član može mergati tuđe PR-ove |
| Srednji tim (4+) | Voditelj dokumentacije mergea sve PR-ove |
| Formalni projekt | Samo maintainer, uz obavezni Approve |

> 💡 **Preporuka:** Postavi pravilo u timu da **autor ne mergea vlastiti PR**. Četiri oka uvijek vide više od dva.

***

## 9.3 Merge kroz GitHub sučelje

Ovo je najčešći i najjednostavniji način — sve se radi kroz preglednik.

### Korak 1: Otvori Pull Request

1. Idi na `https://github.com/FGAG-docs/EU-Project-Template`
2. Klikni na karticu **"Pull requests"**
3. Odaberi PR koji je spreman za merge

### Korak 2: Provjeri status

Na dnu PR stranice vidiš status provjera:

```text
+----------------------------------------------------------+
|  [V]  1 approving review                                 |
|  [V]  All conversations resolved                         |
|  [V]  No merge conflicts                                 |
|                                                          |
|         [ Merge pull request v ]                         |
+----------------------------------------------------------+
```

Ako su sve tri zelene kvačice — spreman si za merge.

> ⚠️ **Ako vidiš crveni X uz "Merge conflicts":** Vidi poglavlje 9.5 — konflikte treba riješiti prije mergea.

### Korak 3: Odaberi tip mergea

Klikni na **strelicu v** pored gumba "Merge pull request" — pojavljuju se tri opcije:

| Opcija | Što radi | Kada koristiti |
|--------|----------|----------------|
| **Create a merge commit** | Spaja sve commitove, dodaje jedan "merge commit" | Preporuka za početnike — najjednostavnije |
| **Squash and merge** | Sve commitove spljoštava u jedan | Kada imaš puno sitnih "work in progress" commitova koje ne trebaš čuvati |
| **Rebase and merge** | Premješta commitove na vrh main grane | Napredno — izbjegavaj dok ne upoznaš Git bolje |

**Za ovaj projekt koristite: "Create a merge commit"** — uvijek jasno što se i kada spojilo.

### Korak 4: Potvrdi merge

1. Klikni **"Merge pull request"**
2. Pojavljuje se polje za potvrdu s automatski generiranom porukom — možeš je ostaviti kakva jest ili kratko urediti
3. Klikni **"Confirm merge"**

✅ **Provjera uspjeha:** GitHub prikazuje:
```text
Pull request successfully merged and closed
```

### Korak 5: Obriši branch

Odmah nakon mergea GitHub nudi gumb:
```text
[ Delete branch ]
```

**Klikni ga.** Radni branch više nije potreban — promjene su u `main`. Brisanje brancha ne briše promjene, samo čisti repozitorij od zastarjelih grana.

> 💡 **Zašto brisati branch?** Repozitorij s desetak starih, zastarjelih brancheva postaje zbunjujuć. Čist repozitorij = samo aktivni branchevi su vidljivi.

***

## 9.4 Ažuriranje lokalnog repozitorija nakon mergea

Nakon što je merge napravljen na GitHubu, tvoje lokalno računalo još uvijek ne zna za tu promjenu. Trebaš preuzeti ažurirani `main`.

### U Obsidianu

1. Otvori **Command Palette** (`Ctrl+P`)
2. Upiši: `git checkout`
3. Odaberi: **"Obsidian Git: Switch branch"** -> odaberi `main`
4. Klikni gumb **v Pull** u Source Control panelu

 Lokalni `main` sada sadrži sve mergane promjene.

### Git CLI alternativa

```cmd
# Prebaci se na main granu
git checkout main

# Preuzmi najnovije promjene s GitHuba
git pull origin main
```

***

## 9.5 Rješavanje merge konflikata

### Što je konflikt?

Konflikt nastaje kada su **isti redci iste datoteke** izmijenjeni na dva različita brancha koji se pokušavaju spojiti. Git ne zna koju verziju zadržati — traži od tebe da odlučiš.

```text
<<<<<<< HEAD (main grana)
Projekt se provodi u tri faze.
=======
Projekt se provodi u četiri faze, od kojih je prva pripremna.
>>>>>>> ana-kovac/uvod (tvoj branch)
```

Git je označio:
- Između `<<<<<<< HEAD` i `=======` -> verzija koja je u `main`
- Između `=======` i `>>>>>>>` -> tvoja verzija s brancha

### Kako riješiti konflikt — korak po korak

Konflikte je **najlakše riješiti na GitHubu**, direktno u pregledniku, za jednostavne slučajeve.

**Na GitHubu:**

1. GitHub prikazuje upozorenje na PR stranici:
   ```text
   This branch has conflicts that must be resolved
   [ Resolve conflicts ]
   ```
2. Klikni **"Resolve conflicts"**
3. GitHub prikazuje datoteku s označenim konfliktima
4. Uredi tekst:
   - Obriši linije s `<<<<<<<`, `=======` i `>>>>>>>`
   - Zadrži onu verziju teksta koja je ispravna (ili kombiniraj obje)
5. Klikni **"Mark as resolved"**
6. Klikni **"Commit merge"**
7. Nastavi s normalnim mergeom

> ⚠️ **Za složenije konflikte** koji zahvaćaju više datoteka ili veće dijelove teksta — obavijesti maintainera i riješite zajedno. Ne pogađaj.

### Kako spriječiti konflikte

Konflikti su rijetki ako tim poštuje dogovor o podjeli rada (Poglavlje 5). Ako se ipak pojave češće, najčešći uzrok je:

- Dugo čekanje s otvaranjem PR-a (branch je previše zastario)
- Dvije osobe mijenjaju isti zajednički element (uvodni tekst, naslovnicu)

Rješenje: **kraći ciklusi rada** — manji PR-ovi, češće merganje.

***

## 9.6 Nakon mergea — što dalje?

Nakon što je tvoj PR mergean:

```text
1. Prebaci se na main i napravi pull (9.4)
2. Kreiraj novi branch za sljedeći zadatak (Poglavlje 6)
3. Počni pisati sljedeće poglavlje (Poglavlje 7)
```

Radni ciklus se ponavlja. Svaki PR je jedna zatvorena cjelina — jasna, pregledana i dokumentirana.

***

## 9.7 Git CLI alternativa za merge

> ℹ️ **Napomena:** Merge kroz CLI preporučujemo samo maintainerima s iskustvom. Za svakodnevni rad, GitHub sučelje iz poglavlja 9.3 je jednostavnije i sigurnije.

```cmd
# Prebaci se na main
git checkout main

# Preuzmi najnovije promjene
git pull origin main

# Spoji branch u main
git merge ana-kovac/uvod

# Pošalji na GitHub
git push origin main

# Obriši lokalni branch (opcionalno)
git branch -d ana-kovac/uvod
```

***

## ✅ Što smo naučili u ovom poglavlju

| Koncept | Objašnjenje |
|---------|-------------|
| **Merge** | Spajanje radnog brancha u main nakon odobrenog pregleda |
| **Merge commit** | Najjednostavniji tip mergea — preporučen za početnike |
| **Delete branch** | Brisanje brancha nakon mergea — čisti repozitorij |
| **Konflikt** | Nastaje kada isti redci iste datoteke postoje u dvije verzije |
| **Resolve conflicts** | GitHub alat za ručno rješavanje konflikata u pregledniku |
| **Pull nakon mergea** | Lokalni `main` se mora ručno ažurirati nakon online mergea |

> 💡 **Zlatno pravilo:** Merge je završetak jednog ciklusa rada, ne kraj projekta. Nakon svakog mergea odmah kreiraš novi branch za sljedeći zadatak. Repozitorij je živ — uvijek postoji aktivan posao u tijeku.

***

**<- Prethodno poglavlje:** [Poglavlje 8 – Pull Request](08-pull-request.md)
**Sljedeće poglavlje:** [Poglavlje 10 – Word DOCX template: koncept ->](10-word-template.md)










