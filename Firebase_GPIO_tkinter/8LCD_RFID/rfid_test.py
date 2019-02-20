from MFRC522 import MFRC522
import signal
import sys
import RPi.GPIO as GPIO
from tkinter  import *


def end_read(signal, frame):
    print("ctrl+c captured, ending read.");
    GPIO.cleanup();
    sys.exit(0);
    

if __name__ == "__main__":
    GPIO.setwarnings(False);
    signal.signal(signal.SIGINT, end_read);
    root = Tk();
    root.title("RFID");
    root.mainloop();