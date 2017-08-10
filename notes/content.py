from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24);

while True:
    print("Distance to %.2f m" % sensor.distance);
    sleep(1);
