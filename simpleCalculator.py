# Name: simpleCalculator
# Description: A simple calculator that can add, subtract, multiply, and divide
# Author: Taqi Khaliqdad
# Date: 20/01/2023
# Version: 1.0
# Purpose: To create a simple calculator that can add, subtract, multiply, and divide using Python Object Oriented Programming


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2
    
    def power(self):
        return self.num1 ** self.num2 



def ask_User():
    print("Welcome to the simple calculator!")
    print("Please enter the first number: ")
    num1 = int(input())
    print("Please enter the second number: ")
    num2 = int(input())
    print("Please enter the operation you would like to perform: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    operation = int(input())
    return num1, num2, operation



ask_User()
num1, num2, operation = ask_User()
calc = Calculator(num1, num2)
if operation == 1:
    print(calc.add(num1, num2))
elif operation == 2:
    print(calc.subtract(num1, num2))
elif operation == 3:
    print(calc.multiply(num1, num2))
elif operation == 4:
    print(calc.divide(num1, num2))
elif operation == 5:
    print(calc.power(num1, num2))
else:
    print("Invalid operation")


