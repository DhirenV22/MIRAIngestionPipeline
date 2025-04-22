import fitz  # PyMuPDF
from docx import Document


def extract_pdf_text(file_path):
    text = ""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        print(f"Extracted text from PDF: {file_path}")
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return text


def extract_docx_text(file_path):
    text = ""
    try:
        doc = Document(file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
        print(f"Extracted text from DOCX: {file_path}")
    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")
    return text
