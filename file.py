>>> from gpiozero import LED
>>> led = LED(26)
>>> led.on()
>>> led.off()
>>> led.toggle();
>>> led.toggle();
>>> led.blink(1,1,3,True)
>>> led.blink(0.3,0.3,100,True)
>>> 
