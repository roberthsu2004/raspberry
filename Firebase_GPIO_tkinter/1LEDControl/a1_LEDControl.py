from tkinter import *
from gpiozero import LED
import requests
import threading
import datetime
import time
import json

class App:
    firebase_url = "https://raspberryfirebase.firebaseio.com/";
    def __init__(self,master):
        self.ledText = StringVar();
        self.ledState = "";
        self.led25 = LED(25);
        master.title("LED Control");
        master.option_add("*Font",("verdana",18,"bold"));
        f = Frame(master);
        xf = Frame(f,relief=GROOVE,borderwidth=2);
        titleLabel = Label(f,text="LED Control").place(relx=0.05,rely=0.025,anchor=NW);
        xf.pack(expand=YES,fill=BOTH,padx=5,pady=20);
        button = Button(xf,textvariable=self.ledText,command=lambda :self.userClick()).pack(expand=YES,fill=BOTH,padx=80,pady=50);
        f.pack(fill=BOTH,expand=YES);
        self.getFirebaseData();
    
    def userClick(self):
        if self.ledState == "OPEN" :
            newState = "CLOSE";
        else:
            newState = "OPEN";
        
        t = time.time();
        date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S");
        data = {"LED25":newState,"date":date};
        try:
            result = requests.put(App.firebase_url + "/" + "raspberrypi/LED_Control.json",data=json.dumps(data));
        except:
            return;
        print("status code = %s, Respone = %s" % (str(result.status_code),result.text));

        
    
    def getFirebaseData(self):
        try:
            response = requests.get(App.firebase_url + "/" + "raspberrypi/LED_Control.json");
        except:
            threading.Timer(0.1,self.getFirebaseData).start();
            return;
        
        if response.status_code == 200 :
            self.ledState = response.json()["LED25"];
            if self.ledState == "OPEN":
                self.ledText.set("LED CLOSE");
                self.led25.on();
            elif self.ledState == "CLOSE":
                self.ledText.set("LED OPEN");
                self.led25.off();
        
        threading.Timer(0.1,self.getFirebaseData).start();




root = Tk();
root.geometry("400x300");
display = App(root);
root.mainloop();
