# Encapsulation: Holding data and methods together

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True 
    
    def borrow(self):
        if self.available:
            self.available = False
            return f"You have borrowed'{self.title}'."
        return f"'{self.title}' is already borrowed."
    
    def return_book(self):
        self.available = True
        return f"You have returned '{self.title}'."
    
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Available: {self.available}"