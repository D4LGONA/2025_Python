import turtle

num1, num2 = 0, 0
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
    turtle.title('거북이로 2진수 논리합(비트OR) 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)
    num1 = int(input("2진수 입력: "), 2)
    num2 = int(input("2진수 입력: "), 2)
    num3 = num1 | num2
    write_num(bin(num1), num1, swidth / 2, 100)
    write_num(bin(num2), num2, swidth / 2, 0)
    write_num(bin(num3), num3, swidth / 2, -100)
    turtle.done()