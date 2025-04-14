from turtle import *
from random import *

swidth, sheight = 300, 300
title('거북이가 랜덤한 별 그리기')
setup(width = swidth + 50, height = sheight + 50)
screensize(swidth, sheight)
t = Turtle('turtle')
t.pensize(3)

while True:
    r = random(); g = random(); b = random()
    t.pencolor((r, g, b))
    t.penup()
    x = randrange(-swidth // 2, swidth //2)
    y = randrange(-sheight//2, sheight//2)
    t.goto(x, y)
    t.pendown()
    starLen = randrange(10, 100)
    for i in range(5):
        t.forward(starLen)
        t.left(144)
done()
