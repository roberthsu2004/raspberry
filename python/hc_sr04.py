from hcsr04sensor import sensor
import time

TRIGGER_PIN = 25
ECHO_PIN = 8
print("按下STOP可以中斷程式")
try:
    while True:
        print("run")
        
        sr04 = sensor.Measurement(TRIGGER_PIN, ECHO_PIN)
        raw_measurement = sr04.raw_distance()
        distance = sr04.distance_metric(raw_measurement)
        print(distance)
        time.sleep(1)
except KeyboardInterrupt:
    print("control-c 關閉程式")
except:
    print("關閉程式")