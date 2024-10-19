dinner_guests = ['Joker', 'Gypsy Crusader', 'Hitler']

length = len(dinner_guests)

print(f"total initial guests{length}")

print("Oh no, Hitler can't make it")

guest_1 = "Hitler"

dinner_guests.remove(guest_1)

print("Inviting King Lionheart instead")

new_guest = "King Lionheart"

dinner_guests.append(new_guest)

for dinner_guest in dinner_guests:
    print(f"Welcome to my dinner party {dinner_guest}")

print("I have found a bigger table! Inviting 3 more new guests")

# adding at the start of the list
dinner_guests.insert(0, 'Marvin')

# adding at the middle of the list
dinner_guests.insert(2, 'Max')

# adding at the end of the list
dinner_guests.append('Reuben')

print("Welcome our new guests!")

for dinner_guest in dinner_guests:
    print(f"Welcome to my dinner party {dinner_guest}")

print("Oops sorry, the boss said only 2 guests are allowed on the table tonight")

# Keep removing guests until only 2 remain
while len(dinner_guests) > 2:
    leaving_guest = dinner_guests.pop()
    print(f'Sorry it had to be you {leaving_guest}')

for dinner_guest in dinner_guests:
    print(f"Welcome for the finalized guests Mr {dinner_guest}")

del dinner_guests[0]
del dinner_guests[0]

print(f"anybody here? {dinner_guests}")

