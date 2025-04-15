# Inheritance

from book import Book

class Magazine(Book):
    def __init__(self, title, editor, year):
        super().__init__(title, editor, year)
    
    def borrow(self):
        return f"'{self.title}' is a magazine and cannot be borrowed, Just read it"

    