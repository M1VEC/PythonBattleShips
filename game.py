class game:

    def __init__(self, board, boats):
        self.boats = boats
        self.userBoard = board.getUserBoard()
        self.gameBoard = self.boats.getGameBoard()

    def runGame(self, userGuess):
        self.userGuess = userGuess
        if self.getGameBoardContents(self.userGuess) == 'B ':
           return self.hit()
        else:
            return self.noHit()

    def hit(self):
        self.setBothBoards(self.userGuess, 'H ')
        return 'H'

    def noHit(self):
        self.checkShot = self.getUserBoardContents(self.userGuess)
        if self.checkShot == '..':
            return  self.miss()
        elif self.checkShot == 'H ':
            return 'PH'
        elif self.checkShot == '  ':
            return 'PM'

    def miss(self):
        self.setBothBoards(self.userGuess, ' ')
        return 'M'

    def setBothBoards(self, coOrdinates, prompt):
        self.userBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)
        self.gameBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)
        return

    def getUserBoardContents(self,coOrdinates):
        return self.userBoard[coOrdinates[0], coOrdinates[1]]

    def getGameBoardContents(self, coOrdinates):
        return self.gameBoard[coOrdinates[0], coOrdinates[1]]
