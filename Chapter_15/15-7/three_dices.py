from die import Die
import plotly.express as pt

#Create 3 D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

#roll those dices
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#analyze
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+2)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize
title = "Rolling 3 D6"
labels = {'x': 'Results', 'y':'Frequency of Results'}

fig = pt.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html('3_D6.html', auto_open=True)