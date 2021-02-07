from setGameBoard import setGameBoard
from gameDifficulty import gameDifficulty
from boat import boat

def main():

    gameMode = gameDifficulty('normal')
    boardSize = gameMode.getSize()
    
    gameBoard = setGameBoard(boardSize)
    gameBoard.createBoard()

    boatLength = 5
    addBoat = boat(boardSize, boatLength, gameBoard.returnBoard())
    addBoat.addStartingPoint()

    boatLength = 3
    addBoat1 = boat(boardSize, boatLength, addBoat.returnBoatBoard())
    addBoat1.addStartingPoint()
    print(addBoat1.returnBoatBoard())    
    

main()