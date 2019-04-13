def menu(wine, entree, dessert='pudding'):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}

print(menu('chardonnay','chicken'))
print(menu('chardonnay','chicken',dessert='doughnut'))

