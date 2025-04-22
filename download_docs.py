import os
import requests


def download_file(url, save_dir="downloads"):
    os.makedirs(save_dir, exist_ok=True)
    filename = url.split("/")[-1].split("?")[0]
    path = os.path.join(save_dir, filename)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/89.0.4389.82 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
        return path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None
