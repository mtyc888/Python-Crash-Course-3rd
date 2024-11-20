sandwich_orders = ['tuna', 'veggie', 'grilled cheese', 'turkey', 'steak']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwitch.")
    finished_sandwich.append(current_sandwich)

print('\n')

for sandwich in finished_sandwich:
    print(f"I made a {sandwich} sandwich")

