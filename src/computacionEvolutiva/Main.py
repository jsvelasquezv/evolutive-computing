'''
Created on 16/10/2010

@author: Desktop
'''
import random
from BoardManager import BoardManager
from computacionEvolutiva.EvolutionaryOperators import EvolutionaryOperators


if __name__ == '__main__':
    queens = 8
    initialPopulation = 200
    iterations = 1000
    mutationProbability = 100
    
    operator = EvolutionaryOperators()
    boardManager = BoardManager(queens, initialPopulation)
    
    print "Soluciones de la poblacion inicial " 
    for i in boardManager.getSolutions():
        print i.getUbications(), i.getFitnessValue()
    
    for i in range(iterations):
        fathers = boardManager.getFathers()
        sons = operator.geneticCross(fathers[0],fathers[1])
        for son in sons :
            boardManager.insertIfIsSolution(son)
        if operator.isThereMutation(mutationProbability):
            board = boardManager.extractBoard(random.randint(0,len(boardManager.getBoards())-1)) 
            boardManager.insertBoard(operator.geneticMutation(board))
    
    print "Soluciones " 
    for i in boardManager.getSolutions():
        print i.getUbications(), i.getFitnessValue()