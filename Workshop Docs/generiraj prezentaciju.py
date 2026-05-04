import datetime
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# --- Osnovne postavke ---
SIRINA = Inches(13.333)
VISINA = Inches(7.5)

FONT_NASLOV = "Calibri"
FONT_TIJELO = "Calibri"

BOJA_NASLOV = RGBColor(0x1B, 0x3A, 0x5C)
BOJA_TIJELO = RGBColor(0x33, 0x33, 0x33)
BOJA_POZADINA = RGBColor(0xFF, 0xFF, 0xFF)
BOJA_ZAGLAVLJE_TABLICE = RGBColor(0x1B, 0x3A, 0x5C)
BOJA_TEKST_ZAGLAVLJE = RGBColor(0xFF, 0xFF, 0xFF)

# --- Pomoćne funkcije ---

def dodaj_broj_slajda(slide, broj):
    left = SIRINA - Inches(1.2)
    top = VISINA - Inches(0.5)
    txBox = slide.shapes.add_textbox(left, top, Inches(1.0), Inches(0.4))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = str(broj)
    p.font.size = Pt(10)
    p.font.color.rgb = BOJA_NASLOV
    p.alignment = PP_ALIGN.RIGHT

def oblikuj_naslov(shape, text):
    shape.text = text
    for paragraph in shape.text_frame.paragraphs:
        paragraph.font.size = Pt(30)
        paragraph.font.bold = True
        paragraph.font.color.rgb = BOJA_NASLOV
        paragraph.font.name = FONT_NASLOV

def oblikuj_tijelo(placeholder, bullets):
    text_frame = placeholder.text_frame
    text_frame.clear()
    text_frame.word_wrap = True
    for i, bullet in enumerate(bullets):
        if i == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()
        p.text = bullet
        p.font.size = Pt(18)
        p.font.color.rgb = BOJA_TIJELO
        p.font.name = FONT_TIJELO
        p.space_after = Pt(6)

def novi_slajd(prs, layout_index, title, bullets=None, slide_number=1):
    layout = prs.slide_layouts[layout_index]
    slide = prs.slides.add_slide(layout)
    pozadina = slide.background
    fill = pozadina.fill
    fill.solid()
    fill.fore_color.rgb = BOJA_POZADINA

    title_shape = slide.shapes.title
    if title_shape:
        oblikuj_naslov(title_shape, title)
    
    if bullets and len(slide.shapes.placeholders) > 1:
        body = slide.shapes.placeholders[1]
        oblikuj_tijelo(body, bullets)
    
    dodaj_broj_slajda(slide, slide_number)
    return slide

def naslovni_slajd(prs, title, subtitle, slide_number):
    layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(layout)
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BOJA_POZADINA

    title_shape = slide.shapes.title
    oblikuj_naslov(title_shape, title)
    title_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

    subtitle_shape = slide.shapes.placeholders[1]
    subtitle_shape.text = subtitle
    for paragraph in subtitle_shape.text_frame.paragraphs:
        paragraph.font.size = Pt(20)
        paragraph.font.color.rgb = BOJA_TIJELO
        paragraph.font.name = FONT_TIJELO
        paragraph.alignment = PP_ALIGN.CENTER

    dodaj_broj_slajda(slide, slide_number)
    return slide

def slajd_s_tablicom(prs, title, zaglavlje1, zaglavlje2, redovi, slide_number):
    layout = prs.slide_layouts[5]  # Blank
    slide = prs.slides.add_slide(layout)
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BOJA_POZADINA

    left = Inches(0.8)
    top = Inches(0.4)
    width = SIRINA - Inches(1.6)
    height = Inches(0.8)
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = BOJA_NASLOV
    p.font.name = FONT_NASLOV
    p.alignment = PP_ALIGN.LEFT

    broj_redaka = len(redovi) + 1
    broj_stupaca = 2
    table_left = Inches(1.0)
    table_top = Inches(1.4)
    table_width = SIRINA - Inches(2.0)
    table_height = Inches(3.0)

    shape = slide.shapes.add_table(broj_redaka, broj_stupaca, table_left, table_top, table_width, table_height)
    table = shape.table

    table.columns[0].width = int(table_width * 0.4)
    table.columns[1].width = int(table_width * 0.6)

    for col_idx, header_text in enumerate([zaglavlje1, zaglavlje2]):
        cell = table.cell(0, col_idx)
        cell.text = header_text
        for paragraph in cell.text_frame.paragraphs:
            paragraph.font.size = Pt(20)
            paragraph.font.bold = True
            paragraph.font.color.rgb = BOJA_TEKST_ZAGLAVLJE
            paragraph.font.name = FONT_TIJELO
            paragraph.alignment = PP_ALIGN.CENTER
        cell.fill.solid()
        cell.fill.fore_color.rgb = BOJA_ZAGLAVLJE_TABLICE
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE

    for i, (prvi, drugi) in enumerate(redovi):
        row_idx = i + 1
        for col_idx, cell_text in enumerate([prvi, drugi]):
            cell = table.cell(row_idx, col_idx)
            cell.text = cell_text
            for paragraph in cell.text_frame.paragraphs:
                paragraph.font.size = Pt(16)
                paragraph.font.color.rgb = BOJA_TIJELO
                paragraph.font.name = FONT_TIJELO
            cell.fill.solid()
            if i % 2 == 0:
                cell.fill.fore_color.rgb = RGBColor(0xF0, 0xF5, 0xFA)
            else:
                cell.fill.fore_color.rgb = BOJA_POZADINA
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE

    dodaj_broj_slajda(slide, slide_number)
    return slide

