from datetime import datetime
d = datetime.now();
print("{:%Y-%m-%d %H:%M:%S}".format(d));


def calculate_temperatures(kelvin):
    celsius = kelvin - 273;
    fahrenheit = celsius * 9 / 5 + 32;
    return (celsius, fahrenheit)

(c,f) = calculate_temperatures(340);
print("celsius:",c);
print("fahrenheit",f);
