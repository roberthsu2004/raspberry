from tkinter import *

class App:
    def __init__(self,master):
        master.title("LED Control");

root = Tk();
root.geometry("400x300");
display = App(root);
root.mainloop();
