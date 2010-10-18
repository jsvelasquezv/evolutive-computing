'''
Created on 18/10/2010

@author: Desktop
'''
import random
from BoardManager import BoardManager
from computacionEvolutiva.EvolutionaryOperators import EvolutionaryOperators
from time import clock

initialTime = None

class EvolutionaryAlgorithm:
    '''
    classdocs
    '''
    __queens = None
    __initialPopulation = None
    __iterations = None
    __mutationProbability = None
    __numberOfIndividues = None
    

    def __init__(self, queens, initialPopulation, iterations, mutationProbability, numberOfIndividues):
        '''
        Constructor
        '''
        self.__queens = queens
        self.__initialPopulation = initialPopulation
        self.__iterations = iterations
        self.__mutationProbability = mutationProbability
        self.__numberOfIndividues = numberOfIndividues
        
    def runAlgorithm(self):
        print "Parametros:"
        print "Numero de reinas         ", self.__queens
        print "Poblacion inicial        ", self.__initialPopulation
        print "Iteraciones              ", self.__iterations
        print "Probabilidad de mutacion ", self.__mutationProbability
        print "Torneo de                ", self.__numberOfIndividues
        
        print "\nSoluciones\n "
        global initialTime
        initialTime = clock()
        operator = EvolutionaryOperators()
        boardManager = BoardManager(self.__queens, self.__initialPopulation)
        
        for i in range(self.__iterations):
            fathers = boardManager.getFathers(self.__numberOfIndividues)
            sons = operator.geneticCross(fathers[0],fathers[1])
            for son in sons :
                boardManager.insertIfIsSolution(son)
            if operator.isThereMutation(self.__mutationProbability):
                board = boardManager.extractBoard(random.randint(0,len(boardManager.getBoards())-1)) 
                boardManager.insertBoard(operator.geneticMutation(board))
        
    
#        for i in boardManager.getSolutions():
#            print i.getUbications()   