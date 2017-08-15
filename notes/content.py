from tkinter import *

class App:
    def __init__(self,master):
        fm = Frame(master);
        Button(fm, text="Left").pack(side=TOP,fill=X);
        Button(fm, text = "This is the Center button").pack(side=TOP);
        Button(fm, text= "Right").pack(side=TOP,fill=X);
        fm.pack();
        


root = Tk();
root.option_add("*font",("Verdana",12,"bold"));
root.title("Pack - Example1");
display = App(root);
root.mainloop();
