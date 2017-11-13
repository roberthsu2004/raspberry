#python2.x

from Tkinter import *;

import requests;
import json;
import threading;
import smbus;
import time;
from pirc522 import RFID
import signal

# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
    #LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

    # Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

    #Open I2C interface
    #bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1




class App:
    #rfid

    
    def lcd_init(self):
        # Initialise display
        self.lcd_byte(0x33,LCD_CMD) # 110011 Initialise
        self.lcd_byte(0x32,LCD_CMD) # 110010 Initialise
        self.lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
        self.lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
        self.lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01,LCD_CMD) # 000001 Clear display
        time.sleep(E_DELAY)

    def lcd_byte(self,bits, mode):
        # Send byte to data pins
        # bits = the data
        # mode = 1 for data
        #        0 for command

        bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
        bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

        # High bits
        bus.write_byte(I2C_ADDR, bits_high)
        self.lcd_toggle_enable(bits_high)

        # Low bits
        bus.write_byte(I2C_ADDR, bits_low)
        self.lcd_toggle_enable(bits_low)

    def lcd_toggle_enable(self,bits):
        # Toggle enable
        time.sleep(E_DELAY)
        bus.write_byte(I2C_ADDR, (bits | ENABLE))
        time.sleep(E_PULSE)
        bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
        time.sleep(E_DELAY)

    def lcd_string(self,message,line):
        # Send string to display

        message = message.ljust(LCD_WIDTH," ")

        self.lcd_byte(line, LCD_CMD)

        for i in range(LCD_WIDTH):
            self.lcd_byte(ord(message[i]),LCD_CHR)
        
    def __init__(self,master):
        #initialise display
        self.lcd_init();
        
        
        self.master = master;
        self.angleValue = 0;
        self.valueVariable = IntVar();
        self.rfidValue = StringVar();
        self.line1Value = StringVar();
        self.line2Value = StringVar();

        self.firebase_url = "https://raspberryfirebase.firebaseio.com";
       

        #for tk
        mainFrame = Frame(self.master);
        lcdFrame = Frame(mainFrame);
        borderFrame = Frame(lcdFrame,borderwidth=2,relief=GROOVE,pady=30,padx=10);
        Label(lcdFrame,text="LCD").place(relx=0.03,anchor=NW);
        line1Frame = Frame(borderFrame);
        Label(line1Frame,text="第一行文字").pack(side=LEFT,padx=5,pady=10);
        Entry(line1Frame, width=40, textvariable=self.line1Value).pack(side=LEFT,expand=YES);
        line1Frame.pack();
        line2Frame = Frame(borderFrame);
        Label(line2Frame,text="第二行文字").pack(side=LEFT,padx=5,pady=10);
        Entry(line2Frame, width=40, textvariable=self.line2Value).pack(side=LEFT);
        line2Frame.pack();
        buttonFrame = Frame(borderFrame);
        Button(buttonFrame,text="改變文字",command=self.changeLCDdisplay).pack(side=TOP,fill=X,expand=YES);
        buttonFrame.pack(fill=X);
        self.line1Value.set("111111111");
        self.line2Value.set("2222222222");
        borderFrame.pack(padx=10,pady=10);
        lcdFrame.pack();

        rfidFrame = Frame(mainFrame);
        Label(rfidFrame,textvariable=self.rfidValue).pack();
        self.rfidValue.set("distance:0cm");
        rfidFrame.pack();
        mainFrame.pack();
    
    def changeLCDdisplay(self):
         line1 = self.line1Value.get();
         line2 = self.line2Value.get();
         self.lcd_string(line1,LCD_LINE_1);
         self.lcd_string(line2,LCD_LINE_2);
    
    def showRfidNumber(self,message):
        self.lcd_string(message,LCD_LINE_1);
        self.line1Value.set(message);

    
    
'''
    def distanceHandler(self):
        try:
            distance = self.hr04.getCmDistance();
            if distance != None:
                self.distanceValue.set("distance:%d" % distance);
                passData = {"distance":distance};
                request = requests.patch(self.firebase_url + "/raspberrypi/servo.json",data = json.dumps(passData));

                #loadData
                getJson = requests.get(self.firebase_url + "/raspberrypi/servo.json").json();

                angle = getJson["angle"];
                self.valueVariable.set(angle);
                self.servo.angle = angle;
        except:
            pass;

'''      
    


if __name__ == "__main__":  
    
    root = Tk();
    root.title("Servo And HC-HR04");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    display = App(root);

    rdr = RFID()
    util = rdr.util()
    # Set util debug to true - it will print what's going on
    util.debug = False;
    uid0 = 0;
    uid1 = 0;
    uid2 = 0;
    uid3 = 0;
    

    def rfidWait():
        rdr.wait_for_tag();
        # Request tag
        (error, data) = rdr.request()
        if not error:
            (error, uid) = rdr.anticoll();
            if not error:
                global uid0;
                global uid1;
                global uid2;
                global uid3; 
                global display;               
                if uid0 != uid[0] and uid1 != uid[1] and uid2 != uid[2] and uid3 != uid[3]:
                    message = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]);
                    print(message); 
                    display.showRfidNumber(message);                       
                    uid0 = uid[0];
                    uid1 = uid[1];
                    uid2 = uid[2];
                    uid3 = uid[3]; 

        threading.Timer(0.2,rfidWait).start();

    rfidWait();
    root.mainloop();
