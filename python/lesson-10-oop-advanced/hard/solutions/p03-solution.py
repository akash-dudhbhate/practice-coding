"""SOLUTION: Book with property, classmethod, staticmethod (Hard)"""
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._borrowed = False

    @property
    def is_available(self):
        return not self._borrowed

    def borrow(self):
        if self._borrowed:
            raise ValueError("Already borrowed")
        self._borrowed = True

    def return_book(self):
        self._borrowed = False

    @classmethod
    def from_string(cls, s):
        title, author, isbn = s.split("|")
        return cls(title, author, isbn)

    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 10 or len(isbn) == 13

if __name__ == "__main__":
    b = Book("1984", "Orwell", "1234567890")
    assert b.is_available == True
    b.borrow()
    assert b.is_available == False
    b2 = Book.from_string("Dune|Herbert|9876543210")
    assert b2.title == "Dune"
    assert Book.is_valid_isbn("1234567890") == True
    assert Book.is_valid_isbn("123") == False
    print("All tests passed!")
