from gpiozero import MCP3008
from tkinter import *

class App:
    ldr = MCP3008(channel=7);
    adc = MCP3008(channel=6);
    
    def __init__(self,master):
        self.master = master;
        mainFrame = Frame(master);
        subFrame = Frame(mainFrame,relief=GROOVE,borderwidth=2);
        subFrame.pack(fill=BOTH,expand=YES,padx=20,pady=20);
        title = Label(mainFrame,text="brightness").place(anchor=NW,relx=0.08,rely=0.01);
        self.temperatureValue = StringVar();
        self.temperatureLabel = Label(subFrame,textvariable=self.temperatureValue);
        self.temperatureLabel.pack(fill=X,pady=30);
        self.brightnessValue = StringVar();
        self.brightnessLabel = Label(subFrame,textvariable=self.brightnessValue);
        self.brightnessLabel.pack(fill=X,pady=30);
        mainFrame.pack(fill=BOTH,expand=YES);
        self.autoUpdate();

    def autoUpdate(self):
        self.temperatureValue.set("temperature:%.2f" % (App.adc.value * 3.3 * 100));
        self.brightnessValue.set("brightness:%.2f" % App.ldr.value);
                
        self.master.after(500,self.autoUpdate);
        

root = Tk();
root.title("brightness");
root.geometry("400x300");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*forground","#888888");
display = App(root);
root.mainloop();
