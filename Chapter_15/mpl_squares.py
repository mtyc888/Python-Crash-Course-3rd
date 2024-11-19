import matplotlib.pyplot as plt

#create a list of squares as data for our plot
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

#styling
plt.style.use('Solarize_Light2')

#declare the plotting function
fig, ax = plt.subplots()
#plot the data, linewidth controls the thickness of the line
#input_values will be the x axis and squares be the y axis
ax.plot(input_values,squares, linewidth=3)

#Set chart ttle and label x and y axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square Of Value", fontsize=24)

#set size of tick labels.
ax.tick_params(labelsize=24)

#this opens matplotlib's viewer
plt.show()