number = input('how many guest?')
number = int(number)
if number > 8:
    print(f"{number} is too much, please wait for another table")
else:
    print(f"Table for {number} coming right up!")