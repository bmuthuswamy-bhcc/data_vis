from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []
num_rolls = 10000
for roll_num in range(num_rolls):
	result = die.roll()
	results.append(result)

# Analyze the results
# count how many times we roll each number
x_values = list(range(1, die.num_sides+1))
frequencies = []
for value in x_values:
	frequency = results.count(value)
	frequencies.append(frequency)

data = [Bar(x=x_values, y=frequencies)] # have a bar for each of the possible results

x_axis_config = {'title' : 'Die Roll'}
y_axis_config = {'title' : 'Frequency of Die Roll'}

my_layout = Layout(title='Results of rolling one six-sided die ' + str(num_rolls) + ' times',
	xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data' : data, 'layout' : my_layout},filename='d6.html')

