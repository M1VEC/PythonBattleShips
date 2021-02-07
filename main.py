from gameBoard import gameBoard

def main():
    boardSize = [10,10]
    
    game = gameBoard(boardSize)
    game.createBoard()
    
    game.insertShip(2, 2)
    
    game.labelAxis()
    print(game.returnBoard())

main()