import os
import requests
from urllib.parse import urlparse
import re


def download_file(url, save_dir="downloads"):
    os.makedirs(save_dir, exist_ok=True)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/89.0.4389.82 Safari/537.36"
        )
    }

    try:
        with requests.get(url, headers=headers, stream=True, timeout=15) as response:
            response.raise_for_status()

            # Attempt to extract filename from Content-Disposition header
            content_disposition = response.headers.get("Content-Disposition")
            if content_disposition:
                filename_match = re.findall(
                    'filename="?([^";]+)"?', content_disposition
                )
                if filename_match:
                    filename = filename_match[0]
                else:
                    filename = os.path.basename(urlparse(url).path)
            else:
                filename = os.path.basename(urlparse(url).path)

            if not filename:
                print(f"Could not determine filename for URL: {url}")
                return None

            path = os.path.join(save_dir, filename)

            with open(path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            print(f"Downloaded: {filename}")
            return path

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None
