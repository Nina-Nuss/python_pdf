from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# PDF-Dokument erstellen
c = canvas.Canvas("doc.pdf", pageSize=A4)  # Breite x Höhe in Punkten (1 Punkt = 1/72 Zoll)

# Überschrift
c.setFont("Helvetica-Bold", 16)
c.drawString(80, 800, "Erstellen eines PDFs mit ReportLab")



# Linie unter der Überschrift
c.line(80, 780, 500, 780)

c.setFont("Helvetica-Bold", 12)

c.drawString(80, 760, "Vorbereitung:")

c.setFont("Helvetica", 9)

c.drawString(100, 740, "1: Komandozeile: pip install reportlab")
c.drawString(100, 720, "2: Texteditor: from reportlab.pdfgen import canvas from reportlab.lib.pagesizes import A4")

c.drawString(100, 700, "3: Texteditor: c = canvas.Canvas('dateiname.pdf', pagesize=A4)")
c.drawString(380, 700, "# erstellt ein neues PDF-Dokument")


# Untertitel
c.setFont("Helvetica-Bold", 12)
c.drawString(80, 680, "Wichtige Funktionen von ReportLab:")

# Informationen in logischer Reihenfolge
c.setFont("Helvetica", 9)

c.drawString(100, 660, "-  c.setFont(schriftart, größe) ")
c.drawString(270, 660, "# Setzt die Schriftart und Größe, z.B. ('Helvetica' oder 'Helvetica-Bold', 12)")

c.drawString(100, 640, "-  c.drawString(x, y, 'text')")
c.drawString(270, 640, "# Fügt Text an der Position x, y hinzu, z.B. (100, 700, 'Hallo Welt')")

 # erstellt ein neues PDF-Dokument

 # erstellt ein neues PDF-Dokument
# Farbiges Beispiel
c.setFillColorRGB(0, 0, 1)  # Farbe auf Blau setzen (RGB-Werte von 0 bis 1)
c.drawString(100, 620, "-  c.setFillColorRGB(rot, grün, blau) ")
c.drawString(270, 620, "# Setzt die Füllfarbe für den Text, z.B. (0, 0, 1) für Blau")

# Farbe zurücksetzen
c.setFillColorRGB(0, 0, 0)  # Farbe auf Schwarz zurücksetzen
c.drawString(100, 600, "-  c.line(x1, y1, x2, y2)")
c.drawString(270, 600, "# Zeichnet eine Linie zwischen zwei Punkten, z.B. (100, 600, 400, 600)")

c.drawString(80, 570, "Reminder:")
c.drawString(80, 560, "x: Links, Rechts (Horizontal-Achse)")
c.drawString(80, 550, "y: Unten, Oben (Vertikal-Achse)")


c.setTitle("Mein PDF")         # PDF-Titel setzen
c.setAuthor("Max Mustermann")  # PDF-Autor setzen
c.setSubject("Wichtiges Dokument") # PDF-Betreff setzen

c.drawString(80, 510, "URL: https://docs.reportlab.com/")

# PDF speichern
c.save()

