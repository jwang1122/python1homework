from turtle import *
from shapes import *

pen1 = Turtle()

pen1.width(3)

pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -180, -200, 90)
pen1.end_fill()
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -180, -20, 60)
pen1.end_fill()
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -180, 100, 40)
pen1.end_fill()
pen1.color('black')
pen1.begin_fill()
drawCircle(pen1, -190, 150, 5)
pen1.end_fill()
pen1.color('black')
pen1.begin_fill()
drawCircle(pen1, -170, 150, 5)
pen1.end_fill()
pen1.color('brown')
pen1.begin_fill()
drawLine(pen1, -120, 35, 50, 100)
pen1.color('brown')
pen1.begin_fill
drawLine(pen1, -240, 35, 125, 100)

pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 180, -200, 90)
pen1.end_fill()
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 180, -20, 60)
pen1.end_fill()
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 180, 100, 40)
pen1.end_fill()
pen1.color('black')
pen1.begin_fill()
drawCircle(pen1, 190, 150, 5)
pen1.end_fill()
pen1.color('black')
pen1.begin_fill()
drawCircle(pen1, 170, 150, 5)
pen1.end_fill()
pen1.color('brown')
pen1.begin_fill()
drawLine(pen1, 240, 40, 50, 100)
pen1.color('brown')
pen1.begin_fill()
drawLine(pen1, 120, 40, 125, 100)

mainloop()