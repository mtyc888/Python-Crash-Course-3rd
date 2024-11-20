string = 'apple'

string2 = string.upper()

print(string == string2)

string2 = string.title()

print(string == string2)

check = 2
if check > 2 or check > 1:
    print('true')
else:
    print('false')

check = 2
if check > 2 and check > 1:
    print('true')
else:
    print('false')


list = ['a', 'b', 'c']

check = 'a' in list
print('is it in the list? ',check)

check = 'f' in list
print('is it in the list? ',check)