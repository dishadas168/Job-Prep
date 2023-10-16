from pypdf import PdfReader
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s - %(lineno)d")

def get_text_from_pdf(pdf):

    out = ""
    try:
        reader = PdfReader(pdf)
        for page in reader.pages:
            out += page.extract_text()
    except Exception as e:
        logging.error("An error occured in the PDF extraction process : %s", str(e))

    return out

