from boat import boat

class addBoats:
    
    def __init__(self, gameMode, board):
        self.boardSize = gameMode.getSize()
        self.numberOfBoats = gameMode.getBoatCount()
        self.boatLengths = gameMode.getBoatLengths()
        self.boat = boat
        self.gameBoard = board
        self.boatBoard = self.gameBoard
        return self.addGameBoats()
    
    def addGameBoats(self):
        for num in range(0,self.numberOfBoats):
            self.createBoat(self.boatLengths[num])
    
    def createBoat(self, boatLength):
        addBoat = self.boat(self.boardSize, boatLength, self.gameBoard.getGameBoard())
        addBoat.addStartingPoint()
        self.boatBoard = addBoat.getBoatBoard()
        
    def getBoatBoard(self):
        return self.boatBoard

    def getBoatCount(self):
        return self.numberOfBoats

    def getBoatLengths(self):
        return self.boatLengths

