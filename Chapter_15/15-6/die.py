from random import randint

class Die:
    """A class representing a single Die"""

    def __init__(self, num_sides=6):
        """Assuming a 6 sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value per call between 1 and number of sides"""
        return randint(1, self.num_sides)