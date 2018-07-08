#!/usr/bin/python2.7

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

def end_read(signal, frame):
    global continue_reading;
    print "ctrl+C captured, ending read."
    continue_reading = False;
    GPIO.cleanup();

def useCard():
    print "checked card";
    uidString =  str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]);
    print "Card read UID: " +  uidString;
    firestore_ref = db.collection(u'recordsOfEntry').document();
    t = time.time();
    date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S");    
    firestore_ref.set({u'datatime':unicode(date),u'uid':unicode(uidString)});
    GPIO.output(LED_green,GPIO.HIGH)
    time.sleep(0.5);
    GPIO.output(LED_green,GPIO.LOW);
    

if __name__ == "__main__":
    #define LED pin variable
    LED_green = 13;
    LED_red = 11;
    counter = 0;

    #checked uid
    uid=[];
    preUid0 = 0;
    preUid1 = 0;
    preUid2 = 0;
    preUid3 = 0;

    #define firebase
    cred = credentials.Certificate("raspberryfirebase-firebase-adminsdk-q4ht6-1608c845ce.json");
    firebase_admin.initialize_app(cred);
   
    db = firestore.client();
    
    

    #define output
    GPIO.setmode(GPIO.BOARD);
    GPIO.setup(LED_green,GPIO.OUT);
    GPIO.setup(LED_red,GPIO.OUT);
    GPIO.setwarnings(False);
    continue_reading = True;
    
    #ctrl + c gameover
    signal.signal(signal.SIGINT, end_read)
    MIFAREReader = MFRC522.MFRC522();

    print "Welcome to the MFRC522 data read example";
    print "Press Ctrl-C to stop."

    while continue_reading:
        #scan for cards
        
        (status,tagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL);
        if status == MIFAREReader.MI_OK:
            pass;
        
        
        (status,uid) = MIFAREReader.MFRC522_Anticoll();
        if status == MIFAREReader.MI_OK:
            uid0 = uid[0];
            uid1 = uid[1];
            uid2 = uid[2];
            uid3 = uid[3];
        
            if uid0 != preUid0 or uid1 != preUid1 or uid2 != preUid2 or uid3 != preUid3:
                preUid0 = uid0;
                preUid1 = uid1;
                preUid2 = uid2;
                preUid3 = uid3;
                useCard();
        
        

    
