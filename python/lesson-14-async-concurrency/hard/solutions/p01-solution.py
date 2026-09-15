"""SOLUTION: Async Rate Limiter (Hard)"""
import asyncio
import time

async def limited_task(sem, task_id):
    async with sem:
        print(f"  Task {task_id} started")
        await asyncio.sleep(0.1)
        print(f"  Task {task_id} done")
        return task_id

async def main():
    sem = asyncio.Semaphore(3)
    tasks = [limited_task(sem, i) for i in range(10)]
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    results = asyncio.run(main())
    assert sorted(results) == list(range(10))
    print("All tests passed!")
