"""
randomly
"""
from turtle import *
from random import *

def distance():
    return randint(-200,200)
    
def angle():
    return randint(-360,360)

yichen = Turtle()
yichen.shape("turtle")
yichen.color("turquoise")
yichen.pensize(5)
yichen.shapesize(2)
yichen.forward(120)
yichen.left(90)
yichen.fd(100)

def tap(x, y):
    yichen.right(angle())
    yichen.forward(distance())

yichen.onclick(tap)


mainloop()