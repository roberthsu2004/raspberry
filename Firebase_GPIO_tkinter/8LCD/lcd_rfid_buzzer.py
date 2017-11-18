from pirc522 import RFID
import RPi.GPIO as GPIO
from Tkinter import *
import signal
import time
import smbus
import threading;
import requests;
import json;

def lcd_init():
      # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)




#LCD
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

#RFID

rdr = RFID()
util = rdr.util()
# Set util debug to true - it will print what's going on
util.debug = True
uid0 = 0;
uid1 = 0;
uid2 = 0; 
uid3 = 0;

#lcd
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
lcd_init()

#tkinter
root = Tk();
line1Value = StringVar();
line2Value = StringVar();

#firebase
firebase_url = "https://raspberryfirebase.firebaseio.com"

def display():
    global root;
    global line1Value;
    global line2Value;
    #root= Tk();
    root.title("RFID LCD BUZZER");
    root.option_add("*font",("Helvetica",18,"bold"));
    root.option_add("*background","gold");
    mainFrame = Frame(root);
    lcdFrame = Frame(mainFrame);
    
    borderFrame = Frame(lcdFrame,borderwidth=2,relief=GROOVE,pady=30,padx=10);
    Label(lcdFrame,text="LCD").place(relx=0.03,anchor=NW);
    line1Frame = Frame(borderFrame);
    Label(line1Frame,text="第一行文字").pack(side=LEFT,padx=5,pady=10);
    Entry(line1Frame,width=40,textvariable=line1Value).pack(side=LEFT);
    line1Frame.pack();
    line2Frame = Frame(borderFrame);
    Label(line2Frame,text="第二行文字").pack(side=LEFT,padx=5,pady=10);
    Entry(line2Frame,width=40,textvariable=line2Value).pack(side=LEFT);
    line2Frame.pack();
    buttonFrame = Frame(borderFrame);
    Button(buttonFrame,text="改變文字",command=changeLCDdisplay).pack(fill=X,expand=YES);
    buttonFrame.pack(fill=X);
    borderFrame.pack(padx=10,pady=10);
    lcdFrame.pack();
    mainFrame.pack();
    
    

def changeLCDdisplay():
    line1 = line1Value.get();
    line2 = line2Value.get();
    lcd_string(line1,LCD_LINE_1);
    lcd_string(line2,LCD_LINE_2);
    passData = {"line1":line1,"line2":line2};
    request = requests.patch(firebase_url + "/raspberrypi/LCD.json",data=json.dumps(passData));

def firebaseHandler():
    getJson = requests.get(firebase_url + "/raspberrypi/LCD.json").json();
    line1Value.set(getJson["line1"]);
    line2Value.set(getJson["line2"]);
    lcd_string(getJson["line1"],LCD_LINE_1);
    lcd_string(getJson["line2"],LCD_LINE_2);

    threading.Timer(2,firebaseHandler).start();



def main():
    # Wait for tag
    rdr.wait_for_tag()
    #print("wait");
    # Request tag
    (error, data) = rdr.request()
    global uid0;
    global uid1;
    global uid2; 
    global uid3;
    global line1Value;
    global line2Value;
    
    if not error:
        #print("\nDetected")

        (error, uid) = rdr.anticoll()
        if not error:
            # Print UID

            
            if uid[0] != uid0 or uid[1] != uid1 or uid[2] != uid2 or uid[3] != uid3:
                 print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                 GPIO.setup(36, GPIO.OUT)
                 p = GPIO.PWM(36, 50)
                 p.start(50)
                 p.ChangeFrequency(523)
                 time.sleep(0.2);
                 p.stop()
                 message = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]);
                 lcd_string(message,LCD_LINE_2);
                 lcd_string("RFID        <",LCD_LINE_1);
                 line1Value.set("RFID        <");
                 line2Value.set(message);

                 passData = {"cardID":message};
                 request = requests.post(firebase_url + "/raspberrypi/rfid.json",data=json.dumps(passData));

                 uid0 = uid[0];
                 uid1 = uid[1];
                 uid2 = uid[2];
                 uid3 = uid[3];
    
    threading.Timer(0.1,main).start();



display();

threading.Timer(0.1,main).start();
threading.Timer(2,firebaseHandler).start();
root.mainloop();
