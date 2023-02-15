#PyPDF2 is Python library
from PyPDF2 import PdfReader

pdf_f = open("Pdfsample2.pdf", 'rb')
pdf_reader = PdfReader(pdf_f)
page_count = len(pdf_reader.pages);
page = pdf_reader.pages[0]
text = page.extract_text()
        # print(text);
        #This is used for split the text into lines
print(text)
print("_____________________________________________________________________________")
lines = text.splitlines()

print(lines)
print(enumerate(lines[0]));