import random 

class boat:

    def __init__(self, size, boatLength, board):   #add board seperate so I can add previous boat boards
        self.boardSizeX = size[0]
        self.boardSizeY = size[1]
        self.boatLength = boatLength
        self.boatBoard = board
        return 
    
    def addStartingPoint(self):
        self.startPointX = random.randint(1,(self.boardSizeX-1))
        self.startPointY = random.randint(1,(self.boardSizeY-1))
        if self.returnCoOrdinateContents(self.startPointX, self.startPointY) == '..':
            self.addToBoat()
        else:
            return self.addStartingPoint()

    def addToBoat(self):
        options = ["horizontal", "vertical"]
        if self.boatLength > 1:
            if random.choice(options) == "horizontal":
                    self.addToBoatHorizontal()
            else:
                    self.addToBoatVertical()    
        return    

    def addToBoatHorizontal(self):
        if (self.startPointY + self.boatLength) > self.boardSizeY:
            return self.addStartingPoint()
        else:
            tempBoatCoordinates = []
            for num in range(0,self.boatLength):
                if self.returnCoOrdinateContents(self.startPointX, self.startPointY) == '..':
                    tempBoatCoordinates.append(self.startPointY)
                    self.startPointY += 1
                else:
                    return self.addStartingPoint()            
            for num in tempBoatCoordinates:
                self.setCoOrrdinate([self.startPointX, num])    


    def addToBoatVertical(self):
        if (self.startPointX + self.boatLength) > self.boardSizeX:
            return self.addStartingPoint()
        else:
            tempBoatCoordinates = []    
            for num in range(0,self.boatLength):
                if self.returnCoOrdinateContents(self.startPointX, self.startPointY) == '..':
                    tempBoatCoordinates.append(self.startPointX)
                    self.startPointX += 1
                else:
                    return self.addStartingPoint()
            for num in tempBoatCoordinates:
                self.setCoOrrdinate([num, self.startPointY])    



    def setCoOrrdinate(self, coOrdinate):
        self.boatBoard[coOrdinate[0], coOrdinate[1]] = '{:2}'.format("B")

    def returnCoOrdinateContents(self, AxisX, AxisY):
        return  self.boatBoard[AxisX, AxisY]

    def returnBoatBoard(self):
        return self.boatBoard
