pizzas = ['Pepperoni', 'Alfredo', 'Deep Dish']
friends_pizza = pizzas[:]
friends_pizza.append('Chicken')

print('mine')

for pizza in pizzas:
    print(pizza)

print('friends')

for pizza in friends_pizza:
    print(pizza)