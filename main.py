from game import game
from addBoats import addBoats
from setGameBoard import setGameBoard
from gameDifficulty import gameDifficulty
from userInput import userInput

def main():
    userInput 
    gameMode = gameDifficulty('normal')
    board = setGameBoard(gameMode.getSize())
    boats = addBoats(gameMode, board)

    newGame = game(board, boats)

    for num in range(1,10):
        guess = [num, 5]
        print(newGame.runGame(guess))
        guessAgain = [2, 10 -num]
        print(newGame.runGame(guessAgain))

    print("Game Board")
    print(board.getGameBoard())
    #need to check if any boats are left or count down how many are left
    #need to keep track of shots taken
    #maybe add hit to miss ratio or accuracy percentage
main()