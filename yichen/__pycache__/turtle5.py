"""
limit the turtle within the limit bounds
"""


from turtle import *
from random import *


def newX():
    return randint(-300,300)


def newY():
    return randint(-300, 300)


yichen = Turtle()
yichen.shape("turtle")
yichen.color("turquoise")
yichen.pensize(5)
yichen.shapesize(2)
yichen.forward(120)
yichen.right(45)
yichen.fd(50)


def tap(x, y):
    pos = yichen.position()
    x = pos[0] + newX()
    y = pos[1] + newY()
    if x > 300 or x < -300: x = pos[0]
    if y > 300 or y < -300: y = pos[1]
    yichen.goto(x, y)


yichen.onclick(tap)
mainloop()