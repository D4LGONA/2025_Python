from turtle import *
from random import *

def rightClick(x, y):
    shapesize(randrange(1, 10))
    c = (random(), random(), random())
    pencolor(c)
    color(c)
    goto(x, y)
    right(randrange(0, 359))
    stamp()

title('거북이로 그림 그리기')
shape('turtle')
onscreenclick(rightClick, 3)
done()