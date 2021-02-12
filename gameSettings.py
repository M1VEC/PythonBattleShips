from setBoard import setBoard
from addBoats import addBoats

class gameSettings:
    #Responisble for setting the game difficulty, the game and user boards and then placing the boats.
    
    def __init__(self):
        self.size = []
        self.boatCount = 0
        self.boatLengths = []

    def setMode(self, gameMode):
        self.gameMode = gameMode
        if self.gameMode == 'easy':
            self.setEasy()
        elif self.gameMode == 'normal':
            self.setNormal()
        elif self.gameMode == 'hard':
            self.setHard()
        return self.createNewBoard()
    
    def createNewBoard(self):
        self.board = setBoard(self.size)
        return addBoats(self)
        

    def setEasy(self):
        self.size = [6,6]
        self.boatCount = 2
        self.boatLengths = [3, 5]
        self.maxShots = 15
        return

    def setNormal(self):
        self.size = [10,10]
        self.boatCount = 5
        self.boatLengths = [3, 4, 2, 3, 4]
        self.maxShots = 40
        return

    def setHard(self):
        self.size = [13,13]
        self.boatCount = 7
        self.boatLengths = [3, 4, 2, 5, 2, 4, 3]
        self.maxShots = 60
        return

    def getSize(self):
        return self.size

    def getBoatCount(self):
        return self.boatCount

    def getBoatLengths(self):
        return self.boatLengths
    
    def getTotalBoatHits(self):
        return sum(self.boatLengths)
        
    def getmaxShots(self):
        return self.maxShots
    
    def getGameBoard(self):
        return self.board.getGameBoard()

    def getUserBoard(self):
        return self.board.getUserBoard()
