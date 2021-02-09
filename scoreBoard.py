class scoreBoard:
    
    def __init__(self, availableHits):
        self.availableHits = availableHits
        self.score = 0
        return
    
    def userShot(self, userShot):
        if userShot == 'H ':
            self.hitShot()
        else:
            self.missedShot()
        return

    def totalValidShots(self):
        self.totalShotsValid = self.totalHits + self.totalMiss
        return 
    
    def hitShot(self):
        self.totalHits += 1
        return self.totalHits
    
    def missedShot(self):
        self.totalMiss += 1
        return self.totalMiss
    