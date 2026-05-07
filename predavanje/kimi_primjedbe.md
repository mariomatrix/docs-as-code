 Evo mojeg analitičkog osvrta na tri poglavlja uputstva, s fokusom na primjerenost za ciljanu publiku — početnike u docs-as-code.

---

## Što uputstvo dobro radi

### 1. Jezik i ton
Ton je izrazito podržavajući i nenametljiv. Autor svjesno smanjuje tjeskobu početnika kroz fraze poput *"Ne moraš odmah razumjeti svaki pojam"* i *"Nema straha od 'pokvario/la sam dokument'"*. To je ključno jer docs-as-code može zvučati zastrašujuće za nekoga tko nikad nije čuo za Git.

### 2. Struktura "zašto → kako → provjera"
Svako poglavlje prati isti obrazac: objašnjava **zašto** nešto trebaš, daje **korak-po-korak** upute, a onda **provjeru uspjeha**. To smanjuje anksioznost — čitač uvijek zna je li na pravom putu.

### 3. Analogije su pogođene
- Git kao "napredni Track Changes"
- GitHub kao "Google Drive, ali za kod"
- PAT kao "privremena propusnica"

Ove usporedbe povezuju nepoznato s poznatim, što je najbolja strategija za početnike.

### 4. Vizualni elementi
Dijagram tijeka rada (Poglavlje 1.4), tablice usporedbe i checkliste na kraju poglavlja pomažu različitim tipovima učenja — vizualnim i strukturiranim.

### 5. Iskreno upravljanje očekivanjima
Procjena vremena (2–3 sata postavljanja, 1 dan prakse) i naglasak da se ovo radi samo jednom — to pomaže čitaču da planira i ne odustane usred procesa.

---

## Područja koja bi se mogla poboljšati

### 1. Pretpostavka o kontekstu
Uputstvo pretpostavlja da čitač **već ima projekt i administratora** koji će ga dodati u repozitorij (Poglavlje 2.4). Ali što ako netko čita ovo samostalno, bez tima? Nema uputa za:
- Kreiranje vlastitog repozitorija
- Što učiniti ako nema administratora
- Kako vježbati bez "pravog" projekta

**Sugestija:** Dodati odjeljak "Ako nemaš tim — kako vježbati sam" ili barem napomenuti da ovo uputstvo pretpostavlja postojeći projekt.

### 2. Redoslijed može zbuniti
Poglavlje 3 instalira plugin u **privremenom vaultu**, ali upozorava da će se postavke morati ponoviti u "pravom" vaultu (Poglavlje 4). To znači da čitač radi posao dvaput. 

**Sugestija:** Razmisliti o tome je li ovo najučinkovitiji redoslijed. Alternativa: prvo klonirati repozitorij (Poglavlje 4), pa onda instalirati plugin jednom — u pravom vaultu. To bi smanjilo dupli rad i potencijalnu zabunu.

### 3. Terminal/Command Prompt — prvi susret
Poglavlje 2.1 prvi put uvodi Command Prompt bez ikakvog uvoda u to što je to. Za apsolutne početnike, "crni prozor" može biti zastrašujuć. Nema objašnjenja zašto se neke naredbe pišu u CMD, a neke radnje rade kroz GUI.

**Sugestija:** Kratko objasniti *zašto* neke stvari moraju ići kroz terminal (Git konfiguracija, provjera verzije), a druge kroz GUI (Obsidian, GitHub web).

### 4. Grananje (branching) — spomenuto, ali ne objašnjeno
U Poglavlju 1.4, u dijagramu tijeka rada, pojavljuje se "Branch" kao korak. U Poglavlju 3.6 spominje se "Current branch" u status baru. Ali nigdje u ova tri poglavlja nema objašnjenja što je grana, zašto je važna, ni kako se kreira.

**Sugestija:** U Poglavlju 1.4 dodati jednu rečenicu što je grana, ili barem napomenuti da će biti objašnjeno u kasnijem poglavlju. Inače čitač gleda termin kojeg ne razumije.

### 5. Quarto — instaliran, ali ne demonstriran
Quarto se instalira (Poglavlje 2.3), ali u ova tri poglavlja nema niti jednog primjera kako izgleda `.qmd` datoteka, kako se pokreće, ni što čitač može očekivati kao rezultat. To ostavlja "visjeći" koncept.

**Sugestija:** U Poglavlju 1.5 (Uloga svakog alata) dodati primjer: "Evo kako izgleda Markdown prije i nakon Quarta" — čak i jedna slika ili opis.

