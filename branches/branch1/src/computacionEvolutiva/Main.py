'''
Created on 16/10/2010

@author: Desktop
'''

import Logger
import sys
from EvolutionaryAlgorithm import EvolutionaryAlgorithm
from timeit import Timer

if __name__ == '__main__':
#    print len(sys.argv)
#    if len(sys.argv) < 6:
#        print "Faltan Parametros"
        
    print "hoal esto es un branch" 
    queens = 8
    initialPopulation = 2000
    iterations = 500
    mutationProbability = 40
    numberOfIndividues = 5
    
    logger=Logger.Logger(sys.stdout,'./salida.txt')
    sys.stdout=logger
    
    evolutionaryAlgorithm = EvolutionaryAlgorithm(queens, initialPopulation, iterations, mutationProbability, numberOfIndividues) 
    t = Timer(evolutionaryAlgorithm.runAlgorithm)
    time = t.timeit(1)
       
    print "\nTiempo de ejecucion ", time, "segundos"
    logger.close()