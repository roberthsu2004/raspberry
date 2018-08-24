#! /usr/bin/python2.7

from Tkinter import *
from gpiozero import Buzzer
from lcd_display import lcd

class App:
    def __init__(self,master):
        #buzzer init
        self.bz = Buzzer(16)
        #Tkinter
        buzzerFrame = Frame(master);
        Button(buzzerFrame,text="Buzzer Control",command=self.userClickBuzzer,padx=10,pady=10).pack(padx=30,pady=10);
        buzzerFrame.pack();
        
        #lcd
        my_lcd = lcd();
        my_lcd.display_string('Raspberry Pi',1);
        my_lcd.display_string('Hello' ,2);
        
    def userClickBuzzer(self):
        self.bz.beep(on_time=0.5, off_time=0.5, n=1,);

if __name__ == "__main__":
    tk = Tk();
    tk.title("RFID_LCD_BUZZER");
    tk.option_add("*font",("verdana",18,"bold"));
    tk.option_add("*background","gold");
    tk.option_add("*foreground","#888888");
    app = App(tk);
    tk.mainloop();