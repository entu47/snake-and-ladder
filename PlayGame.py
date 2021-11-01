from Dice import Dice
import time
from PlayerDetails import PlayerDetails
from Validate import Validate
from Move import Move

#This is Playgame class which is Inherited by Dice, Move , Validate, PlayerDetails class.
#This class will be used to play the game by using other class which are inherited.



class PlayGame(Dice, Move, Validate, PlayerDetails):
    #This function is used to play the game
    def play(self):
        name = PlayerDetails() #Created the object of PlayerDetails Class
        playerName1 = name.getDetails() #Called the getDetails method from PlayerDetails class for player1
        playerName2 = name.getDetails() #Called the getDetails method from PlayerDetails class for player2
        ob = Dice() #Created the object of Dice Class
        move = Move() #Created the object of Move Class
        valid = Validate() #Created the object of Validate Class
        position1 = 0 #Intilize the Position for player1
        position2 = 0 #Intilize the Position for player2
        while True:
            input1 = input("Hey {} press enter to play".format(playerName1)) #Taking Input from User To play the game
            print("-------------------------------------------")
            print("Player {} position is: {}".format(playerName1, position1)) #Printing the name and Initial position for player1

            value = ob.dice() #Calling the dice method 
            print("Roling dice.........")
            time.sleep(1) #to delay some time in output
            print("Dice value is:", value) #printing the Value of dice
            position1 = move.getposition(position1, value) #Setting the new positing a/c to dice value
            print("Position of player {} is: {}".format(playerName1, position1))#Printing the name and Next position for player1

            #this will check the winner and if you won then this will break the loop
            if valid.checkWin(position1):
                break
            position1 = valid.validateMove(position1, value) #This will check if move is valid or not

            input2 = input("Hey {} hit enter to play".format(playerName2))#Taking Input from User To play the game
            print("-------------------------------------------")
            print("Player {} position is: {}".format(playerName2, position2))#Printing the name and Initial position for player2
            value1 = ob.dice() #Calling the dice method
            print("Roling dice.........")
            time.sleep(1)#to delay some time in output
            print("Dice value is:", value1)#printing the Value of dice
            position2 = move.getposition(position2, value1)#Setting the new positing a/c to dice value
            print("Position of player {} is: {}".format(playerName2, position2))#Printing the name and Next position for player2

            #this will check the winner and if you won then this will break the loop
            if valid.checkWin(position2):
                break
            position2 = valid.validateMove(position2, value1) #This will check if move is valid or not

