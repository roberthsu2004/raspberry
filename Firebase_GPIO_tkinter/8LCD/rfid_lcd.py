#! /usr/bin/python2.7

from Tkinter import *
from gpiozero import Buzzer
from lcd_display import lcd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



class App:
    def __init__(self,master):
        #firebase_init
        #firebase
        global register
        cred = credentials.Certificate('../raspberryfirebase-firebase-adminsdk-q4ht6-296b3b1772.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://raspberryfirebase.firebaseio.com/'})
        self.lcdRef = db.reference('raspberrypi/LCD')
        
        
        #buzzer init
        self.bz = Buzzer(16)
        #Tkinter
        #for buzzer
        buzzerFrame = Frame(master);
        Button(buzzerFrame,text="Buzzer Control",command=self.userClickBuzzer,padx=10,pady=10).pack(padx=30,pady=10);
        buzzerFrame.pack();
        
        #for lcd
        lcdFrame = Frame(master);
        self.entryString1 = StringVar();
        self.entryString2 = StringVar();
        Entry(master, textvariable=self.entryString1 ).pack();
        self.entryString1.set("tfirst line");
        Entry(master, textvariable=self.entryString2 ).pack();
        self.entryString2.set("second line");
        lcdFrame.pack();
        #lcd
        my_lcd = lcd();
        my_lcd.display_string('Raspberry Pi',1);
        my_lcd.display_string('Hello' ,2);
        
        #firebase register
        register = self.lcdRef.listen(self.lcdCallBack);
        
    def userClickBuzzer(self):
        self.bz.beep(on_time=0.5, off_time=0.5, n=1,);
        
    def lcdCallBack(self,event):
        print event.data;
        print event.event_type;
        print event.path;
        if event.path == "/":
            self.entryString1.set(event.data['line1']);
            self.entryString2.set(event.data['line2']);
        elif event.path == "/line1":
            self.entryString1.set(event.data);
        elif event.path == "/line2":
            self.entryString2.set(event.data);

def on_closing():
    tk.destroy();
    register.close();
    

if __name__ == "__main__":
    tk = Tk();
    tk.title("RFID_LCD_BUZZER");
    tk.option_add("*font",("verdana",18,"bold"));
    tk.option_add("*background","gold");
    tk.option_add("*foreground","#888888");
    tk.protocol("WM_DELETE_WINDOW",on_closing);    
    app = App(tk);
    tk.mainloop();
    
