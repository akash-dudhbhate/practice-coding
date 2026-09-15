"""SOLUTION: Library Composition (Hard)"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Library: {len(self)} books"

if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("1984", "Orwell"))
    lib.add_book(Book("Animal Farm", "Orwell"))
    lib.add_book(Book("Dune", "Herbert"))
    assert len(lib) == 3
    orwell = lib.find_by_author("Orwell")
    assert len(orwell) == 2
    print("All tests passed!")
