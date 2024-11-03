from random import choice

possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

winning_tickets = []

print("Let's see what the winning ticket is")

while len(winning_tickets) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_tickets:
        print(f"We pulled a {pulled_item}")
        winning_tickets.append(pulled_item)

print(f"The final winning ticket is: {winning_tickets}")