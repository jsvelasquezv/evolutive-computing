
class Board:

    def __init__(self, queens, ubications):
        self.__queens = queens
        self.__ubications = ubications
        self.__calculateFitnessValue()
        
    def numberOfQueens(self):
        return self.__queens
    
    def getUbications(self):
        return self.__ubications
    
    def getFitnessValue(self):
        return self.__fitnessValue
    
    def __calculateFitnessValue(self):
        checks = 0
        board = self.getUbications()
        for i in range(len(board)):
            for j in range(len(board))[i+1:]: 
                checks += self.__check([board[i],i],[board[j],j])
        self.__fitnessValue = checks
    
    def __check(self, position1, position2):
        """Verifies if two queens are checking"""
        position1Row = position1[0]
        position1column = position1[1]
        while (position1column <= position2[1]):
            position1Row+=1
            position1column+=1
            if position1Row == position2[0] and position1column == position2[1]:
                return -1
        position1Row = position1[0]
        position1column = position1[1]
        while (position1column <= position2[1]):
            position1Row-=1
            position1column+=1
            if position1Row == position2[0] and position1column == position2[1]:
                return -1  
        return 0
    
    def __cmp__(self,other):
        return cmp(self.getFitnessValue(), other.getFitnessValue())
    
        