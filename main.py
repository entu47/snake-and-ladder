
'''Develop a Snakes and Ladders game. The game development should focus on below key points: -
1. This is standard snakes and ladders game with following key entities
a. Board
b. Dice
c. Snake
d. Ladder
2. The game should support min. of 2 players
3. It should focus more on class designs and how the interaction between the classes will 
happen
4. No user interface is required, the game can be demonstrated using console
5. Application should be configurable to allow different snakes and ladders configuration
'''

from PlayGame import PlayGame
if __name__ == '__main__':
    play = PlayGame()
    play.play()


