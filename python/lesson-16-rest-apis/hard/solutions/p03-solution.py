"""SOLUTION: scrape_api — paginated fetch with rate limiting (Hard)"""
import time
import requests

def scrape_api(base_url, endpoint, rate_limit=0.5):
    """Fetch paginated data with rate limiting. Handle 429 with Retry-After."""
    results = []
    page = 1

    while True:
        url = f"{base_url}/{endpoint}"
        params = {"page": page, "per_page": 100}
        response = requests.get(url, params=params)

        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 60))
            print(f"Rate limited. Waiting {retry_after}s...")
            time.sleep(retry_after)
            continue

        response.raise_for_status()
        data = response.json()

        if not data:
            break

        results.extend(data)

        if len(data) < 100:
            break

        page += 1
        time.sleep(rate_limit)

    return results

if __name__ == "__main__":
    results = scrape_api("https://api.github.com", "users/torvalds/repos")
    print(f"Total items scraped: {len(results)}")
