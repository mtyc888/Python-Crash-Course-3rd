from die import Die
import plotly.express as px
#create the die
die = Die()

#roll the die a few times
results = []

for result in range(1000):
    result = die.roll()
    results.append(result)

#analyze the data
frequencies = []
poss_reults = range(1,die.num_sides+1)
for value in poss_reults:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
title = "Results of Rolling One D6 Die 1000 Times"
labels = {'x': 'Results', 'y':'Frequencies of the results'}
fig = px.bar(x=poss_reults, y=frequencies, title=title, labels=labels)
fig.write_html('die_frequency.html', auto_open=True)