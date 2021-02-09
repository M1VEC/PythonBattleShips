class game:

    def __init__(self, board, boats):
        self.boats = boats
        self.boardSize = board.getBoardSize()
        self.userBoard = board.getUserBoard()
        self.gameBoard = self.boats.getGameBoard()
        self.shot = 0

    def runGame(self, userGuess):
        self.userGuess = userGuess
        self.shot = self.getGameBoardContents(self.userGuess)
        if self.shot == 'B ':
           return self.hit()
        else:
            self.noHit()

    def hit(self):
        self.setBothBoards(self.userGuess, 'H ')
        return

    def noHit(self):
        self.checkShot = self.getUserBoardContents(self.userGuess)
        if self.checkShot == '..':
            return  self.miss()
        elif self.checkShot == 'H ':
            return print("Previous Hit")    
        elif self.checkShot == '  ':
            print("Previous Miss") 
        return

    def miss(self):
        self.setBothBoards(self.userGuess, ' ')
        return

    def setBothBoards(self, coOrdinates, prompt):
        self.userBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)
        self.gameBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)
        return

    def getUserBoardContents(self,coOrdinates):
        return self.userBoard[coOrdinates[0], coOrdinates[1]]

    def getGameBoardContents(self, coOrdinates):
        return self.gameBoard[coOrdinates[0], coOrdinates[1]]

    def setUserBoard(self, coOrdinates, prompt):
        self.userBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)

    def setGameBoard(self, coOrdinates, prompt):
        self.gameBoard[coOrdinates[0], coOrdinates[1]] = '{:2}'.format(prompt)    