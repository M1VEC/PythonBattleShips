class game:

    def __init__(self, board, boats, userGuess):
        self.boats = boats
        self.boardSize = board.getBoardSize()
        self.userBoard = board.getUserBoard()
        self.gameBoard = self.boats.getGameBoard()
        self.userGuessX = userGuess[0]
        self.userGuessY = userGuess[1]
        return self.runGame()

    def runGame(self):
        print(self.getGameBoardContents(self.userGuessX, self.userGuessY))
        if self.getGameBoardContents(self.userGuessX, self.userGuessY) == 'B ':
            print("HIT")
        elif self.getGameBoardContents(self.userGuessX, self.userGuessY) == 'M ':
            print("Already tried")
        elif self.getGameBoardContents(self.userGuessX, self.userGuessY) == 'H ':
            print("Already hit")    
        else:
            print("MISS")
        return

    def getUserBoardContents(self, AxisX, AxisY):
        return self.userBoard[AxisX, AxisY]

    def getGameBoardContents(self, AxisX, AxisY):
        return self.gameBoard[AxisX, AxisY]    

    def setUserBoard(self, coOrdinates, prompt):
        self.userBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)

    def setGameBoard(self, coOrdinates, prompt):
        self.gameBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)    