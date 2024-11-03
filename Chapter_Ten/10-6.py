try:
    x = input("Give me a number")
    x = int(x)

    y = input("Give me another number")
    y = int(y)



except ValueError:
    print("Numbers only")
else:

    z = x + y

    print(f"Result: {z}")