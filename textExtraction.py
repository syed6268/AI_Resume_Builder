import pdfplumber
pdf_path='C:/Users/Mustafa Syed/Desktop/resumeschezeenfazulbhoy.pdf'
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
pdf_text = extract_text_from_pdf('C:/Users/Mustafa Syed/Desktop/resumeschezeenfazulbhoy.pdf')
