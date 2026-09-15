"""SOLUTION: Package Structure (Medium)"""
# Simulated package structure in a single file for reference
# In practice: myapp/__init__.py, myapp/utils.py, myapp/models/user.py

# myapp/utils.py
from datetime import datetime

def format_date(dt=None, fmt="%Y-%m-%d"):
    dt = dt or datetime.now()
    return dt.strftime(fmt)

# myapp/models/user.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User({self.name}, {self.email})"

# Test
if __name__ == "__main__":
    assert format_date(datetime(2024, 1, 15)) == "2024-01-15"
    u = User("Akash", "akash@test.com")
    assert u.name == "Akash"
    print("All tests passed!")
