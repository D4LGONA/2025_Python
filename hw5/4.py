from turtle import *
from math import *
from random import *
t1, t2, t3 = [None] * 3
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6
swidth, sheight = 300, 300

if __name__ == "__main__":
    title("거북이 만나기")
    setup(width = swidth+ 50, height = sheight + 50)
    screensize(swidth, sheight)
    t1 = Turtle('turtle'); t1.color('red'); t1.penup()
    t2 = Turtle('turtle'); t2.color('green'); t2.penup()
    t3 = Turtle('turtle'); t3.color('blue'); t3.penup()
    t1.goto(-100, -100); t2.goto(0,0);t3.goto(100,100)
    t1.speed(10); t2.speed(10); t3.speed(10)
    while True:
        angle = randrange(0, 360)
        dist = randrange(1, 50)
        t1.left(angle); t1.forward(dist)
        angle = randrange(0, 360)
        dist = randrange(1, 50)
        t2.left(angle); t2.forward(dist)
        angle = randrange(0, 360)
        dist = randrange(1, 50)
        t3.left(angle); t3.forward(dist)

        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()

        if sqrt((t1X - t2X) ** 2 + (t1Y - t2Y) ** 2) <= 20 or \
            sqrt((t1X - t3X) ** 2 + (t1Y - t3Y) ** 2) <= 20 or \
            sqrt((t2X - t3X) ** 2 + (t2Y - t3Y) ** 2) <= 20:
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
            break
    done()
