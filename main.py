# main.py
from crawler import crawl_site
from download_docs import download_file
from extract_text import extract_pdf_text, extract_docx_text
from save_json import save_json
from parse import parse_document  # Assuming you have a parse.py module
import os

BASE_URL = "https://www.metrostar.com"

all_links = crawl_site(BASE_URL, depth=2)

# Manually add the Benefits & Perks PDF link if it's not already in the list
benefits_pdf = (
    "https://www.metrostar.com/wp-content/uploads/2025/04/Benefits-and-Perks-2025.pdf"
)
if benefits_pdf not in all_links:
    all_links.append(benefits_pdf)

print(f"Total links found: {len(all_links)}")
print("\n".join(all_links))

doc_texts = []

for link in all_links:
    if link.endswith(".pdf") or link.endswith(".docx"):
        file_path = download_file(link)
        if file_path:
            if file_path.endswith(".pdf"):
                text = extract_pdf_text(file_path)
            elif file_path.endswith(".docx"):
                text = extract_docx_text(file_path)
            parsed_data = parse_document(text)  # Process the extracted text
            doc_texts.append({"url": link, "text": text, "parsed": parsed_data})

save_json(doc_texts, "mira_ingested_data.json")
