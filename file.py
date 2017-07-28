from gpiozero import Button
from time import sleep

button = Button(pin=2,pull_up=True,bounce_time=None);
while True:
    if button.is_pressed:
        print("button is pressed");
    else:
        print("button is not pressed");

    sleep(1);
