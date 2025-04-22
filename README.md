# MetroStar Data Ingestion Pipeline

This project is designed to crawl MetroStar's website, download relevant documents (PDFs and DOCXs), extract their text content, and save the results into a structured JSON file for further analysis or processing.

## 📁 Project Structure

- `main.py`: Orchestrates the crawling, downloading, text extraction, and saving processes.
- `crawler.py`: Contains functions to crawl the website and collect document links.
- `download_docs.py`: Handles downloading of PDF and DOCX files.
- `extract_text.py`: Extracts text from downloaded documents.
- `parse.py`: Processes and cleans extracted text.
- `save_json.py`: Saves the processed data into a JSON file.
- `requirements.txt`: Lists all Python dependencies required to run the project.
- `README.md`: Provides an overview and setup instructions for the project.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/metrostar-ingestion-pipeline.git
   cd metrostar-ingestion-pipeline

2. **Create and activate a virutal environment:**
python -m venv venv

venv\Scripts\activate

3. **Install the required packages:**
pip install -r requirements.txt

3. **Install Playwright browsers**
playwright install

### Usage
To run the data ingestion pipeline:
python main.py 

### Configuration
The base URL and crawling depth can be adjusted in main.py:

BASE_URL = "https://www.metrostar.com"
DEPTH = 2

To manually add specific document links (e.g., Benefits & Perks PDF), append them to the all_links list in main.py:
all_links.append("https://www.metrostar.com/wp-content/uploads/2025/04/Benefits-and-Perks-2025.pdf")

### Testing
Ensure that each module functions correctly:

Crawler: Verify that crawler.py collects the correct URLs.

Downloader: Check that download_docs.py successfully downloads documents.

Extractor: Confirm that extract_text.py accurately extracts text.

Parser: Ensure that parse.py processes text as intended.

Saver: Validate that save_json.py writes the JSON file correctly.

