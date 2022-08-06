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
        fig, ax = plt.subplots()
        ax.scatter(rw.x_values, rw.y_values, s=15)

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

