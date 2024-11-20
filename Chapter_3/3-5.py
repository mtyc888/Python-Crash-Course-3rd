dinner_guests = ['Joker', 'Gypsy Crusader', 'Hitler']
print("Oh no, Hitler can't make it")

guest_1 = "Hitler"

dinner_guests.remove(guest_1)

print("Inviting King Lionheart instead")

new_guest = "King Lionheart"

dinner_guests.append(new_guest)

for dinner_guest in dinner_guests:
    print(f"Welcome to my dinner party {dinner_guest}")