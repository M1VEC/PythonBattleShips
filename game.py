class game:

    def __init__(self, board, boats, userGuess):
        self.boats = boats
        self.boardSize = board.getBoardSize()
        self.userBoard = board.getUserBoard()
        self.gameBoard = self.boats.getGameBoard()
        self.userGuess = userGuess
        self.shot = 0
        return self.runGame()

    def runGame(self):
        self.shot = self.getGameBoardContents(self.userGuess)
        if self.shot == 'B ':
           return self.hit()
        elif self.shot == '..':
            return self.miss()
        return self.noHitOrMiss()

    def hit(self):
        print("HIT")
        return

    def miss(self):
        print("MISS")
        return

    def noHitOrMiss(self):
        if self.shot == 'H ':
            return "Previous Hit"
        elif self.shot == ' ':
            return "Previous Miss" 
        return

    def getUserBoardContents(self,coOrdinates):
        return self.userBoard[coOrdinates[0], coOrdinates[1]]

    def getGameBoardContents(self, coOrdinates):
        return self.gameBoard[coOrdinates[0], coOrdinates[1]]

    def setUserBoard(self, coOrdinates, prompt):
        self.userBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)

    def setGameBoard(self, coOrdinates, prompt):
        self.gameBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)    