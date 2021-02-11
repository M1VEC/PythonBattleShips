def gameMode():
    modes = ("easy", "normal", "hard")
    printPrompt("Select difficulty:   easy     normal      hard")
    mode = input()
    if mode in modes:
        return mode
    else:
        return gameMode()

def getUserGuess(boardSize):
    userguess = [userGuess("Enter down co-ordinate: "), userGuess("Enter across co-ordinate: ")]
    if (userguess[0] < boardSize[0] and userguess[0] >= 0) and (userguess[1] < boardSize[1] and userguess[1] >= 0) :
        return userguess
    else:
        print("Both co-ordinates must be equal to or greater than 1 and less than " +str(boardSize[0]))
        return getUserGuess(boardSize)

def userGuess(prompt):
    return int(input(prompt))

def printPrompt(prompt):
    return print(prompt)

def printScoreTally(scoreTally, gameSetting):
    print("Game Over!")
    print(gameSetting.getGameBoard())
    if scoreTally.gettotalValidShots() > 0:
        print("Hits = " + str(scoreTally.getTotalHits()))
        print("Miss = " + str(scoreTally.getTotalMiss()))
        print("Total shots = " + str(scoreTally.gettotalValidShots()))
        print("Total boats = " + str(scoreTally.getAvailableHits()))
        print("Total boats left= " + str(scoreTally.getTotalLeft()))
        print("Hit accuracy = " + str(round(scoreTally.getHitAccuracy())) + "%")