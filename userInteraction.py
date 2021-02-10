def gameMode():
    print("easy     normal      hard")
    return  input("Select difficulty: ")

def getUserGuess():
    return [userGuess("Enter down co-ordinate: ") ,userGuess("Enter across co-ordinate: ")]

def userGuess(prompt):
    return int(input(prompt))

def printPrompt(prompt):
    return print(prompt)