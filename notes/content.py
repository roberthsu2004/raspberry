Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=[34,'Fred',12,False,72.3]
>>> a[1]
'Fred'
>>> a[1] = 777
>>> a
[34, 777, 12, False, 72.3]
>>> a[50] = 777
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[50] = 777
IndexError: list assignment index out of range
>>> len(a);
5
>>> a.append("new");
>>> a
[34, 777, 12, False, 72.3, 'new']
>>> a.insert(2,"new2")
>>> a
[34, 777, 'new2', 12, False, 72.3, 'new']
>>> a = [34, 'Fred', 12, False, 72.3];
>>> b = [74, 75]
>>> a.extend(b);
>>> a
[34, 'Fred', 12, False, 72.3, 74, 75]
>>> a.pop();
75
>>> a
[34, 'Fred', 12, False, 72.3, 74]
>>> a.pop(0);
34
>>> a
['Fred', 12, False, 72.3, 74]
>>> "abc def ghi".split()
['abc', 'def', 'ghi']
>>> "abc--de--ghi".split('--')
['abc', 'de', 'ghi']
>>> 
>>> a = [34, 'Fred', 12, False, 72.3]
>>> for x in a:
	print(x)

	
34
Fred
12
False
72.3
>>> for (i,x) in enumerate(a):
	print(i,x);

	
0 34
1 Fred
2 12
3 False
4 72.3
>>> 
