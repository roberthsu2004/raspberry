from tkinter import *
from gpiozero import MCP3008
from threading import Timer

class GUI:
    def __init__(self,w):
        self.lightness = MCP3008(channel=7)
        self.temperature = MCP3008(channel=6)
        
        self.temperatureText = StringVar()
        self.lightnessText = StringVar();
        mainFrame = Frame(w,relief=GROOVE, borderwidth=2)
        Label(mainFrame, text="溫度").grid(row=0, column=0,sticky=E,padx=5,pady=20)
        Label(mainFrame, text="光線").grid(row=1, column=0,sticky=E,padx=5,pady=20)
        Entry(mainFrame, width= 25, state= DISABLED, textvariable=self.temperatureText).grid(row=0,column=1,sticky=W,padx=5,pady=20)
        self.temperatureText.set("123.456")
        Entry(mainFrame, width= 25, state= DISABLED, textvariable=self.lightnessText).grid(row=1,column=1,sticky=W,padx=5,pady=20)
        self.lightnessText.set("456.789")
        mainFrame.pack(padx=10,pady=10)
        self.autoUpdate()
    
    def autoUpdate(self):        
        lightnessValue = self.lightness.value * 1000;
        temperatureValue = self.temperature.value * 3.3 * 100
        self.temperatureText.set("{:.2f}".format(temperatureValue))
        self.lightnessText.set("{:.3f}".format(lightnessValue))
        Timer(1,self.autoUpdate).start()

if __name__ == "__main__":
    window = Tk()
    window.title("溫度和光線的感應")
    window.option_add("*font",("verdana",18,"bold"))
    window.option_add("*background","#068587")
    window.option_add("*foreground", "#FFFFFF")
    #window.geometry("500x200")
    myGui = GUI(window)
    window.mainloop()
    