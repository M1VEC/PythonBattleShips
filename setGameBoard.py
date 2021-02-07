import numpy as np

class setGameBoard:

    def __init__(self, boardSize):
        self.boardSizeX = boardSize[0]
        self.boardSizeY = boardSize[1]
        self.board =[]
        return

    def createBoard(self):
        self.board = np.full((self.boardSizeX, self.boardSizeY),'{:2}'.format(".."))
        self.labelAxis()

    def returnBoard(self):
        return self.board

    def labelAxis(self):
        for label in range(0,self.boardSizeX):
            self.board[0,label] = '{:2}'.format(label)

        for label in range(0,self.boardSizeY):
            self.board[label,0] = '{:2}'.format(label)
        return

    def returnCoOrdinateContents(self, AxisX, AxisY):
        return  self.board[AxisX, AxisY]

    # def setCoOrrdinate(self, coOrdinate):
    #     self.board[coOrdinate[0], coOrdinate[1]] = 'B'