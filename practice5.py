# multiple inhertence im OOP
# multiple inhertence is a feature of OOP that allows a class to inherit attributes and methods from more than one parent class


class Driver:
    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car

    def drive(self):
        print(self.name, "is driving")

    def vehicle(self):
        print(self.name, "is driving a", self.car)

class Rider:
    def __init__(self, name, age, motorcycle):
        self.name = name
        self.age = age
        self.motorcycle = motorcycle

    def ride(self):
        print(self.name, "is riding")

    def vehicle(self):
        print(self.name, "is riding a", self.motorcycle)

class Uber(Driver, Rider):
    def __init__(self, name, age, car, motorcycle):
        Driver.__init__(self, name, age, car)
        Rider.__init__(self, name, age, motorcycle)
        Driver.car = car
        Rider.motorcycle = motorcycle

    def pay(self):
        print(self.name, "is paying")


john0101 = Uber("John", 25, "Toyota", "Honda")
john0101.drive()
john0101.ride()
john0101.pay()
john0101.vehicle()
john0101.motorcycle()






