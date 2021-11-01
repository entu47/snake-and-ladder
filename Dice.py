import random

#This is Class for Dice
#This will return some random value
class Dice:
    def dice(self):
        value = random.randint(1,6)
        return value 