"""SOLUTION: Concurrent with gather (Easy)"""
import asyncio
import time

async def task1():
    await asyncio.sleep(0.3)
    return "task1 done"

async def task2():
    await asyncio.sleep(0.5)
    return "task2 done"

async def main():
    start = time.time()
    results = await asyncio.gather(task1(), task2())
    elapsed = time.time() - start
    print(f"Both tasks took {elapsed:.2f}s (should be ~0.5, not 0.8)")
    return results

if __name__ == "__main__":
    results = asyncio.run(main())
    assert results == ["task1 done", "task2 done"]
    print("All tests passed!")
