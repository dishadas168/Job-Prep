from pypdf import PdfReader

def get_text_from_pdf(pdf):
    reader = PdfReader(pdf)
    out = ""
    for page in reader.pages:
        out += page.extract_text()
    return out

