dinner_guests = ['Joker', 'Gypsy Crusader', 'Hitler']
print("Oh no, Hitler can't make it")

guest_1 = "Hitler"

dinner_guests.remove(guest_1)

print("Inviting King Lionheart instead")

new_guest = "King Lionheart"

dinner_guests.append(new_guest)

for dinner_guest in dinner_guests:
    print(f"Welcome to my dinner party {dinner_guest}")

print("I have found a bigger table! Inviting 3 more new guest")

#adding at the start of the list
dinner_guests.insert(0,'Marvin')

#adding at the middle of the list
dinner_guests.insert(2,'Max')

#adding at the end of the list
dinner_guests.append('Reuben')

print("Welcome our new guests!")

for dinner_guest in dinner_guests:
    print(f"Welcome to my dinner party {dinner_guest}")