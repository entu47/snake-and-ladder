import time

#This class will Check the winner and validate the move
#This has two methos of winning and Validating Move
class Validate:
    #This method will check for Winner
    def checkWin(self, pos):
        if pos == 100:
            print("Yeeee, Congo..! You Won This Match!")
            return True
        else:
            return False
    #This method will check if the Move is valid or not
    def validateMove(self, pos, value):
        if pos > 100:
            pos -= value
            time.sleep(1)
            print("Cannot move! It's a invalid Move")
            time.sleep(2)
            print("Back to previous position {}".format(pos))
            return pos
        else:
            return pos
