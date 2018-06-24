from tkinter import *
from gpiozero import MCP3008
from threading import Timer
import firebase_admin;
from firebase_admin import credentials;
from firebase_admin import db;
class App:
    def __init__(self,master):
        #initial firebase
        cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-1608c845ce.json');
        firebase_admin.initialize_app(cred, {
'databaseURL': 'https://raspberryfirebase.firebaseio.com/'});
        self.mcp3008Ref = db.reference("raspberrypi/MCP3008");
        
        #initial gpiozero
        self.ldr = MCP3008(channel=7);
        self.adc = MCP3008(channel=6);
        
        #tkinter
        brightnessFrame = Frame(master,relief=GROOVE,borderwidth=2);
        brightnessSubFrame = Frame(brightnessFrame);
        Label(brightnessSubFrame,text="brightness",anchor=NW).pack(fill=BOTH,pady=10,padx=10);
        self.brightnessValue = StringVar();
        Label(brightnessSubFrame,textvariable=self.brightnessValue).pack(fill=BOTH,pady=10);
        self.brightnessValue.set("0.12345");
        brightnessSubFrame.pack(ipady=40,ipadx=150);
        brightnessFrame.pack(padx=30,pady=30);
        
        temperatureFrame = Frame(master,relief=GROOVE,borderwidth=2);
        temperatureSubFrame = Frame(temperatureFrame);
        Label(temperatureSubFrame,text="temperature",anchor=NW).pack(fill=BOTH,pady=10,padx=10);
        self.temperatureValue = StringVar();
        Label(temperatureSubFrame,textvariable=self.temperatureValue).pack(fill=BOTH,pady=10);
        self.temperatureValue.set("0.12345");
        temperatureSubFrame.pack(ipady=40,ipadx=150);
        temperatureFrame.pack(padx=30,pady=30);
        self.autoUpdate();
        
    def autoUpdate(self):
        self.brightnessValue.set("brightness:{0:.2f}".format(self.ldr.value * 1000));
        self.temperatureValue.set("temperature:{0:.2f}".format(self.adc.value * 3.3 * 100));
        try:
            self.mcp3008Ref.update({
                'brightness':self.ldr.value * 1000,
                'temperature':self.adc.value * 3.3 * 100
                });
        except:
            pass;
        
        Timer(1,self.autoUpdate).start();
        


if __name__ == "__main__":
    root = Tk();
    root.title("溫度和光線感應");
    root.option_add("*font",("verdana",18,"bold"));
    root.option_add("*background","gold");
    root.option_add("*foreground","#888888");
    display = App(root);
    root.mainloop();
