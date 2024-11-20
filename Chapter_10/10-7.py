print('type quit to quit')
while True:
    try:
        x = input("Give me a number")
        if x == 'quit':
            break
        x = int(x)

        y = input("Give me another number")
        if y == 'quit':
            break
        y = int(y)



    except ValueError:
        print("Numbers only")
    else:

        z = x + y

        print(f"Result: {z}")