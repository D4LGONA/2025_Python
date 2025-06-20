from tkinter import *
from tkinter.ttk import *
import random
import time
import threading

class ThreadProgressBar():
    def __init__(self, parent):
        self.progress = Progressbar(parent, orient=HORIZONTAL, length=500)
        self.progress.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
        self.thread = threading.Thread(target=self.runProgress, args=(self.progress,))
        self.thread.start()

    def runProgress(self, progress):
        hop = 0
        while True:
            hop = random.randrange(0, 10)
            if progress['value'] >= 100:
                break
            progress['value'] += hop
            time.sleep(0.5)

def runThreadProgress():
    thBar1 = ThreadProgressBar(window)
    thBar2 = ThreadProgressBar(window)
    thBar3 = ThreadProgressBar(window)

window = Tk()
window.geometry('300x250')
window.title('멀티 스레드')

threadButton = Button(window, text='멀티스레드 시작', command=runThreadProgress)
threadButton.pack(side = TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)

window.mainloop()