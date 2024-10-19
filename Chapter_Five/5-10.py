current = ['a','b','c','d','e']
new = ['f','g','h','a','r']

currentList = []
newList = []

for user in current:
    currentList.append(user.lower())

for user in new:
    newList.append(user.lower())

for user in currentList:
    if user in newList:
        print(f'{user} please change your name, it has been taken')
    else:
        print(f'{user} welcome')