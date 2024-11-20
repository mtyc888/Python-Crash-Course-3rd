from die import Die
import plotly.express as pt

#create both die
die_1 = Die()
die_2 = Die()

#roll those dices
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#analyze
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_result = range(2, max_result+1)
for value in poss_result:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize
title = "Results of multiplying instead of adding"
labels = {"x":"Results", "y":"Frequencies of the results"}
fig = pt.bar(x=poss_result, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html('multiply.html', auto_open = True)