from gpiozero import LED
import requests
content = requests.get("https://raspberryfirebase.firebaseio.com/test/lcd.json", verify=False)
print("status code:",content.status_code);
print("json:",content.json());

led = LED(17);
if content.json():
    led.on();
else:
    led.off();
