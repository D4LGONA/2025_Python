from tkinter import *

def myFunc():
    global var, labelImage
    if var.get() == 1:
        labelImage.configure(image=photo1)
    elif var.get() == 2:
        labelImage.configure(image=photo2)
    elif var.get() == 3:
        labelImage.configure(image=photo3)
    else:
        labelImage.configure(image=None)

window = Tk()
window.geometry('400x400')
window.title("반려동물 선택하기")

labelText = Label(window, text = '좋아하는 동물 투표', fg = 'blue', font=('궁서체'))
labelText.pack()

var = IntVar()
rb1 = Radiobutton(window, text='강아지', variable=var, value=1)
rb1.pack()
rb2 = Radiobutton(window, text='고양이', variable=var, value=2)
rb2.pack()
rb3 = Radiobutton(window, text='토끼', variable=var, value=3)
rb3.pack()

buttonOk = Button(window, text='사진 보기', command=myFunc)
buttonOk.pack()

photo1 = PhotoImage(file='GIF/dog3.gif')
photo2 = PhotoImage(file='GIF/cat.gif')
photo3 = PhotoImage(file='GIF/rabbit.gif')
labelImage = Label(window, width=200, height=200, bg='yellow', image=None)
labelImage.pack()

window.mainloop()

