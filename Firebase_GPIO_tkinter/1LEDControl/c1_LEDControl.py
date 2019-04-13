from tkinter import *
from sys import path

def displayWindow(w):
    mainFrame = Frame(w,borderwidth=2,relief=GROOVE)
    mainFrame.pack(padx=10,pady=10)

if __name__ == "__main__":
    window = Tk();
    window.title("LED Control")
    window.geometry("300x200")
    displayWindow(window);
   
    window.mainloop();
    