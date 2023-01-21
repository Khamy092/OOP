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
