


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, A3, A2
import json
from datetime import datetime

blatt = A4
x,y = blatt
x,y = (int(x),int(y))
print(f"X = {x} Y = {y}")









import string
c = canvas.Canvas("L Titel.pdf", pagesize=blatt)
def titel(fontSize=60):
    """Schreibt RECHNUNG groß oben links hin"""
    c.setFontSize(fontSize)    
    c.drawString(x*0.1,y-y*0.15,"RECHNUNG")
    # print(x*0.1,y-y*0.1)

titel()
c.save()



from datetime import datetime
c = canvas.Canvas("L NrDatum.pdf", pagesize=blatt)
def nrDatum(nummer, datum, fontSize=15):
    """Schreibt die Rechnungsnummer an die Rechte seite der Rechnung"""
    c.setFontSize(fontSize)
    tempx, tempy = x-x*0.1,y-y*0.20
    c.drawRightString(tempx, tempy, f"Rechnung NR. {nummer}")
    tempx, tempy = tempx, tempy -15
    c.drawRightString(tempx, tempy, datum)

nrDatum(12345, datetime.today().strftime('%d . %m . %Y'))
c.save()




c = canvas.Canvas("L Receiver.pdf", pagesize=blatt)
def receiver(person, fontSize=15):
    """Schreibt den Rechnungsempfänger unter den Titel"""
    c.setFontSize(fontSize)
    c.drawString(x*0.1,y-y*0.20,"RECHNUNG AN:")
    tempx, tempy = x*0.1,y-y*0.20 -15
    for i in person:
        tempx, tempy = tempx, tempy -15
        c.drawString(tempx, tempy,i)

receiver(["Vincent Muster","Jede Strasse 123","12345 Jede Stadt"])
c.save()



c = canvas.Canvas("L Einkaufsliste.pdf", pagesize=blatt)
def rechnung(einkaufsliste, fontSize=15):
    """Nimmt ein jsonfilepath zu einer Einkaufliste entgegen
    und gibt eine graphische Liste mit den gekauften Items wieder"""
    steuer = 19
    c.setFontSize(fontSize)
    tempx, tempy = x-x*0.1,y-y*0.35
    # tempx, tempy = tempx, tempy -10
    # with open(jsonfilepath, "r",encoding="UTF-8") as file:

    # file = json.load(file)
    c.drawRightString(tempx, tempy, file["verkäufer"])
    tempx, tempy = x*0.1,y-y*0.35
    tempx, tempy = tempx, tempy -10
    c.line(x *0.9, tempy, x * 0.1, tempy)
    tempx, tempy = tempx, tempy -20
    c.drawString(tempx + 10, tempy, "Beschreibung")
    c.drawString(x * 0.5, tempy, "Anzahl")
    c.drawString(x * 0.65, tempy, "Preis")
    c.drawString(x * 0.8, tempy, "Summe")
    tempx, tempy = tempx, tempy -20
    c.line(x *0.9, tempy, x * 0.1, tempy)
    zwischensumme = 0
    for i in einkaufsliste:
        tempx, tempy = tempx, tempy -20
        c.drawString(tempx + 10, tempy, i["produkt"])
        c.drawString(x * 0.5, tempy, str(i["menge"]))
        c.drawString(x * 0.65, tempy, str(i["preis_pro_einheit"]) + "€")
        # summe = (int((i["preis_pro_einheit"] * i["menge"])*100))/100
        summe = round(i["preis_pro_einheit"] * i["menge"],2)
        c.drawString(x * 0.8, tempy, str(summe) + "€")
        zwischensumme += summe
        tempx, tempy = tempx, tempy -20
        c.line(x *0.9, tempy, x * 0.1, tempy)
    tempx, tempy = tempx, tempy -20
    c.drawString(x * 0.5, tempy, f"Zwischensumme")
    c.drawString(x * 0.8, tempy, f"{zwischensumme}€")
    
    tempx, tempy = tempx, tempy -40
    c.drawString(x * 0.5, tempy, f"Steuer ({steuer} %)")
    steuer = round(zwischensumme * (steuer /100),2)
    c.drawString(x * 0.8, tempy, f"{steuer}€")
    tempx, tempy = tempx, tempy -20
    c.line(x *0.9, tempy, x * 0.5, tempy)
    tempx, tempy = tempx, tempy -20
    c.drawString(x * 0.5, tempy, f"Summe")
    endsumme = round(zwischensumme + steuer,2)
    c.drawString(x * 0.8, tempy, f"{endsumme}€")
    # print(endsumme)


with open("Einkaufliste.json", "r",encoding="UTF-8") as file:
    file = json.load(file)
    rechnung(file["einkaufsliste"])

c.save()



def create_pdf(json_data, blatt, font, receiver_font, nrDatum_font, rechnung_font):
    with open(json_data, "r",encoding="UTF-8") as file:
        global c, x, y # Declare as global to modify the global variables
        x,y = blatt
        x,y = (int(x),int(y))
        file = json.load(file)
        c = canvas.Canvas(f"Rechnung_{file['person']['name']}.pdf", pagesize=blatt)
        titel(font)
        receiver([file["person"]["name"] + file["person"]["nachname"], file["person"]["wohnort"], str(file["person"]["postleitzahl"]) + file["person"]["stadt"]], receiver_font)
        nrDatum(file["vertragsnummer"], datetime.today().strftime('%d . %m . %Y'), nrDatum_font)
        rechnung(file["einkaufsliste"], rechnung_font)
        c.save()

create_pdf("Einkaufliste.json", A4, 40, 15, 15, 15)

create_pdf("Einkaufliste2.json", A2, 30, 10, 10, 10)


