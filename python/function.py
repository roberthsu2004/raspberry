def do_nothing():
    print("do_nothing")

def echo(anything):
    return anything + ' ' + anything

def commentary(color):
    if color == 'red':
        return "It's a tomato"
    elif color == "green":
        return "It's a green pepper."
    elif color == "bee purple":
        return " I don't know what"
    else:
        return "I've never heard of the color " + color + "."
    
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}

    
do_nothing();
print(echo('Rumplestiltskin'))
print(commentary("vilot"));
print(menu('chardonnay','chicken','cake'));

