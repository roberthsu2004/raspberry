from gpiozero import RGBLED
from tkinter import *
import requests
import json
import threading

class App:
    __sendJob = None;
    master = None;
    firebase_url = "https://raspberryfirebase.firebaseio.com";
    redPin = 22;
    greenPin = 27;
    bluePin = 17;
    rgbLed = RGBLED(redPin,greenPin,bluePin);
    timer = None;
    
    def __init__(self,master):
        self.master = master;
        '''variable class'''
        self.redScaleValue = IntVar();
        self.greenScaleValue = IntVar();
        self.blueScaleValue = IntVar();
        
        mainFrame = Frame(master,width=700,height=400);        
        leftFrame = Frame(mainFrame,bg="#bbbbbb",width=200);        
        self.resultCanvas = Canvas(leftFrame,width=200,height=200,bg="#bbbbbb");       
        self.rectangleItem = self.resultCanvas.create_rectangle(15,15,185,185,fill="blue");
        self.resultCanvas.pack(side=LEFT);
        
        leftFrame.pack(side=LEFT,fill=Y,expand=YES);
        
        rightFrame=Frame(mainFrame,bg="#bbbbbb",width=500);
        self.createRightArea(rightFrame);
        
        rightFrame.pack(side=LEFT,fill=Y);
        
        mainFrame.pack(fill=BOTH,expand=YES);
        self.getDataFromFirebase();

    def createRightArea(self,master):
        redLabel = Label(master,text="Red",fg="red",justify=LEFT,compound=LEFT).pack(fill=X,pady=10);
        self.redScale = Scale(master,from_=0,to=255,orient=HORIZONTAL,length=500,bg="red",foreground="white",relief=FLAT,borderwidth=0,command=self.redChange,variable=self.redScaleValue);
        self.redScale.pack(fill=X,pady=10,padx=5);
        self.redScale.bind("<ButtonPress>",self.buttonPress);
        self.redScale.bind("<ButtonRelease>",self.buttonRelease);
        greenLabel = Label(master,text="Green",fg="green",justify=LEFT,compound=LEFT).pack(fill=X,pady=10);
        self.greenScale = Scale(master,from_=0,to=255,orient=HORIZONTAL,length=500,bg="green",foreground="white",relief=FLAT,borderwidth=0,command=self.greenChange,variable=self.greenScaleValue);
        self.greenScale.pack(fill=X,pady=10,padx=5);
        self.greenScale.bind("<ButtonPress>",self.buttonPress);
        self.greenScale.bind("<ButtonRelease>",self.buttonRelease);
        blueLabel = Label(master,text="Blue",fg="blue",justify=LEFT,compound=LEFT).pack(fill=X,pady=10);
        self.blueScale = Scale(master,from_=0,to=255,orient=HORIZONTAL,length=500,bg="blue",foreground="white",relief=FLAT,borderwidth=0,command=self.blueChange,variable=self.blueScaleValue);
        self.blueScale.pack(fill=X,pady=10,padx=5);
        self.blueScale.bind("<ButtonPress>",self.buttonPress);
        self.blueScale.bind("<ButtonRelease>",self.buttonRelease);

    def redChange(self,redEvent):
        self.colorChange();
    
    def greenChange(self,greenChange):
        self.colorChange();
    
    def blueChange(self,blueChange):
        self.colorChange();

    def sendToFirebase(self):
        '''send To Firebase'''
        sendRedValue = int(self.redScale.get());
        sendGreenValue = int(self.greenScale.get());
        sendBlueValue = int(self.blueScale.get());        
        #print("red:%d,green:%d,blue:%d" % (sendRedValue,sendGreenValue,sendBlueValue));
        jsonData = {"red":sendRedValue,"green":sendGreenValue,"blue":sendBlueValue};
        r = requests.put(self.firebase_url + "/raspberrypi/RGB_LED.json",data=json.dumps(jsonData));
        
    def getDataFromFirebase(self):   
        r = requests.get(self.firebase_url + "/raspberrypi/RGB_LED.json");
        try:
            receiveData = r.json();
            receiveRed = receiveData["red"];
            receiveGreen = receiveData["green"];
            receiveBlue = receiveData["blue"];
            self.rgbLed.color = (receiveRed/255.0,receiveGreen/255.0,receiveBlue/255.0);
            self.redScaleValue.set(receiveRed);
            self.greenScaleValue.set(receiveGreen);
            self.blueScaleValue.set(receiveBlue);
            print("red:%d,green:%d,blue:%d" % (receiveRed,receiveGreen,receiveBlue));
            tk_rgb = "#%02x%02x%02x" % (receiveRed,receiveGreen,receiveBlue);
            print(tk_rgb);
            self.resultCanvas.itemconfig(self.rectangleItem,fill=tk_rgb);
        except:
            return;

        self.timer = threading.Timer(1,self.getDataFromFirebase);
        self.timer.start();
        print(self.timer);
        
    def colorChange(self):
        
        if self.__sendJob:
            self.master.after_cancel(self.__sendJob);
        
        self.__sendJob = self.master.after(100,self.sendToFirebase);

    def buttonPress(self,event):
        if self.timer.is_alive:
            self.timer.cancel();
        
    def buttonRelease(self,event):        
        self.timer = threading.Timer(1,self.getDataFromFirebase);
        self.timer.start();
        
        
    
        

root = Tk();
root.geometry("700x400");
root.title("RGB_LED");
root.option_add("*Font",("Helvetica",18,"bold"));
root.option_add("*background","#bbbbbb");
display = App(root);
root.mainloop();
