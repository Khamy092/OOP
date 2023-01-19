# multiple inhertence im OOP
# multiple inhertence is a feature of OOP that allows a class to inherit attributes and methods from more than one parent class


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def drive(self):
        print(self.name, "is driving")

class Rider:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ride(self):
        print(self.name, "is riding")

class Uber(Driver, Rider):
    def __init__(self, name, age):
        Driver.__init__(self, name, age)
        Rider.__init__(self, name, age)

    def pay(self):
        print(self.name, "is paying")


