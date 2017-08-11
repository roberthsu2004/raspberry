from tkinter import *
from gpiozero import AngularServo
from HR04 import HR04
import requests
import json


class App:
    def __init__(self,master):
        self.master = master;
        #HR04
        self.hr04 = HR04(23,24);
        self.distanceHandler();
        
        
    def distanceHandler(self):
        distance = self.hr04.getCmDistance();
        if distance != None:
            print("%.2f cm" % distance);
        else:
            print("too long");
            
        self.master.after(1000,self.distanceHandler);

if __name__ == "__main__":
    root = Tk();
    root.title("servo And HC-HR04");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    display = App(root);
    root.mainloop();
    
