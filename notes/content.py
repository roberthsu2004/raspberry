from tkinter import *
from gpiozero import AngularServo
from HR04 import HR04
import requests
import json

class App:
    def __init__(self,master):
        self.master = master;

if __name__ == "__main__":
    root = Tk();
    root.title("servo And HC-HR04");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    display = App(root);
    root.mainloop();
    
