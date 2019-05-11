from tkinter import *

class GUI:
    def __init__(self,w):
        mainFrame = Frame(w,relief=GROOVE, borderwidth=2)
        Label(mainFrame, text="溫度").grid(row=0, column=0,sticky=E,padx=5,pady=20)
        Label(mainFrame, text="光線").grid(row=1, column=0,sticky=E,padx=5,pady=20)
        Entry(mainFrame, width= 25, state= DISABLED, text='temperature').grid(row=0,column=1,sticky=W,padx=5,pady=20)
        Entry(mainFrame, width= 25, state= DISABLED, text='sunshin').grid(row=1,column=1,sticky=W,padx=5,pady=20)
        mainFrame.pack()

if __name__ == "__main__":
    window = Tk()
    window.title("溫度和光線的感應")
    window.option_add("*font",("verdana",18,"bold"))
    window.option_add("*background","#068587")
    window.option_add("*foreground", "#FFFFFF")
    #window.geometry("500x200")
    myGui = GUI(window)
    window.mainloop()
    