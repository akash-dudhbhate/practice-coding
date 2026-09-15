"""SOLUTION: Producer-Consumer with Queue (Hard)"""
import asyncio

async def producer(queue):
    for i in range(10):
        await queue.put(f"item-{i}")
        await asyncio.sleep(0.05)
    await queue.put(None)  # sentinel
    await queue.put(None)  # one per consumer

async def consumer(queue, cid):
    results = []
    while True:
        item = await queue.get()
        if item is None:
            break
        results.append(f"C{cid}: {item}")
        await asyncio.sleep(0.02)
    return results

async def main():
    queue = asyncio.Queue()
    prod = asyncio.create_task(producer(queue))
    cons = await asyncio.gather(consumer(queue, 1), consumer(queue, 2))
    await prod
    total = len(cons[0]) + len(cons[1])
    return total

if __name__ == "__main__":
    total = asyncio.run(main())
    assert total == 10
    print("All tests passed!")
