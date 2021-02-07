import numpy as np

class gameBoard:

    def __init__(self, boardSize):
        self.boardSizeX = boardSize[0]
        self.boardSizeY = boardSize[1]
        self.board =[]
        return

    def createBoard(self):
        self.board = np.full((self.boardSizeX, self.boardSizeY),".")

    def returnBoard(self):
        return self.board

    def insertShip(self, xaxis, yaxis):
        self.board[xaxis,yaxis] = "X"

    def labelAxis(self):
        for label in range(0,self.boardSizeX):
            self.board[0,label] = str(label)
        for label in range(0,self.boardSizeY):
            self.board[label,0] = str(label)
        return