
import random
from BoardManager import BoardManager
from EvolutionaryOperators import EvolutionaryOperators
from time import clock

initialTime = None

class EvolutionaryAlgorithm:

    def __init__(self, queens, initialPopulation, iterations, mutationProbability, numberOfIndividues):
 
        print "Parametros:"
        print "Numero de reinas         ", queens
        print "Poblacion inicial        ", initialPopulation
        print "Iteraciones              ", iterations
        print "Probabilidad de mutacion ", mutationProbability
        print "Torneo de                ", numberOfIndividues
        
        print "\nSoluciones\n "
        global initialTime
        initialTime = clock()
        
        self.__queens = queens
        self.__initialPopulation = initialPopulation
        self.__iterations = iterations
        self.__mutationProbability = mutationProbability
        self.__numberOfIndividues = numberOfIndividues
        self.__boardManager = BoardManager(self.__queens, self.__initialPopulation)
        self.__operator = EvolutionaryOperators()
        
    def runAlgorithm(self):
        for i in range(self.__iterations):
            fathers = self.__boardManager.getFathers(self.__numberOfIndividues)
            sons = self.__operator.geneticCross(fathers[0],fathers[1])
            for son in sons :
                self.__boardManager.insertBoard(son)
            if self.__operator.isThereMutation(self.__mutationProbability):
                board = self.__boardManager.extractBoard(random.randint(0,len(self.__boardManager.getBoards())-1)) 
                self.__boardManager.insertBoard(self.__operator.geneticMutation(board))
        
    
    def getSolutions(self):
        return self.__boardManager.getSolutions()
        