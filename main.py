from game import game
from addBoats import addBoats
from setBoard import setBoard
from gameSettings import gameSettings
from scoreBoard import scoreBoard
import userInteraction

def main():
    gameSetting = gameSettings()
    gameSetting.setMode(userInteraction.gameMode())
    board = setBoard(gameSetting)
    boats = addBoats(gameSetting, board)

    newGame = game(board, boats)
    userInteraction.printPrompt(board.getUserBoard())
    scoreTally = scoreBoard(gameSetting)
    
    for num in range(0,gameSetting.getmaxShots()):
        userGuess = userInteraction.getUserGuess()
        shotResult = newGame.runGame(userGuess)
        scoreTally.userShot(shotResult)
        userInteraction.printPrompt(board.getUserBoard())
        if scoreTally.getTotalHits() == scoreTally.getAvailableHits():
            break
        
    userInteraction.printPrompt("Game Over")
    userInteraction.printPrompt(board.getGameBoard())
    userInteraction.printScoreTally(scoreTally)
    
main()
