from Board import Board
import time
from random import randint


#This is class for snake in which we have inherited Board class
#This will return the position after bitten by the snake
class Snake(Board):

    def snake(self, pos):
        obj = Board()
        msg =["Oops! You Bitten By Snake ~~~~~~~>","Shiiii Snake Bite you~~~~>","Shitt This Snake yaar ~~~~~>","dang~~~~>"]
        if pos in obj.snake:
            pos = obj.snake[pos]
            print(msg[randint(0,3)])
            time.sleep(1)
        return pos
