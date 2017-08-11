from HR04 import HR04
from gpiozero import AngularServo
from time import sleep

hr04 = HR04(23,24);
servo = AngularServo(18,min_angle=0,max_angle=90);

while True:
        try:
                distance = hr04.getCmDistance();
                print("Distance to %.2f cm" % distance);
                
                if distance < 10:
                    servo.min();
                else:
                    servo.max();
        except:
                print("too long");
                pass;
        
        sleep(1);

        

    
    
    
    
