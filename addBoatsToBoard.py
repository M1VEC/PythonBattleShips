from boat import boat

class addBoatsToBoard:
    
    def __init__(self, gameMode, gameBoard):
        self.boardSize = gameMode.getSize()
        self.numberOfBoats = gameMode.getBoatCount()
        self.boatLengths = gameMode.getBoatLengths()
        self.boat = boat
        self.gameBoard = gameBoard
        self.boatBoard = gameBoard
        return
    
    def addABoat(self):
        for num in range(0,self.numberOfBoats):
            self.createBoat(self.boatLengths[num])
    
    def createBoat(self, boatLength):
        addBoat = self.boat(self.boardSize, boatLength, self.gameBoard.returnBoard())
        addBoat.addStartingPoint()
        self.boatBoard = addBoat.returnBoatBoard()
        
    def returnBoatBoard(self):
        return self.boatBoard