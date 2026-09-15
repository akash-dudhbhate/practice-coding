"""SOLUTION: download_large_file — chunked download with progress (Hard)"""
import os
import requests

def download_large_file(url, filepath, chunk_size=8192):
    """Download a file in chunks with progress display. Handle network errors."""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        downloaded = 0

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        pct = (downloaded / total_size) * 100
                        print(f"\rDownloaded: {downloaded}/{total_size} bytes ({pct:.1f}%)", end="")
                    else:
                        print(f"\rDownloaded: {downloaded} bytes", end="")

        print(f"\nDone! Saved to {filepath}")
        return filepath

    except requests.ConnectionError:
        print(f"\nNetwork error — partial file may exist at {filepath}")
        if os.path.exists(filepath):
            os.remove(filepath)
        raise
    except requests.Timeout:
        print(f"\nDownload timed out")
        raise

if __name__ == "__main__":
    download_large_file(
        "https://raw.githubusercontent.com/python/cpython/main/README.rst",
        "README.rst"
    )
