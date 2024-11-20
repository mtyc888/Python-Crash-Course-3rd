prompt = "\n What is your age?"
prompt = "\n Enter 'quit' to exit"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Ticket is free')
    elif age > 3 and age < 12:
        print('Ticket will be $10')
    elif age > 12:
        print('Ticket will be $15')
     