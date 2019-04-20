animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print('at the top level:',animal)
print_global()


def change_and_print_local():
    animal = 'wombat'
    print('inside change_and_print_local:',animal);    
    print('after the change:', animal)

change_and_print_local();

def change_global_animal():
    global animal;
    animal = 'fruitbatBit'
    print('change_global_animal:', animal)

change_global_animal();
