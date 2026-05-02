# Docs-as-Code: Nova era pisanja projektne dokumentacije
**Trajanje:** 60 minuta
**Publika:** Nastavnici, istraživači, administracija

---

## 1. Uvod i zašto smo ovdje (5 min)
*Ovaj dio držimo jako kratkim jer svi već znaju za ove probleme.*
* **Trenutno stanje:** Slanje Word dokumenata mailom, rad na Teamsima uz česta prepisivanja.
* **Problem:** "Prijava_EU_vFinal_Zadnje_Ispravljeno_v4.docx". Konflikti kad više ljudi piše u isto vrijeme, razbijeno formatiranje, i gubitak starih verzija teksta.
* **Rješenje:** A što bi bilo kada bismo tekstualne dokumente tretirali jednako precizno i sustavno kao što programeri tretiraju svoj kod?

## 2. Što je Docs-as-Code? (15 min)
* **Ključni koncept:** Dokumenti se pišu u najobičnijem tekstualnom formatu (bez "nevidljivog" Word formatiranja), a onda se na kraju **automatski pretvaraju** u predivan PDF ili DOCX.
* **Jedan izvor istine:** Svi rade na istim datotekama u istom spremniku.
* **Čuvanje povijesti (Versioning):** Sustav točno pamti tko je, kada i zašto obrisao ili dodao svaki pojedini znak. Nema više "Save As".
* **Razdvajanje sadržaja od izgleda:** Vi pišete *što* želite reći, a sustav (Pandoc/Quarto) brine o tome *kako* to izgleda na kraju (fontovi, margine, zaglavlja).
* **Savršeno za Umjetnu Inteligenciju (AI):** AI alati (ChatGPT, Copilot) prirodno komuniciraju i generiraju tekst u Markdownu. Čisti tekstualni dokumenti omogućavaju AI-u da trenutno sažme vaše radove ili pomogne u pisanju, bez saplitanja o skriveni Wordov kod.

## 3. Naši alati - Magični trokut (10 min)
Nećemo vas učiti programirati, koristit ćemo vizualne alate!
1. **Obsidian (Editor):** Tu pišemo. Izgleda jednostavno, odličan je za povezivanje misli i izrazito brz.
2. **Quarto / Pandoc (Prevoditelj):** Motor koji tekst koji smo napisali pretvara u službene EU Prijave (PDF i DOCX).
3. **Git / GitHub (Skladište):** Mjesto gdje dokumenti žive. Koristit ćemo **Obsidian Git ekstenziju** – što znači da nikad ne morate izaći iz Obsidiana da biste spremili i podijelili verziju dokumenta s kolegama. Sve se rješava jednim klikom unutar aplikacije!

## 4. Live Demo: Prijava za EU Projekt (20 min)
*Demos je najvažniji dio predavanja!*
1. **Pokazivanje strukture:** Otvorite `Demo-Projekt` u Obsidianu. Pokažite datoteke i mape (`Istrazivanje`, `Zajednicki_Rad`).
2. **UUID i Graph View:** Pokažite `Istrazivanje` mapu. Objasnite kako svaki dokument može imati jedinstveni ID (UUID) u pozadini. Pokažite **Graph view** (veze između bilješki, web clipper članaka i EU prijave) - vizualni prikaz vašeg "mozga projekta".
3. **Zajednički rad (Spajanje dokumenata):** Otvorite mapu `Zajednicki_Rad`. Pokažite kako Ana piše `01_Uvod_Ana.md`, a Marko `02_Razrada_Marko.md`. Pokažite `index.md` datoteku koja ih automatski spaja. Objasnite: Nema više prepisivanja iz jednog u drugi dokument!
4. **Pisanje teksta:** Otvorite `01_Prijava_EU_Projekta.md`, napišite jedan paragraf, ubacite sliku ili jednostavnu tablicu.
5. **Reference:** Pokažite kako se lako citira iz Mendeleya/Zotera (`[@autor2024]`).
6. **Slanje promjena (Commit & Branch):** Kliknite u Obsidian Git pluginu na ikonu za spremanje. Objasnite publici: "Sada sam ovo spremio na svoju radnu kopiju (granu/branch), ali to još nije u službenom dokumentu."
7. **Prikaz Pull Requesta (Odobravanje):** Otvorite GitHub u web pregledniku. Pokažite kako se otvara *Pull Request*. 
   - Pokažite publici sučelje za usporedbu: "Pogledajte kako sustav sam označava crvenom bojom što sam obrisao, a zelenom što sam dodao."
   - Pokažite kako možete ostaviti komentar na specifičnu liniju teksta.
   - Kliknite na veliki zeleni gumb **Merge pull request** i objasnite: "Kao voditelj, sada sam službeno odobrio Anin tekst u glavni dokument."
8. **Magija (Automatizacija):** Nakon klika na Merge, pokažite kako se zeleni kružić (GitHub Actions) vrti. Objasnite da "Robot sada čita vaš spojeni tekst, dodaje naslovnicu, brojeve stranica, bibliografiju, i kreira DOCX i PDF."
9. **Rezultat:** Preuzmite i otvorite kreirani PDF/DOCX pred publikom!

## 5. Sljedeći koraci (10 min)
* **Je li ovo za sve?** Ne. Idealno je za veće projekte, prijave, elaborate, knjige. Nije za kratki dopis.
* **Kako početi?** Pilot faza! Tko želi, može dobiti gotov *Template* repozitorij i instalacijske upute.
* Pitanja i odgovori.
