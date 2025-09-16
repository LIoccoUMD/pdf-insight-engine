from etl.extract import extract_pdf, DATA_DIR


def run_ingestion():
    raise NotImplementedError("run_ingestion method has not been implemented yet")
    return
# run_ingestion()

def run_analysis():
    raise NotImplementedError("run_analysis method has not been implemented yet")
    return
# run_analysis()

def start_server(mode):
    raise NotImplementedError("start_server method has not been implemented yet")
    return
# start_server("api")

files = [
    "cocacola2025.pdf",
    "ford2024.pdf",
    "goog2024.pdf"
]

text = extract_pdf([DATA_DIR / f for f in files])
# print(text)
for filename, content in text.items():
    print(f"--- {filename} --- {len(content)} characters extracted ---")
    print(content[:1])  # Show the first 400 characters
    print("...\n")