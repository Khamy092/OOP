# Practice 4: Abstract Base Classes

# abstract base class:
#  - cannot be instantiated
#  - can be subclassed
#  - can contain abstract methods
#  - abstract methods must be implemented in subclasses
# - abstract methods are defined using the @abstractmethod decorator


from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod # abstract method decorator - used to define abstract methods

    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle01 = Rectangle(10, 20)
print("Area is: ", rectangle01.area())
print("Perimeter is: ", rectangle01.perimeter())