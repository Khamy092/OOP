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




# b11 = Book("The Hobbit", "J.R.R. Tolkien", 19.99)
# a32 = Author("J.R.R. Tolkien", "info@jpmorgan.com")


# print(type(b11) == type(a32)) # we can compare the type of two objects and see if they are the same.
# print(type(b11) == Book) # comparing the type of an object to a specific class.

# print(type(b11)) # type function returns the type of the object.
# print(type(a32))


class Car:
    def __init__(self, make, year, price):
        self.make = make
        self.year = year
        self.price = price

    carMakes = ["Toyota", "Honda", "Audi", "BMW", "Ford"]

    def get_make(self):
        if self.make in Car.carMakes:
            return self.make
        else:
            raise ValueError("We don't buy this make of car.")

    def get_year(self):
        if self.year >= 2010:
            return self.year
        else:
            raise ValueError("We don't buy cars older than 2010.")

    
    def get_price(self):
        return self.price

   
def get_buyDecision():
        
    global buyDecision
    buyDecision = None

    if Car.get_make != "BMW" or Car.get_make == "Audi":
        if Car.get_price > 10000:
            buyDecision = False
            return Car.get_price
        else:
            return Car.get_price
            buyDecision = True

c121 = Car("Honda", 2012, 11900)

print("Make:" ,c121.get_make())
print("Year:" ,c121.get_year())
print("Price:" , "$",c121.get_price())
print()
print("Buy: " , get_buyDecision())
print()
input("Press Enter to exit...")