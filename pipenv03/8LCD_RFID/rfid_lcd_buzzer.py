#! usr/bin/python3.5

from MFRC522 import MFRC522
import sys
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter  import *
import time
import threading
import datetime

from raspi_gpio.lcd_display import lcd


#from lcd_display import lcd

class App():
    def __init__(self,window):
        #initial firestore
        cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-7d3f9d2d5e.json')
        firebase_admin.initialize_app(cred)
        self.firestoreClient = firestore.client()
        
        
        #buzzer init
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(36,GPIO.OUT);
        self.buzzer = GPIO.PWM(36, 100);
        #self.buzzer.start(50);
        self.buzzer.start(100);
        time.sleep(0.3);
        self.buzzer.stop();
        
        
        #lcd init
        #self.lcd = lcd_display()
        
        ##checked rfid
        self.uid=[];
        self.preUid0 = 0;
        self.preUid1 = 0;
        self.preUid2 = 0;
        self.preUid3 = 0;
        self.MIFAREReader = MFRC522();
        self.rfidHandler();
        
    def rfidHandler(self):
        (status, tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL);
        if status == self.MIFAREReader.MI_OK:
            print("status success");
       
        
        (status, self.uid) = self.MIFAREReader.MFRC522_Anticoll();
        if status == self.MIFAREReader.MI_OK:
            uid0 = self.uid[0];
            uid1 = self.uid[1];
            uid2 = self.uid[2];
            uid3 = self.uid[3];
            if uid0 != self.preUid0 or uid1 != self.preUid1 or uid2 != self.preUid2 or uid3 != self.preUid3:
                #bee
                self.buzzer.start(100);
                time.sleep(0.3);
                self.buzzer.stop();
                
                #card check
                self.preUid0 = uid0;
                self.preUid1 = uid1;
                self.preUid2 = uid2;
                self.preUid3 = uid3;
                threading.Timer(5,self.clearPreUid).start();
                self.useCard();
             
        
        threading.Timer(0.5,self.rfidHandler).start();
    def clearPreUid(self):
        self.preUid0 = 0;
        self.preUid1 = 0;
        self.preUid2 = 0;
        self.preUid3 = 0;
    
    
    def useCard(self):
        print("Checked card");
        uidString = str(self.uid[0]) + "," + str(self.uid[1]) + "," +  str(self.uid[2]) + "," + str(self.uid[3]);
        print("Card read UID:" + uidString);
        document_ref = self.firestoreClient.collection('recordsOfEntry').document();
        t = time.time();
        date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S");
        document_ref.set({
            'datatime':date,
            'uid':uidString
            });



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
