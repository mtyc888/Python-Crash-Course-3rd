import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
cubes = [1,8,27,64,125]

input_values_2 = range(1,5001)
cubes_2 = [input**3 for input in input_values_2]

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()

ax.scatter(input_values_2, cubes_2, c=cubes_2, cmap=plt.cm.Blues, s=10)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Numbers", fontsize=24)
ax.set_ylabel("Cube of Numbers", fontsize=24)

plt.show()