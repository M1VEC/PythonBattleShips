import numpy as np
from pandas import *
from gameBoard import gameBoard
from gameDifficulty import gameDifficulty

def main():

    gameMode = gameDifficulty('hard')

    boardSize = gameMode.getSize()
    
    game = gameBoard(boardSize)
    game.createBoard()
    
    game.insertShip(2, 2)
    game.labelAxis()
    
    print(game.returnBoard())

main()