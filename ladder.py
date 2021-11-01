from random import randint
from Board import Board

#This is class for ladder in which we have inherited Board class
#This will return the position after climbed by ladder
class Ladder(Board):

    def ladder(self, pos):
        obj = Board()
        msg =["Yay Got a ladder ####","Yahoooo ## I am climbing","#### Coming up by ladder"]
        if pos in obj.ladder:
            pos = obj.ladder[pos]
            print(msg[randint(0,2)])
        return pos
