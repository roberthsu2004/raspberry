#! usr/bin/python3.5

from MFRC522 import MFRC522
import sys
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter  import *
from gpiozero import Buzzer
import time

class App():
    def __init__(self,window):
        #initial firestore
        cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json')
        firebase_admin.initialize_app(cred)
        self.firestoreClient = firestore.client()
        
        
        #buzzer init
        #GPIO.setmode(GPIO.BCM);
        GPIO.setup(16,GPIO.OUT);
        self.buzzer = GPIO.PWM(16, 100);
        #self.buzzer.start(50);
        self.buzzer.start(100);
        time.sleep(0.3);
        self.buzzer.stop();
        




def on_closing():
    print("ctrl+c captured, ending read.");
    GPIO.cleanup();
    sys.exit(0);
    

if __name__ == "__main__":
    GPIO.setwarnings(False);    
    root = Tk();
    root.title("RFID_LCD_BUZZER");
    root.option_add("*font",("verdana",18,"bold"));
    root.option_add("*background","gold");
    root.option_add("*foreground","#888888");
    root.protocol("WM_DELETE_WINDOW",on_closing);
    app = App(root)      
    root.mainloop();
