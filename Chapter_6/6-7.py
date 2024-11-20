people = []
person = {
    'firstname': 'marvin',
    'lastname' : 'tan',
    'age':'25',
    'city':'penang'
}
people.append(person)
person = {
    'firstname': 'lemmy',
    'lastname': 'matts',
    'age':2,
    'city':'sitka',
}
people.append(person)

for person in people:
    name = f'{person['firstname']} {person['lastname']}'
    age = person['age']
    city = person['city']

    print(f'{name} is {age} years old and from {city}')