from gpiozero import PWMLED
from time import sleep
from tkinter import *
import requests
import json
import threading


class App:
    firebase_url = "https://raspberryfirebase.firebaseio.com";
    __job = None;
    __currentLedValue=0;
    __pin = 25;
    def __init__(self,master):
        '''initital led'''
        self.led = PWMLED(self.__pin);
        self.led.value = 0;
        '''initial tkinter'''
        self.master = master;
        mainFrame = Frame(master);
        subFrame = Frame(mainFrame,relief=GROOVE,borderwidth=2);
        customFont = font.Font(family="Helvetica",size=12);        
        title = Label(mainFrame,text="PWM_LED").place(relx=0.05,rely=0.01,anchor=NW);
        self.scale = Scale(subFrame,orient=HORIZONTAL, from_=0, to=100,tickinterval=10,font=customFont,command=self.userUpdateValue);
        
        self.scale.pack(fill=X,expand=YES,padx=20);        
        subFrame.pack(fill=BOTH,expand=YES,padx=20,pady=20);
        mainFrame.pack(fill=BOTH,expand=YES);
        self.getDataFromFirebase();

    def userUpdateValue(self,event):
        if self.__job:
            self.master.after_cancel(self.__job);
        self.__job = self.master.after(500,self.__do_something);
        

    def __do_something(self):
        self.__jon = None;
        getData = {"pwm_value":self.scale.get()};
        requests.put(self.firebase_url + "/" + "raspberrypi/PWM_Led.json",data=json.dumps(getData));

    def getDataFromFirebase(self):        
        r = requests.get(self.firebase_url + "/raspberrypi/PWM_Led.json");
        try:
            receiveData = r.json();
            value = receiveData["pwm_value"];
            if  value != self.__currentLedValue:
                self.__currentLedValue = value;
                self.led.value = value/100;
               
        except:
            return;
        
        threading.Timer(1,self.getDataFromFirebase).start();
        
        

root = Tk();
root.title("PWMLED");
root.geometry("500x200");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*foreground","#888888");
display = App(root);
root.mainloop();

