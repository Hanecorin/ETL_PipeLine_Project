from datetime import date


class bitDTO:
    def __init__(self, newasset, newname, newdate, newopen, newhigh, newlow, newclose):
        # self.id = newid
        self.asset = newasset
        self.name = newname
        self.date = newdate
        self.open = newopen
        self.high = newhigh
        self.low = newlow
        self.close = newclose
        
        
        
        
    # def getId(self):
    #     return self.id
        
    # def setId(self, newId):
    #     self.id = newId
        
    def getAsset(self):
        return self.asset
        
    def setAsset(self, newAsset):
        self.asset = newAsset
        
    def getName(self):
        return self.name
        
    def setName(self, newName):
        self.name = newName
        
    def getDate(self):
        return self.date
        
    def setDate(self, newDate):
        self.date = newDate
        
    def getOpen(self):
        return self.open
        
    def setOpen(self, newOpen):
        self.open = newOpen
    
    def getHigh(self):
        return self.high
        
    def setHigh(self, newHigh):
        self.high = newHigh
        
    def getLow(self):
        return self.low
        
    def setLow(self, newLow):
        self.low = newLow
        
    def getClose(self):
        return self.close
        
    def setClose(self, newClose):
        self.close = newClose
        
        
    
    
    
    
    
    def __str__(self):
        return '이름 : ' + self.name + ', 날짜 : ' + str(self.date) + ', 개장시가격 : ' + str(self.open) +', 상한가 : ' + str(self.high) + ', 하한가 : ' + str(self.low) + ', 마감시 가격 : ' + str(self.close)
    
    
# 단순 단위 test용 코드
if __name__ == '__main__':
    bitcoin = bitDTO(500, 'gd', 'gd', 'gd', 1.2, 1.1, 1.1, 1.1)
    
    print(bitcoin) #__str__() 자동 호출 java의 tostring() 과 동일
