from gpiozero import MCP3008
from time import sleep

pot = MCP3008(0);
ldr = MCP3008(1);
adc = MCP3008(7);


while True:
    print("variable:%.5f" % pot.value);
    print("======================");
    print("light:%.5f" % ldr.value);
    
    for value in  adc.values:
        print(value * 3.3 * 100);
        
    sleep(100);
