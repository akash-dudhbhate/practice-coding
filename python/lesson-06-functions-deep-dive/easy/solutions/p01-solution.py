"""SOLUTION: Greet with Default (Easy)"""
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    assert greet("Akash") == "Hello, Akash!"
    assert greet("Dev", "Hi") == "Hi, Dev!"
    print("All tests passed!")
