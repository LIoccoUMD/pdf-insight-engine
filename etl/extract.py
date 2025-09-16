import pymupdf
import pandas as pd
from pathlib import Path

# Ingest the data -- this is currently ingest.py in the tut i am following


def extract_pdf(pdf_paths):
    """
    Extract raw text from a PDF file. pdf_paths should be a pd.Series
    Returns a pd.Series object.

    texts = the entire text for one file
    """
    try:
        if isinstance(pdf_paths, str):
            return extract_helper(pdf_paths)
        if isinstance(pdf_paths, list):
            texts = {Path(path).stem: extract_helper(path) for path in pdf_paths}
            print(texts.keys()) # make keys more easily indexable (splice filename from end)
            return texts
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_paths}")
    except Exception as e:
        raise Exception(f"Error processing PDF {pdf_paths}: {str(e)}")


def extract_helper(pdf_path):
    doc = pymupdf.open(pdf_path)
    text = "".join(page.get_text() for page in doc)
    doc.close()
    return text
