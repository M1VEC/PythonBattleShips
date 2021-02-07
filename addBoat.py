import random

class addBoat:

    def __init__(self, gameMode, game):
        self.gameMode = gameMode
        self.game = game
        self.size = gameMode.getSize()
        self.boardSizeX = self.size[0]
        self.boardSizeY = self.size[1]
        self.boatCount = gameMode.getBoatCount()
        return


    def addAllShips(self):
        for boat in range(1,self.boatCount):
            self.addShip()
            return

    def addShip(self):
        self.startPointX = random.randint(1,self.boardSizeX-1)
        self.startPointY = random.randint(1,self.boardSizeY-1)
        if self.game.returnCoOrdinateContents(self.startPointX,self.startPointY) == '..':
            self.game.setCoOrrdinate([self.startPointX,self.startPointY])
        else:
            return self.addShip()


        print(self.game.returnCoOrdinateContents(self.startPointX,self.startPointY))
        return


