from tkinter import *

master = Tk()

def openLed():
    print("Open")

def closeLed():
    print("Close")


openBtn = Button(master, text="OPEN", command=openLed)
openBtn.pack()
for i in range(1,10):
    closeBtn = Button(master, text=("CLOSE"+str(i)),command=closeLed)
    closeBtn.pack()

master.mainloop()

#http://effbot.org/tkinterbook/button.htm