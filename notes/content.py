from tkinter import *

class App:
    def __init__(self,master):
        master.geometry("300x200");
        fm = Frame(master,width=300,height=200);
        Button(fm, text="Left").pack(side=LEFT);
        Button(fm, text = "This is the Center button").pack(side=LEFT);
        Button(fm, text= "Right").pack(side=LEFT);
        fm.pack();
        


root = Tk();
root.option_add("*font",("Verdana",12,"bold"));
root.title("Pack - Example1");
display = App(root);
root.mainloop();
