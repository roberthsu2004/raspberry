letters = 'abcdefghijklmnopqrstuvwxyz';
print(letters[0]);
print(letters[-1]);
#print(letters[100]);
#letters[0] = 'c'

name = 'Henny';
name = name.replace('H','P')
print(name);

print(letters[:]);
print(letters[20:]);
print(letters[10:]);
print(letters[12:15]);
print(letters[-3:]);
print(letters[4:20:3]);

print(len(letters))
todos = 'get gloves, get mask, give cat vitamins, call ambulance'
dos = todos.split(',');
print(dos);
print(todos.find('cat'));
