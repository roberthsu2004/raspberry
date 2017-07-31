from gpiozero import LED
from time import sleep
import requests
import json

led = LED(22);
while True:
    firebase_url = "https://raspberryfirebase.firebaseio.com/"
    content = requests.get(firebase_url + "test/led.json",verify=False);
    newState =content.json();    
    if newState:
        led.on();
    else:
        led.off();
    
    sleep(0.2);
