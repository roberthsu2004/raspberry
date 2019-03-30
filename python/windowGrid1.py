from tkinter import *
import RPi.GPIO as GPIO
import time

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setwarnings(False)


master = Tk()
master.title("Window Grid")

def flightLed():
   print("run")
    


    
def windowClose():
    print("window close")
    master.destroy()
    GPIO.cleanup()

for x in range(1,10):
    for y in range (1,10):
        openBtn = Button(master, text= str(x*y), command=flightLed)
        openBtn.grid(row=x, column=y,sticky=W,padx=10,pady=10)


master.protocol("WM_DELETE_WINDOW", windowClose)
master.mainloop()

#http://effbot.org/tkinterbook/button.htm
#https://coldnew.github.io/f7349436/

