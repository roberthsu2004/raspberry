import RPi.GPIO as GPIO
import time


class HR04(object):
    def __init__(self,trig,echo):
        GPIO.setmode(GPIO.BCM);
        self.trig = trig;
        self.echo = echo;
        #print("distance Measurement In Progess");
        GPIO.setup(self.trig,GPIO.OUT);
        GPIO.setup(self.echo,GPIO.IN);

    def __str__():
        return "control HR04";

    def getCmDistance(self):
        GPIO.output(self.trig,False);
        #print("Waiting For sensor To Settle");
        #time.sleep(1);
        try:
            GPIO.output(self.trig,True);
            time.sleep(0.00001);
            GPIO.output(self.trig,False);
            while GPIO.input(self.echo)==0:
                pulse_start = time.time();
            while GPIO.input(self.echo)==1:
                pulse_end = time.time();

            pulse_duration = pulse_end-pulse_start;
            distance = pulse_duration * 17150;
            distance = round(distance,2);
            GPIO.cleanup();
            if distance < 2 or distance > 400:
                return None;
            else:
                return distance;  
            
        except:
            return None;
        
