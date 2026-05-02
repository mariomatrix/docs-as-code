# Česta Pitanja (Q&A): Timski rad, Odobravanja i Konflikti

Ovaj dokument je priprema za vas kao predavača. Očekujte da će kolege pitati: *"Što ako nas dvoje radimo u isto vrijeme?"* ili *"Tko odlučuje što je konačna verzija?"*. Evo kako im to objasniti jednostavnim rječnikom.

---

## 1. Što je "Pull Request" (Zahtjev za promjenom)?

**Stari način:** Asistent napiše poglavlje, pošalje ga profesoru na mail kao `poglavlje_v1.docx`. Profesor ga čita, prepravlja i šalje nazad.
**Docs-as-Code način:** To se zove *Pull Request*. 

* **Kako to objasniti:** "Zamislite Pull Request kao službeni prijedlog izmjene. Mlađi istraživač u svom Obsidianu napiše novi tekst i kaže sustavu: *'Završio sam, predlažem da ovo uđe u službenu prijavu.'* Taj tekst ne ide odmah u glavni dokument, nego stoji na svojevrsnoj čekaonici na GitHubu."

## 2. Odobravanje (Review & Approval)

Jednom kada je zahtjev (Pull Request) postavljen, glavni istraživač (ili voditelj projekta) dobiva obavijest.

* **Kako to izgleda:** Voditelj otvori GitHub u web pregledniku. Sustav mu crvenom bojom pokazuje što je izbrisano, a zelenom što je dodano. 
* **Track Changes na steroidima:** Voditelj može kliknuti na bilo koji redak teksta i napisati komentar (npr. *"Ovaj paragraf o statici treba proširiti"*). Autor to vidi, popravi u svom Obsidianu i pošalje ispravak.
* **Odobrenje (Merge):** Kada je voditelj zadovoljan, klikne veliki zeleni gumb *"Merge Pull Request"*. U tom trenutku, taj tekst postaje dio službenog dokumenta i sustav (Quarto) automatski generira novi PDF.

## 3. Konflikti (Merge Conflicts) - Bauk kojeg se svi boje

**Što je to?** 
Konflikt se događa *samo* kada dvije osobe istovremeno mijenjaju **isti redak teksta u istoj datoteci**. Sustav je pametan, ali nije vidovnjak – ne zna čiju rečenicu treba zadržati.

**Kako to objasniti publici?**
"Ako Ana piše Uvod, a Marko Zaključak u *istoj* datoteci, sustav će to bez problema spojiti. Ali ako i Ana i Marko u isto vrijeme prepravljaju drugu rečenicu trećeg paragrafa, sustav će se zaustaviti i prijaviti *Konflikt*."

**Kako to rješavamo?**
1. **Prevencijom (Najvažnije!):** Zato smo u demou pokazali mapu `Zajednicki_Rad`. Ako Ana ima svoj dokument (`01_Uvod_Ana.md`), a Marko svoj (`02_Razrada_Marko.md`), konflikti su **matematički nemogući**. Quarto ih na kraju samo slijepi u jedan PDF. Podijelite veliki dokument na manje `.md` datoteke!
2. **Komunikacijom:** Kao i u stvarnom svijetu, dogovorite se tko radi na kojem poglavlju.
3. **Tehničko rješenje u Obsidianu:** Ako se konflikt ipak dogodi, Obsidian će u tekstu pokazati obje verzije označene strelicama (npr. `<<<<<<< HEAD`). Vi samo trebate obrisati verziju teksta koja vam se ne sviđa, obrisati te strelice i ponovno stisnuti "Spremi" (Commit). 

> **Ključna poruka za publiku:** "U Wordu, ako dvoje ljudi piše po istom dokumentu na Teamsu, Word će često samo stvoriti novu datoteku `dokument-Ana-laptop.docx` i ostaviti vama da ručno pronalazite razlike. Git vas *tjera* da taj problem riješite odmah, a čuva apsolutno sve stare verzije da nikad ništa ne izgubite."

---

## 4. Što je s povjerljivošću podataka?

**Pitanje iz publike:** *"Nećemo valjda staviti prijavu za kompetitivni EU projekt na javni GitHub da je svi vide?"*

**Kako odgovoriti:** "Apsolutno ne. Na GitHubu (ili GitLabu) možete kreirati **privatne repozitorije** kojima pristup imaju samo pozvani članovi tima. Akademske institucije dobivaju besplatne napredne pakete na GitHubu, a mnogi fakulteti već imaju i vlastiti interno hostirani GitLab server koji je potpuno zatvoren za vanjski svijet i ispunjava sve sigurnosne zahtjeve."
