from tkinter import *
from sys import path

def displayWindow(w):
    mainFrame = Frame(w,borderwidth=2,relief=GROOVE)
    Button(mainFrame,text="Press Me").pack(expand=True,fill=BOTH,padx=40,pady=25);
    mainFrame.pack(expand=True,fill=BOTH,padx=10,pady=10)

if __name__ == "__main__":
    window = Tk();
    window.title("LED Control")
    window.geometry("300x200")
    displayWindow(window);
   
    window.mainloop();
    