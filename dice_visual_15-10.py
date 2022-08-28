# task 15-10, part 1: die roll simulation with Matplotlib library
# Matplotlib color's scheme: https://matplotlib.org/stable/gallery/color/named_colors.html

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

from die import Die

# Create the die objects
die_1 = Die(6)
die_2 = Die(6)

# Make the several trows and save the results to the list
results = [die_1.roll() + die_2.roll() for roll_num in range(10)]

# Analise the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
x_values = list(range(2, max_result+1))

plt.style.use('grayscale')
fig, ax = plt.subplots()
ax.bar(x_values, frequencies, color='coral')

# Set the graph title and the same for 'x' and 'y' lines
ax.set_title("Results of rolling a D6 and a D6 dies 10 times", fontsize=24, color='maroon')
ax.set_xlabel("Result", fontsize=14, color='maroon')
ax.set_ylabel("Frequency of result", fontsize=14, color='maroon')

# Set ranges for x and y axis
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(1)
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

# Set the font size for the signatures
ax.tick_params(axis='both', labelsize=14, colors='firebrick')

plt.show()