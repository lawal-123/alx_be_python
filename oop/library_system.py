class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        reurn f"{self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title, autor, file_size):
        self.file_size = file_size
    def __str__(self):
        return f"{super().__str__()} (EBook, Size: {self.file_size} MB)"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"{super().__str__()} (PrintBook, Pages: {self.page_count})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        for book in self.books:
            print(book)
main.py
python
Copy code
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create library instance
    library = Library()

    # Create some book instances
    book1 = PrintBook("1984", "George Orwell", 328)
    book2 = EBook("The Great Gatsby", "F. Scott Fitzgerald", 2)
    book3 = PrintBook("To Kill a Mockingbird", "Harper Lee", 281)

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List all books in the library
    print("Books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()
