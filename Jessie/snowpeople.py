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
pen1.color('purple','purple')
pen1.begin_fill()
drawRectangle(pen1, -115, 155, 30, 50)
pen1.end_fill()

#Rest of hat
pen1.color('purple','purple')
pen1.width(5)
drawLine(pen1,-125, 155, 0, 50)
pen1.width(0)

#the left eye
pen1.color('blue','blue')
pen1.begin_fill()
drawCircle(pen1, -110, 130, 3)
pen1.end_fill()

#the right eye
pen1.color('blue','blue')
pen1.begin_fill()
drawCircle(pen1, -90, 130,3)
pen1.end_fill()

#the mouth
pen1.color('red','red')
pen1.begin_fill()
pen1.width(3)
drawLine(pen1, -110, 120, 0, 20)
pen1.width(0)

#the middle circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, 12, 45)
pen1.end_fill()

# the bottem circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -100, -117, 65)

#first top button in middle cicle
pen1.color('teal','teal')
pen1.begin_fill()
drawCircle(pen1, -100, 70, 6)
pen1.end_fill()

#second button in middle circle
pen1.color('teal','teal')
pen1.begin_fill()
drawCircle(pen1, -100, 40, 6)
pen1.end_fill()

#first button in bottom cicle
pen1.color('teal','teal')
pen1.begin_fill()
drawCircle(pen1, -100, -40, 6)
pen1.end_fill()

#second button in bottom circle
pen1.color('teal','teal')
pen1.begin_fill()
drawCircle(pen1, -100, -70, 6)
pen1.end_fill()

#left arm
pen1.color('brown','brown')
pen1.width(5)
drawLine(pen1,-125, 60, 185, 60)
pen1.width(0)

#the other male
#The top circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 100, 100, 30)
pen1.end_fill()

#the left eye
pen1.color('blue','blue')
pen1.begin_fill()
drawCircle(pen1, 90, 130,3)
pen1.end_fill()

#the right eye
pen1.color('blue','blue')
pen1.begin_fill()
drawCircle(pen1, 110, 130, 3)
pen1.end_fill()

#the mouth
pen1.color('red','red')
pen1.begin_fill()
drawLine(pen1, 90, 120, 0, 20)
pen1.end_fill()

#the hat
pen1.color('pink','pink')
pen1.begin_fill()
drawTriangle(pen1, 70, 150, 0, 60 )
pen1.end_fill()


#the middle circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 100, 12, 45)
pen1.end_fill()

# the bottem circle
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 100, -117, 65)

#first top button in middle cicle
pen1.color('pink','pink')
pen1.begin_fill()
drawCircle(pen1, 100, 70, 6)
pen1.end_fill()

#second button in middle circle
pen1.color('teal','teal')
pen1.begin_fill()
drawCircle(pen1, 100, 40, 6)
pen1.end_fill()

#first button in bottom cicle
pen1.color('pink','pink')
pen1.begin_fill()
drawCircle(pen1, 100, -40, 6)
pen1.end_fill()

#second button in bottom circle
pen1.color('teal','teal')
pen1.begin_fill()
drawCircle(pen1, 100, -70, 6)
pen1.end_fill()



mainloop()