from tkinter import *
<<<<<<< HEAD
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
    
=======

def ledClose():
    print("ledClose");
    
def ledOpen():
    print("ledOpen");

def appInterface(window):
    frame = Frame(window,borderwidth=1,relief=GROOVE);
    Label(frame,
          text="LED Controler",
          font=("Helvetica", 20)
          ,anchor=W).pack(fill=X);
    
    Button(frame,text="open",
           pady=50,
           font=("Helvetica", 20),
           command=ledOpen).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(frame,text="close"
           ,pady=50,           
           font=("Helvetica", 20),command=ledClose).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    frame.pack(padx=10,pady=10,fill=X);
    
    rgbFrame = Frame(window,borderwidth=1,relief=GROOVE);
    Button(rgbFrame,text="RED"
           ,pady=50,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(rgbFrame,text="GREEN"
           ,pady=50,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(rgbFrame,text="BLUE"
           ,pady=50,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    rgbFrame.pack(padx=10,pady=10,fill=X);
    
    numberFrame = Frame(window,borderwidth=1,relief=GROOVE);
    Button(numberFrame,text="1"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(numberFrame,text="2"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    
    Button(numberFrame,text="3"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    Button(numberFrame,text="4"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    Button(numberFrame,text="5"
           ,pady=25,           
           font=("Helvetica", 20)).pack(side=LEFT,
                                        fill=X,
                                        expand=True,
                                        padx=10,
                                        pady=20);
    numberFrame.pack(padx=10,pady=10,fill=X);


if __name__ == '__main__':
    app = Tk();
    
    app.title("LEDControl");
    app.geometry("500x600");
    app.option_add("*Button.Background","#007A9B");
    app.option_add("*Button.Foreground","white");
    appInterface(window=app);
    app.mainloop();

>>>>>>> 4b76a21dd1b7316bc64e9d1728c7a7d0f21d8877
