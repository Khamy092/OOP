# challenge 1:
# Create a class for a bank account, with methods for depositing and withdrawing money,
# as well as checking the balance.


class bankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited", amount, "into your account")
    
    def withdraw(self, amount):
        self.balance -= amount
        print("You have withdrawn", amount, "from your account")

    def checkBalance(self):
        print("Your account balance is", self.balance)


john0100 = bankAccount("John", 1000)
john0100.deposit(100)
john0100.withdraw(50)
john0100.checkBalance()


# challenge 2:
# Create a class for a car, with methods for accelerating and braking, and a property for the current speed.


class car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print("You have accelerated", amount, "mph")

    def brake(self, amount):
        self.speed -= amount
        print("You have braked", amount, "mph")

    def currentSpeed(self):
        print("Your current speed is", self.speed, "mph")


john0101 = car("John", 0)
john0101.accelerate(50)
john0101.brake(25)
john0101.currentSpeed()


# challenge 3:
# Create a class for a library, with methods for checking out and returning books, and a property for the current inventory of books.

class library:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def checkOut(self, book):
        self.books.remove(book)
        print("You have checked out", book)

    def returnBook(self, book):
        self.books.append(book)
        print("You have returned", book)

    def currentInventory(self):
        print("The current inventory of books is", self.books)


john0102 = library("John", ["book1", "book2", "book3"])
john0102.checkOut("book1")
john0102.returnBook("book1")
john0102.currentInventory()
