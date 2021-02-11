from game import game
from gameSettings import gameSettings
from scoreBoard import scoreBoard
import userInteraction

def main():
    gameSetting = gameSettings()
    gameSetting.setMode(userInteraction.gameMode())
    boardSize = gameSetting.getSize()
    
    newGame = game(gameSetting)
    userInteraction.printPrompt(gameSetting.getUserBoard())
    scoreTally = scoreBoard(gameSetting)
    
    for num in range(0,gameSetting.getmaxShots()):
        userGuess = userInteraction.getUserGuess(boardSize)
        if userGuess[0] == 0 or userGuess[1] == 0:
            break
        shotResult = newGame.runGame(userGuess)
        scoreTally.userShot(shotResult)
        userInteraction.printPrompt(gameSetting.getUserBoard())
        if scoreTally.getTotalHits() == scoreTally.getAvailableHits():
            break
        
    userInteraction.printScoreTally(scoreTally, gameSetting)
    
main()
