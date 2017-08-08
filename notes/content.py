from gpiozero import MCP3008
from time import sleep

pot = MCP3008(0);
ldr = MCP3008(1);

while True:
    print("variable:%.2f" % pot.value);
    print("======================");
    print("light:%.5f" % ldr.value);
    sleep(1);
