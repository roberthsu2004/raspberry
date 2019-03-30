furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("skink")
    else:
        print("human")

count = 1
while count <= 5:
    print(count)
    count += 1;
    
while True:
    stuff = input("String to capitalize [type q to quit]")
    if stuff == 'q':
        break;
    print(stuff.capitalize());
    
while True:
    value = input("Integer, please [q to quit]")
    if value == 'q':
        break;
    
    number = int(value)
    
    if number % 2 == 0:
        continue
    
    print(number, "squared is", number*number);
    
    