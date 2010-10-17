'''
Created on 16/10/2010

@author: Desktop
'''
import random
from BoardManager import BoardManager
from computacionEvolutiva.EvolutionaryOperators import EvolutionaryOperators
import Logger
import sys

if __name__ == '__main__':
    queens = 8
    initialPopulation = 200
    iterations = 1000
    mutationProbability = 15
    numberOfIndividues = 5
    
    logger=Logger.Logger(sys.stdout,'./salida.txt')
    sys.stdout=logger
    print "Parametros:"
    print "Numero de reinas         ", queens
    print "Poblacion inicial        ", initialPopulation
    print "Iteraciones              ", iterations
    print "Probabilidad de mutacion ", mutationProbability
    print "Torneo de                ", numberOfIndividues
    
    operator = EvolutionaryOperators()
    boardManager = BoardManager(queens, initialPopulation)
    
    for i in range(iterations):
        fathers = boardManager.getFathers(numberOfIndividues)
        sons = operator.geneticCross(fathers[0],fathers[1])
        for son in sons :
            boardManager.insertIfIsSolution(son)
        if operator.isThereMutation(mutationProbability):
            board = boardManager.extractBoard(random.randint(0,len(boardManager.getBoards())-1)) 
            boardManager.insertBoard(operator.geneticMutation(board))
    
    print "\nSoluciones\n "

    for i in boardManager.getSolutions():
        print i.getUbications()   
    logger.close()