from gpiozero import MotionSensor

def main():
    motionSensor = MotionSensor(pin=21,queue_len=5,sample_rate=120,threshold=0.2);
    
    while True:
        if motionSensor.motion_detected:
            print("active");
        else:
            print("inactive");
            
if __name__ == "__main__":
    main();
