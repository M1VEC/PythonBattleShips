from game import game
from addBoats import addBoats
from setBoard import setBoard
from gameSettings import gameSettings
from scoreBoard import scoreBoard
import userInteraction

def main():
    gameSetting = gameSettings()
    gameSetting.setMode(userInteraction.gameMode())
    boardSize = gameSetting.getSize()
    board = setBoard(boardSize)
    
    boats = addBoats(gameSetting, board)
    newGame = game(board, boats)
    userInteraction.printPrompt(board.getUserBoard())
    scoreTally = scoreBoard(gameSetting)
    
    for num in range(0,gameSetting.getmaxShots()):
        userGuess = userInteraction.getUserGuess(boardSize)
        if userGuess[0] == 0 or userGuess[1] == 0:
            break
        shotResult = newGame.runGame(userGuess)
        scoreTally.userShot(shotResult)
        userInteraction.printPrompt(board.getUserBoard())
        if scoreTally.getTotalHits() == scoreTally.getAvailableHits():
            break
        
    userInteraction.printScoreTally(scoreTally, board)
    
main()
