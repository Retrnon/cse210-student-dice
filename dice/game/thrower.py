import random

class Thrower(object):
    
    def __init__(self):
        """
        Initializes object attributes
        """
        self.dice = []
        self.score = 0

    def throw_dice(self):
        """
        Clears previous Dice and throws Dice and randomizes 5d6 dice in self.dice
        """
        self.dice.clear()
        for x in range(5):
            self.dice.append(random.randint(1, 6))

    def get_points(self):
        """
        Counts instances of 5s and 1s and returns the sum
        """
        return (self.dice.count(5) * 50 + self.dice.count(1) * 100)

    def can_throw(self):
        """
        Checks and returns True if there are any instances of 1s ir 5s in self.dice
        """
        return any([die == 1 for die in self.dice]) or any([die == 5 for die in self.dice])
