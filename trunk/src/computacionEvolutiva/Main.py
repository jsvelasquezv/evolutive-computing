
import Logger
import sys
from EvolutionaryAlgorithm import EvolutionaryAlgorithm
from timeit import Timer

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print "Faltan Parametros"
        print "Uso:"
        print "python Main.py <queens> <initialPopulation> <iterations> <mutationProbability> <numberOfIndividues>"
        print "Main.py 10 50 5000 15 5"        
    else:
        queens = int(sys.argv[1])
        initialPopulation = int(sys.argv[2])
        iterations = int(sys.argv[3])
        mutationProbability = int(sys.argv[4])
        numberOfIndividues = int(sys.argv[5])
        
        logger=Logger.Logger(sys.stdout, sys.argv[6])
        sys.stdout=logger
        
        evolutionaryAlgorithm = EvolutionaryAlgorithm(queens, initialPopulation, iterations, mutationProbability, numberOfIndividues) 
        t = Timer(evolutionaryAlgorithm.runAlgorithm)
        time = t.timeit(1)
           
        print "\nTiempo de ejecucion ", time, "segundos"
        print "Numero de soluciones", len(evolutionaryAlgorithm.getSolutions())
        logger.close()