### 6. Rješavanje problema (troubleshooting)
Iako postoje upozorenja (npr. "Ako vidiš grešku..."), nema sustavnog odjeljka o najčešćim problemima. Primjerice:
- Što ako PAT token istekne usred rada?
- Što ako Obsidian Git ne vidi Git (čest problem s PATH-om)?
- Što ako dođe do konflikta prilikom pulla?

**Sugestija:** Dodati "Najčešći problemi i rješenja" na kraj Poglavlja 3 ili kao zaseban dodatak.

### 7. Dostupnost za različite operativne sustave
Iako postoje macOS napomene, one su umetnute ad-hoc. Windows je primarni. Za timove s miješanim OS-ovima, to može stvarati nejednakost u iskustvu.

---

## Ukupna procjena

| Aspekt | Ocjena | Komentar |
|--------|--------|----------|
| Jezik i pristupačnost | ⭐⭐⭐⭐⭐ | Izvrsno prilagođeno početnicima |
| Struktura i logičnost | ⭐⭐⭐⭐☆ | Dobar tok, ali redoslijed Poglavlja 3/4 se može poboljšati |
| Tehnički detalji | ⭐⭐⭐⭐☆ | Dovoljno za početak, ali nedostaje dubina u rješavanju problema |
| Cjelovitost | ⭐⭐⭐☆☆ | Pretpostavlja puno konteksta (tim, admin, projekt) |
| Praktična primjenjivost | ⭐⭐⭐⭐☆ | Checkliste i provjere pomažu, ali dupli rad u Pog. 3 smanjuje efikasnost |

---

## Ključna preporuka

Ako bi trebalo izdvojiti **jednu** stvar za doradu: **spajanje Poglavlja 3 i 4 u jedan cjelovit tok** — klonirati repozitorij prvo, pa onda instalirati i konfigurirati plugin direktno u pravom vaultu. To eliminira dupli rad, smanjuje zabunu i čini uputstvo kraćim za 15–20 minuta.

Uputstvo je u srži **vrlo dobro napisano** — jasno, strpljivo i metodično. Gornje primjedbe su više o finom štihu nego o temeljnim propustima. Za ciljanu publiku (početnike u docs-as-code unutar organiziranog tima), ovo je solidna osnova koja će znatno smanjiti barijeru ulaska u novi način rada.

pd 3-7
 Evo analitičkog osvrta na poglavlja 3–7 (i njihove nastavke), s fokusom na primjerenost za početnike u docs-as-code.

---

## Područja koja bi se mogla poboljšati

### 1. Poglavlje 3: Dupli rad s privremenim vaultom
Ovo je najveći strukturni problem cijelog uputstva. Poglavlje 3 tjera čitača da:
1. Instalira i konfigurira plugin u **privremenom vaultu**
2. Ponovi **istu instalaciju i konfiguraciju** u pravom vaultu (Poglavlje 4)

Autor to opravdava s "ovaj put znaš točno što radiš", ali to je **15–20 minuta duplog rada** za početnika koji i tako ima previše novih informacija.

**Sugestija:** Preurediti Poglavlje 3 da bude "Priprema za instalaciju" (objašnjenje što će raditi), a stvarnu instalaciju pomaknuti u Poglavlje 4 nakon otvaranja pravog vaulta. Ili, alternativno, u Poglavlju 3 instalirati plugin globalno (ako je to moguće u Obsidianu) ili barem dati upute za brzo kopiranje postavki.

### 2. Poglavlje 4: Git autentikacija prilikom kloniranja
Poglavlje 4.2 spominje da će terminal možda tražiti korisničko ime i lozinku, i da se kao lozinka upisuje PAT token. Ali:

- Ne objašnjava **što ako se ne pojavi prozor za autentikaciju** (što je često slučaj s Credential Managerom na Windowsu)
- Ne objašnjava **što ako kloniranje ne uspije** zbog nedostatka pristupa repozitoriju
- Ne spominje **SSH ključeve** kao alternativu PAT-u (što je u praksi često preferirano)

**Sugestija:** Dodati troubleshooting odlomak: "Ako kloniranje ne radi — provjeri ove 3 stvari."

### 3. Poglavlje 5: "Vlasništvo" je timski dogovor, ne tehničko ograničenje
Uputstvo kaže: "Ako je Ana zadužena za Uvod, nitko drugi ne smije otvarati niti uređivati datoteku." To je **procesna preporuka**, ali tehnički Git to **ne sprječava**. Početnik bi mogao pomisliti da postoji neka zaštita.

