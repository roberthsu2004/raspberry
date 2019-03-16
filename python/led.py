import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(3,GPIO.IN)
GPIO.setwarnings(False)

while True:
    #GPIO.output(22,GPIO.HIGH)
    #time.sleep(0.2)
    #GPIO.output(22,GPIO.LOW)
    #time.sleep(0.2)
    inputValue = GPIO.input(3)
    print(inputValue)
    time.sleep(0.3)

GPIO.cleanup();