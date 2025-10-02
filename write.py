from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# PDF mit Text erstellen
c = canvas.Canvas("doc.pdf", pagesize=letter)
c.drawString(100, 700, "Hello, World!")
c.drawString(100, 680, "This PDF was created using ReportghjgjLab.")

c.save()