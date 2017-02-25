from gpiozero import MCP3008
from time import sleep
from tkinter import *
import requests
import json

class App:
    __master = None;
    __autoJob = None;
    ldr = MCP3008(channel=7);
    adc = MCP3008(channel=6);
    firebase_url = "https://raspberryfirebase.firebaseio.com";
    
    def __init__(self,master):
        self.__master = master;
        mainFrame = Frame(master);
        subFrame = Frame(mainFrame,relief=GROOVE,borderwidth=2);
        title = Label(mainFrame,text="brightness").place(anchor=NW,relx=0.08,rely=0.01);
        self.temperatureValue = StringVar();
        self.temperatureLabel = Label(subFrame,textvariable=self.temperatureValue);
        self.temperatureLabel.pack(fill=X,pady=30);
        self.brightnessValue = StringVar();
        self.brightnessLabel = Label(subFrame,textvariable = self.brightnessValue);
        self.brightnessLabel.pack(fill=X,pady=30);
        
        self.autoUpdate();
        subFrame.pack(fill=BOTH,expand=YES,padx=20,pady=20);
        mainFrame.pack(fill=BOTH,expand=YES);

    def autoUpdate(self):
        try:
            self.temperatureValue.set("temperature:%.2f" % (self.adc.value * 3.3 * 100));
            self.brightnessValue.set("brightness:%.2f" % self.ldr.value);
            ''''firebase'''
            passData = {"temperature":"%.2f" % (self.adc.value * 3.3 * 100),"brightness":"%.2f" % self.ldr.value};
            request = requests.put(self.firebase_url + "/raspberrypi/MCP3008.json",data=json.dumps(passData));
            print(request);
           
        except:
            print("error");
            

        self.__master.after(500,self.autoUpdate);
        
        
    
root = Tk();
root.title("brightness");
root.geometry("400x300+30+30");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*forground","#888888");
app = App(root);
root.mainloop();
    