**Sugestija:** Dodati rečenicu: *"Ovo je timski dogovor, ne tehničko ograničenje — Git te neće fizički spriječiti da otvoriš tuđu datoteku, ali poštovanje ovog pravila štiti tim od konflikata."*

### 4. Poglavlje 6: Branching bez vizualne povratne informacije
Command Palette je moćan, ali **nevidljiv** — nema gumba, nema izbornika. Za početnike koji tek uče koncept grana, to može biti zbunjujuće. Uputstvo daje CLI alternativu, ali ne objašnjava kako **vizualno potvrditi** da si stvarno na drugom branchu (osim statusne trake).

**Sugestija:** Dodati screenshot ili ASCII prikaz Source Control panela s više brancheva, ili barem objasniti kako otvoriti "Branch" pogled u Obsidianu (ako postoji).

### 5. Poglavlje 7: Commit poruke — previše automatsko?
Uputstvo preporučuje automatsku poruku: `{{date}} - {{hostname}}: {{numFiles}} datoteka izmijenjeno`. Ali u istom poglavlju (7.7) daje primjere dobrih ručnih poruka kao `Dodati poglavlje 1.2 - Ciljevi projekta`.

**Kontradikcija:** Ako je automatska poruka dovoljna, zašto učiti ručne? Ako su ručne bolje, zašto preporučiti automatsku?

**Sugestija:** Jasno razgraničiti: automatska poruka je za **brze, česte commite** (draft faza), ručna poruka je za **logičke cjeline** prije pusha/PR-a.

### 6. Nedostaje "Što ako nešto pođe po zlu" u svakodnevnom radu
Poglavlje 7.6 opisuje idealni tijek, ali ne spominje:
- Što ako zaboraviš commitati prije zatvaranja Obsidiana?
- Što ako kolega pusha izmjene u tvoju datoteku dok ti pišeš?
- Što ako slučajno commitaš na `main` umjesto na svoj branch?

**Sugestija:** Dodati "Najčešće greške i kako ih ispraviti" na kraj Poglavlja 7.

### 7. LaTeX formule — previše za početnike?
Poglavlje 7.2 uključuje detaljnu LaTeX referencu s 15+ simbola. Iako kontekst (EU projekti) opravdava potrebu, to može preplaviti početnika koji tek uči osnovni Markdown.

**Sugestija:** Izdvojiti LaTeX u zaseban odjeljak ili dodatak, označen kao "Napredno — preskoči ako tek učiš osnove". Osnovno poglavlje 7.2 bi trebalo završiti nakon tablica i slika.

### 8. Poglavlje 4.4: `.obsidian` folder — nedosljednost s Poglavljem 2.6
Poglavlje 2.6 objašnjava `.gitignore` i navodi da se `.obsidian/workspace.json` ignorira, ali `.obsidian/plugins/` dijeli. Poglavlje 4.4 kaže: **"Ne diraj"** za cijeli `.obsidian` folder. To je kontradiktorno — ako se dijele plugini, korisnik bi ih trebao vidjeti i možda konfigurirati.

**Sugestija:** Pojasniti: `.obsidian` sadrži i dijeljene postavke (koje ćeš vidjeti) i osobne postavke (koje Git ignorira). Ne diraj znači "ne briši ništa bez razloga", ne "apsolutna zabrana".

---

## Ukupna procjena (Poglavlja 3–7)

| Aspekt | Ocjena | Komentar |
|--------|--------|----------|
| Struktura i logičnost | ⭐⭐⭐⭐☆ | Dobar tok, ali dupli rad u Pog. 3 smanjuje efikasnost |
| Tehnički detalji | ⭐⭐⭐⭐☆ | Dovoljno za početak, ali nedostaje dubina u rješavanju problema |
| Procesna disciplina | ⭐⭐⭐⭐⭐ | Izvrsno — uči ne samo alate, već i timske navike |
| Praktična primjenjivost | ⭐⭐⭐⭐☆ | Dnevni ritam i checkliste pomažu, ali idealizirani scenarij |
| Rješavanje problema | ⭐⭐⭐☆☆ | Nedostaje sustavni troubleshooting |
| Dostupnost za različite razine iskustva | ⭐⭐⭐☆☆ | LaTeX i YAML mogu preplaviti apsolutne početnike |

---

