from tkinter import *
import RPi.GPIO as GPIO

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setwarnings(False)


master = Tk()

def openLed():
    GPIO.output(LED,GPIO.HIGH);
    

def closeLed():
    GPIO.output(LED,GPIO.LOW)
    
def windowClose():
    print("window close")
    master.destroy()
    GPIO.cleanup()

Label(master, text="OPEN LIGHT").grid(row=0, column=0, sticky=W)
openBtn = Button(master, text="OPEN", command=openLed)
openBtn.grid(row=0, column=1,sticky=W)

Label(master, text="CLOSE LIGHT").grid(row=1, column=0, sticky=W)
closeBtn = Button(master, text=("CLOSE"),command=closeLed)
closeBtn.grid(row=1,column=1,sticky=W)
master.protocol("WM_DELETE_WINDOW", windowClose)
master.mainloop()

#http://effbot.org/tkinterbook/button.htm
#https://coldnew.github.io/f7349436/
