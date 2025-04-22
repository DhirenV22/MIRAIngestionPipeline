from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright

visited = set()


def is_internal_link(base_url, link):
    return base_url in link or urlparse(link).netloc == ""


def is_valid_url(url):
    parsed = urlparse(url)
    return (
        parsed.scheme in ["http", "https"]
        and not url.startswith("javascript:")
        and not url.startswith("tel:")
    )


def crawl_site(base_url, depth=2):
    all_links = set()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        queue = [base_url]
        for _ in range(depth):
            next_queue = []
            for url in queue:
                if url in visited:
                    continue
                print(f"Crawling: {url}")
                visited.add(url)
                try:
                    page.goto(url, timeout=15000)
                    anchors = page.query_selector_all("a[href]")
                    for a in anchors:
                        href = a.get_attribute("href")
                        if href:
                            full_url = urljoin(url, href)
                            if is_valid_url(full_url) and (
                                full_url.endswith(".pdf")
                                or full_url.endswith(".docx")
                                or is_internal_link(base_url, full_url)
                            ):
                                full_url = full_url.split("#")[
                                    0
                                ]  # remove hash fragment
                                all_links.add(full_url)
                                next_queue.append(full_url)
                except Exception as e:
                    print(f"Error crawling {url}: {e}")
            queue = list(set(next_queue))
        browser.close()
    return list(all_links)
