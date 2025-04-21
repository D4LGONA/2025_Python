from turtle import *
from random import *

myTurtle, tx, ty, tcolor, tsize, tshape, tangle = [None] * 7
playerTurtles = []
swidth, sheight = 500, 500

if __name__ == "__main__":
    title('거북이 리스트 활용 (정렬)')
    setup(width=swidth+50, height=sheight+50)
    screensize(swidth,sheight)
    for i in range(5):
        myTurtle = Turtle('turtle')
        tx = randrange(-swidth//2, swidth//2)
        ty = randrange(-sheight//2, sheight//2)
        r = random(); g = random(); b = random()
        tsize = randrange(10,100)/10
        tangle = randrange(1,360)
        playerTurtles.append([myTurtle, tx, ty, tsize, r, g, b, tangle])

    for i in range(len(playerTurtles) - 1):
        for k in range(i+1, len(playerTurtles)):
            if playerTurtles[i][3] > playerTurtles[k][3]:
                playerTurtles[i], playerTurtles[k] = playerTurtles[k], playerTurtles[i]
    savex, savey = playerTurtles[0][1], playerTurtles[0][2]

    for tlist in playerTurtles:
        myTurtle = tlist[0]
        myTurtle.penup()
        myTurtle.goto(savex,savey)
        myTurtle.color((tlist[4], tlist[5], tlist[6]))
        myTurtle.pencolor((tlist[4], tlist[5], tlist[6]))
        myTurtle.turtlesize(tlist[3])
        myTurtle.pendown()
        myTurtle.goto(tlist[1], tlist[2])
        myTurtle.left(tlist[7])
        savex = tlist[1]
        savey = tlist[2]
    done()