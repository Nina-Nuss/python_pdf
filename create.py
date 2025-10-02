from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# PDF-Dokument erstellen test
c = canvas.Canvas("doc.pdf", pagesize=A4)  # Breite x Höhe in Punkten (1 Punkt = 1/72 Zoll)
#TEST
# Text hinzufügen
c.drawString(200, 700, "Erstellen eines PDFs mit ReportLab")
c.drawString(100, 680, "in der Kommandozeile eingeben: pip install reportlab")
c.drawString(100, 660, "Standard Letter Größe: 612 x 792 Punkte")

# Weitere Texte und Formatierungen
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 620, "Großer Tihgfdölkhhgtel")
c.drawString(200, 720, "Großer Titel")
c.drawString(200, 320, "Großer Titel")

c.setFont("Helvetica", 12)
c.drawString(200, 600, "Normaler Text in Standavcbcvbrd-Schriftgröße")

# Linie zeichnen
c.line(100, 580, 500, 580)

# PDF speichern
c.save()

print("✅ PDF 'doc.pdf' wurde erfolgreich erstellt!")