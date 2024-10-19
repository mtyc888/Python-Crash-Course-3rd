usernames = ['admin','b','c','d','e']

for name in usernames:
    if name != 'admin':
        print(f'hello {name}')
    else:
        print(f'hello {name}, would you like to view status report')