
import Logger
import sys
from EvolutionaryAlgorithm import EvolutionaryAlgorithm
from timeit import Timer

if __name__ == '__main__':
#    print len(sys.argv)
#    if len(sys.argv) < 6:
#        print "Faltan Parametros"
        

    queens = 20
    initialPopulation = 50
    iterations = 5000
    mutationProbability = 15
    numberOfIndividues = 5
    
    logger=Logger.Logger(sys.stdout,'./salida.txt')
    sys.stdout=logger
    
    evolutionaryAlgorithm = EvolutionaryAlgorithm(queens, initialPopulation, iterations, mutationProbability, numberOfIndividues) 
    t = Timer(evolutionaryAlgorithm.runAlgorithm)
    time = t.timeit(1)
       
    print "\nTiempo de ejecucion ", time, "segundos"
    print "Numero de soluciones", len(evolutionaryAlgorithm.getSolutions())
    logger.close()