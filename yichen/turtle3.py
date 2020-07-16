"""
response mouse click on turtle to move turtle around
"""
from turtle import *
yichen = Turtle()
yichen.shape("turtle")
yichen.color("blue")
yichen.pensize(5)
yichen.shapesize(3)
yichen.forward(120)
yichen.left(90)
yichen.fd(100)

def tap(x, y):
    yichen.right(45)
    yichen.forward(50)
yichen.onclick(tap)

mainloop()