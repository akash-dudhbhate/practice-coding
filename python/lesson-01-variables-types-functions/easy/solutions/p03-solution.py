"""
SOLUTION: Celsius to Fahrenheit (Easy)
=======================================
Convert Celsius to Fahrenheit using the formula F = C * 9/5 + 32.
"""
def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32

if __name__ == "__main__":
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert abs(celsius_to_fahrenheit(-40) - (-40.0)) < 0.01
    print("All tests passed!")
