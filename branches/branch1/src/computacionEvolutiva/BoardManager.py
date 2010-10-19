'''
Created on 17/10/2010

@author: Desktop
'''
from Board import Board
from random import shuffle
import bisect
import random
import copy
import EvolutionaryAlgorithm
from time import clock


class BoardManager:
    '''
    classdocs
    '''
    
    __queens = None
    __boards = []
    __solutions = []

    def __init__(self, queens, initialNumberOfBoards):
        '''
        Constructor
        '''
        self.__queens = queens
        self.__randomBoards(range(1,queens+1), initialNumberOfBoards)
          
    def getBoards(self):
        return self.__boards
    
    def extractBoard(self, pos):
        board = copy.copy(self.__boards[pos])
        del self.__boards[pos]
        return board
        
    
    def getSolutions(self):
        return self.__solutions
    
    def insertBoard(self,board):
        """inserts a board in a sorted way"""
        bisect.insort(self.__boards, board)
        self.insertIfIsSolution(board)
    
    def insertIfIsSolution(self, board):
        if board.getFitnessValue() == 0:
            add = True
            for solution in self.getSolutions():
                if board.getUbications() == solution.getUbications():
                    add = False
            if add:
                import Main
                print board.getUbications(), (clock() - Main.initialTime), "segundos"
                self.__solutions.append(copy.copy(board)) 
       
    def getFathers(self, numberOfIndividues):
        """Returns the fathers 
            Obtiene los N tableros al azar
            Ordena los tableros segun sufitness
            retorn los 2 mejores
        """
        individues = range(len(self.__boards))
        shuffle(individues)
        individues = individues[0:numberOfIndividues]
        candidates = []
        for i in individues:
            candidates.append(self.__boards[i])
        candidates = sorted(candidates, key=lambda candidate: candidate.getFitnessValue())
        return [candidates[len(candidates)-1],candidates[len(candidates)-2]]  
    
    def __randomBoards(self, board, numberOfBoards):
        """Generates numberOfBoards random permutations from the board"""
        for i in range(0, numberOfBoards):
            aux = copy.copy(board)
            random.shuffle(aux)
            self.insertBoard(Board(self.__queens,aux))
    

    