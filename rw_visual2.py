# task 15-3

import matplotlib.pyplot as plt

from random_walk import RandowWalk

show_graph = True

while True:

    if show_graph:
        # Create a random walk
        rw = RandowWalk()
        rw.fill_walk()

        # Create a random walk graph
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(12, 7))
        point_numbers = range(rw.num_points)
        ax.plot(rw.x_values, rw.y_values, linewidth=0.6, c='deepskyblue')
        # crs link: https://matplotlib.org/stable/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py

        # Hide the axis
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Repaint the first and the last points on the diagram
        ax.scatter(0, 0, c='green', edgecolor='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

        plt.show()

        keep_running = input("Generate a new one graph? (y/n) ")

    # Check keep running parameter
    if keep_running == 'n':
        break
    elif keep_running == 'y':
        show_graph = True
        continue
    else:
        keep_running = input("Incorrect symbols. Please type 'y' or 'n' only.\n Generate a new one graph? (y/n) ")
        show_graph = False