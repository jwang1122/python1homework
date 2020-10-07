from turtle import *
from shapes import *

pen1 = Turtle()

#the male
#The top circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, 100, 30)
pen1.end_fill()

#The top of the hat
pen1.color('purple')
pen1.begin_fill()
drawRectangle(pen1, -115, 155, 30, 50)
pen1.end_fill()

#Rest of hat
pen1.color('purple')
pen1.width(5)
drawLine(pen1,-125, 155, 0, 50)
pen1.width(0)

#the left eye
pen1.color('blue')
pen1.begin_fill()
drawCircle(pen1, -110, 130, 3)
pen1.end_fill()

#the right eye
pen1.color('blue')
pen1.begin_fill()
drawCircle(pen1, -90, 130,3)
pen1.end_fill()

#the mouth
#the bottom
pen1.color('red')
pen1.width(3)
drawLine(pen1, -105, 115, 0, 10)
pen1.width(0)

#the left part of mouth
pen1.color('red')
pen1.width(3)
drawLine(pen1, -90, 120, 135, 5)
pen1.width(0)

#the right part of mouth
pen1.color('red')
pen1.width(3)
drawLine(pen1, -110, 120, 45, 5)
pen1.width(0)

#the middle circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, 12, 45)
pen1.end_fill()

#the bottem circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, -117, 65)

#first top button in middle cicle
pen1.color('teal')
pen1.begin_fill()
pen1.width(3)
drawCircle(pen1, -100, 70, 6)
pen1.end_fill()

#second button in middle circle
pen1.color('teal')
pen1.begin_fill()
drawCircle(pen1, -100, 40, 6)
pen1.end_fill()

#first button in bottom cicle
pen1.color('teal')
pen1.begin_fill()
drawCircle(pen1, -100, -40, 6)
pen1.end_fill()

#second button in bottom circle
pen1.color('teal')
pen1.begin_fill()
drawCircle(pen1, -100, -70, 6)
pen1.end_fill()
pen1.width(0)

#left arm
pen1.color('brown')
pen1.width(5)
drawLine(pen1,-135, 60, 120, 70)
pen1.width(0)

#right arm
pen1.color('brown')
pen1.width(5)
drawLine(pen1,-65, 60, 60, 70)
pen1.width(0)

##the female
##The top circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 100, 100, 30)
pen1.end_fill()

##the left eye
pen1.color('blue')
pen1.begin_fill()
drawCircle(pen1, 90, 130,3)
pen1.end_fill()

##the right eye
pen1.color('blue')
pen1.begin_fill()
drawCircle(pen1, 110, 130, 3)
pen1.end_fill()

##the mouth
##the bottom
pen1.color('red')
pen1.width(3)
drawLine(pen1, 95, 115, 0, 10)
pen1.width(0)

##the left part of mouth
pen1.color('red')
pen1.width(3)
drawLine(pen1, 90, 120, 45, 5)
pen1.width(0)

##the right part of mouth
pen1.color('red')
pen1.width(3)
drawLine(pen1, 110, 120, 135, 5)
pen1.width(0)

##the hair
##the left piece of hair
pen1.color('gold')
pen1.width(5)
drawLine(pen1, 65, 110, 292, 60)
pen1.width(0)

##the right piece of hair
pen1.color('gold')
pen1.width(5)
drawLine(pen1, 135, 110, 248, 60)
pen1.width(0)

##the hat
pen1.color('pink')
pen1.begin_fill()
drawTriangle(pen1, 75, 150, 0, 50 )
pen1.end_fill()


##the middle circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 100, 12, 45)
pen1.end_fill()

##the bottem circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 100, -117, 65)

##first top button in middle cicle
pen1.color('pink')
pen1.begin_fill()
pen1.width(3)
drawCircle(pen1, 100, 70, 6)
pen1.end_fill()

##second button in middle circle
pen1.color('teal')
pen1.begin_fill()
drawCircle(pen1, 100, 40, 6)
pen1.end_fill()

##first button in bottom cicle
pen1.color('pink')
pen1.begin_fill()
drawCircle(pen1, 100, -40, 6)
pen1.end_fill()
pen1.width(0)

##second button in bottom circle
pen1.color('teal')
pen1.begin_fill()
drawCircle(pen1, 100, -70, 6)
pen1.end_fill()

##right arm
pen1.color('brown')
pen1.width(5)
drawLine(pen1, 135, 60, 120, 70)
pen1.width(0)

##left arm
pen1.color('brown')
pen1.width(5)
drawLine(pen1, 65, 60, 60, 70)
pen1.width(0)

##the flower
pen1.color('pink','yellow')
pen1.begin_fill()
pen1.width(14)
drawCircle(pen1, 100, 0, 14)
pen1.end_fill()
pen1.width(0)


pen1.hideturtle
mainloop()