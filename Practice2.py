# Python OOP Practice 2


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email




b11 = Book("The Hobbit", "J.R.R. Tolkien", 19.99)
a32 = Author("J.R.R. Tolkien", "info@jpmorgan.com")


print(type(b11) == type(a32)) # we can compare the type of two objects and see if they are the same.
print(type(b11) == Book) # comparing the type of an object to a specific class.

print(type(b11)) # type function returns the type of the object.
print(type(a32))
