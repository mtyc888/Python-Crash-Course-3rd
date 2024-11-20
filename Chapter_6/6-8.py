pets = []
pet = {
    'owner':'george',
    'breed':'husky',
    'age':1,
    'weight': 43,
}
pets.append(pet)
pet = {
    'owner':'timmy',
    'breed':'shepard',
    'age':2,
    'weight': 53,
}
pets.append(pet)

for pet in pets:
    owner = pet['owner']
    breed = pet['breed']
    age = pet['age']
    weight = pet['weight']
    print(f"this pet is owned by {owner} it is a {breed} {age} years old and weights {weight} kg")