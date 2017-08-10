from HR04 import HR04
from time import sleep

hr04 = HR04(23,24);

while True:
    print("Distance to %.2f cm" % hr04.getCmDistance());
    sleep(1);
