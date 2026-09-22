"""
Auto-Check System — Lesson 10 (OOP Advanced)
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
    if not hasattr(module, 'Vehicle'):
        return False, "Class 'Vehicle' not found"
    if not hasattr(module, 'Car'):
        return False, "Class 'Car' not found"
    c = module.Car("Toyota", "Camry", 2020, 4)
    if "2020 Toyota Camry" not in c.display():
        return False, "Car.display() should contain '2020 Toyota Camry'"
    if "4 doors" not in c.display():
        return False, "Car.display() should contain '4 doors'"
    v = module.Vehicle("Honda", "Civic", 2019)
    if "2019 Honda Civic" not in v.display():
        return False, "Vehicle.display() should contain '2019 Honda Civic'"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'Rectangle'):
        return False, "Class 'Rectangle' not found"
    r = module.Rectangle(4, 5)
    if r.area != 20:
        return False, "Rectangle(4,5).area should be 20 (property, no parens)"
    if r.perimeter != 18:
        return False, "Rectangle(4,5).perimeter should be 18 (property, no parens)"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'Student'):
        return False, "Class 'Student' not found"
    s = module.Student("Akash", "A")
    if str(s) != "Student: Akash (A)":
        return False, "str(Student('Akash','A')) should be 'Student: Akash (A)'"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'Vector'):
        return False, "Class 'Vector' not found"
    v1 = module.Vector(1, 2)
    v2 = module.Vector(3, 4)
    if (v1 + v2) != module.Vector(4, 6):
        return False, "Vector(1,2) + Vector(3,4) should equal Vector(4,6)"
    if (v2 - v1) != module.Vector(2, 2):
        return False, "Vector(3,4) - Vector(1,2) should equal Vector(2,2)"
    if str(v1) != "Vector(1, 2)":
        return False, "str(Vector(1,2)) should be 'Vector(1, 2)'"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'BankAccount'):
        return False, "Class 'BankAccount' not found"
    acc = module.BankAccount("Akash", 100)
    if acc.balance != 100:
        return False, "balance property should return 100"
    acc.deposit(50)
    if acc.balance != 150:
        return False, "after deposit(50), balance should be 150"
    try:
        acc.withdraw(200)
        return False, "withdraw(200) with balance 150 should raise ValueError"
    except ValueError:
        pass
    try:
        acc.deposit(-5)
        return False, "deposit(-5) should raise ValueError"
    except ValueError:
        pass
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'Shape'):
        return False, "Abstract class 'Shape' not found"
    if not hasattr(module, 'Circle') or not hasattr(module, 'Square'):
        return False, "Classes 'Circle' and 'Square' not found"
    c = module.Circle(5)
    if abs(c.area() - 78.5398) > 0.01:
        return False, "Circle(5).area() should be ~78.54"
    s = module.Square(4)
    if s.area() != 16 or s.perimeter() != 16:
        return False, "Square(4).area() should be 16 and perimeter() 16"
    try:
        module.Shape()
        return False, "Shape() should not be instantiable (abstract)"
    except TypeError:
        pass
    return True, "All tests passed!"


def check_hard_p01(module):
    for cls in ('Employee', 'Manager', 'Developer'):
        if not hasattr(module, cls):
            return False, f"Class '{cls}' not found"
    e = module.Employee("Eve", 50000)
    if e.calculate_salary() != 50000:
        return False, "Employee.calculate_salary() should return base salary"
    m = module.Manager("Alice", 80000, ["Bob", "Carol"])
    if m.calculate_salary() != 80200:
        return False, "Manager with 2-person team should be 80200"
    d = module.Developer("Dave", 70000, ["Python", "JS"])
    if d.calculate_salary() != 70100:
        return False, "Developer with 2 languages should be 70100"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'Stack'):
        return False, "Class 'Stack' not found"
    s = module.Stack()
    if not s.is_empty():
        return False, "new Stack should be empty"
    s.push(1)
    s.push(2)
    if s.size() != 2:
        return False, "size() after 2 pushes should be 2"
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


def check_hard_p03(module):
    if not hasattr(module, 'Book'):
        return False, "Class 'Book' not found"
    b = module.Book("1984", "Orwell", "1234567890")
    if b.is_available is not True:
        return False, "new Book().is_available should be True"
    b.borrow()
    if b.is_available is not False:
        return False, "after borrow(), is_available should be False"
    b.return_book()
    if b.is_available is not True:
        return False, "after return_book(), is_available should be True"
    b2 = module.Book.from_string("Dune|Herbert|9876543210")
    if b2.title != "Dune" or b2.author != "Herbert" or b2.isbn != "9876543210":
        return False, "from_string should parse 'Title|Author|ISBN'"
    if module.Book.is_valid_isbn("1234567890") is not True:
        return False, "is_valid_isbn('1234567890') should be True"
    if module.Book.is_valid_isbn("123") is not False:
        return False, "is_valid_isbn('123') should be False"
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
        print("  LESSON 10 — AUTO-CHECK ALL")
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
                if "NoneType" in str(e):
                    print(f"  {check_id}: FAIL — a function returned None — write the body!")
                else:
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
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
