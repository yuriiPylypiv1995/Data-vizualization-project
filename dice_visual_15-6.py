# task 15-6, 15-9

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create the die objects
die_1 = Die(8)
die_2 = Die(8)

# Make the several trows and save the results to the list
results = [die_1.roll() + die_2.roll() for roll_num in range(10)]

# Analise the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D8 and a D8 dies 10 times', xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d8.html')