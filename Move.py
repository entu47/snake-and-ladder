
from Snake import Snake
from ladder import Ladder
import time

#This is the move class which is Inherited by Snake and ladder class
#This will return the Final position on the board , After bitten by snake or Climbed by ladder, or Normal move

class Move(Snake,Ladder):

    def getposition(self,pos,value):
        sn = Snake()
        ld = Ladder()
        pos += value
        print("Your Position is {}".format(pos))
        pos = sn.snake(pos)
        pos = ld.ladder(pos)
        time.sleep(1)
        return pos