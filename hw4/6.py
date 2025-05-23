import turtle

number = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

def write_num(binary, num, curX, curY):
    for i in range(len(binary) - 2):
        turtle.goto(curX, curY)
        if num & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1


if __name__ == '__main__':
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)
    number = int(input("10진수 입력: "))
    write_num(bin(number), number, swidth / 2, 0)
    turtle.done()