from game import game
from addBoats import addBoats
from setGameBoard import setGameBoard
from gameDifficulty import gameDifficulty
from userInput import userInput

def main():
    userInput 
    gameMode = gameDifficulty('hard')
    board = setGameBoard(gameMode.getSize())
    
    boats = addBoats(gameMode, board)
    guess = [5,4]
    newGame = game(board, boats, guess)

    print(board.getGameBoard())
    print(board.getUserBoard())
    
    
   
main()