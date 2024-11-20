fav_num = {
    'p1':[1,2],
    'p2':[3,4],
    'p3':[5,6],
    'p4':[7,8],
    'p5':[9,10]
}

for name, number in fav_num.items():
    print(f"{name}'s favourite number is:")
    for num in number:
        print(f'{num}')