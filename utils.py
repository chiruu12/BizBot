
from PyPDF2 import PdfReader
def pdf_to_text(file):
    """Convert the PDF file to text."""
    pdf_reader = PdfReader(file)  # Creates a PDF reader object
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()  # Extracts text from each page
    return text

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file given its path."""
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text