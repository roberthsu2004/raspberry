import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setwarnings(False)

while True:
    GPIO.output(25,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(25,GPIO.LOW)
    time.sleep(0.2)

GPIO.cleanup();