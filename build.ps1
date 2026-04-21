# ============================================
# Docs-as-code build script (Windows)
# Projekt: Sanacija stadiona Poljud
# ============================================

Write-Host "➡️ Pokrećem build..." -ForegroundColor Cyan

# 1. Kreiraj / očisti build folder
if (Test-Path build) {
    Write-Host "🧹 Brišem postojeći build folder..."
    Remove-Item build -Recurse -Force
}
New-Item -ItemType Directory -Path build | Out-Null

# 2. Lista dokumenata (redoslijed je BITAN!)
$docs = @(
    "index.md",
    "00-admin/*.md",
    "01-opis-projekta/*.md",
    "02-tehnicka-dokumentacija/*.md"
)

# 3. Build DOCX
Write-Host "📄 Generiram Word dokument..."

pandoc `
  $docs `
  -o build/sanacija-poljud.docx `
  --reference-doc=.\reference.docx `
  --toc `
  --number-sections `
  --metadata title="Sanacija stadiona Poljud"

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Greška kod DOCX builda!" -ForegroundColor Red
    exit 1
}

# 4. Build PDF (opcionalno - treba LaTeX)
Write-Host "📕 Generiram PDF..."

pandoc `
  $docs `
  -o build/sanacija-poljud.pdf `
  --toc `
  --number-sections `
  --pdf-engine=xelatex `
  --metadata title="Sanacija stadiona Poljud"

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️ PDF build nije uspio (vjerojatno nemaš LaTeX)" -ForegroundColor Yellow
}

# 5. Otvori Word dokument
Write-Host "🚀 Otvaram Word dokument..."
Start-Process "build/sanacija-poljud.docx"

Write-Host "✅ Build gotov!" -ForegroundColor Green