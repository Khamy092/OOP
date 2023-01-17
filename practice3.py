

# inheritance is a way to create a new class for using details of an existing class without modifying it.
#  The newly formed class is a derived class (or child class). Similarly, the existing class is a base class 
# (or parent class). It is a way to reuse the code functionality and provides fast implementation time.


class Vehicles:
    def __init__(self, name, model, color, price):
        self.name = name
        self.model = model
        self.color = color
        self.price = price


class Car(Vehicles):
    def __init__(self, name, model, color, price):
        super().__init__(name, model, color, price)
        
        # super() function is used to give access to methods and properties of
        #  a parent or sibling class.
        

class Motorbike(Vehicles): # Motorbike is a child class of Vehicles
    def __init__(self, name, model, color, price):
       super().__init__(name, model, color, price)

class Truck(Vehicles): # Truck is a child class of Vehicles
    def __init__(self, name, model, color, price):
        super().__init__(name, model, color, price)


car1 = Car("BMW", "2019", "Black", 100000)
motor1 = Motorbike("Honda", "2018", "Red", 50000)
truck1 = Truck("TATA", "2017", "White", 200000)

print(car1.name, car1.model, car1.color, car1.price)
print(motor1.name, motor1.model, motor1.color, motor1.price)
print(truck1.name, truck1.model, truck1.color, truck1.price)

