import random 

class boat:

    def __init__(self, size, boatLength, board):   #add board seperate so I can add previous boat boards
        self.boardSizeX = size[0]
        self.boardSizeY = size[1]
        self.boatLength = boatLength
        self.boatBoard = board

        print(self.boatBoard)
        return

    def addStartingPoint(self):
        self.startPointX = random.randint(1,self.boardSizeX-1)
        self.startPointY = random.randint(1,self.boardSizeY-1)

        if self.returnCoOrdinateContents(self.startPointX,self.startPointY) == '..':
            self.setCoOrrdinate([self.startPointX,self.startPointY])
        else:
            self.addStartingPoint()
        self.addToBoat(3)
    

    def addToBoat(self, length):
        options = ["horizontal", "vertical"]
        if length > 1:
            # direction = random.choice(options)
            # print(direction)
            if random.choice(options) == "horizontal":
                self.addToBoatHorizontal()
            else:
                self.addToBoatVertical()    

        return    

    def addToBoatHorizontal(self):
        print("horizontal")
        return

    def addToBoatVertical(self):
        print("vertical")
        return


    def setCoOrrdinate(self, coOrdinate):
        self.boatBoard[coOrdinate[0], coOrdinate[1]] = 'B'

    def returnCoOrdinateContents(self, AxisX, AxisY):
            return  self.boatBoard[AxisX, AxisY]
