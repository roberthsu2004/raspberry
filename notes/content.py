from tkinter import *
from gpiozero import AngularServo
from HR04 import HR04
import requests
import json


class App:
    def __init__(self,master):
        self.master = master;       

        #for gpio servo initial
        self.servo = AngularServo(18,min_angle=0,max_angle=90);
        self.servo.angle = 0;

        #HR04
        self.hr04 = HR04(23,24);
        self.distanceHandler();

        #for tk
        mainFrame = Frame(self.master);
        servoFrame = Frame(mainFrame);
        borderFrame = Frame(servoFrame,borderwidth=2,relief=GROOVE,pady=30,padx=10);
        borderFrame.pack(side=TOP,padx=10,pady=10);
        servoFrame.pack(side=TOP);
        mainFrame.pack();
        
        
    def distanceHandler(self):
        distance = self.hr04.getCmDistance();
        if distance != None:
            print("%.2f cm" % distance);
            if distance < 10:
                self.servo.angle = 0;
            else:
                self.servo.angle = 45;
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
    
