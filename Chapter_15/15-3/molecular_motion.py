import matplotlib.pyplot as plt

from pollen import Pollen
#Keep making new walks, as long as the program is active
while True:
    #make a random walk
    rw = Pollen(5000)
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    #we use range to generate a list of numbers equal to the number of points in the walks
    #this shows how the walk moves from it's starting point to it's ending point
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_value, rw.y_value, linewidth=1)

    #removing the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #here we use set_aspect() method to specify that both axes should have equal spacing between tick marks
    ax.set_aspect('equal')
    #emphasize starting point and last point
    ax.scatter(0,0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none')
    ax.set_title("Path of a pollen grain on the surface of a drop of water. Red(destination) Green(starting point)")
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break

