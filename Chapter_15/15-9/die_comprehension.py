import plotly.express as pt
from die import Die

die_1 = Die()
die_2 = Die(10)

#comprehension (shortcut)
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

#analyze

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+1)

#comprehension (shortcut)
frequencies = [results.count(value) for value in poss_results]

#visualize
title = "Rolling D6 and D10"
labels = {'x':'Results', 'y':'Frequencies of Results'}
fig = pt.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.write_html("D6D10.html", auto_open=True)
