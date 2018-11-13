# coding=UTF-8

from MFRC522 import MFRC522
import signal
from liquidcrystal_i2c import liquidcrystal_i2c
import RPi.GPIO as GPIO
import time
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import *
import threading

def end_read(signal, frame):
    global continue_reading;
    print("ctrl+c captured, ending read.");
    continue_reading = False;

def onSelect(evt):
    global thirdFrame;
    w = evt.widget;
    index = int(w.curselection()[0]);
    value = w.get(index);
    thirdFrame.pack_forget();
    thirdFrame = Frame(root);
    docs = firestoreDb.collection(u'門禁資料').where(u'uid', u'==', str(value)).limit(10).get();
    for (index,doc) in enumerate(docs):
        #print('uid = {}'.format(doc.get('uid')));
        #Label(itemFrame,text=doc.get('uid'),width=15).pack(side=LEFT,anchor=W);
        #Label(itemFrame,text=doc.get('datatime'),width=20).pack(side=LEFT,anchor=W);
        Label(thirdFrame,text=doc.get('uid'),width=20).grid(row=index,column=0,sticky=W);
        Label(thirdFrame,text=doc.get('datatime'),width=20).grid(row=index,column=1,sticky=W);
        #itemFrame.pack();
        
    thirdFrame.pack();
    
    
def displayWindow():
    global mainFrame;
    global thirdFrame;
    root.title("RFID-LCD-BUZZER");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    
    #read firestoredata
    docs = firestoreDb.collection(u'門禁資料').order_by(u'datatime',direction=firestore.Query.DESCENDING).limit(5).get();
    mainFrame = Frame(root)
    for (index,doc) in enumerate(docs):
        #itemFrame = Frame(mainFrame);
        print('uid = {}'.format(doc.get('uid')));
        #Label(itemFrame,text=doc.get('uid'),width=15).pack(side=LEFT,anchor=W);
        #Label(itemFrame,text=doc.get('datatime'),width=20).pack(side=LEFT,anchor=W);
        Label(mainFrame,text=doc.get('uid'),width=20).grid(row=index,column=0,sticky=W);
        Label(mainFrame,text=doc.get('datatime'),width=20).grid(row=index,column=1,sticky=W);
        #itemFrame.pack();
    mainFrame.pack();
    
    secondFrame = Frame(root);
    allCarInfo = firestoreDb.collection(u'卡片資訊').get()
    listbox = Listbox(secondFrame);
    for carInfo in allCarInfo:
        listbox.insert('end', carInfo.get(u'carID'));
    listbox.pack();
    listbox.bind('<<ListboxSelect>>',onSelect);
    secondFrame.pack();
    
    thirdFrame = Frame(root);
    thirdFrame.pack();
    

def rfid_sensor():
        global mainFrame;
        #checkuid
        uid = [];
        preUid0 = 0;
        preUid1 = 0;
        preUid2 = 0;
        preUid3 = 0;
        (status, tagType)= MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL);
        if status == MIFAREReader.MI_OK:
            print("card detected");
        
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
                print("check card");
                uidString = str(uid0) + "," + str(uid1) + "," + str(uid2) + "," + str(uid3);
                lcd.printline(0, 'card Number'.center(16));
                lcd.printline(1, uidString.center(16));
                #firestore
                t = time.time();
                doc_ref = firestoreDb.collection(u'門禁資料').document(str(t));
                
                date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S");
                doc_ref.set({u'datatime':date, u'uid': uidString})
                
                #firestore
                #add Car Infomation
                
                
                
                carInfoRef = firestoreDb.collection(u'卡片資訊').where(u'carID', u'==' , uidString).get();
                i = 0
                for carInfo in carInfoRef:
                    i += 1;
                    print(carInfo.get(u'carID'));
                
                #i == 0 no this carID
                if i == 0:
                    newCar = firestoreDb.collection(u'卡片資訊').document();
                    newCar.set({u'carID': uidString});
                
                
                
                buzzer = GPIO.PWM(36,50);
                buzzer.start(50);
                time.sleep(0.2);
                buzzer.stop();
                #docs = firestoreDb.collection(u'門禁資料').where(u'uid', u'==', u'34,64,67,213').get();
                #for doc in docs:
                    #print(doc);
                    #print('uid = {},datetime:{}'.format(doc.get('uid'),doc.get('datatime')));
                
                docs = firestoreDb.collection(u'門禁資料').order_by(u'datatime',direction=firestore.Query.DESCENDING).limit(20).get();
                if mainFrame != None:
                    mainFrame.pack_forget();
                
                mainFrame = Frame(root)
                for (index,doc) in enumerate(docs):
                    #itemFrame = Frame(mainFrame);
                    print('uid = {}'.format(doc.get('uid')));
                    #Label(itemFrame,text=doc.get('uid'),width=15).pack(side=LEFT,anchor=W);
                    #Label(itemFrame,text=doc.get('datatime'),width=20).pack(side=LEFT,anchor=W);
                    Label(mainFrame,text=doc.get('uid'),width=20).grid(row=index,column=0,sticky=W);
                    Label(mainFrame,text=doc.get('uid'),width=20).grid(row=index,column=1,sticky=W);
                    #itemFrame.pack();
                mainFrame.pack();
    
        threading.Timer(1,rfid_sensor).start();
    
    
    

if __name__ == "__main__":
    #initial firestore
    cred = credentials.Certificate('raspberryfirebase-firebase-adminsdk-q4ht6-1608c845ce.json')
    firebase_admin.initialize_app(cred)
    firestoreDb = firestore.client()
    #tkinter
    root = Tk();
    mainFrame = None;
    thirdFrame = None;
    displayWindow();
    
    
    #rfid
    continue_reading = True;
    signal.signal(signal.SIGINT, end_read);
    MIFAREReader = MFRC522();
    
    
    #lcd
    lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27,1);
    lcd.printline(0, 'LCM1602 IIC V2'.center(16))
    lcd.printline(1, 'and'.center(16))
    
    #buzzer init
    GPIO.setmode(GPIO.BOARD);
    GPIO.setup(36,GPIO.OUT);
    GPIO.setwarnings(False);
    
    buzzer = GPIO.PWM(36,50);
    buzzer.start(50);
    time.sleep(0.5);
    buzzer.stop();
    print(root);    
    rfid_sensor();
    root.mainloop();
    
    
    
        

