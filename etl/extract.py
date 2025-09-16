import pymupdf
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def extract_pdf(pdf_paths):
    """
    Extract raw text from one or more PDF files.

    Args:
        pdf_paths (str | list[str]):
            - A single path to a PDF file as a string.
            - Or a list of paths to multiple PDF files.

    Returns:
        str | dict[str, str]:
            - If a single path is provided, returns the extracted text as a string.
            - If a list of paths is provided, returns a dictionary mapping
              filenames (without extension) to their extracted text.

    Raises:
        FileNotFoundError: If any provided file path does not exist.
        Exception: If an error occurs during PDF processing.
    """
    try:
        if isinstance(pdf_paths, str):
            return extract_helper(pdf_paths)
        if isinstance(pdf_paths, list):
            texts = {Path(path).stem: extract_helper(path)
                          for path in pdf_paths}
            # make keys more easily indexable (splice filename from end)
            print(texts.keys())
            return texts
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_paths}")
    except Exception as e:
        raise Exception(f"Error processing PDF {pdf_paths}: {str(e)}")


def extract_helper(pdf_path):
    """
    Extract raw text from a single PDF file.

    Args:
        pdf_path (str | pathlib.Path):
            Path to a PDF file. If a relative path is given,
            it is resolved against the project 'data/' directory.

    Returns:
        str: The full extracted text from the PDF file.

    Raises:
        FileNotFoundError: If the file cannot be found at the resolved path.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.is_absolute():
        pdf_path = DATA_DIR / pdf_path  # resolve relative to data folder
    pdf_path = pdf_path.resolve()

    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")

    doc = pymupdf.open(str(pdf_path))
    text = "".join(page.get_text() for page in doc)
    doc.close()
    return text
