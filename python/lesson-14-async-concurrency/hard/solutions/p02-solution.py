"""SOLUTION: Async Scraper with Timeout (Hard)"""
import asyncio

async def fetch_with_timeout(url, timeout=5):
    try:
        await asyncio.wait_for(asyncio.sleep(0.1), timeout=timeout)
        return f"OK: {url}"
    except asyncio.TimeoutError:
        return f"TIMEOUT: {url}"

async def scrape_all(urls):
    return await asyncio.gather(*[fetch_with_timeout(url) for url in urls])

if __name__ == "__main__":
    urls = [f"https://api{i}.example.com" for i in range(5)]
    results = asyncio.run(scrape_all(urls))
    assert len(results) == 5
    assert all("OK" in r for r in results)
    print("All tests passed!")
