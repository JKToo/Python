#Name: Justin K Too
#Email: justin.too27@myhunter.cuny.edu#
#This program takes user input and displays a turtle in that color

import turtle
turtle.colormode(255)
obj = turtle.Turtle()
obj.shape("turtle")

for i in range(0, 255, 10):
    obj.forward(10)
    obj.pensize(i)
    obj.color(0,0,i)
