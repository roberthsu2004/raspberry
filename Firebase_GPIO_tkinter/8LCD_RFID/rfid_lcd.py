# coding=Big5
#! /usr/bin/python2.7


from Tkinter import *
#from gpiozero import Buzzer
from lcd_display import lcd

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import datetime
import threading


class App:
    def __init__(self,master):
        #firebase_init
        #firebase
        global register
        cred = credentials.Certificate('../raspberryfirebase-firebase-adminsdk-q4ht6-296b3b1772.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://raspberryfirebase.firebaseio.com/'})
        self.lcdRef = db.reference('raspberrypi/LCD')
        self.firestoreClient = firestore.client();
        
        
        
        
        #buzzer init
        #self.bz = Buzzer(16)
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(36,GPIO.OUT);    
        GPIO.setwarnings(False);
        
        self.p = GPIO.PWM(36, 50)
        
        
        #Tkinter
        #for buzzer
        buzzerFrame = Frame(master);
        Button(buzzerFrame,text="Buzzer Control",command=self.userClickBuzzer,padx=10,pady=10).pack(padx=30,pady=10,expand=YES,fill=BOTH);
        buzzerFrame.pack(expand=YES,fill=BOTH);
        
        #for lcd
        lcdFrame = Frame(master);
        self.entryString1 = StringVar();
        self.entryString2 = StringVar();
        entry1Frame = Frame(lcdFrame);
        Label(entry1Frame,text="name").pack(side=LEFT);
        Entry(entry1Frame,textvariable=self.entryString1,width=50).pack(side=LEFT,padx=10);
        self.entryString1.set("tfirst line");
        entry1Frame.pack(expand=YES,fill=BOTH,padx=10,pady=10);
        
        entry2Frame = Frame(lcdFrame);
        Label(entry2Frame,text="pwd").pack(side=LEFT);
        Entry(entry2Frame, textvariable=self.entryString2,width=50).pack(side=LEFT,expand=YES,fill=BOTH,padx=10);
        self.entryString2.set("second line");
        entry2Frame.pack(expand=YES,fill=BOTH,padx=10,pady=10);
        
        Button(lcdFrame,text="Entry Send",command=self.userClickSend,padx=10,pady=10).pack(padx=30,pady=10,expand=YES,fill=BOTH);
        lcdFrame.pack();
        #lcd
        self.my_lcd = lcd();
        
        #firebase register
        try:
            register = self.lcdRef.listen(self.lcdCallBack);
        except ApiCallError as error:
            print("apiCallError");
       
            
        #checked uid
        self.uid=[];
        self.preUid0 = 0;
        self.preUid1 = 0;
        self.preUid2 = 0;
        self.preUid3 = 0;
        self.MIFAREReader = MFRC522.MFRC522();
        self.rfidHandler();
        
    def rfidHandler(self):
        #scan for cards
        
        (status,tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL);
        if status == self.MIFAREReader.MI_OK:
             pass;
        
        
        (status,self.uid) = self.MIFAREReader.MFRC522_Anticoll();
        if status == self.MIFAREReader.MI_OK:
            uid0 = self.uid[0];
            uid1 = self.uid[1];
            uid2 = self.uid[2];
            uid3 = self.uid[3];
        
            if uid0 != self.preUid0 or uid1 != self.preUid1 or uid2 != self.preUid2 or uid3 != self.preUid3:
                self.preUid0 = uid0;
                self.preUid1 = uid1;
                self.preUid2 = uid2;
                self.preUid3 = uid3;
                self.useCard();
    
        threading.Timer(0.1,self.rfidHandler).start();
    
    def useCard(self):
        print "checked card";
        uidString =  str(self.uid[0]) + "," + str(self.uid[1]) + "," + str(self.uid[2]) + "," + str(self.uid[3]);
        print "Card read UID: " +  uidString;
        document_ref = self.firestoreClient.collection(u'recordsOfEntry').document();
        t = time.time();
        date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S");    
        document_ref.set({u'datatime':unicode(date),u'uid':unicode(uidString)});
        
        
        
    
        
    def userClickSend(self):
        try:
            self.lcdRef.update({
                'line1':self.entryString1.get(),
                'line2':self.entryString2.get()
                });
            
        except ValueError as error:
             print("value Error");
        except ApiCallError as error:
             print("apiCallError");
        
    def userClickBuzzer(self):
        #self.bz.beep(on_time=0.5, off_time=0.5, n=1,);
        self.p.start(50)
        #self.p.ChangeFrequency(523)
        time.sleep(0.1)
        self.p.stop();
        print('call buzzer');
        
    def lcdCallBack(self,event):
        print event.data;
        print event.event_type;
        print event.path;
        if event.path == "/":
            self.entryString1.set(event.data['line1']);
            self.entryString2.set(event.data['line2']);
            self.my_lcd.display_string(event.data['line1'],1);
            self.my_lcd.display_string(event.data['line2'],2);
        elif event.path == "/line1":
            self.entryString1.set(event.data);
            self.my_lcd.display_string(event.data,1);
        elif event.path == "/line2":
            self.entryString2.set(event.data);
            self.my_lcd.display_string(event.data,2);

def on_closing():
    tk.destroy();    
    register.close();
    GPIO.cleanup();
    

if __name__ == "__main__":
    
    tk = Tk();
    tk.title("RFID_LCD_BUZZER");
    tk.option_add("*font",("verdana",18,"bold"));
    tk.option_add("*background","gold");
    tk.option_add("*foreground","#888888");
    tk.protocol("WM_DELETE_WINDOW",on_closing);
    
    
    app = App(tk);
    tk.mainloop();
    
