"""SOLUTION: Async Start/End (Easy)"""
import asyncio
import time

async def start_end():
    print("Start")
    await asyncio.sleep(0.5)
    print("End")

if __name__ == "__main__":
    start = time.time()
    asyncio.run(start_end())
    elapsed = time.time() - start
    assert 0.4 < elapsed < 0.7
    print(f"Took {elapsed:.2f}s — tests passed!")
