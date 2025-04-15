from digitalbook import DigitalBook

ebook = DigitalBook("Python for All", "Guido van Rossum", 2020, 75)

print(ebook.get_details())
print(ebook.stream())
print(ebook.borrow())
