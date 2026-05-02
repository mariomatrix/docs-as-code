Koncept predavanja
Trajanje: 90 minuta (60 min predavanje + 30 min demo/Q&A)
Ciljana publika: Nastavnici, istraživači, administracija — mješovita tehnička pismenost.
Struktura
1. Uvod i problem (10 min)Trenutno stanje: Teams + WordBolne točke: versioning, merge conflicts, formatiranje, gubici podataka, nedostatak audit traila
2. Što docs-as-code znači: dokumenti kao kod — versioning, review, automatizacija, single source of truth2. Osnovni koncepti (15 min)Version control sustavi (Git) — što rješavaju, zašto su bolji od "Save As" Markup jezici: Markdown vs LaTeX vs Word — kad što koristiti Repository struktura za projekte i dokumente Branching strategija za dokumente (feature branches za sekcije)
3. Toolchain (15 min)Minimalni: Git + Markdown + VS Code (ili Obsidian)Akademski: Git + LaTeX + Overleaf (ili self-hosted GitLab s LaTeX runnerom) Hybrid: Word + Git (da, moguće je preko git-lfs ili specijalnih alata)CI/CD za dokumente: automatski PDF build, provjera pravopisa, validacija referenci, provjera formata4. Timski rad (10 min)Pull request workflow za recenzije i 
review = document review
Rješavanje konflikata – eksplicitno vs implicitno Uloge: author, reviewer, maintainer, approver Automatizacija (10 min)Template repository s već postavljenom strukturom za EU prijave, znanstvene radove, projektnu dokumentaciju Automatski PDF export na commit ili merge Provjera formata (npr. za EU prijave — font, margine, struktura)Integracija s reference managerima (Zotero, JabRef, Mendeley)
Demo (20 min) 
Pokaži stvarni repository s primjerom prijave projekta ili znanstvenog radaCommit \(\rightarrow \) build \(\rightarrow \) PDFPull request s komentarima i sugestijama
Merge i automatsko generiranje finalnog dokumenta
Povijest promjena — tko je što mijenjao i kad7. Implementacijski plan (10 min)
Faza 1: Pilot s jednom grupom ili katedrom (2-3 mjeseca)
Faza 2: Template i dokumentacija za ostale
Faza 3: Obuka i rollout na širu zajednicuŠto zadržati od starog sustava (npr. Teams za komunikaciju i sastanke)