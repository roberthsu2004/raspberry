from tkinter import *
from gpiozero import AngularServo
from HR04 import HR04
import requests
import json


class App:
    
    def __init__(self,master):
        self.master = master;
        self.firebase_url = "https://raspberryfirebase.firebaseio.com";
        self.angleValue = 0;
        #HR04
        self.hr04 = HR04(23,24);
        self.distanceHandler();
        
        #for gpio servo initial
        self.servo = AngularServo(18,min_angle=0,max_angle=90);
        self.servo.angle = 90;
        #for tk
        
        mainFrame = Frame(self.master);
        servoFrame = Frame(mainFrame);
        borderFrame = Frame(servoFrame,borderwidth=2,relief=GROOVE,pady=30,padx=10);        
        Label(servoFrame,text="Servo").place(relx=0.03,anchor=NW);
        self.valueVariable = IntVar();
        self.button0 = Radiobutton(borderFrame,text="0",variable=self.valueVariable,value=0,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button25 = Radiobutton(borderFrame,text="25",variable=self.valueVariable,value=25,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button50 = Radiobutton(borderFrame,text="50",variable=self.valueVariable,value=50,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button75 = Radiobutton(borderFrame,text="75",variable=self.valueVariable,value=75,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.button90 = Radiobutton(borderFrame,text="90",variable=self.valueVariable,value=90,indicatoron=0,padx=20,command=self.changeDegree).pack(side=LEFT,padx=20);
        self.valueVariable.set(90);
        
        borderFrame.pack(side=TOP,padx=10,pady=10);    
        servoFrame.pack(side=TOP);
        
        distanceFrame = Frame(mainFrame);
        self.distanceValue = StringVar();
        self.label = Label(distanceFrame,textvariable=self.distanceValue);
        self.distanceValue.set("distance:0cm");
        self.label.pack();
        distanceFrame.pack(side=TOP);
        mainFrame.pack();

    def __str__(self):
        return "servo control and HR04 distance"
    
    def changeDegree(self):
        self.angleValue = self.valueVariable.get();
        #self.servo.angle = value;
        passData = {"angle":self.angleValue};
        request = requests.patch(self.firebase_url + "/raspberrypi/servo.json",data=json.dumps(passData));

    def distanceHandler(self):
         try:
            self.hr04 = HR04(23,24);
            distance = self.hr04.getCmDistance();
            if distance != None:                
                self.distanceValue.set("distance:%d" % distance);
                passData = {"distance":distance};
                request = requests.patch(self.firebase_url + "/raspberrypi/servo.json",data=json.dumps(passData));
            
            getJson = requests.get(self.firebase_url + "/raspberrypi/servo.json").json();
            angle = getJson["angle"];
            self.valueVariable.set(angle);
            self.servo.angel = int(angle);
         except:
            pass;
            
         self.master.after(1000,self.distanceHandler);
        
        

if __name__ == "__main__":
    root = Tk();
    root.title("servo And HC-HR04");
    root.option_add("*font",("Helvetica",18, "bold"));
    root.option_add("*background","gold");
    #root.option_add("*activeBackground","#333");
    #root.option_add("*activeForeground","white");
    #root.option_add("*highlightBackground","red");
    #root.option_add("*HighlightColor","red");
    app = App(root);
    root.mainloop();
    
    
    
