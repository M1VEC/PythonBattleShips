from game import game
from addBoats import addBoats
from setBoard import setBoard
from gameSettings import gameSettings
import userInteraction

def main():
    gamesetting = gameSettings()
    gamesetting.setMode('normal')
    
    board = setBoard(gamesetting.getSize())
    boats = addBoats(gamesetting, board)

    newGame = game(board, boats)
    print(board.getUserBoard())

    for num in range(1,5):
        userGuess = userInteraction.getUserGuess()
        print(newGame.runGame(userGuess)) 
        print(board.getUserBoard())

    print("Game Board")
    print(board.getGameBoard())

    #need to check if any boats are left or count down how many are left
    #need to keep track of shots taken
    #maybe add hit to miss ratio or accuracy percentage
main()