def gameMode():
    modes = ("easy", "normal", "hard")
    printPrompt("Select difficulty:   easy     normal      hard")
    mode = input()
    if mode in modes:
        return mode
    else:
        return gameMode()

def getUserGuess():
    return [userGuess("Enter down co-ordinate: ") ,userGuess("Enter across co-ordinate: ")]

def userGuess(prompt):
    return int(input(prompt))

def printPrompt(prompt):
    return print(prompt)

def printScoreTally(scoreTally):
    print("Hits = " + str(scoreTally.getTotalHits()))
    print("Miss = " + str(scoreTally.getTotalMiss()))
    print("Total shots = " + str(scoreTally.gettotalValidShots()))
    print("Total boats = " + str(scoreTally.getAvailableHits()))
    print("Hit accuracy = " + str(round(scoreTally.getHitAccuracy())) + "%")