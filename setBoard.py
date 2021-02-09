import numpy as np
import copy

class setBoard:

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.gameBoard =[]                      #gameBoard refers to the board with boat locations
        self.userBoard = []                     #userBoard refers to the board that the user interacts with
        return self.createBoard()

    def createBoard(self):
        self.gameBoard = np.full((self.boardSize[0], self.boardSize[1]),'{:2}'.format(".."))
        self.labelAxis()
        self.userBoard = copy.deepcopy(self.gameBoard)

    def labelAxis(self):
        for label in range(0,self.boardSize[0]):
            self.gameBoard[0,label] = '{:2}'.format(label)

        for label in range(0,self.boardSize[1]):
            self.gameBoard[label,0] = '{:2}'.format(label)
        return

    def getGameBoard(self):
        return self.gameBoard

    def getUserBoard(self):
        return self.userBoard 

    def getBoardSize(self):
        return self.boardSize   
