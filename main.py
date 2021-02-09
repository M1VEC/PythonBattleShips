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
        newGame.runGame(guess)
        guessAgain = [2, 10 -num]
        newGame.runGame(guessAgain)


    print(board.getUserBoard())
main()