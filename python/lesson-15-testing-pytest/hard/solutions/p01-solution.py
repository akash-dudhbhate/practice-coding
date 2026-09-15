"""SOLUTION: BankAccount Test Suite (Hard)"""
import pytest

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

@pytest.fixture
def account():
    return BankAccount("Test", 100)

def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70

def test_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(200)

def test_negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-10)

@pytest.mark.parametrize("amount", [10, 50, 100])
def test_valid_deposits(account, amount):
    account.deposit(amount)
    assert account.balance == 100 + amount

if __name__ == "__main__":
    acc = BankAccount("Test", 100)
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(30)
    assert acc.balance == 120
    try:
        acc.withdraw(200)
    except ValueError:
        pass
    try:
        acc.deposit(-10)
    except ValueError:
        pass
    print("All tests passed!")
