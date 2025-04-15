# Inheritance: 

from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def stream(self):

        return f"Streaming '{self.title}' of size {self.file_size}MB."
    
    def borrow(self):
        return f"{self.title}' is a digital book and cannot be borrowed, Just stream it"