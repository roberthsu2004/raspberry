>>> s = "name\tage\nMatt\t14"
>>> print(s)
name	age
Matt	14
>>> s1 = "abc";
>>> s2 = "def"
>>> s = s1 + s2
>>> print(s)
abcdef
>>> s1 + 12
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s1 + 12
TypeError: Can't convert 'int' object to str implicitly
>>> "123" + 123
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    "123" + 123
TypeError: Can't convert 'int' object to str implicitly
>>> int("123") + 123
246
>>> 
