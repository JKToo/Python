#Name: Justin K Too
#Email: justin.too27@myhunter.cuny.edu
#This program takes userInput and turns left

import turtle
obj = turtle.Turtle()
for i in range(5):
    userInput = input("Enter a number: ")
    obj.left(int(userInput))
    obj.forward(100)
