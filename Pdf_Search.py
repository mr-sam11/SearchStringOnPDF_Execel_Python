# PyPDF2 is Python library
from PyPDF2 import PdfReader


def search_str(pdf_file, search_string):
    # Open the PDF file
    pdf_f = open(pdf_file, 'rb')
    pdf_reader = PdfReader(pdf_f)
    page_count = len(pdf_reader.pages);

    # This loop is used for pages of the PDF
    for page_num in range(page_count):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        # print(text);
        # This is used for split the text into lines
        lines = text.splitlines()
        # print(lines);
        # This loop is used for the lines of the text
        for line_num, line in enumerate(lines):
            # This conditional statement for if string is found
            if search_string in line:
                print(f"String is '{search_string}' found on page {page_num + 1} line {line_num + 1}")


#  Program For Search string on PDF and display the line and page no.
pdf_file = 'Pdfsample2.pdf'
search_string = input("Enter String Which You Want To Search   = ");
# search_string = "medical"
search_str(pdf_file, search_string)
