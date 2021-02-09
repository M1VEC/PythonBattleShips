from game import game
from addBoats import addBoats
from setBoard import setBoard
from gameSettings import gameSettings
import userInteraction

def main():
    gamesetting = gameSettings()
    gamesetting.setMode(userInteraction.gameMode())

    board = setBoard(gamesetting.getSize())
    boats = addBoats(gamesetting, board)

    newGame = game(board, boats)
    print(board.getUserBoard())

    for num in range(1,5):
        userGuess = userInteraction.getUserGuess()
        newGame.runGame(userGuess)
        print(board.getUserBoard())

    print("Game Over")
    print(board.getGameBoard())

    #gameSetting.getTotalBoatHit() returns total amount of hits available 
    #need to check if any boats are left or count down how many are left
    #need to keep track of shots taken
    #maybe add hit to miss ratio or accuracy percentage
main()