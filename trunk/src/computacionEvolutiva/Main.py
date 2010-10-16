'''
Created on 16/10/2010

@author: Desktop
'''

import random
import copy
from random import shuffle

def randomBoards(board, numberOfBoards):
    """Generates numberOfBoards random permutations from the board"""
    boards = []
    for i in range(1, numberOfBoards):
        aux = copy.copy(board)
        random.shuffle(aux)
        boards.append(aux)
    return boards

def check(position1, position2):
    """Verifies if two queens are checking"""
    position1Row = position1[0]
    position1column = position1[1]
    while (position1column <= position2[1]):
        position1Row+=1
        position1column+=1
        if position1Row == position2[0] and position1column == position2[1]:
            return -1
    position1Row = position1[0]
    position1column = position1[1]
    while (position1column <= position2[1]):
        position1Row-=1
        position1column+=1
        if position1Row == position2[0] and position1column == position2[1]:
            return -1  
    return 0

def fitness(board):
    """Returns the fitness value of the board"""
    checks = 0
    for i in range(len(board)):
        for j in range(len(board))[i+1:]: 
            checks+=check([board[i],i],[board[j],j])
    return checks

def fatherSelection(boards):
    """Returns the fathers, """
    individues = range(len(boards))
    shuffle(individues)
    individues = individues[0:5]
    map = {}
    for i in individues: 
        map[i]=fitness(boards[i])
    order = sorted(map, key=map.get)
#    print order
    return [boards[order[len(order)-1]],boards[order[len(order)-2]]] 

def geneticCross(father1, father2):
    c = random.randint(0,len(father1)-1)
    son1 = father1[:c]
    son2 = father2[:c]
    for i in father2: 
        if not i in son1:
            son1.append(i)
    for i in father1: 
        if not i in son2:
            son2.append(i)
    return [son1, son2]

def geneticMutation(board):
    num1 = random.randint(0,len(board)-1)
    num2 = random.randint(0,len(board)-1)
    aux=board[num1]
    board[num1]=board[num2]
    board[num2]=aux
    print board


if __name__ == '__main__':
    queens = 8
    initialPopulation = 10
    iterations = 1000
    mutationProbability = 15
               
    board = range(queens)    
    boards = randomBoards(board,initialPopulation)

    solutions = []
    for board in boards:
        if(fitness(board) == 0):
            solutions.append(copy.copy(board))
    
#    print boards
#    print solutions


    map = {}
    for i in range(len(boards)): 
        map[i]=fitness(boards[i])
    order = sorted(map, key=map.get)
#    print order
#    print map
    
    
    

    print "Soluciones de la poblacion inicial ",solutions

    for i in range(iterations):
        fathers = fatherSelection(boards)
#        print fathers
        sons = geneticCross(fathers[0],fathers[1])
#        print sons
        for son in sons:
            if(fitness(son) == 0):
                solutions.append(copy.copy(son))        
#        print "----"

        boards[order[0]] = sons[0]
        boards[order[1]] = sons[1]
#    geneticMutation([1,2,3,4,5,6,7,8,9])


    print "Soluciones luego del algoritmo ",solutions



    