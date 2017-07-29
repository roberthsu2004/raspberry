import requests
from time import sleep
from gpiozero import LED

led = LED(26);
while True:
    firebase_url = "https://raspberryfirebase.firebaseio.com/"
    r = requests.get(firebase_url+"/led.json?print=pretty",verify=False);
    
    if r.json():   
        led.on();
    else:
        led.off();
    
    sleep(1);
