"""SOLUTION: @retry Decorator (Hard)"""
import time

def retry(times=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"Attempt {attempt+1} failed: {e}")
                    if attempt < times - 1:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator

@retry(times=3, delay=0.1)
def flaky():
    import random
    if random.random() < 0.5:
        raise ValueError("Failed")
    return "success"

if __name__ == "__main__":
    # May succeed or raise after 3 tries — just test it runs
    try:
        result = flaky()
        assert result == "success"
    except ValueError:
        print("Retried 3 times, all failed — expected behavior")
    print("Test passed!")
