import matplotlib.pyplot as plt

x_value = range(1,1001)
y_value = [x**2 for x in x_value]

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()

#plotting a single point
#color the lower y_values light blue and the points with higher y_values darker blue
ax.scatter(x_value,y_value, c=y_value, cmap=plt.cm.Blues, s=10)

#Set chart title and label axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Numbers", fontsize=24)
ax.set_ylabel("Square of Numbers", fontsize=24)

#set the range for each axis.
#minimum and maximum for both x and y axis, so 4 numbers
ax.axis([0,1100,0,1_100_000])
#ticklabel_format() allows us to overide the default tick label styles for any plot
ax.ticklabel_format(style='plain')

#set size of tick labels
ax.tick_params(labelsize=14)
#saving your plots
#first arguement is the filename
#second arguement trims extra whitespaces from the plot
plt.savefig('squares_plot.png', bbox_inches='tight')
