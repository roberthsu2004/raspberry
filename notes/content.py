>>> s = "It was the best of X. It was the worst of X"
>>> s.replace("X","times");
'It was the best of times. It was the worst of times'
>>> "aBcDe".upper()
'ABCDE'
>>> "aBcDe".lower();
'abcde'
>>> x = 101
>>> if x > 100:
	print("x is big");
	print("y is big");

x is big
y is big
>>> x = 101'
SyntaxError: EOL while scanning string literal
>>> x = 101
>>> if x > 100:
	print("x is big");
else:
	print("x is small");

x is big
>>> 
>>> x = 90
>>> if x > 100:
	print("x is big");
elif x < 10:
	print("x is small");
else:
	print("x is medium");
