from tkinter import *
from gpiozero import AngularServo
from HR04 import HR04
import requests
import json


class App:
    def __init__(self,master):
        self.master = master;       
        self.angleValue = 0;
        self.valueVariable = IntVar();
        self.distanceValue =  StringVar();
        self.firebase_url = "https://raspberryfirebase.firebaseio.com";
        
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
        Label(servoFrame,text="Servo").place(relx=0.03,anchor=NW);

        self.button0 = Radiobutton(borderFrame,text="0",variable=self.valueVariable,value=0,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button25 = Radiobutton(borderFrame,text="25",variable=self.valueVariable,value=25,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button50 = Radiobutton(borderFrame,text="50",variable=self.valueVariable,value=50,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button75 = Radiobutton(borderFrame,text="75",variable=self.valueVariable,value=75,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button90 = Radiobutton(borderFrame,text="90",variable=self.valueVariable,value=90,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        borderFrame.pack(side=TOP,padx=10,pady=10);
        servoFrame.pack(side=TOP);

        distanceFrame = Frame(mainFrame);
        self.label = Label(distanceFrame,textvariable = self.distanceValue);
        self.distanceValue.set("distance:0cm");
        self.label.pack();
        distanceFrame.pack(side=TOP);
        mainFrame.pack();
        
    def changeDegree(self):
        self.angleValue = self.valueVariable.get();
        print(self.angleValue);
        passData = {"angle":self.angleValue};
        requests.patch(self.firebase_url + "/raspberrypi/servo.json",data=json.dumps(passData));
        
        
    def distanceHandler(self):
        try:
            distance = self.hr04.getCmDistance();
            if distance != None:
                print("%.2f cm" % distance);
                self.distanceValue.set("distance:%d cm" % distance);
                passData = {"distance":distance};
                requests.patch(self.firebase_url + "/raspberrypi/servo.json",data=json.dumps(passData));
                
            else:
                print("too long");

            getJson = requests.get(self.firebase_url + "/raspberrypi/servo.json").json();
            angle = getJson["angle"];
            self.valueVariable.set(angle);
            self.servo.angle = float(angle);
        except:
            print("except");
            pass;
            
        self.master.after(1000,self.distanceHandler);

if __name__ == "__main__":
    root = Tk();
    root.title("servo And HC-HR04");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    display = App(root);
    root.mainloop();
    
