# Practice 6
# Understanding simple OOP Concepts

# Challenge 1: Create a class called "Dog" that has attributes for the dog's name, breed, and age.
# Write a method to calculate the dog's age in dog years (1 human year = 7 dog years).

class Dog():
    def __init__(self, name, breed, age):

        self.name = name
        self.breed = breed
        self.age = int(age) # limiting the age to be integer only.

    def calculate_age(self):

        return self.age * 7



Dog001 = Dog("Charlie", "Spanish", 2)

print("Dog: " + str(Dog001.name))
print("Breed: " + str(Dog001.breed))
print("Age in dog years: " + str(Dog001.calculate_age()))

# end