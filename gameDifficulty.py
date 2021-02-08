class gameDifficulty:

    def __init__(self, difficulty):
        self.gameMode = difficulty
        self.size = []
        self.boatCount = 0
        self.boatLengths = []
        return self.setMode()

    def setMode(self):
        if self.gameMode == 'easy':
            return self.setEasy()
        elif self.gameMode == 'normal':
            return self.setNormal()
        elif self.gameMode == 'hard':
            return self.setHard()
        return

    def setEasy(self):
        self.size = [6,6]
        self.boatCount = 2
        self.boatLengths = [2, 3]
        return

    def setNormal(self):
        self.size = [10,10]
        self.boatCount = 5
        self.boatLengths = [3, 4, 2, 3, 4]
        return

    def setHard(self):
        self.size = [13,13]
        self.boatCount = 7
        self.boatLengths = [3, 4, 2, 5, 2, 4, 3]
        return

    def getSize(self):
        return self.size

    def getBoatCount(self):
        return self.boatCount

    def getBoatLengths(self):
        return self.boatLengths
    
    
    