class gameDifficulty:

    def __init__(self, difficulty):
        self.gameMode = difficulty
        self.size = []
        self.boatCount = 0
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
        self.size = [5,5]
        self.boatCount = 2
        return

    def setNormal(self):
        self.size = [10,10]
        self.boatCount = 3
        return

    def setHard(self):
        self.size = [13,13]
        self.boatCount = 4
        return

    def getSize(self):
        return self.size

    def getBoatCount(self):
        return self.boatCount

    