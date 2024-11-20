import plotly.express as pt
from die import Die

#Create 2 D8's
die_1 = Die(8)
die_2 = Die(8)

#roll those dices
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize
title = "Results of Rolling two D8's"
labels = {'x':'Results', 'y':'Frequency of Results'}

fig = pt.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

fig.write_html('Rolling_Two_D8.html', auto_open=True)