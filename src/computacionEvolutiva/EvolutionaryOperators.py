'''
Created on 17/10/2010

@author: Desktop
'''
import random
from Board import Board 

class EvolutionaryOperators:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def geneticCross(self, father1, father2):
        c = random.randint(0,len(father1.getUbications())-1)
        son1 = father1.getUbications()[:c]
        son2 = father2.getUbications()[:c]
        for i in father2.getUbications(): 
            if not i in son1:
                son1.append(i)
        for i in father1.getUbications(): 
            if not i in son2:
                son2.append(i)
        return [Board(father1.numberOfQueens(), son1), Board(father2.numberOfQueens(), son2)]

    def geneticMutation(self, board):
        ubications = board.getUbications()
        num1 = random.randint(0,len(ubications)-1)
        num2 = random.randint(0,len(ubications)-1)
        aux = ubications[num1]
        ubications[num1] = ubications[num2]
        ubications[num2] = aux
        return Board(board.numberOfQueens(), ubications)
    
    def isThereMutation(self, mutationProbability):
        c = random.randint(0,100)
        if(c < mutationProbability):
            return True
        return False
    