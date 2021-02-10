class scoreBoard:
    
    def __init__(self, gameSetting):
        self.availableBoatHits = gameSetting.getTotalBoatHits()
        self.totalHits = 0
        self.totalMiss = 0
        self.invalidShots = 0       
        self.totalValidShots = 0
        return
    
    def userShot(self, userShot):
        if userShot == 'H':
            self.setHitShot()
        elif userShot == 'M':
            self.setMissedShot()
        else:
            self.setInvalidShot()
        return

    def setHitShot(self):
        self.totalHits += 1
        return self.totalHits
    
    def setMissedShot(self):
        self.totalMiss += 1
        return self.totalMiss
    
    def setInvalidShot(self):
        self.invalidShots += 1
        return self.invalidShots
    
    def getTotalHits(self):
        return self.totalHits
    
    def getTotalMiss(self):
        return self.totalMiss
    
    def getAvailableHits(self):
        return self.availableBoatHits

    def getHitAccuracy(self):
        self.hitAccuracy = (self.totalHits / self.totalValidShots) * 100
        return self.hitAccuracy
        
    def gettotalValidShots(self):
        self.totalValidShots = self.totalHits + self.totalMiss
        return self.totalValidShots
    