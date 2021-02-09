from game import game
from addBoats import addBoats
from setGameBoard import setGameBoard
from gameDifficulty import gameDifficulty
import userInput

def main():
    gameMode = gameDifficulty('normal')
    board = setGameBoard(gameMode.getSize())
    boats = addBoats(gameMode, board)

    newGame = game(board, boats)
    print(board.getUserBoard())

    for num in range(1,5):
        userGuess = userInput.getUserGuess()
        print(newGame.runGame(userGuess)) 
        print(board.getUserBoard())

    print("Game Board")
    print(board.getGameBoard())

    #need to check if any boats are left or count down how many are left
    #need to keep track of shots taken
    #maybe add hit to miss ratio or accuracy percentage
main()