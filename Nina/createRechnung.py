from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import black, white

def create_invoice_pdf(filename="rechnung.pdf"):
    """Erstellt eine PDF-Rechnung, die genau wie das Beispielbild aussieht"""
    
    # PDF-Dokument erstellen
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # Startposition von oben
    y_pos = height - 3*cm
    
    # RECHNUNG - Große Überschrift
    c.setFont("Helvetica-Bold", 32)
    c.drawString(3*cm, y_pos, "RECHNUNG")
    
    y_pos -= 4*cm
    
    # Rechnungsdetails - Links und Rechts
    c.setFont("Helvetica-Bold", 10)
    
    # Links: RECHNUNG AN:
    c.drawString(3*cm, y_pos, "RECHNUNG AN:")
    
    # Rechts: RECHNUNG NR. und Datum
    c.drawString(13*cm, y_pos, "RECHNUNG NR. 12345")
    
    y_pos -= 0.5*cm
    c.drawString(13*cm, y_pos, "28. APRIL 2030")
    
    y_pos -= 1*cm
    
    # Kundendetails
    c.setFont("Helvetica", 10)
    c.drawString(3*cm, y_pos, "VINCENT VOGELSTETTER")
    y_pos -= 0.4*cm
    c.drawString(3*cm, y_pos, "JEDE STRASSE 123")
    y_pos -= 0.4*cm
    c.drawString(3*cm, y_pos, "12345 JEDE STADT")
    
    y_pos -= 2.5*cm
    
    # Dienstleister
    c.setFont("Helvetica", 9)
    c.drawString(9*cm, y_pos, "FOTOGRAFIE - SARAH MARCHSREITER")
    
    y_pos -= 1.5*cm
    
    # Tabelle - Kopfzeile
    c.setFont("Helvetica-Bold", 10)
    
    # Tabellenkopf Hintergrund (grau)
    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.rect(3*cm, y_pos - 0.3*cm, 15*cm, 0.8*cm, fill=1, stroke=0)
    
    # Tabellenkopf Text
    c.setFillColorRGB(0, 0, 0)
    c.drawString(3.2*cm, y_pos, "Beschreibung")
    c.drawString(10*cm, y_pos, "Anzahl")
    c.drawString(12.5*cm, y_pos, "Preis")
    c.drawString(15.5*cm, y_pos, "Summe")
    
    y_pos -= 1*cm
    
    # Tabelleninhalt
    c.setFont("Helvetica", 10)
    
    # Zeile 1: Eventfotografie
    c.drawString(3.2*cm, y_pos, "Eventfotografie (4-stündiges Event)")
    c.drawString(10.2*cm, y_pos, "4")
    c.drawString(12.2*cm, y_pos, "125€")
    c.drawString(15.2*cm, y_pos, "500€")
    
    # Linie unter erster Zeile
    c.line(3*cm, y_pos - 0.2*cm, 18*cm, y_pos - 0.2*cm)
    
    y_pos -= 0.8*cm
    
    # Zeile 2: Portraitfotoshooting
    c.drawString(3.2*cm, y_pos, "Portraitfotoshooting")
    c.drawString(10.2*cm, y_pos, "1")
    c.drawString(12.2*cm, y_pos, "185€")
    c.drawString(15.2*cm, y_pos, "185€")
    
    # Linie unter zweiter Zeile
    c.line(3*cm, y_pos - 0.2*cm, 18*cm, y_pos - 0.2*cm)
    
    y_pos -= 0.8*cm
    
    # Zeile 3: Bildbearbeitung
    c.drawString(3.2*cm, y_pos, "Bildbearbeitung (35 Bilder)")
    c.drawString(10.2*cm, y_pos, "35")
    c.drawString(12.5*cm, y_pos, "5€")
    c.drawString(15.2*cm, y_pos, "175€")
    
    # Linie unter dritter Zeile
    c.line(3*cm, y_pos - 0.2*cm, 18*cm, y_pos - 0.2*cm)
    
    y_pos -= 1.2*cm
    
    # Zwischensumme
    c.setFont("Helvetica-Bold", 10)
    c.drawString(13*cm, y_pos, "Zwischensumme")
    c.drawString(15.5*cm, y_pos, "860€")
    
    y_pos -= 0.6*cm
    
    # Steuer
    c.setFont("Helvetica", 10)
    c.drawString(13*cm, y_pos, "Steuer (0 %)")
    c.drawString(16*cm, y_pos, "0 €")
    
    y_pos -= 0.8*cm
    
    # Gesamtsumme - Schwarzer Balken
    c.setFillColorRGB(0, 0, 0)
    c.rect(12.5*cm, y_pos - 0.3*cm, 5.5*cm, 0.8*cm, fill=1, stroke=0)
    
    # Summe Text in Weiß
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(13*cm, y_pos, "Summe")
    c.drawString(15.5*cm, y_pos, "860€")
    
    # Zurück zu schwarz für weiteren Text
    c.setFillColorRGB(0, 0, 0)
    
    y_pos -= 4*cm
    
    # Zahlungsinformationen
    c.setFont("Helvetica-Bold", 10)
    c.drawString(3*cm, y_pos, "ZAHLUNGSINFORMATIONEN:")
    
    y_pos -= 0.8*cm
    
    c.setFont("Helvetica", 10)
    c.drawString(3*cm, y_pos, "EMPFÄNGER: SARAH MARCHSREITER")
    
    y_pos -= 0.5*cm
    c.drawString(3*cm, y_pos, "KONTONUMMER: 0123 4567 8901")
    
    # PDF speichern
    c.save()
    print(f"Rechnung wurde erfolgreich erstellt: {filename}")

def main():
    """Hauptfunktion zum Erstellen der Rechnung"""
    create_invoice_pdf("rechnung_sarah_marchsreiter.pdf")

if __name__ == "__main__":
    main()