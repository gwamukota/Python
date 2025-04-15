from book import Book
from library import Library

lib = Library("Test Library")
lib.add_book(Book("Atomic Habits", "James Clear", 2018))
lib.add_book(Book("Deep Work", "Cal Newport", 2016))

print("Library Catalogue:")
for book in lib.list_books():
    print(book)

# found = lib.find_book("Deep Work")
# print(found.borrow() if found else "Book not found.")