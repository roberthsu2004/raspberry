from gpiozero import Button
from signal import pause
import requests
import json

firebase_url = "https://raspberryfirebase.firebaseio.com/"

def button_press():
    content = requests.get(firebase_url + "test/led.json",verify=False);
    newState = not content.json();    
    jsonValue = {"led":newState}
    requests.put(firebase_url + "test.json",data=json.dumps(jsonValue));

button = Button(17);
button.when_pressed = button_press;
pause();

