def print_args(*args):
    print('Positional argument tuple:',args)

print_args()
print_args(3,2,1,'wait!','uh...')


def print_more(required1,required2,*args):
    print('need this one:',required1)
    print('need this one too:',required2)
    print('all the rest:',args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')


def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon');

#docsString

def echo(anything):
    ' echo returns its input argument'
    return anything

print(echo.__doc__)