## Ključna preporuka

Ako bi trebalo izdvojiti **jednu** stvar za doradu: **ukinuti privremeni vault u Poglavlju 3** i integrirati instalaciju plugina u Poglavlje 4, nakon kloniranja repozitorija. To bi:
- Skratilo uputstvo za ~20% (3 umjesto 4 koraka u postavljanju)
- Eliminirialo glavnu točku zabune ("Zašto moram ponavljati isto?")
- Smanjilo kognitivno opterećenje u kritičnoj ranoj fazi

Druga preporuka: dodati **"Najčešće greške i kako ih ispraviti"** na kraj Poglavlja 7 kao brzi referentni vodič — početnici će ga koristiti češće nego bilo koji drugi dio uputstva.

---

## Usporedba s prvim tri poglavlja

| Element | Poglavlja 1–3 | Poglavlja 3–7 |
|--------|---------------|---------------|
| Fokus | Koncepti i instalacija | Operativni rad i timska suradnja |
| Napetost | "Hoću li uspjeti instalirati?" | "Hoću li slučajno pokvariti tuđi rad?" |
| Ključna emocija | Zbunjenost od novih alata | Strah od grešaka u timskom kontekstu |
| Autorov odgovor | Strpljivo objašnjavanje | Prevencija kroz konvencije |

Uputstvo prepoznaje da se **psihološki izazov mijenja** nakon instalacije — s "kako ovo radi?" na "kako ne napraviti grešku?". Odgovor kroz konvencije (vlasništvo, branching, česti commiti) je pametan i pokazuje da autor razumije ne samo alate, već i **ljudsku stranu promjene**.

 Evo analitičkog osvrta na poglavlja 8–13, s fokusom na primjerenost za početnike u docs-as-code.

---

## Što uputstvo dobro radi

### 1. Poglavlje 8 (Pull Request) — odličan prijelaz s "pisanja" na "predaju"
Nakon što su poglavlja 6–7 naučila kako pisati i commitati, Poglavlje 8 savršeno zatvara ciklus rada objašnjavajući **zašto PR postoji** (kapija kontrole kvalitete) prije nego što objašnjava **kako** ga otvoriti. Analogija s "predajom zadaće profesoru" je pogođena — povezuje formalni GitHub proces s iskustvom koje svaki početnik ima iz škole.

### 2. Poglavlje 9 (Merge) — jasno odvaja odgovornosti
Jasno razgraničava tko smije mergati (maintainer) i zašto autor ne smije mergati vlastiti PR. To uči **timsku disciplinu** koja je često zanemarena u tehničkim uputstvima. Dijagram životnog ciklusa PR-a (8.5) i vizualni prikaz statusa mergea (zelene kvačice) su izvrsni za vizualne učenike.

### 3. Poglavlje 10 (Word template) — rješava ključnu zabunu
Jedna od najčešćih zabuna početnika u docs-as-code je: *"Ako ne formatiram u Wordu, tko odlučuje kako će izgledati?"* Poglavlje 10 elegantno objašnjava separaciju sadržaja i oblika. Dijagram "Kako Quarto koristi template" (10.2) je odličan. Naglasak da autor **ne treba dirati template** smanjuje tjeskobu.

### 4. Poglavlje 11 (GitHub Actions) — pravi odnos "trebaš znati / ne trebaš znati"
Autor svjesno odvaja ono što korisnik **treba znati** (status ikone, gdje gledati log, kako preuzeti artifact) od onoga što **ne treba znati** (YAML sintaksa, runners, environment varijable). To je ključno za početnike koji inače osjećaju da moraju razumjeti sve. Analogija s "automatskom praonicom rublja" je odlična.

### 5. Poglavlje 12 (Lokalni render) — pragmatično razgraničenje
Jasno objašnjava **zašto** renderirati lokalno (brza provjera, rad bez interneta) i **kada** (prije pusha). Tablica usporedbe lokalnog rendera vs. GitHub Actions (12.6) je korisna referenca. Upute za otvaranje terminala iz File Explorera (adresna traka → `cmd`) su izvrsne za Windows početnike koji se boje terminala.

### 6. Poglavlje 13 (Dodaci) — izvrsna ideja, dobro izvedena
Cheat sheet (13.1) je kompaktan i pokriva svakodnevne akcije. Rječnik pojmova (13.2) prevodi žargon u razumljiv jezik. Top 10 grešaka (13.3) su stvarne, praktične situacije — ne teoretski scenariji. Savjet o korištenju AI alata (13.4) je moderan i praktičan.

