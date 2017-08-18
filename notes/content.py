from gpiozero import MotionSensor

def main():
    motionSensor = MotionSensor(21);
    
    while True:
        if motionSensor.motion_detected:
            print("active");
        else:
            print("inactive");
            
if __name__ == "__main__":
    main();
