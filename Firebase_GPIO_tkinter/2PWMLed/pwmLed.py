from gpiozero import PWMLED
from tkinter import *
from tkinter import font
import json
import requests
import threading;


class App:
    '''這是app的class用來做控制pwm的介面'''

    def __init__(self,master):
        '''這是初始化'''
        self.pin = 25;
        self.job = None;
        self.master = None;
        self.scale = None;
        self.scaleValue = IntVar();
        self.firebase_url = "https://raspberryfirebase.firebaseio.com"
        self.led = PWMLED(self.pin);


        #介面
        self.master = master;
        mainFrame = Frame(self.master);
        subFrame = Frame(mainFrame,relief=GROOVE,borderwidth=2);
        title = Label(subFrame,text="PWM_LED").pack(padx=20,pady=20);
        smallFont = font.Font(family="Helvetica",size=12);
        self.scale =Scale(subFrame,orient=HORIZONTAL,from_=0,to=100,tickinterval=10,font=smallFont,command=self.userUpdateValue,variable=self.scaleValue).pack(fill=BOTH,expand=YES,padx=10,pady=10);
        subFrame.pack(fill=BOTH,expand=YES,padx=10,pady=10);
        mainFrame.pack(fill=BOTH,expand=YES);
        self.getDataFromFirebase();
    
    def userUpdateValue(self,event):
        if self.job:
            self.master.after_cancel(self.job)

        self.job = self.master.after(100,self.do_something);
    
    def do_something(self):
        print(self.scaleValue.get());
        getData = {"pwm_value":self.scaleValue.get()};
        try:
            requests.put(self.firebase_url+"/raspberrypi/PWM_Led.json",data=json.dumps(getData));
        except:
            print("put data error");

        self.job = None;

    def getDataFromFirebase(self):
        try:
            response = requests.get(self.firebase_url + "/raspberrypi/PWM_Led.json");
            receiveData = response.json();
            value = receiveData["pwm_value"];
            self.scaleValue.set(value);
            self.led.value = value/100.0;
        except:
            print("get data error";);
            print(error);
        finally:
            threading.Timer(0.2,self.getDataFromFirebase).start();
        

       
        

root = Tk();
root.title("PWMLED");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","#000000");
root.option_add("*foreground","#ffffff");
root.geometry("500x200");
display = App(root);
root.mainloop();
