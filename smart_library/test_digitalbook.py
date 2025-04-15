from digitalbook import DigitalBook

ebook = DigitalBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 2.5)

print(ebook.get_details())
print(ebook.stream())
print(ebook.borrow())
