from tkinter import *
from gpiozero import MCP3008
from threading import Timer
import requests
import json

class App:
    firebase_url = "https://raspberryfirebase.firebaseio.com"
    def __init__(self,master):
        self.ldr = MCP3008(channel=7);
        self.adc = MCP3008(channel=6);
        brightnessFrame = Frame(master,relief=GROOVE,borderwidth=2);
        birghtnessSubFrame = Frame(brightnessFrame);
        Label(birghtnessSubFrame,text="明亮度",anchor=W).pack(fill=BOTH,pady=10,padx=10);
        self.brightnessValue = StringVar();
        Label(birghtnessSubFrame,textvariable=self.brightnessValue).pack(fill=BOTH,pady=10);
        self.brightnessValue.set("0.12345");
        birghtnessSubFrame.pack(ipady=40,ipadx=150);
        brightnessFrame.pack(pady=30,padx=30);

        temperatureFrame = Frame(master,relief=GROOVE,borderwidth=2);
        temperatureSubFrame = Frame(temperatureFrame);
        Label(temperatureSubFrame,text="溫度",anchor=W).pack(fill=BOTH,pady=10,padx=10);
        self.temperatureValue = StringVar();
        Label(temperatureSubFrame,textvariable=self.temperatureValue).pack(fill=BOTH,pady=10);
        self.temperatureValue.set("23");
        temperatureSubFrame.pack(ipady=40,ipadx=150);
        temperatureFrame.pack(pady=30,padx=30);
        self.autoUpdate();
    
    def autoUpdate(self):
        self.brightnessValue.set("brightness:%.2f" % self.ldr.value);
        self.temperatureValue.set("temperature:%.2f" % (self.adc.value * 3.3 * 100));
        #firebase
        passData = {"temperature":"%.2f" % (self.adc.value * 3.3 * 100),"brightness":"%.2f" % self.ldr.value}
        try:
            requests.put(App.firebase_url + "/raspberrypi/MCP3008.json",data=json.dumps(passData));
        except:
            Timer(1,self.autoUpdate).start();
            return;

        Timer(1,self.autoUpdate).start();



root = Tk();
root.title("溫度和光線感應");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*forground","#888888");
display = App(root);
root.mainloop();
