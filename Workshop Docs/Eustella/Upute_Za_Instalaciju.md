# Upute za instalaciju: Docs-as-Code radno okruženje

Ovaj vodič namijenjen je postavljanju vašeg osobnog računala za rad prema "Docs-as-Code" principu. Cilj nam je pisati u Obsidianu i jednim klikom sinkronizirati rad s kolegama.

## 1. Instalacija Quarta (Za automatsko formatiranje PDF i DOCX)
Quarto je znanstveno-tehnički sustav za izdavanje koji u pozadini koristi Pandoc.
1. Otiđite na službenu stranicu: [Quarto Download](https://quarto.org/docs/get-started/)
2. Preuzmite i instalirajte "Quarto CLI" za Windows.
3. *To je to. Quarto će sada sam rješavati komplicirane pretvorbe.*

## 2. Instalacija Gita (Sustav za verzije)
1. Otiđite na: [Git for Windows](https://git-scm.com/download/win)
2. Kliknite Download i instalirajte program (možete samo klikati "Next" kroz cijelu instalaciju, zadane postavke su u redu).

## 3. Instalacija Obsidiana (Aplikacija za pisanje)
1. Otiđite na: [Obsidian](https://obsidian.md/)
2. Preuzmite i instalirajte aplikaciju.
3. Otvorite aplikaciju i odaberite **"Open folder as vault"** (Otvorite mapu na računalu u kojoj se nalazi repozitorij vašeg projekta, npr. `Demo-Projekt`).

## 4. Postavljanje Obsidian Git Plugina
Ovo je ključni korak koji nam omogućuje da radimo s verzijama bez napuštanja Obsidiana.
1. U Obsidianu, kliknite na zupčanik (Settings) u donjem lijevom kutu.
2. Idite na **"Community plugins"** i isključite "Safe mode" (Turn off safe mode).
3. Kliknite na **"Browse"** i u tražilicu upišite `Obsidian Git`.
4. Instalirajte plugin (autor: Denis Olehov) i kliknite **"Enable"**.
5. Pod postavkama samog Obsidian Git plugina možete uključiti:
   - *Auto Backup*: Postavite na npr. `15` minuta. Sustav će sam svako 15 minuta spremati vaš rad i slati na poslužitelj.
   - *Pull updates on startup*: Sustav će automatski preuzeti rad vaših kolega kada upalite aplikaciju.

### Kako sinkronizirati ručno?
Ako ne želite auto-backup, možete u Obsidianu stisnuti `Ctrl + P` (Command palette), upisati `Git: Commit all changes and push` i pritisnuti Enter. Također možete dodati i malu ikonicu u alatnu traku pomoću postavki plugina.
