#Importiert wichtige Methoden und Blattgröße welche in  teilt diese in x un y aufgeteilt wird 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, A3
import json
from json import load
import string
import math
import datetime

blatt = A4 
x, y = blatt
x,y = (int(x),int(y))
print(f"X = {x} Y = {y}")

c = canvas.Canvas("PDFs/Titel.pdf", pagesize=blatt)
def titel(x, y, fontSize=40): # Nutze alle Parameter
    """Schreibt RECHNUNG groß oben links hin"""
# (x*0.10 , y*0.85, ....)

titel(x*0.10 , y*0.85, 34)
c.save()
