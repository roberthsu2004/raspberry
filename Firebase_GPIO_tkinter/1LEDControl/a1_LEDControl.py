from tkinter import *
from gpiozero import LED
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading
import datetime
import time


class App:
    
    def __init__(self,master):
        self.ledText = StringVar();
        self.ledState = "";
        self.led25 = LED(25);
        self.cred = credentials.Certificate("raspberryfirebase-firebase-adminsdk-q4ht6-1608c845ce.json");
        firebase_admin.initialize_app(self.cred,{
            'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
        });
        self.ref = db.reference("raspberrypi/LED_Control");        
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
        print("newState={0}".format(newState));
        try:
            self.ref.update({
                'LED25': newState,
                'date': date
            });

        except:
            return;
        
        
    
    def getFirebaseData(self):
        try:
            response = self.ref.get();            
        except:
            threading.Timer(0.2,self.getFirebaseData).start();
            return;
        
        self.ledState = response["LED25"];
        if self.ledState == "OPEN":
            self.ledText.set("LED CLOSE");
            self.led25.on();
        elif self.ledState == "CLOSE":
            self.ledText.set("LED OPEN");
            self.led25.off();

        threading.Timer(0.2,self.getFirebaseData).start();




root = Tk();
root.geometry("400x300");
display = App(root);
root.mainloop();
