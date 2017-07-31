Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> l = ["abc", "def", "ghi", "ijk"]
>>> [x.upper() for x in l]
['ABC', 'DEF', 'GHI', 'IJK']
>>> phone_numbers = {"Simon":"01234 56789","Jane":"0123 98765"};
>>> phone_numbers
{'Simon': '01234 56789', 'Jane': '0123 98765'}
>>> phone_numbers["Simon"]
'01234 56789'
>>> phone_numbers["jane"]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    phone_numbers["jane"]
KeyError: 'jane'
>>> phone_numbers["]
	      
SyntaxError: EOL while scanning string literal
>>> phone_numbers["Jane"]
'0123 98765'
>>> a = {'key1':'value1','key2':'value2'}
>>> b = {'b_key1':a}
>>> n
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> b
{'b_key1': {'key2': 'value2', 'key1': 'value1'}}
>>> phone_numbers["robert"] = "0987654321"
>>> phone_numbers
{'Simon': '01234 56789', 'Jane': '0123 98765', 'robert': '0987654321'}
>>> phone_numbers.pop("Jane")
'0123 98765'
>>> phone_numbers
{'Simon': '01234 56789', 'robert': '0987654321'}
>>> for name in phone_numbers
SyntaxError: invalid syntax
>>> for name in phone_numbers:
	print(name);

	
Simon
robert
>>> for name,num in phone_numbers.items():
	print(name + " " + num);

	
Simon 01234 56789
robert 0987654321
>>> 
