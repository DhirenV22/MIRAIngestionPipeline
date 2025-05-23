import os
import logging
from crawler.crawler import crawl_site
from crawler.download_docs import download_file
from crawler.extract_text import extract_pdf_text, extract_docx_text
from crawler.save_json import save_json
from crawler.parse import parse_document

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = "https://www.metrostar.com"
BENEFITS_PDF = (
    "https://www.metrostar.com/wp-content/uploads/2025/04/Benefits-and-Perks-2025.pdf"
)


def main():
    try:
        logging.info(f"Starting crawl at {BASE_URL}")
        all_links = crawl_site(BASE_URL, depth=2)

        # Ensure the Benefits & Perks PDF link is included
        if BENEFITS_PDF not in all_links:
            all_links.append(BENEFITS_PDF)

        logging.info(f"Total links found: {len(all_links)}")

        doc_texts = []

        for link in all_links:
            if link.endswith((".pdf", ".docx")):
                file_path = download_file(link)
                if file_path:
                    try:
                        if file_path.endswith(".pdf"):
                            text = extract_pdf_text(file_path)
                        elif file_path.endswith(".docx"):
                            text = extract_docx_text(file_path)
                        else:
                            logging.warning(f"Unsupported file type: {file_path}")
                            continue

                        parsed_data = parse_document(text)
                        doc_texts.append(
                            {"url": link, "text": text, "parsed": parsed_data}
                        )
                    except Exception as e:
                        logging.error(f"Error processing file {file_path}: {e}")
        save_json(doc_texts, "mira_ingested_data.json")
        logging.info("Data ingestion completed successfully.")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
