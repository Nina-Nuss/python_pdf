from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, A3
blatt = A3
x,y = blatt
x,y = (int(x),int(y))
x = 250
y = 150
c = canvas.Canvas("integer.pdf", pagesize=blatt)
c.setFont("Helvetica", 12)
c.drawString(x, y, "Hallo Welt")
c.save()


