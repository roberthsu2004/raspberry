def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon');

#docsString

def echo(anything):
    ' echo returns its input argument'
    return anything

print(echo.__doc__)