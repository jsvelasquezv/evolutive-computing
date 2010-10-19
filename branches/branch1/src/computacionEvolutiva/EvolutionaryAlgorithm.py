'''
Created on 18/10/2010

@author: Desktop
'''
import random
import threading

class EvolutionaryAlgorithm(threading.Thread):
    '''
    classdocs
    '''
    __queens = None
    __initialPopulation = None
    __iterations = None
    __mutationProbability = None
    __numberOfIndividues = None
    __operator = None
    __boardManager = None

    def __init__(self, queens, initialPopulation, iterations, mutationProbability, numberOfIndividues, operator, boardManager):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.__queens = queens
        self.__initialPopulation = initialPopulation
        self.__iterations = iterations
        self.__mutationProbability = mutationProbability
        self.__numberOfIndividues = numberOfIndividues
        self.__operator = operator
        self.__boardManager = boardManager
        
    def run(self):
        for i in range(self.__iterations):
            fathers = self.__boardManager.getFathers(self.__numberOfIndividues)
            sons = self.__operator.geneticCross(fathers[0],fathers[1])
            for son in sons :
                self.__boardManager.insertIfIsSolution(son)
            if self.__operator.isThereMutation(self.__mutationProbability):
                board = self.__boardManager.extractBoard(random.randint(0,len(self.__boardManager.getBoards())-1)) 
                self.__boardManager.insertBoard(self.__operator.geneticMutation(board))
