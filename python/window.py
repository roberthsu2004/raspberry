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


openBtn = Button(master, text="OPEN", command=openLed)
openBtn.pack()

closeBtn = Button(master, text=("CLOSE"),command=closeLed)
closeBtn.pack()
master.protocol("WM_DELETE_WINDOW", windowClose)
master.mainloop()

#http://effbot.org/tkinterbook/button.htm
#https://coldnew.github.io/f7349436/