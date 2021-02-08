from game import game
from addBoats import addBoats
from setGameBoard import setGameBoard
from gameDifficulty import gameDifficulty

def main():
    gameMode = gameDifficulty('hard')
    gameBoard = setGameBoard(gameMode.getSize())
    userBoard = gameBoard.returnBoard()
    
    boats = addBoats(gameMode, gameBoard)
    
    newGame = game(gameBoard, boats)


    print(boats.returnBoatBoard())
    
   
main()