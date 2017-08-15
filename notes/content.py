from gpiozero import MCP3008
from tkinter import *

class App:
    ldr = MCP3008(channel=7);
    adc = MCP3008(channel=6);
    def __init__(self,master):
        self.master = master;
        self.autoUpdate();

    def autoUpdate(self):
        print("adc.value:%.2f" % (App.adc.value * 3.3 * 100));
        print("ldr.value:%.2f" % App.ldr.value);
        
        self.master.after(500,self.autoUpdate);
        

root = Tk();
root.title("brightness");
root.geometry("400x300");
root.option_add("*font",("verdana",18,"bold"));
root.option_add("*background","gold");
root.option_add("*forground","#888888");
display = App(root);
root.mainloop();
