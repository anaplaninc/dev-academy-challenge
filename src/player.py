import random


class Player:
    """ Basic player class holding score """
    held_score = 0
    unheld_score = 0

    def __init__(self, name):
        self.name = name

    def roll(self):
        """ Rolls dice. Stores rolled value if not 1, returns value """
        unheld_temp = random.randint(1, 6)
        if unheld_temp == 1:
            return unheld_temp
        self.unheld_score += unheld_temp
        return unheld_temp

    def hold(self):
        """ Adds current held score to player totals """
        self.held_score += self.unheld_score
        self.unheld_score = 0
