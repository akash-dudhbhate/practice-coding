"""SOLUTION: BankAccount Class (Medium)"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.balance}"

if __name__ == "__main__":
    acc = BankAccount("Akash", 100)
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(30)
    assert acc.balance == 120
    try:
        acc.withdraw(200)
        assert False
    except ValueError:
        pass
    print("All tests passed!")
