from snowman import *
from turtle import *


p = Turtle()
snowman1 = Snowman(150, -200, 30, 50, 100, True)
snowman1.draw(p)
snowlady1 = Snowman(-150, -200, 30, 50, 100, False)
snowlady1.draw(p)
snowboy1 = Snowman(0, -200, 20, 30, 50, True)
snowboy1.draw(p)
exitonclick()