import plotly.express as px
from die import Die

#Create the dices
die_1 = Die()
die_2 = Die(10)

#Make some rolls
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the result
title = "Results of Rolling a D6 and a D10 50000 times"
labels = {'x':'Results', 'y':'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html('D6D10.html', auto_open =True)