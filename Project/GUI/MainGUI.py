from tkinter import *

class MainGui:
    def setUI(self): #메인
        pass

    def __init__(self):
        self.window = Tk()
        self.window.title("자판기")
        self.window.geometry("600x600")

        self.setUI()
        self.window.mainloop()