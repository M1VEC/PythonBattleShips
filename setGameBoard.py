import numpy as np
import copy

class setGameBoard:

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.boardSizeX = boardSize[0]
        self.boardSizeY = boardSize[1]
        self.gameBoard =[]                      #gameBoard refers to the board with boat locations
        self.userBoard = []                     #gameBoard refers to the board with that the user interacts with
        return self.createBoard()

    def createBoard(self):
        self.gameBoard = np.full((self.boardSizeX, self.boardSizeY),'{:2}'.format(".."))
        self.labelAxis()
        self.userBoard = copy.deepcopy(self.gameBoard)

    def labelAxis(self):
        for label in range(0,self.boardSizeX):
            self.gameBoard[0,label] = '{:2}'.format(label)

        for label in range(0,self.boardSizeY):
            self.gameBoard[label,0] = '{:2}'.format(label)
        return

    def getCoOrdinateContents(self, AxisX, AxisY):
        return  self.board[AxisX, AxisY]
        
    def getGameBoard(self):
        return self.gameBoard

    def getUserBoard(self):
        return self.userBoard 

    def getBoardSize(self):
        return self.boardSize   
