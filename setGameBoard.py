import numpy as np
import copy

class setGameBoard:

    def __init__(self, boardSize):
        self.boardSizeX = boardSize[0]
        self.boardSizeY = boardSize[1]
        self.board =[]
        self.userBoard = []
        return self.createBoard()

    def createBoard(self):
        self.board = np.full((self.boardSizeX, self.boardSizeY),'{:2}'.format(".."))
        self.labelAxis()
        self.userBoard = copy.deepcopy(self.board)

    def returnBoard(self):
        return self.board

    def returnUserBoard(self):
        return self.userBoard    

    def labelAxis(self):
        for label in range(0,self.boardSizeX):
            self.board[0,label] = '{:2}'.format(label)

        for label in range(0,self.boardSizeY):
            self.board[label,0] = '{:2}'.format(label)
        return

    def returnCoOrdinateContents(self, AxisX, AxisY):
        return  self.board[AxisX, AxisY]
