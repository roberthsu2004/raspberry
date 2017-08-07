from tkinter import *

class App:
    def __init__(self,master):
        self.master = master;
        mainFrame = Frame(master);
        subFrame = Frame(mainFrame,relief=GROOVE,borderwidth=2);
        subFrame.pack(fill=X,expand=YES,padx=20);
        mainFrame.pack(fill=BOTH,expand=YES)

root = Tk();
root.title("PWMLED");
root.geometry("500x200");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*foreground","#888888");
display = App(root);
root.mainloop();
