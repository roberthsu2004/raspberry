change_local():
    global animal,car    
    animal = 'wombat'
    car = 'fort'
    print('locals',locals());

if __name__ == '__main__':
    animal = 'fruitbat'
    car = 'fort'
    change_local();
    print('global',globals());


