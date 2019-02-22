from MFRC522 import MFRC522
import signal
import sys
import RPi.GPIO as GPIO
from tkinter  import *

class App():
    def __init__(self,window):
        pass;

'''
def end_read(signal, frame):
    print("ctrl+c captured, ending read.");
    GPIO.cleanup();
    sys.exit(0);
'''

def on_closing():
    print("ctrl+c captured, ending read.");
    GPIO.cleanup();
    sys.exit(0);
    

if __name__ == "__main__":
    GPIO.setwarnings(False);
    #signal.signal(signal.SIGINT, end_read);
    root = Tk();
    root.title("RFID_LCD_BUZZER");
    root.option_add("*font",("verdana",18,"bold"));
    root.option_add("*background","gold");
    root.option_add("*foreground","#888888");
    root.protocol("WM_DELETE_WINDOW",on_closing);
    app = App(root)      
    root.mainloop();
