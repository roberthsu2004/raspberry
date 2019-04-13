from tkinter import *
from sys import path

buttonText = None


def displayWindow(w):
    global buttonText
    buttonText = StringVar()
    buttonText.set("OPEN")
    mainFrame = Frame(w,borderwidth=2,relief=GROOVE)    
    Button(mainFrame,textvariable=buttonText,font=("Helvetica", 18, "bold italic"),command=userClick).pack(expand=True,fill=BOTH,padx=40,pady=25);
    mainFrame.pack(expand=True,fill=BOTH,padx=10,pady=10)
   
def userClick():    
    print("user click");
    if buttonText.get() == "OPEN":
        buttonText.set("CLOSE")
    else:
        buttonText.set("OPEN")

if __name__ == "__main__":
    
    window = Tk();
    window.title("LED Control")
    window.geometry("300x200")
    displayWindow(window);
   
    window.mainloop();
    