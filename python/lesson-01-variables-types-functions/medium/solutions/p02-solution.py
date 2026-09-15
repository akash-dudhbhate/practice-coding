"""
SOLUTION: Leap Year (Medium)
=============================
Determine if a year is a leap year.
Rules: divisible by 4, but not by 100 unless also by 400.
"""
def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == "__main__":
    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2024) == True
    assert is_leap_year(2023) == False
    print("All tests passed!")
