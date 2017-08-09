from gpiozero import MCP3008,LED
from time import sleep

pot = MCP3008(0);
ldr = MCP3008(1);
relay = LED(17);

while True:
    print("variable:%.5f" % pot.value);
    print("======================");
    print("light:%.5f" % ldr.value);
    #light = 0.11 , dark = 0.02
    if ldr.value > 0.06:
        relay.on();
    else:
        relay.off();
    sleep(1);
