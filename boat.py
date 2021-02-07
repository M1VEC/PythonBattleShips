import random 

class boat:

    def __init__(self, size, boatLength, board):   #add board seperate so I can add previous boat boards
        self.boardSizeX = size[0]
        self.boardSizeY = size[1]
        self.boatLength = boatLength
        self.boatBoard = board
        self.index = 1
        return

    def addStartingPoint(self):
        self.startPointX = random.randint(1,self.boardSizeX-1)
        self.startPointY = random.randint(1,self.boardSizeY-1)
        if self.returnCoOrdinateContents(self.startPointX,self.startPointY) == '..':
            self.setCoOrrdinate([self.startPointX,self.startPointY])
        else:
            self.addStartingPoint()
        self.addToBoat()


    def addToBoat(self):
        options = ["horizontal", "vertical"]
        if self.boatLength > 1:
            if random.choice(options) == "horizontal":
                for num in range(1,self.boatLength):
                    self.addToBoatHorizontal()
            else:
                for num in range(1,self.boatLength):
                    self.addToBoatVertical()    
        return    



    def addToBoatHorizontal(self):
        if self.startPointY +1 != 9:
            if self.returnCoOrdinateContents(self.startPointX,self.startPointY +1) == '..':
                self.setCoOrrdinate([self.startPointX,self.startPointY +1])
                self.startPointY += 1
                self.index += 1
        else:
            self.setCoOrrdinate([self.startPointX,self.startPointY -self.index])
            self.startPointY -= 1
        return


    def addToBoatVertical(self):
        if self.startPointX +1 != 9:
            if self.returnCoOrdinateContents(self.startPointX +1,self.startPointY) == '..':
                self.setCoOrrdinate([self.startPointX +1,self.startPointY])
                self.startPointX += 1
                self.index += 1
        else:
            self.setCoOrrdinate([self.startPointX -self.index,self.startPointY])
            self.startPointX -= 1
        return


    def setCoOrrdinate(self, coOrdinate):
        self.boatBoard[coOrdinate[0], coOrdinate[1]] = '{:2}'.format("B")


    def returnCoOrdinateContents(self, AxisX, AxisY):
        return  self.boatBoard[AxisX, AxisY]


    def returnBoatBoard(self):
        return self.boatBoard
