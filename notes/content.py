from tkinter import *

class App:
    def __init__(self,master):
        master.title("LED Control");
        master.option_add("*Font",("Verdana",18,"bold"));
        self.ledText = StringVar();
        f = Frame(master);
        xf = Frame(f,relief=GROOVE,borderwidth=2);
        titleLabel = Label(f,text="LED control").place(relx=0.05,rely=0.025,anchor=NW);
        button = Button(xf,textvariable=self.ledText,command=lambda:self.userClick()).pack(expand=YES,fill=BOTH,padx=50,pady=50);
        self.ledText.set("LED OPEN");
        xf.pack(fill=BOTH,expand=20, padx=20,pady=20);
        f.pack(fill=BOTH,expand=YES);
    
    def userClick(self):
        print("userClick");

root = Tk();
root.geometry("400x300");
display = App(root);
root.mainloop();
