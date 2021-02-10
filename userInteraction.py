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