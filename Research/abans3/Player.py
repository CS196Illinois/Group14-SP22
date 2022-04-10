class Player:
    def __init__(self, ppg, rpg, apg, pie, fgp, tpp, ftp, stl, blk, tov):
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg
        self.pie = pie
        self.fgp = fgp
        self.tpp = tpp
        self.ftp = ftp
        self.stl = stl
        self.blk = blk
        self.tov = tov
    
    def assignValue(self):
        return self.ppg + self.rpg*1.3 + self.apg*1.5 + self.blk*1.7 + self.stl*1.7 - self.tov*2.3 + self.tpp*3 + self.ftp*1.7 + self.fgp*2 + self.pie*2

    def percentChange(num1, num2):
        difference = abs(num1 = num2)
        return difference/num1

    def changeInValue(self, newPPG, newRPG, newAPG, newBLK, newSTL, newTOV, newTPP, newFTP, newFGP, newPIE):
        oldValue = assignValue(self)
        
