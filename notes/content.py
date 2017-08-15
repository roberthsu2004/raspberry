from gpiozero import MCP3008
from tkinter import *

class App:
    def __init__(self,master):
        self.master = master;

root = Tk();
root.title("brightness");
root.geometry("400x300");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*forground","#888888");
display = App(root);
root.mainloop();
