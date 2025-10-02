from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('doc.pdf')

# printing nujkmber of pages in pdf file
print(len(reader.pages))

# creating a page object
page = reader.pages[0]

# extracting text from page
print(page.extract_text())