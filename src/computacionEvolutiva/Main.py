'''
Created on 16/10/2010

@author: Desktop
'''

import Logger
import sys

from time import clock
from EvolutionaryAlgorithm import EvolutionaryAlgorithm   
from BoardManager import BoardManager
from computacionEvolutiva.EvolutionaryOperators import EvolutionaryOperators
import multiprocessing
initialTime = 0

if __name__ == '__main__':
#    print len(sys.argv)
#    if len(sys.argv) < 6:
#        print "Faltan Parametros"

    
    
    
    initialTime = clock() 
    queens = 8
    initialPopulation = 2000
    iterations = 2000
    mutationProbability = 40
    numberOfIndividues = 5
   
    logger=Logger.Logger(sys.stdout,'./salida.txt')
    sys.stdout=logger
        
    print "Parametros:"
    print "Numero de reinas         ", queens
    print "Poblacion inicial        ", initialPopulation
    print "Iteraciones              ", iterations
    print "Probabilidad de mutacion ", mutationProbability
    print "Torneo de                ", numberOfIndividues
    
    print "\nSoluciones\n "

    operator = EvolutionaryOperators()
    boardManager = BoardManager(queens, initialPopulation)
    

    threads = []
    for i in range(multiprocessing.cpu_count()):
        evolutionaryAlgorithm = EvolutionaryAlgorithm(queens, initialPopulation, iterations/multiprocessing.cpu_count(), mutationProbability, numberOfIndividues, operator, boardManager)
        evolutionaryAlgorithm.start()
        threads.append(evolutionaryAlgorithm) 
    
    for t in threads:
        t.join()

    print "\nTiempo de ejecucion ", clock() - initialTime, "segundos"
    logger.close()