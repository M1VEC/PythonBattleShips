from boat import boat

class addBoats:
    
    def __init__(self, gameMode, board):
        self.boardSize = gameMode.getSize()
        self.numberOfBoats = gameMode.getBoatCount()
        self.boatLengths = gameMode.getBoatLengths()
        self.boat = boat
        self.gameBoard = board.getGameBoard()
        return self.addGameBoats()
    
    def addGameBoats(self):
        for num in range(0,self.numberOfBoats):
            self.createBoat(self.boatLengths[num])
    
    def createBoat(self, boatLength):
        addBoat = self.boat(self.boardSize, boatLength, self.gameBoard)
        addBoat.addStartingPoint()
        self.gameBoard = addBoat.getGameBoard()
        
    def getGameBoard(self):
        return self.gameBoard

    def getBoatCount(self):
        return self.numberOfBoats

    def getBoatLengths(self):
        return self.boatLengths