---

## Područja koja bi se mogla poboljšati

### 1. Poglavlje 8: Nedostaje "što ako nemaš recenzenta?"
Uputstvo pretpostavlja da postoji osoba koja će pregledati PR. U malim timovima (2–3 osobe) ili kada svi pišu istovremeno, recenzent može biti nedostupan. Nema uputa za:
- Što ako si jedini autor trenutno aktivan?
- Možeš li sam sebi postaviti PR i pregledati ga?
- Koliko dugo čekati na recenziju?

**Sugestija:** Dodati odjeljak "Ako recenzent nije dostupan" s preporukom (npr. "Ako nemaš recenzenta 24 sata, javi voditelju").

### 2. Poglavlje 9: "Delete branch" može zvučati zastrašujuće
Za početnika, gumb "Delete branch" zvuči kao da briše rad. Iako uputstvo objašnjava da se promjene ne brišu, to je kritična točka gdje bi netko mogao paničariti.

**Sugestija:** Dodati veći vizualni naglasak (⚠️ ili 💡) uz objašnjenje da brisanje brancha **ne briše commitove**, zajedno s mini-dijagramom:
```
branch (radna kopija)  -->  merge u main  -->  branch se briše
     |                                                    |
     +-----> commitovi su trajno spremljeni u main <------+
```

### 3. Poglavlje 10: Nedostaje primjer "prije i poslije"
Iako objašnjava mehanizam, nema vizualnog primjera kako izgleda Markdown tekst **prije** i kako izgleda Word dokument **poslije** primjene templatea. Za početnika je teško zamisliti ovu transformaciju.

**Sugestija:** Dodati dvije slike ili ASCII prikaze:
- Lijevo: `# Naslov poglavlja` (sirovi Markdown)
- Desno: Naslov poglavlja u Calibri 16pt Bold plavi (renderirani Word)

### 4. Poglavlje 11: "Crveni X" — ali što ako je greška u templateu?
Top 10 grešaka (13.3) pokriva mnoge scenarije, ali Poglavlje 11 ne objašnjava što ako Actions padne zbog greške u `.github/workflows/render.yml` koju korisnik nije dirao.

**Sugestija:** Dodati rečenicu: *"Ako greška pokazuje na `.github/workflows/` folder, a ti nisi dirao te datoteke — to je posao maintainera. Pošalji mu screenshot loga."*

### 5. Poglavlje 12: `quarto preview` vs. `quarto render` — nedostaje upozorenje
`quarto preview` pokreće lokalni server koji "gleda" datoteke. Ako početnik zatvori terminal bez `Ctrl+C`, server ostaje aktivan u pozadini i može zauzimati port.

**Sugestija:** Dodati mali upozoravajući okvir: *"Za zaustavljanje previewa uvijek pritisni `Ctrl+C` u terminalu. Ako zaboraviš, sljedeći put možeš dobiti grešku da je port zauzet."*

### 6. Poglavlje 12: `_quarto.yml` — nedostaje vizualna poveznica
Uputstvo kaže "ako fali tvoja datoteka u `chapters`, poglavlje neće biti u outputu". Ali početnik ne zna kako izgleda ispravan unos. Primjer YAML-a je dan, ali nema vizualne poveznice s lijevim izbornikom u Obsidianu.

**Sugestija:** Dodati primjer: *"Ako si kreirao/la `docs/04-zakljucak.md`, a u `_quarto.yml` piše samo do `03-rezultati.md`, tvoje poglavlje je nevidljivo za Quarto."*

### 7. Poglavlje 13: Cheat sheet — nedostaje "Undo" akcije
Cheat sheet pokriva "sretni put", ali ne pokriva najčešće "spašavanje" situacije: **kako poništiti zadnji commit**, **kako vratiti obrisanu datoteku**, **kako izaći iz merge konflikta ako zapneš**.

**Sugestija:** Dodati redak u cheat sheet:
| Poništi zadnji commit (ako nisi pushao) | — | `git reset --soft HEAD~1` |

### 8. Poglavlje 13: Greška #10 — humor je dobar, ali nedostaje struktura
Greška #10 ("Ne razumijem zašto se Quarto ruši") ima humorističan ton ("GIT! GIT! GIT!"), ali praktički savjet ("Kopiraj grešku i pošalji administratoru") je previše pasivan. Za početnika koji želi naučiti, bilo bi korisnije dati **jedan konkretan primjer** kako samostalno dijagnosticirati.

