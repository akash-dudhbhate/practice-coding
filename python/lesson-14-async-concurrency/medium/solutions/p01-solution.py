"""SOLUTION: Fetch All Concurrently (Medium)"""
import asyncio

async def fetch(url):
    await asyncio.sleep(0.1)  # simulate network
    return f"Response from {url}"

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(url) for url in urls])

if __name__ == "__main__":
    urls = ["https://a.com", "https://b.com", "https://c.com"]
    results = asyncio.run(fetch_all(urls))
    assert len(results) == 3
    assert "a.com" in results[0]
    print("All tests passed!")
