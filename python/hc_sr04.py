from hcsr04sensor import sensor
import time

TRIGGER_PIN = 25
ECHO_PIN = 8
print("按下STOP可以中斷程式")
try:
    while True:
        print("run")
        time.sleep(10)
except:
    print("關閉程式")