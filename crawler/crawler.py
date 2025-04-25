from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import time

visited = set()


def is_internal_link(base_url, link):
    base_netloc = urlparse(base_url).netloc
    link_netloc = urlparse(link).netloc
    return base_netloc == link_netloc or link_netloc == ""


def is_valid_url(url):
    parsed = urlparse(url)
    return (
        parsed.scheme in ["http", "https"]
        and not url.startswith("javascript:")
        and not url.startswith("tel:")
    )


def crawl_site(base_url, depth=2):
    all_links = set()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    queue = [base_url]
    for _ in range(depth):
        next_queue = []
        for url in queue:
            if url in visited:
                continue
            print(f"Crawling: {url}")
            visited.add(url)
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code != 200:
                    print(
                        f"Failed to retrieve {url}: Status code {response.status_code}"
                    )
                    continue
                soup = BeautifulSoup(response.content, "html.parser")
                anchors = soup.find_all("a", href=True)
                for a in anchors:
                    href = a["href"]
                    full_url = urljoin(url, href)
                    if is_valid_url(full_url):
                        full_url = full_url.split("#")[0]  # remove hash fragment
                        if full_url not in visited:
                            if full_url.endswith((".pdf", ".docx")) or is_internal_link(
                                base_url, full_url
                            ):
                                all_links.add(full_url)
                                next_queue.append(full_url)
            except Exception as e:
                print(f"Error crawling {url}: {e}")
            time.sleep(1)  # Be polite and avoid overwhelming the server
        queue = list(set(next_queue))
    return list(all_links)
