"""SOLUTION: fetch_with_retry — exponential backoff (Medium)"""
import time
import requests

def fetch_with_retry(url, max_retries=3):
    """Retry on failure (5xx or timeout) with exponential backoff."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code < 500:
                return response.json()
            print(f"Server error {response.status_code}, retrying...")
        except requests.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
        except requests.ConnectionError:
            print(f"Connection error on attempt {attempt + 1}")

        if attempt < max_retries - 1:
            wait = 2 ** attempt  # 1s, 2s, 4s
            print(f"Waiting {wait}s before retry...")
            time.sleep(wait)

    raise Exception(f"Failed after {max_retries} retries")

if __name__ == "__main__":
    data = fetch_with_retry("https://httpbin.org/get")
    print(data["url"])
