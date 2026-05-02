# Vademecum: Docs-as-Code

Ovaj kratki priručnik (šalabahter) služi za brzi podsjetnik na svakodnevni rad u Docs-as-Code okruženju koristeći Obsidian.

---

## 1. Brza Instalacija

Za samostalan rad na vašem računalu potrebno je jednom instalirati sljedeća tri programa (sve postavke tijekom instalacije ostavite na zadanim vrijednostima):

1. **[Git for Windows](https://git-scm.com/download/win):** Motor u pozadini koji pamti verzije.
2. **[Quarto CLI](https://quarto.org/docs/get-started/):** Sustav koji pretvara vaš tekst u PDF i DOCX.
3. **[Obsidian](https://obsidian.md/):** Aplikacija za pisanje (vaš digitalni notes).

Nakon instalacije, u Obsidianu odaberite **"Open folder as vault"** i odaberite mapu vašeg projekta.

---

## 2. Nužni Pluginovi u Obsidianu

Uđite u *Settings (zupčanik)* -> *Community plugins* -> *Turn off safe mode* -> *Browse*. Instalirajte sljedeće:

* **Obsidian Git:** Najvažniji plugin. Omogućava spremanje verzija i slanje na server bez korištenja terminala.
  * *Preporučena postavka:* Uključite `Auto Backup` na svakih 15 minuta.
* **Templater (za Snippets/Predloške):** Omogućava brzo ubacivanje unaprijed definiranih komada teksta (snippets). Npr. stisnete kraticu i on vam sam izbaci praznu Markdown tablicu, današnji datum ili UUID.
* **Web Clipper (opcionalno):** Za brzo spremanje tekstova s interneta direktno u Obsidian.
* **Dataview (opcionalno):** Napredna ekstenzija za automatsko generiranje tablica iz vaših bilješki.

---

## 3. Šalabahter za Markdown (Osnovne naredbe)

Zaboravite miša i izbornike, formatirajte tekst tipkovnicom!

| Želim napraviti... | Pišem u Obsidianu ovako... |
| :--- | :--- |
| **Glavni naslov** | `# Naslov` |
| **Podnaslov** | `## Podnaslov` |
| **Podebljano** | `**Ovo je važno**` |
| **Kurziv** | `*Ovo je koso*` |
| **Lista s nabrajanjem** | `- Prva stavka`<br>`- Druga stavka` |
| **Tablica** | <code>\| Stupac 1 \| Stupac 2 \|</code><br><code>\|---|---|</code><br><code>\| Podatak 1 \| Podatak 2 \|</code> |
| **Poveznica na drugi dokument** | `[[Ime drugog dokumenta]]` |
| **Citiranje literature** | `[@oznakaAutora2024]` |
| **Ubacivanje poglavlja** | `{{< include 01_Uvod.md >}}` |

---

## 4. Tijek rada (Workflow)

Vaš svakodnevni rad svodi se na tri jednostavna koraka:

1. **Otvori i preuzmi novo:** Kada otvorite Obsidian, Git plugin će automatski preuzeti promjene koje su kolege napravili dok vas nije bilo (ako ste uključili `Pull updates on startup`).
2. **Piši slobodno:** Kreirajte nove `.md` dokumente, povezujte ih UUID-ovima ili `[[linkovima]]`, provjeravajte veze kroz *Graph View*.
3. **Spremi i Pošalji (Commit):** 
   * Ako vam je uključen Auto-Backup, ne morate raditi ništa.
   * Ako želite ručno spremiti ključnu verziju, pritisnite `Ctrl + P` (ili `Cmd + P` na Macu), upišite `Git: Commit all changes and push` i pritisnite Enter.

Vaš rad je sada na sigurnom (GitHub) i automatski će se generirati konačni PDF!
