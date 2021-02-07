import numpy as np

class gameBoard:

    def __init__(self):
        self.board =[]
        return

    def createBoard(self):
        self.board = np.full((6,4),"X")

    def returnBoard(self):
        return self.board

