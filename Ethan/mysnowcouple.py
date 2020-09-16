from turtle import *
from shapes import *

pen1 = Turtle()

#hat
pen1.color('dark red','dark red')
pen1.begin_fill()
drawRectangle(pen1, -250, 100, 50, 60)
pen1.end_fill()
pen1.color('dark red')
pen1.width(5)
drawLine(pen1, -260, 100, 0, 70)

#head
pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -225, 20, 40)
pen1.end_fill()

#eye
pen1.color('black','blue')
pen1.begin_fill()
drawCircle(pen1, -240, 70, 5)
pen1.end_fill()

#eye
pen1.color('black','blue')
pen1.begin_fill()
drawCircle(pen1, -210, 70, 5)
pen1.end_fill()
 
#mouth
pen1.color('red')
pen1.width(3)
drawLine(pen1, -250, 50, 45, 10)
pen1.width(1)

pen1.color('red')
pen1.width(3)
drawLine(pen1, -245, 43, 0, 40)
pen1.width(1)

pen1.color('red')
pen1.width(3)
drawLine(pen1, -199, 50, 135, 10)
pen1.width(1)

#body
pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -225, -100, 60)
pen1.end_fill()

#bottom
pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, -225, -260, 80)
pen1.end_fill()

#buttons
pen1.color('black','gray')
pen1.begin_fill()
drawCircle(pen1, -225, -10, 9)
pen1.end_fill()

pen1.color('black','gray')
pen1.begin_fill()
drawCircle(pen1, -225, -70, 9)
pen1.end_fill()

pen1.color('black','gray')
pen1.begin_fill()
drawCircle(pen1, -225, -140, 9)
pen1.end_fill()

pen1.color('black','gray')
pen1.begin_fill()
drawCircle(pen1, -225, -220, 9)
pen1.end_fill()

#arms
pen1.color('dark red')
pen1.width(5)
drawLine(pen1, -285, -20, 190, 120)
pen1.width(1)

pen1.color('dark red')
pen1.width(5)
drawLine(pen1, -165, -20, 340, 120)
pen1.width(1)


#SNOWMAN 2

#head
pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 225, 20, 40)
pen1.end_fill()

#eye
pen1.color('black','light green')
pen1.begin_fill()
drawCircle(pen1, 240, 70, 5)
pen1.end_fill()

#eye
pen1.color('black','light green')
pen1.begin_fill()
drawCircle(pen1, 210, 70, 5)
pen1.end_fill()

#mouth
pen1.color('red')
pen1.width(3)
drawLine(pen1, 210, 55, 45, 10)
pen1.width(1)


pen1.color('red')
pen1.width(3)
drawLine(pen1, 240, 55, 135, 10)
pen1.width(1)

pen1.color('red','red')
pen1.begin_fill()
drawCircle(pen1, 225, 40, 8)
pen1.end_fill()

#body
pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 225, -100, 60)
pen1.end_fill()

#bottom
pen1.width(1)
pen1.color('black','white')
pen1.begin_fill()
drawCircle(pen1, 225, -260, 80)
pen1.end_fill()

#buttons
pen1.color('black','yellow')
pen1.begin_fill()
drawCircle(pen1, 225, -10, 9)
pen1.end_fill()

pen1.color('black','purple')
pen1.begin_fill()
drawCircle(pen1, 225, -70, 9)
pen1.end_fill()

pen1.color('black','yellow')
pen1.begin_fill()
drawCircle(pen1, 225, -140, 9)
pen1.end_fill()

pen1.color('black','purple')
pen1.begin_fill()
drawCircle(pen1, 225, -220, 9)
pen1.end_fill()

#arms
pen1.color('dark red')
pen1.width(5)
drawLine(pen1, 165, -20, 190, 120)
pen1.width(1)

pen1.color('dark red')
pen1.width(5)
drawLine(pen1, 285, -20, 45, 55)
pen1.width(1)

pen1.color('dark red')
pen1.width(5)
drawLine(pen1, 320, -60, 130, 60)
pen1.width(1)
 
#hair
pen1.color('dark red')
pen1.width(3)
drawLine(pen1, 245, 95, 65, 40)
pen1.width(1)

pen1.color('dark red')
pen1.width(3)
drawLine(pen1, 255, 95, 65, 50)
pen1.width(1)

pen1.color('dark red')
pen1.width(3)
drawLine(pen1, 198, 95, 120, 50)
pen1.width(1)

pen1.color('dark red')
pen1.width(3)
drawLine(pen1, 208, 95, 120, 40)
pen1.width(1)

#hat
pen1.color('black','yellow')
pen1.begin_fill()
drawTriangle(pen1, 180, 90, 0, 90)
pen1.end_fill()








mainloop()