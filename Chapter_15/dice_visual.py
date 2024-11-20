import plotly.express as px
from die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#Visualize the results
title = "Result of rolling Two 6 Sided Dices"
labels = {'x':'Frequencies of the results', 'y':'Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
#further customize chart
#set distance between x-axix to 1, so every bar on the x-axis is labelled
fig.update_layout(xaxis_dtick=1)
fig.write_html("dices_frequency.html", auto_open=True)
