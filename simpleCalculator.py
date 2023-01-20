# Name: simpleCalculator
# Description: A simple calculator that can add, subtract, multiply, and divide
# Author: Taqi Khaliqdad
# Date: 20/01/2023
# Version: 1.0
# Purpose: To create a simple calculator that can add, subtract, multiply, and divide using Python Object Oriented Programming

import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x500")


lable1 = tk.Label(root, text="Hello, I am a simple calculator")
lable1.pack()

# put the above text in the middle of the screen    
lable1.place(relx=0.5, rely=0.5, anchor="center")


button1 = tk.Button(root, text="Click me")
button1.pack()
button1.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
