from book import Book
from library import Library

lib = Library("Test Library")
lib.add_book(Book("1984", "George Orwell", 1949))
lib.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))

print("Library Catalogue:")
for book in lib.list_books():
    print(book)

# found = lib.find_book("To Kill a Mockingbird")
# print(found.borrow() if found else "Book not found.")