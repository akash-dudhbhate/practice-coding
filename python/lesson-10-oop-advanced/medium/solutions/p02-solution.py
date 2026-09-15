"""SOLUTION: BankAccount with Private Balance (Medium)"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount("Akash", 100)
    assert acc.balance == 100
    acc.deposit(50)
    assert acc.balance == 150
    try:
        acc.withdraw(200)
    except ValueError:
        pass
    print("All tests passed!")
