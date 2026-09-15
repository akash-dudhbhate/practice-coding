"""SOLUTION: CLI Temperature Converter (Medium)"""
import sys

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python p02-solve.py <temp> <C|F>")
        sys.exit(1)
    temp = float(sys.argv[1])
    unit = sys.argv[2].upper()
    if unit == "C":
        print(f"{celsius_to_fahrenheit(temp):.1f} F")
    elif unit == "F":
        print(f"{fahrenheit_to_celsius(temp):.1f} C")
    else:
        print("Unit must be C or F")