**Sugestija:** Zadržati humor, ali dodati: *"Prije nego pošalješ administratoru, provjeri ove 3 stvari: (1) jesi li u pravom folderu, (2) jesi li spremio/la datoteku prije rendera, (3) jesi li zatvorio/la Word dokument prije rendera (Word drži datoteku zaključanom)."*

### 9. Nedostaje poglavlje o "životu nakon prvog projekta"
Poglavlja 8–13 završavaju s "Kraj priručnika!", ali ne objašnjavaju što se događa kada početnik završi prvi projekt i počinje drugi. Treba li ponovno sve instalirati? Kako klonirati novi repozitorij?

**Sugestija:** Dodati kratki odjeljak 13.5: "Sljedeći projekt — što ponoviti, što ne" s checklistom.

---

## Ukupna procjena (Poglavlja 8–13)

| Aspekt | Ocjena | Komentar |
|--------|--------|----------|
| Procesna disciplina | ⭐⭐⭐⭐⭐ | PR, merge, recenzija — sve jasno strukturirano |
| Tehnički detalji | ⭐⭐⭐⭐☆ | Dovoljno za početak, ali nedostaje dubina u edge case-ovima |
| Praktična primjenjivost | ⭐⭐⭐⭐⭐ | Cheat sheet i Top 10 grešaka su izvrsni alati |
| Vizualizacija | ⭐⭐⭐☆☆ | Nedostaje "prije/poslije" primjera za template i render |
| Rješavanje problema | ⭐⭐⭐⭐☆ | Top 10 je dobar, ali nedostaje "undo" referenca |
| Zatvaranje ciklusa | ⭐⭐⭐☆☆ | "Kraj priručnika" je nagao — nedostaje "što dalje" |

---

## Ključne preporuke

### 1. Dodati "prije/poslije" vizualni primjer u Poglavlje 10
Jedna slika ili ASCII prikaz koji pokazuje:
```
Markdown:          Word (nakon template):
# Naslov     -->   NASLOV (Calibri 16pt Bold Plavi)
Tekst...     -->   Tekst... (Times 11pt)
```
To bi eliminirao 80% zabune o tome "tko odlučuje o izgledu".

### 2. Proširiti Cheat Sheet s "spašavanjem"
Dodati 3–4 redka za najčešće "undo" situacije:
- Poništi zadnji commit (prije pusha)
- Vrati obrisani redak (ako si zatvorio Obsidian)
- Prekini merge konflikt i vrati se na prijašnje stanje

### 3. Dodati "Sljedeći projekt" odjeljak na kraj
Kratka checklista što treba ponoviti za novi projekt:
- [ ] Novi GitHub račun? Ne, isti ostaje
- [ ] Nova instalacija alata? Ne, već imam
- [ ] Novi PAT token? Da, ako je stari istekao
- [ ] Novi vault? Da, kloniraj novi repozitorij
- [ ] Novi branch? Da, za svaki zadatak

---

## Usporedba svih poglavlja (1–13)

| Faza | Poglavlja | Glavni izazov za početnika | Autorov odgovor |
|------|-----------|---------------------------|-----------------|
| **Motivacija** | 1 | "Zašto bih mijenjao način rada?" | Usporedba starih vs. novih alata |
| **Postavljanje** | 2–3 | "Hoću li uspjeti instalirati sve?" | Korak-po-korak s provjerama |
| **Prvi rad** | 4–7 | "Kako ne pokvariti tuđi rad?" | Branching, vlasništvo, česti commiti |
| **Timske interakcije** | 8–9 | "Kako predati rad i dobiti odobrenje?" | PR proces s jasnim ulogama |
| **Automatizacija** | 10–12 | "Kako izgleda finalni dokument?" | Template + Actions + lokalni render |
| **Samostalnost** | 13 | "Što ako zapnem sam?" | Cheat sheet, rječnik, AI savjet |

Uputstvo kao cjelina prati **izvrsnu pedagošku krivulju** — od straha prema samostalnosti. Poglavlja 8–13 su posebno jaka u učenju **procesne discipline** (PR, merge, recenzija) koja je često zanemarena u tehničkim vodičima.

Jedina veća mana cijelog uputstva je nedostatak **vizualnih primjera transformacije** (Markdown → Word) i **"undo" referenci** za trenutke panike. Ako se to doda, ovo bi bio vrhunski vodič za početnike u docs-as-code.
