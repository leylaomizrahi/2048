from Grid import Grid
from BaseAI import BaseAI
import math 
import time


class PlayerAI(BaseAI):

    def getMove(self, grid):
        start = time.time() 
        chosenone= None
        bigmac = float("-inf")   
        alpha = float("-inf")
        beta = float("inf")  
        moves = getPlayerChildren(grid,1)     
        move = moves[0][1]
        branch = len(grid.getAvailableCells())
        maxdepth = 2

        if branch > 10: 
            maxdepth = 1
 
        if branch < 4:
            maxdepth = 3

        if len(moves) != 1: 
            for i in range(len(moves)):
                child = moves[i][0]
                depth = maxdepth 
                if child.getAvailableCells() > 3: 
                    depth = 2
                else: 
                    depth = maxdepth
                dir = moves[i][1]
                max = minalg(child, depth, alpha, beta)
                if max > bigmac: 
                    move = dir
                    bigmac = max 
                    chosenone = child
 
        
        print "depth: " , maxdepth
        #numbers = getSameAdjacent(grid)
        #no = []
        #for i in range(1,len(numbers)):
        #   no.append(numbers[i][0])
        #print "Could have been: ", getCould(no)
        #print "But is", no 
        #print getSameAdjacent(grid)[0]
        #print "heuristic:" , getHeuristic(grid)

        end = time.time()
        print "time:", end-start
        return move           



def getHeuristic(grid): 
    numbers = getSameAdjacent(grid)
    no = getCould(numbers)
    max = grid.getMaxTile()
    heuristic = (max/numbers[0])* 2

   #if heuristic is only max/numbers it still performs well and faster: make getNumbers return adj          
    
    for i in range(1,len(numbers)):
        no.append(numbers[i][0])

    if max == grid.map[0][0]:
        heuristic = heuristic +  math.log(max,2) 

    diftile = max - no[len(no)-1] 
    diflen = len(numbers)- len(no)

    if diflen != 0: 
        diftile = diftile/diflen
    else: 
        heuristic = heuristic + impossible(grid,no)


    heuristic = heuristic + gridDesign(grid,no,max) + diftile
    return heuristic 


def impossible(grid, no): 
    #best possible way the best grid could have been layed out
    heuristic = 0 
    while(j < 4 ):                                                                                                                                        
        if grid.map[0][j] == no[len(no)-1-j] or grid.map[j][0] == no[len(no)-1-j]:                                
            heuristic =  heuristic + math.log(no[len(no)-1-j])                                                                                          
        else:                                                                                                                                              
            break                                                                                                                                          
        j = j+1                                                                                                                                            
    return heuristic

def gridDesign(grid, no, max): 
    #best possible way the grid could be layed out 
    heuristic = 0 
    j = 0
    while(j < 4 ):  
        if grid.map[0][j] == max / (j+1): 
            heuristic = heuristic + math.log(max,2) 
        else: 
            break 
        j = j+1
        
    return heuristic 

def getSameAdjacent(grid):
    #get differance between numbers and all of the numbers  
    adj = 1
    numbers = []
    n = grid.size 
    for x in xrange(n):
        for y in xrange(n):
            if grid.map[x][y] != 0:
                    title = math.log(grid.map[x][y],2) 
                    if x != 0 and grid.map[x-1][y] != 0:  
                        adj =  adj + abs(title - math.log(grid.map[x-1][y],2))
                    
                    if y != 0 and grid.map[x][y-1] != 0:
                        adj =  adj + abs(title - math.log(grid.map[x][y-1],2))                        
                    numbers.append((grid.map[x][y],x,y))
                    
    numbers.sort()
    numbers.insert(0,adj)

    return numbers
  # return adj 


def getCould(no):
    numbers = list(no)
    i = 0 
    while(True): 
        if len(numbers) == i+1:
            break
        if numbers[i] == numbers[i + 1]: 
            numbers[i] = numbers[i]*2  
            del numbers[i+1]
            numbers.sort() 
            i = 0 
        else: 
            i = i+1 

    return numbers


def getComputerChildren(grid): 
#possible next moves of the computer
    cells = grid.getAvailableCells()
    children = []

    for cell in cells: 
        for i in range (1,3):
            gridCopy = grid.clone()
            gridCopy.setCellValue(cell, 2 * i)  
            children.append(gridCopy)

    return children 


def getPlayerChildren(grid , no ):
#possible next moves of player
    moves = grid.getAvailableMoves()
    children = []
 
    for move in moves:
        gridCopy = grid.clone()
        gridCopy.move(move)
        if no == 1: 
            children.append((gridCopy,move))
        if no == 2: 
            children.append(gridCopy)
    return children 


def maxalg(grid, lim , alpha, beta):
#PlayerAI picks
    if lim == 0: 
        return getHeuristic(grid) 
    children = getPlayerChildren(grid,2)                                                                                                          
    current = float("-inf")

    for board in children: 
       max = minalg(board,lim - 1, alpha, beta) 
       if max > current: 
           current = max 
       if current >= beta:
            return current
       if current > alpha: 
           alpha = current 

    return current 


def minalg(grid, lim , alpha, beta): 
#Computer AI picks
    if lim == 0:
        return getHeuristic(grid)
    children = getComputerChildren(grid)
    current = float("inf")

    for board in children:
        min = maxalg(board,lim - 1, alpha, beta)
        if min < current: 
            current = min 
        if current <= alpha: 
            return current 
        if current < beta: 
            beta = current 
 
    return current       
