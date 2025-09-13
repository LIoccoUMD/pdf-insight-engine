import pymupdf

# Ingest the data -- this is currently ingest.py in the tut i am following
def extract_pdf(pdf_path):
    """
    Extract raw text frin a PDF file.
    """
    try:
        doc = pymupdf.open(pdf_path)
        text = "".join(page.get_text() for page in doc)
        doc.close()
        return text
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    except Exception as e:
        raise Exception(f"Error processing PDF {pdf_path}: {str(e)}")
