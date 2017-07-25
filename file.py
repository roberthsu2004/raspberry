a = 123
b = 12.34
c = "hello"
d = 'Hello'
e = True

print(a);
print(b);
print(c);
print(d);
print(e);

>>> x = input("Enter Value:")
Enter Value:23
>>> print(x)
23
>>> tempc = input("Enter temp in C:")
Enter temp in C:20
>>> tempF = (int(tempC) * 9) / 5 + 32
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tempF = (int(tempC) * 9) / 5 + 32
NameError: name 'tempC' is not defined
>>> tempF = (int(tempc) * 9) /5 + 32
>>> print(tempF);
68.0
>>> 
