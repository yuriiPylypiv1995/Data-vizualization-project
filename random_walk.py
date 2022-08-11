from random import choice

class RandowWalk:
    """This class generates points for the random walk"""

    def __init__(self, num_points=5000):
        """The attributes initialization"""
        self.num_points = num_points
        # The first coordinate is always 0, 0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all random walking points"""

        while len(self.x_values) < self.num_points:

            # Set point's steps on a diagram
            x_step = self.get_step()
            y_step = self.get_step()

            # Skip steps that do nothing
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new point's position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    @staticmethod
    def get_step():
        """This method calculate steps for 'x' and 'y' axis of diagrams"""

        # Choice direction and duration
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance

        return step