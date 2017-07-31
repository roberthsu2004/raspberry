Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import copy
>>> a = ['it','was','the','best','of','times']
>>> b=copy.copy(a)
>>> b.sort();
>>> a
['it', 'was', 'the', 'best', 'of', 'times']
>>> b
['best', 'it', 'of', 'the', 'times', 'was']
>>> 
>>> l = ['a','b','c','d'];
>>> l[1:3]
['b', 'c']
>>> l[;3]
SyntaxError: invalid syntax
>>> l[:3]
['a', 'b', 'c']
>>> l[3:]
['d']
>>> l[-2:]
['c', 'd']
>>> 
