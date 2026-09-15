"""SOLUTION: Book Class (Easy)"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

if __name__ == "__main__":
    b = Book("1984", "Orwell")
    assert str(b) == "1984 by Orwell"
    print("All tests passed!")
