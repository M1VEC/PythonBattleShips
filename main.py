from addBoats import addBoats
from setGameBoard import setGameBoard
from gameDifficulty import gameDifficulty

def main():
    gameMode = gameDifficulty('normal')
    gameBoard = setGameBoard(gameMode.getSize())
    boats = addBoats(gameMode, gameBoard)
    
    
    print(boats.returnBoatBoard())
    
   
main()