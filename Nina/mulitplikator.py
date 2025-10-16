from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, A3
def create_script(font_size, x, y, page_size):
    c = canvas.Canvas("int.pdf", page_size)
    c.setFont("Helvetica", font_size)
    c.drawString(x, y, "Hallo Welt")
    c.save()
create_script(12, 200, 400, A5)

def create_script(font_size, page_size):
    x,y = page_size # Tuple, Output: [(x)419.528, (y)595.276]
    c = canvas.Canvas("mulitplikator.pdf", page_size)
    c.setFont("Helvetica", font_size)
    c.drawString(x * 0.5, y * 0.5, "Hallo Welt")
    c.save()
create_script(12, A5)