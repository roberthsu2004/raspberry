from tkinter import *

class App:
    def __init__(self,master):
        master.geometry("800x400");
        fm = Frame(master);
        Button(fm, text="Left").pack(side=LEFT,fill=BOTH,expand=YES);
        Button(fm, text = "Center").pack(side=LEFT,fill=BOTH,expand=YES);
        Button(fm, text= "Right").pack(side=LEFT,fill=BOTH,expand=YES);
        fm.pack(fill=BOTH,expand=YES);
        


root = Tk();
root.option_add("*font",("Verdana",12,"bold"));
root.title("Pack - Example3");
display = App(root);
root.mainloop();
