import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make a random walk
rw = RandomWalk()
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()

ax.scatter(rw.x_value, rw.y_value, s=15)
#here we use set_aspect() method to specify that both axes should have equal spacing between tick marks
ax.set_aspect('equal')

plt.show()