from tkinter import *
import requests
import json

class App:
    firebase_url = "https://raspberryfirebase.firebaseio.com"
    __job = None;
    def __init__(self,master):
        self.master = master;
        mainFrame = Frame(master);
        subFrame = Frame(mainFrame,relief=GROOVE,borderwidth=2);
        title = Label(mainFrame,text="PWM_LED").place(relx=0.05,rely=0.01,anchor=NW);
        self.scaleValue = IntVar();
        smallFont = font.Font(family="Helvetica",size=12);
        self.scale = Scale(subFrame,orient=HORIZONTAL, from_=0, to=100,tickinterval=10,font=smallFont,command=self.userUpdateValue,variable=self.scaleValue);
        self.scale.pack(fill=X,expand=YES,padx=20);
        subFrame.pack(fill=BOTH,expand=YES,padx=20,pady=20);
        mainFrame.pack(fill=BOTH,expand=YES);

    def userUpdateValue(self,event):
       print("user update");
       if self.__job:
           self.master.after_cancel(self.__job);
       self.__job = self.master.after(100,self.__do_something);

    def __do_something(self):
        print("user dosomething");
        getData = {"pwm_value":self.scale.get()};
        requests.put(self.firebase_url + "/raspberrypi/PWM_Led.json",data=json.dumps(getData));
        
        self.__job = None;

root = Tk();
root.title("PWMLED");
root.geometry("500x200");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*foreground","#888888");
display = App(root);
root.mainloop();
