import numpy as np
from pandas import *
from gameBoard import gameBoard
from gameDifficulty import gameDifficulty
from addBoat import addBoat

def main():

    gameMode = gameDifficulty('normal')
    boardSize = gameMode.getSize()
    
    game = gameBoard(boardSize)
    game.createBoard()
    
    addBoats = addBoat(gameMode, game)
    addBoats.addAllShips()
    
    
    
    
    # print(game.returnCoOrdinateContents(4,7))    
    print(game.returnBoard())

main()