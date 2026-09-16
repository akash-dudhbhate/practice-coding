"""
Auto-Check System — Lesson 09 (OOP Basics)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _find_file(level_dir, level, num):
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def check_easy_p01(module):
    if not hasattr(module, 'Rectangle'):
        return False, "Class 'Rectangle' not found"
    r = module.Rectangle(4, 5)
    if r.area() != 20:
        return False, "Rectangle(4,5).area() should be 20"
    if r.perimeter() != 18:
        return False, "Rectangle(4,5).perimeter() should be 18"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'Counter'):
        return False, "Class 'Counter' not found"
    c = module.Counter()
    c.increment()
    c.increment()
    if c.get() != 2:
        return False, "Counter after 2 increments should get() == 2"
    c2 = module.Counter()
    if c2.get() != 0:
        return False, "New Counter should start at 0"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'Book'):
        return False, "Class 'Book' not found"
    b = module.Book("1984", "Orwell")
    if str(b) != "1984 by Orwell":
        return False, "str(Book('1984','Orwell')) should be '1984 by Orwell'"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'BankAccount'):
        return False, "Class 'BankAccount' not found"
    acc = module.BankAccount("Akash", 100)
    acc.deposit(50)
    if acc.balance != 150:
        return False, "after deposit(50) balance should be 150"
    acc.withdraw(30)
    if acc.balance != 120:
        return False, "after withdraw(30) balance should be 120"
    try:
        acc.withdraw(200)
        return False, "withdraw(200) with balance 120 should raise ValueError"
    except ValueError:
        pass
    if str(acc) != "Akash: $120":
        return False, "str(acc) should be 'Akash: $120'"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'Stack'):
        return False, "Class 'Stack' not found"
    s = module.Stack()
    if not s.is_empty():
        return False, "new Stack should be empty"
    s.push(1)
    s.push(2)
    if len(s) != 2:
        return False, "len(stack) after 2 pushes should be 2"
    if s.pop() != 2:
        return False, "pop() should return 2"
    if s.peek() != 1:
        return False, "peek() should return 1"
    s2 = module.Stack()
    try:
        s2.pop()
        return False, "pop() on empty stack should raise IndexError"
    except IndexError:
        pass
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'Temperature'):
        return False, "Class 'Temperature' not found"
    t = module.Temperature(100)
    if t.fahrenheit() != 212.0:
        return False, "Temperature(100).fahrenheit() should be 212.0"
    t2 = module.Temperature.from_fahrenheit(32)
    if abs(t2.celsius - 0) > 0.01:
        return False, "from_fahrenheit(32).celsius should be ~0"
    if module.Temperature.to_fahrenheit(0) != 32.0:
        return False, "to_fahrenheit(0) should be 32.0"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'ShoppingCart'):
        return False, "Class 'ShoppingCart' not found"
    cart = module.ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.add_item("bread", 3.0)
    if cart.total() != 4.5:
        return False, "total() should be 4.5"
    cart.remove_item("apple")
    if cart.total() != 3.0:
        return False, "total() after removing apple should be 3.0"
    if "3.0" not in str(cart) and "3" not in str(cart):
        return False, "__str__ should include the total"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'Student'):
        return False, "Class 'Student' not found"
    module.Student.count = 0  # reset shared counter for the test
    s1 = module.Student("Akash", [90, 80])
    s2 = module.Student("Dev")
    if module.Student.get_count() != 2:
        return False, "get_count() after creating 2 students should be 2"
    s2.add_grade(70)
    if s2.average() != 70:
        return False, "s2.average() should be 70"
    if s1.average() != 85.0:
        return False, "s1.average() should be 85.0"
    s3 = module.Student("NoGrades")
    if s3.average() != 0:
        return False, "average() with no grades should be 0"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'Library'):
        return False, "Class 'Library' not found"
    if not hasattr(module, 'Book'):
        return False, "Class 'Book' not found"
    lib = module.Library()
    lib.add_book(module.Book("1984", "Orwell"))
    lib.add_book(module.Book("Animal Farm", "Orwell"))
    lib.add_book(module.Book("Dune", "Herbert"))
    if len(lib) != 3:
        return False, "len(lib) should be 3"
    orwell = lib.find_by_author("Orwell")
    if len(orwell) != 2:
        return False, "find_by_author('Orwell') should return 2 books"
    if str(lib) == "":
        return False, "__str__ should return a summary string"
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,
    "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01,
    "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,
    "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        print("=" * 60)
        print("  LESSON 09 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            try:
                module = load_module(filepath)
                passed, msg = check_func(module)
                status = "PASS" if passed else "FAIL"
                print(f"  {check_id}: {status} — {msg}")
            except Exception as e:
                print(f"  {check_id}: ERROR — {e}")
        print("=" * 60)
        return

    level, num = target.split("/")
    check_id = f"{level}/{num}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        sys.exit(1)

    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        print(f"ERROR — {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
