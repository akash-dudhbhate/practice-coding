#!/usr/bin/env python3
"""Generate reference solution files for all Python lessons."""

import os

BASE = "/home/akash-dev/workspace-personal/practice-coding/python"

# All solutions keyed by lesson_folder/difficulty/pXX
SOLUTIONS = {
    "lesson-01-variables-types-functions": {
        "easy/p01": '''"""
SOLUTION: Max of Two Numbers (Easy)
====================================
Return the larger of two integers without using built-in max().
"""
def max_of_two(a: int, b: int) -> int:
    if a >= b:
        return a
    return b

# Test
if __name__ == "__main__":
    assert max_of_two(3, 7) == 7
    assert max_of_two(10, 5) == 10
    assert max_of_two(4, 4) == 4
    print("All tests passed!")
''',
        "easy/p02": '''"""
SOLUTION: Even or Odd (Easy)
=============================
Return True if even, False if odd.
"""
def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    print("All tests passed!")
''',
        "easy/p03": '''"""
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
''',
        "medium/p01": '''"""
SOLUTION: Max of Three (Medium)
================================
Reuse max_of_two to find the max of three numbers.
"""
def max_of_two(a: int, b: int) -> int:
    return a if a >= b else b

def max_of_three(a: int, b: int, c: int) -> int:
    return max_of_two(max_of_two(a, b), c)

if __name__ == "__main__":
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(5, 1, 4) == 5
    assert max_of_three(2, 8, 3) == 8
    print("All tests passed!")
''',
        "medium/p02": '''"""
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
''',
        "medium/p03": '''"""
SOLUTION: Count Vowels (Medium)
================================
Count vowels in a string (case-insensitive).
"""
def count_vowels(text: str) -> int:
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
    print("All tests passed!")
''',
        "hard/p01": '''"""
SOLUTION: FizzBuzz (Hard)
==========================
Classic FizzBuzz — return a list of strings.
"""
def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

if __name__ == "__main__":
    result = fizzbuzz(15)
    assert result[0] == "1"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"
    print("All tests passed!")
''',
        "hard/p02": '''"""
SOLUTION: Reverse String (Hard)
=================================
Reverse a string WITHOUT using slicing or reversed().
"""
def reverse_string(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result

if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    print("All tests passed!")
''',
        "hard/p03": '''"""
SOLUTION: Is Prime (Hard)
==========================
Check if a number is prime.
"""
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(13) == True
    print("All tests passed!")
''',
    },
    "lesson-02-strings-methods": {
        "easy/p01": '''"""
SOLUTION: Count Vowels (Easy)
==============================
Count vowels in a string (case-insensitive).
"""
def count_vowels(text: str) -> int:
    vowels = set("aeiou")
    return sum(1 for c in text.lower() if c in vowels)

if __name__ == "__main__":
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    print("All tests passed!")
''',
        "easy/p02": '''"""
SOLUTION: Reverse String (Easy)
================================
Reverse a string without using slicing.
"""
def reverse_string(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result

if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    print("All tests passed!")
''',
        "easy/p03": '''"""
SOLUTION: Palindrome Check (Easy)
==================================
Check if a string reads the same forwards and backwards.
"""
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A Santa at NASA") == True
    assert is_palindrome("") == True
    print("All tests passed!")
''',
        "medium/p01": '''"""
SOLUTION: Get Initials (Medium)
================================
Given a full name, return initials. "John Doe" -> "JD".
"""
def get_initials(name: str) -> str:
    parts = name.strip().split()
    return "".join(word[0].upper() for word in parts if word)

if __name__ == "__main__":
    assert get_initials("John Doe") == "JD"
    assert get_initials("Akash  Dev") == "AD"
    assert get_initials("single") == "S"
    assert get_initials("") == ""
    print("All tests passed!")
''',
        "medium/p02": '''"""
SOLUTION: Count Words (Medium)
===============================
Count the number of words in a sentence.
"""
def count_words(sentence: str) -> int:
    return len(sentence.strip().split())

if __name__ == "__main__":
    assert count_words("Hello world") == 2
    assert count_words("  one  two  three  ") == 3
    assert count_words("") == 0
    print("All tests passed!")
''',
        "medium/p03": '''"""
SOLUTION: Replace Spaces with Underscores (Medium)
===================================================
Strip leading/trailing whitespace, then replace internal spaces with underscores.
"""
def replace_spaces(text: str) -> str:
    return text.strip().replace(" ", "_")

if __name__ == "__main__":
    assert replace_spaces("  hello world  ") == "hello_world"
    assert replace_spaces("no spaces") == "no_spaces"
    assert replace_spaces("  single  ") == "single"
    print("All tests passed!")
''',
        "hard/p01": '''"""
SOLUTION: Anagram Check (Hard)
================================
Check if two strings are anagrams (same characters, different order).
"""
def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False
    assert is_anagram("Dormitory", "Dirty room") == True
    print("All tests passed!")
''',
        "hard/p02": '''"""
SOLUTION: Run-Length Encoding (Hard)
=====================================
Compress a string using run-length encoding. "aaabbc" -> "a3b2c1".
"""
def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

if __name__ == "__main__":
    assert run_length_encode("aaabbc") == "a3b2c1"
    assert run_length_encode("abc") == "a1b1c1"
    assert run_length_encode("aaaa") == "a4"
    assert run_length_encode("") == ""
    print("All tests passed!")
''',
        "hard/p03": '''"""
SOLUTION: Extract Email Domain (Hard)
======================================
Extract the domain from an email. "user@gmail.com" -> "gmail.com".
"""
def extract_domain(email: str) -> str:
    if "@" not in email:
        return ""
    return email.split("@")[1]

if __name__ == "__main__":
    assert extract_domain("user@gmail.com") == "gmail.com"
    assert extract_domain("test@company.co.uk") == "company.co.uk"
    assert extract_domain("noatsign") == ""
    print("All tests passed!")
''',
    },
    "lesson-03-lists-tuples": {
        "easy/p01": '''"""
SOLUTION: Sum List (Easy)
==========================
Return the sum of all numbers in a list (no built-in sum()).
"""
def sum_list(nums: list) -> int:
    total = 0
    for n in nums:
        total += n
    return total

if __name__ == "__main__":
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([-1, 1]) == 0
    print("All tests passed!")
''',
        "easy/p02": '''"""
SOLUTION: Reverse List (Easy)
==============================
Return a new list with elements in reverse order (don't mutate input).
"""
def reverse_list(items: list) -> list:
    return items[::-1]

if __name__ == "__main__":
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []
    original = [1, 2, 3]
    reverse_list(original)
    assert original == [1, 2, 3]  # not mutated
    print("All tests passed!")
''',
        "easy/p03": '''"""
SOLUTION: Contains (Easy)
==========================
Return True if target is in the list (no 'in' operator — loop manually).
"""
def contains(items: list, target) -> bool:
    for item in items:
        if item == target:
            return True
    return False

if __name__ == "__main__":
    assert contains([1, 2, 3], 2) == True
    assert contains([1, 2, 3], 5) == False
    assert contains([], 1) == False
    print("All tests passed!")
''',
        "medium/p01": '''"""
SOLUTION: Remove Duplicates (Medium)
=====================================
Return a new list with duplicates removed, preserving order.
"""
def remove_duplicates(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    assert remove_duplicates([]) == []
    print("All tests passed!")
''',
        "medium/p02": '''"""
SOLUTION: Sort By Length (Medium)
==================================
Sort strings by length (shortest first) using sorted() with key.
"""
def sort_by_length(words: list) -> list:
    return sorted(words, key=len)

if __name__ == "__main__":
    assert sort_by_length(["apple", "hi", "cat"]) == ["hi", "cat", "apple"]
    assert sort_by_length([]) == []
    assert sort_by_length(["same", "four"]) == ["same", "four"]
    print("All tests passed!")
''',
        "medium/p03": '''"""
SOLUTION: Swap Pairs (Medium)
==============================
Swap every pair of adjacent elements. Last stays if odd.
"""
def swap_pairs(items: list) -> list:
    result = items[:]
    for i in range(0, len(result) - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return result

if __name__ == "__main__":
    assert swap_pairs([1, 2, 3, 4, 5]) == [2, 1, 4, 3, 5]
    assert swap_pairs([1, 2]) == [2, 1]
    assert swap_pairs([1]) == [1]
    assert swap_pairs([]) == []
    print("All tests passed!")
''',
        "hard/p01": '''"""
SOLUTION: Flatten (Hard)
=========================
Flatten a list that may contain sub-lists (one level deep).
"""
def flatten(nested: list) -> list:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([1, [2], 3]) == [1, 2, 3]
    assert flatten([]) == []
    print("All tests passed!")
''',
        "hard/p02": '''"""
SOLUTION: Second Largest (Hard)
================================
Return the second largest unique value. None if fewer than 2 unique values.
"""
def second_largest(nums: list) -> int:
    unique = list(set(nums))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

if __name__ == "__main__":
    assert second_largest([5, 1, 4, 4, 3]) == 4
    assert second_largest([1, 1, 1]) is None
    assert second_largest([3, 1]) == 1
    print("All tests passed!")
''',
        "hard/p03": '''"""
SOLUTION: Tuple Stats (Hard)
=============================
Given a tuple of numbers, return (min, max, average). Handle empty.
"""
def tuple_stats(nums: tuple) -> tuple:
    if not nums:
        return (None, None, 0.0)
    return (min(nums), max(nums), sum(nums) / len(nums))

if __name__ == "__main__":
    assert tuple_stats((1, 2, 3)) == (1, 3, 2.0)
    assert tuple_stats(()) == (None, None, 0.0)
    assert tuple_stats((5,)) == (5, 5, 5.0)
    print("All tests passed!")
''',
    },
    "lesson-04-dicts-sets": {
        "easy/p01": '''"""
SOLUTION: Word Count (Easy)
=============================
Return a dict mapping each word (lowercased) to its count.
"""
def word_count(text: str) -> dict:
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    assert word_count("the cat the dog") == {"the": 2, "cat": 1, "dog": 1}
    assert word_count("") == {}
    print("All tests passed!")
''',
        "easy/p02": '''"""
SOLUTION: Has Key (Easy)
=========================
Return True if key is in dict using .get() (not 'in').
"""
def has_key(d: dict, key) -> bool:
    return d.get(key) is not None or key in d

if __name__ == "__main__":
    assert has_key({"a": 1}, "a") == True
    assert has_key({"a": 1}, "b") == False
    assert has_key({}, "a") == False
    print("All tests passed!")
''',
        "easy/p03": '''"""
SOLUTION: Unique Items (Easy)
==============================
Return list of unique items preserving order, using a set for tracking.
"""
def unique_items(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    assert unique_items([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert unique_items([]) == []
    print("All tests passed!")
''',
        "medium/p01": '''"""
SOLUTION: Merge Dicts (Medium)
================================
Merge two dicts; d2 values override d1. Don't mutate inputs.
"""
def merge_dicts(d1: dict, d2: dict) -> dict:
    return {**d1, **d2}

if __name__ == "__main__":
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
    assert merge_dicts({}, {"a": 1}) == {"a": 1}
    print("All tests passed!")
''',
        "medium/p02": '''"""
SOLUTION: Invert Dict (Medium)
================================
Swap keys and values. Keep last key for duplicate values.
"""
def invert_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}

if __name__ == "__main__":
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({}) == {}
    print("All tests passed!")
''',
        "medium/p03": '''"""
SOLUTION: Common Elements (Medium)
====================================
Return sorted list of elements in BOTH lists using set intersection.
"""
def common_elements(a: list, b: list) -> list:
    return sorted(set(a) & set(b))

if __name__ == "__main__":
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements([1], [2]) == []
    assert common_elements([], []) == []
    print("All tests passed!")
''',
        "hard/p01": '''"""
SOLUTION: Group By Parity (Hard)
=================================
Group numbers by even/odd. Handle empty input.
"""
def group_by_parity(nums: list) -> dict:
    result = {"even": [], "odd": []}
    for n in nums:
        if n % 2 == 0:
            result["even"].append(n)
        else:
            result["odd"].append(n)
    return result

if __name__ == "__main__":
    assert group_by_parity([1, 2, 3, 4]) == {"even": [2, 4], "odd": [1, 3]}
    assert group_by_parity([]) == {"even": [], "odd": []}
    print("All tests passed!")
''',
        "hard/p02": '''"""
SOLUTION: Set Difference (Hard)
=================================
Return dict with only_a and only_b (symmetric difference split).
"""
def set_difference(a: list, b: list) -> dict:
    set_a, set_b = set(a), set(b)
    return {
        "only_a": sorted(set_a - set_b),
        "only_b": sorted(set_b - set_a),
    }

if __name__ == "__main__":
    assert set_difference([1, 2, 3], [2, 3, 4]) == {"only_a": [1], "only_b": [4]}
    print("All tests passed!")
''',
        "hard/p03": '''"""
SOLUTION: Char Frequency (Hard)
=================================
Return char frequencies for non-space chars, sorted by frequency desc.
"""
def char_frequency(s: str) -> list:
    freq = {}
    for c in s:
        if c != " ":
            freq[c] = freq.get(c, 0) + 1
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))

if __name__ == "__main__":
    assert char_frequency("aab bc") == [("a", 2), ("b", 2), ("c", 1)]
    assert char_frequency("") == []
    print("All tests passed!")
''',
    },
    "lesson-05-control-flow-loops": {
        "easy/p01": '''"""
SOLUTION: Classify Number (Easy)
==================================
Return "positive", "negative", or "zero".
"""
def classify_number(n: int) -> str:
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    return "zero"

if __name__ == "__main__":
    assert classify_number(5) == "positive"
    assert classify_number(-3) == "negative"
    assert classify_number(0) == "zero"
    print("All tests passed!")
''',
        "easy/p02": '''"""
SOLUTION: Sum Range (Easy)
===========================
Sum all integers from start to stop inclusive using a for loop.
"""
def sum_range(start: int, stop: int) -> int:
    total = 0
    for i in range(start, stop + 1):
        total += i
    return total

if __name__ == "__main__":
    assert sum_range(1, 5) == 15
    assert sum_range(0, 0) == 0
    assert sum_range(-2, 2) == 0
    print("All tests passed!")
''',
        "easy/p03": '''"""
SOLUTION: Count Down (Easy)
=============================
Return a list counting down from n to 1 using a while loop.
"""
def count_down(n: int) -> list:
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

if __name__ == "__main__":
    assert count_down(3) == [3, 2, 1]
    assert count_down(1) == [1]
    assert count_down(0) == []
    print("All tests passed!")
''',
        "medium/p01": '''"""
SOLUTION: First Even (Medium)
===============================
Return the first even number using break. None if none found.
"""
def first_even(nums: list) -> int:
    for n in nums:
        if n % 2 == 0:
            return n
    return None

if __name__ == "__main__":
    assert first_even([1, 3, 4, 5]) == 4
    assert first_even([1, 3, 5]) is None
    assert first_even([]) is None
    print("All tests passed!")
''',
        "medium/p02": '''"""
SOLUTION: Skip Negatives (Medium)
===================================
Return a new list of only non-negative numbers using continue.
"""
def skip_negatives(nums: list) -> list:
    result = []
    for n in nums:
        if n < 0:
            continue
        result.append(n)
    return result

if __name__ == "__main__":
    assert skip_negatives([1, -2, 3, -4, 5]) == [1, 3, 5]
    assert skip_negatives([-1, -2]) == []
    assert skip_negatives([]) == []
    print("All tests passed!")
''',
        "medium/p03": '''"""
SOLUTION: Multiplication Table (Medium)
=========================================
Return an n x n multiplication table as list of lists.
"""
def multiplication_table(n: int) -> list:
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

if __name__ == "__main__":
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert multiplication_table(1) == [[1]]
    print("All tests passed!")
''',
        "hard/p01": '''"""
SOLUTION: Is Palindrome (Hard)
================================
Check if s reads the same forwards and backwards using two pointers.
"""
def is_palindrome(s: str) -> bool:
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    print("All tests passed!")
''',
        "hard/p02": '''"""
SOLUTION: Find Pair (Hard)
============================
Return indices of first pair that sum to target. None if no pair.
"""
def find_pair(nums: list, target: int) -> tuple:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

if __name__ == "__main__":
    assert find_pair([2, 7, 11, 15], 9) == (0, 1)
    assert find_pair([1, 2, 3], 10) is None
    print("All tests passed!")
''',
        "hard/p03": '''"""
SOLUTION: Multiplication Table Hard (Hard)
============================================
Print a formatted multiplication table up to n x n.
"""
def print_multiplication_table(n: int) -> None:
    col_width = len(str(n * n)) + 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:{col_width}}", end="")
        print()

if __name__ == "__main__":
    print_multiplication_table(5)
    print("Test passed!")
''',
    },
}

def write_solutions():
    count = 0
    for lesson, problems in SOLUTIONS.items():
        lesson_dir = os.path.join(BASE, lesson)
        for problem_key, solution_code in problems.items():
            difficulty, pnum = problem_key.split("/")
            sol_dir = os.path.join(lesson_dir, difficulty, "solutions")
            os.makedirs(sol_dir, exist_ok=True)
            sol_file = os.path.join(sol_dir, f"{pnum}-solution.py")
            with open(sol_file, 'w') as f:
                f.write(solution_code)
            count += 1
            print(f"  {lesson}/{difficulty}/{pnum}-solution.py")
    print(f"\\nGenerated {count} solution files")

if __name__ == "__main__":
    write_solutions()
