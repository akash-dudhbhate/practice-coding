"""SOLUTION: Async Greet (Easy)"""
import asyncio

async def async_greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"

if __name__ == "__main__":
    result = asyncio.run(async_greet("Akash"))
    assert result == "Hello, Akash!"
    print("All tests passed!")
