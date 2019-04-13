from tkinter import *
from sys import path

def displayWindow(w):
    print("displayWindow");
    print(type(w))
    pass;

if __name__ == "__main__":
    window = Tk();
    window.title("LED Control")
    window.geometry("300x200")
    displayWindow(window);
   
    window.mainloop();
    