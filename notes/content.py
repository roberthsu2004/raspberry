from tkinter import *

class App:
    def __init__(self,master):
        master.title("LED Control");
        master.option_add("*Font",("Verdana",18,"bold"));
        self.ledText = StringVar();
        f = Frame(master);
        xf = Frame(f,relief=GROOVE,borderwidth=2);
        titleLabel = Label(f,text="LED control").place(relx=0.05,rely=0.025,anchor=NW);
        xf.pack(fill=BOTH,expand=20, padx=20,pady=20);
        f.pack(fill=BOTH,expand=YES);

root = Tk();
root.geometry("400x300");
display = App(root);
root.mainloop();
