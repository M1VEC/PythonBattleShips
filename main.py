from gameBoard import gameBoard

def main():
    game = gameBoard()
    game.createBoard()
    print(game.returnBoard())


main()