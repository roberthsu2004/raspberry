empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Jerry', 'Terry', 'Terry', 'Michael']
print(weekdays)
print(type(weekdays))

another_empty_list = list()
print(another_empty_list)

cat_list = list('cat')
print(cat_list)

a_tuple = ('ready', 'fire', 'aim')
print(a_tuple)
print(type(a_tuple))

birthday = '1/3/1978'
print(type(birthday))
birthday_list = birthday.split('/')
print(birthday_list)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
#print(marxes[3])

marxes[2] = 'Wanda'
print(marxes)

print(marxes[0:2])
print(marxes[::2])
print(marxes[::-1])
print(marxes[1:])

marxes.append('zeppo')
print(marxes)
marxes += ['Cummo', 'Karl']
print(marxes)
marxes.insert(3, 'Gummo')
print(marxes)

del marxes[-1];
print(marxes)

