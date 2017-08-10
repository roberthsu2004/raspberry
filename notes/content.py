from HR04 import HR04
from time import sleep

hr04 = HR04(23,24);

while True:
    try:
        distance = hr04.getCmDistance();
        print("Distance to %.2f cm" % distance);
    except:
        print("too long");
        pass;
    sleep(1);