# ========== KREIRANJE PREZENTACIJE ==========
prs = Presentation()
prs.slide_width = SIRINA
prs.slide_height = VISINA

br = 1

naslovni_slajd(prs,
    "Digitalna radionica: Novi način timskog pisanja\nza znanost i projekte",
    "Documents-as-code proces – puna kontrola nad dokumentima", br)
br += 1

novi_slajd(prs, 1, "Zašto smo ovdje danas?", [
    "„Izvješće_v1_final_konačno_Ana_ispravila.docx“",
    "Gubimo sate na traženje prave verzije",
    "Spajanje komentara i formatiranje troši kreativnu energiju",
    "Problem nismo mi – problem je sustav."
], br)
br += 1

slajd_s_tablicom(prs, "Kaos vs. Sustav",
    "Stari način (Kaos)", "Novi način (Sustav)",
    [
        ("Svatko ima svoju datoteku", "Jedna verzija za sve – uvijek aktualna"),
        ("Promjene se lako gube", "Sve izmjene su trajno sačuvane i vidljive"),
        ("Spajanje teksta je ručni posao", "Zna se točno tko je što i kada promijenio"),
        ("Formatiranje oduzima sate", "Dokument se automatski oblikuje sam")
    ], br)
br += 1

novi_slajd(prs, 1, "Promjena paradigme: Razdvajanje sadržaja od dizajna", [
    "Staro: fokus na izgledu (fontovi, margine, brojevi stranica)",
    "Novo: fokus isključivo na sadržaju",
    "Vi pišete samo čisti tekst. Računalo oblikuje.",
    "Prestajemo biti grafički urednici – postajemo autori sadržaja."
], br)
br += 1

novi_slajd(prs, 1, "AI obožava čisti tekst", [
    "Markdown je nativni jezik alata poput ChatGPT, Claude, Copilot",
    "Brže razumijevanje, lakše sažimanje i prevođenje",
    "Vaš repozitorij postaje privatna baza znanja za AI asistenta",
    "Rezultat: Pišete manje, dobivate više."
], br)
br += 1

novi_slajd(prs, 1, "Tri jednostavna alata (0 programiranja)", [
    "1. Obsidian – olovka za pisanje bez distrakcija",
    "2. Git – vremenski stroj koji čuva svaku verziju",
    "3. Quarto – robot koji automatski stvara finalni PDF/DOCX",
    "Sve se odvija unutar Obsidiana. Bez terminala, bez koda."
], br)
br += 1

novi_slajd(prs, 1, "1. Olovka: Pisanje bez distrakcija (Obsidian)", [
    "Izgleda kao Word, ali sprema čisti tekst",
    "Formatiranje tipkovnicom: # Naslov, **podebljano**, [@oznaka2024]",
    "Bez skrivenog oblikovanja, samo sadržaj"
], br)
br += 1

novi_slajd(prs, 1, "2. Vremenski stroj: Apsolutna sigurnost (Git)", [
    "Ništa se ne gubi – povratak na bilo koju stariju verziju jednim klikom",
    "Vidite točno tko je, kada i što mijenjao",
    "Radi u pozadini Obsidiana (plugin Obsidian Git)"
], br)
br += 1

novi_slajd(prs, 1, "3. Robot: Automatsko oblikovanje (Quarto)", [
    "Vi pišete tekst (Markdown), Quarto dodaje naslovnicu, margine, brojeve stranica, bibliografiju",
    "Generira savršen PDF ili DOCX prema službenom predlošku ustanove"
], br)
br += 1

novi_slajd(prs, 1, "Kako izgleda u praksi? (3 jednostavna koraka)", [
    "1. Piši – Otvorite Obsidian, pišete kao u Wordu",
    "2. Podijeli / Odobri – Jedan klik šalje izmjene, kolege pregledavaju i odobravaju (Pull Request)",
    "3. Generiraj – Sustav automatski gradi finalni PDF s potpunim dizajnom"
], br)
br += 1

novi_slajd(prs, 1, "Kraj 'Merge' konflikata: Modularno pisanje", [
    "Stari način: dvoje ljudi prepravlja isti Word dokument → kaos",
    "Docs‑as‑Code način: veliki dokument podijelimo u male .md datoteke",
    "Ana piše 01_Uvod.md, Marko 02_Razrada.md",
    "Quarto ih automatski spaja u jedan PDF",
    "Konflikti su matematički nemogući"
], br)
br += 1

novi_slajd(prs, 1, "Kada (ne) koristiti ovaj pristup?", [
    "✅ Najbolje za: EU projektne prijave, DMP, diplomski/doktorski radovi, timski elaborati",
    "❌ Bolje izbjegavati: kratke interne dopise, jednokratne bilješke, dokumente za jednu osobu"
], br)
br += 1

novi_slajd(prs, 1, "Pilot faza: počnite već danas", [
    "1. Instalirajte Git for Windows, Quarto CLI i Obsidian (sve zadane postavke)",
    "2. Preuzmite gotov fakultetski Template repozitorij",
    "3. Otvorite u Obsidianu, uključite 'Obsidian Git' plugin (auto‑spremanje svakih 15 minuta)",
    "4. Pišite – fokus samo na tekst, dizajn prepustite sustavu",
    "Gotov template i detaljne upute su spremni. Vaš novi čisti radni stol vas čeka."
], br)

# --- SPREMANJE S VREMENSKOM OZNAKOM ---
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
ime_datoteke = f"Docs_as_Code_prezentacija_{timestamp}.pptx"
prs.save(ime_datoteke)
print(f"Prezentacija uspješno spremljena: {ime_datoteke}")