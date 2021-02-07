from setGameBoard import setGameBoard
from gameDifficulty import gameDifficulty
from boat import boat

def main():

    gameMode = gameDifficulty('normal')
    boardSize = gameMode.getSize()
  
    gameBoard = setGameBoard(boardSize)
    gameBoard.createBoard()

    boatLength = 3
    addBoat = boat(boardSize, boatLength, gameBoard.returnBoard())
    addBoat.addStartingPoint()

  
    

main()