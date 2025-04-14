from turtle import *

i, k, tx, ty = [0] * 4
swidth, sheight = 800, 450

if __name__ == '__main__':
    title('거북이 구구단')
    shape('turtle')
    setup(width=swidth + 50, height=sheight + 50)
    screensize(swidth, sheight)
    penup()
    tx,ty = -500, 250
    goto(tx, ty)

    for i in range(1, 10):
        for k in range(2, 10):
            goto(tx + 80 * k, ty - 40 * i)
            gugu = str(k) + 'X' + str(i) + '=' + str(k * i)
            write(gugu, font=('Arial', 12, 'bold'))
    done()
