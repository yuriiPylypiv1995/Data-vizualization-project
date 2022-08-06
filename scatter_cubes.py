# tasks 15.1 and 15.2

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.spring, s=10)

# Set the graph title and the same for 'x' and 'y' lines
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

# Set the font size for the signatures
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for 'x' and 'y' axis
# ax.axis([0, 1100, 0, 1100000])

plt.show()