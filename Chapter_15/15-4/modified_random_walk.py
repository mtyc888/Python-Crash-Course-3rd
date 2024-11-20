import matplotlib.pyplot as plt

from random_walk import RandomWalk
#Keep making new walks, as long as the program is active
while True:
    #make a random walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    #we use range to generate a list of numbers equal to the number of points in the walks
    #this shows how the walk moves from it's starting point to it's ending point
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #removing the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #here we use set_aspect() method to specify that both axes should have equal spacing between tick marks
    ax.set_aspect('equal')

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break

