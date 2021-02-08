class game:

    def __init__(self, gameBoard, boats, userGuess):
        self.boats = boats
        self.gameBoard = gameBoard
        self.boardSize = self.gameBoard.getBoardSize()
        self.userBoard = self.gameBoard.getUserBoard()
        self.boatBoard = self.boats.getBoatBoard()
        self.userGuessX = userGuess[0]
        self.userGuessY = userGuess[1]
        return self.runGame()

    def runGame(self):
        # print(self.boatBoard)
        # print(self.userBoard)
        print(self.getGameBoardContents(5,4))


        return

    def getUserBoardContents(self, AxisX, AxisY):
        return  self.userBoard[AxisX, AxisY]

    def getGameBoardContents(self, AxisX, AxisY):
        return  self.boatBoard[AxisX, AxisY]    

    def setUserBoard(self, coOrdinates, prompt):
        self.userBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)

    def setGameBoard(self, coOrdinates, prompt):
        self.boatBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)    