from random import randint

class Die:
    """This method represents the one game die with 6 sides"""

    def __init__(self, num_sides=6):
        """The game die definition"""
        self.num_sides = num_sides

    def roll(self):
        """Roll the die. Result is a number between 1 and 6"""
        return randint(1, self.num_sides)
