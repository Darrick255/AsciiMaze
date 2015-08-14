from random import randint
import random
import time
import heapq
import pprint
import cmd
import math


def main():
    """main logic. returns None."""
    divWidth = 50
    divHeight = 50
    startX = randint(0, divWidth-1)
    startY = randint(0, divHeight-1)
    for x in range(1):
        div = [[0 for x in range(divWidth)]
               for x in range(divHeight)]  # 0b1111 15 solid
        carveDivIter(startX, startY, div)
    print(printAsciiGrid(div))
    # print(startX, startY)
    # path = pathToList(astar([divWidth-1, divHeight-1], [0, 0], div), [divWidth-1, divHeight-1])
    # print(path)
    # print(printAsciiGrid2(div,path))
    # gLoop([divHeight-1,divWidth-1], div)
# 0   = 0b000000 = all 4 walls
# 1   = 00000001 = no north wall
# 2   = 00000010 = no south wall
# 4   = 00000100 = no east wall
# 8   = 00001000 = no west wall
# 16  = 00010000 = start
# 32  = 00100000 = map&compass
# 64  = 01000000 = lock
# 128 = 10000000 = door
# 0b11111111


# def carveDiv(startX,startY, myDiv):
#     directions = [[0,-1,0b1,0b10,'N'],
#                   [0,1,0b10,0b1,'S'],
#                   [1,0,0b100,0b1000,'E'],
#                   [-1,0,0b1000,0b100,'W']]
#     random.shuffle(directions)
#     for direction in directions:
#         nx = startX + direction[0]
#         ny = startY + direction[1]
#         if ((0 <= ny <= len(myDiv)-1) and (0 <= nx <= len(myDiv[0])-1) and 
    # myDiv[ny][nx] == 0):
#             myDiv[startY][startX] |= direction[2]
#             myDiv[ny][nx] |=direction[3]
#             # print(printAsciiGrid(myDiv))
#             carveDiv(nx,ny, myDiv)
# [row[start_col:end_col] for row in matrix[start_row:end_row]] slice 2d array
def gLoop(start,div):
    def move(player, direction):
        pass
        # return player location
    def drawAllCam(player, div, objects =[], camera=[10,10]): #add a camera view size and scrolling so the player may see 20x20 of a 200x200 grid
        pass
        divBuffer = printAsciiGrid2([row[player[1] - math.floor(camera[1]/2):player[1] + math.floor(camera[1]/2)+1] for row in div[player[0] - math.floor(camera[0]/2):player[0] + math.floor(camera[0]/2)+1]])


        # return map string wity player
    def isLost(player):
        return player[0] == 0 and player[1] == 0
    print('drawing all')
    drawAllCam([15,15], div)
    while(isLost(player) or False):
        pass
        # game loop
        # draw grid based on camera size
        # wait for input
        # move 
        # end loop


def animatePath(div, path, speed):
    while(len(path)):
        # drawAscii
        time.sleep(speed)


def carveDivIter(startX, startY, myDiv):
    """
    An interative version of the recursive backtracking algorithm to generate
    a maze.modifies mydiv array in place. returns None
    """
    stack = []
    stack.append([startX, startY])
    directions = [[0, -1, 0b1, 0b10, 'N'],
                  [0, 1, 0b10, 0b1, 'S'],
                  [1, 0, 0b100, 0b1000, 'E'],
                  [-1, 0, 0b1000, 0b100, 'W']]
    while(len(stack)):
        current = stack[len(stack)-1]
        cX = current[0]
        cY = current[1]
        random.shuffle(directions)
        for direction in directions:
            nx = cX + direction[0]
            ny = cY + direction[1]
            if ((0 <= ny <= len(myDiv)-1) and (0 <= nx <= len(myDiv[0])-1) and
                    (myDiv[ny][nx] == 0)):
                myDiv[cY][cX] |= direction[2]
                myDiv[ny][nx] |= direction[3]
                # print(printAsciiGrid2(myDiv))
                # time.sleep(.005)
                stack.append([nx, ny])
                break
        if current == stack[len(stack)-1]:
            stack.pop()


def printGrid(grid):
    """
    Builds a string representing the maze in integer format.
    returns this string.
    """
    gridBuffer = '\n'
    for row in grid:
        for e in row:
            gridBuffer += ("{0:02d}".format(e) + " ")
        gridBuffer += '\n'
    return gridBuffer


def printAsciiGrid(grid, locations=[]):
    """
    Builds a string representation of the maze using ' ','_', and '|'.
    returns this string.
    """
    # N = 0b00000001
    S = 0b00000010
    E = 0b00000100
    # W = 0b00001000
    gridBuffer = ''
    exit = ''
    exit += '\n'
    exit += 'EXIT\n'
    exit += ' |\n'
    exit += ' V\n'
    gridBuffer += ('  ' + '_' * (len(grid[0]) * 2 - 2) + '\n')
    for y in range(len(grid)):
        gridBuffer += ('|')
        for x in range(len(grid[0])):
            gridBuffer += (' ' if (grid[y][x] & S != 0) else '_')
            if grid[y][x] & E != 0:
                gridBuffer += (
                    ' ' if ((grid[y][x] | grid[y][x+1]) & S != 0) else '_')
            else:
                gridBuffer += ('|')
        gridBuffer += ('\n')

        if len(locations):
            print(gridBuffer.split('\n'))
    return exit + gridBuffer


def printAsciiGrid2(grid, solution=[]):
    """
    Builds a string representation of the maze using ' ','_', and '|'.
    returns this string.
    """
    # N = 0b00000001
    S = 0b00000010
    E = 0b00000100
    # W = 0b00001000
    gridBuffer = ''
    exit = ''
    exit += '\n'
    exit += 'EXIT\n'
    exit += ' |\n'
    exit += ' V\n'
    gridBuffer += ('EXIT' + '==' * (len(grid[0]) * 2 - 1) + '\n')
    for y in range(len(grid)):
        gridBuffer += ('||')
        for x in range(len(grid[0])):
            gridBuffer += ('  ' if (grid[y][x] & S != 0) else '  ')
            if grid[y][x] & E != 0:
                gridBuffer += (
                    '  ' if ((grid[y][x] | grid[y][x+1]) & S != 0) else '  ')
            else:
                gridBuffer += ('||')
        gridBuffer += ('\n')
        gridBuffer += ('||')
        for x in range(len(grid[0])):
            gridBuffer += ('  ' if (grid[y][x] & S != 0) else '==')
            if grid[y][x] & E != 0:
                gridBuffer += (
                    '  ' if ((grid[y][x] | grid[y][x+1]) & S != 0) else '==')
            else:
                gridBuffer += ('||')
        gridBuffer += ('\n')

    gridBufferlist = list(gridBuffer)
    for index, x in enumerate(solution[:len(solution)-1]):
        cx = (x[0]*4+2+1)
        cy = (len(grid[0])*4+2+1)*(1+x[1]*2)
        # print(cx,cy)
        # print('x:',x)
        gridBufferlist[cy+cx]=solution[index+1][2]
        # make list draw solution.
        print(''.join(gridBufferlist))
        time.sleep(.1)

    return exit + ''.join(gridBufferlist)


# state [x,y] g distance path(history of movements)def __init__(self):
class Node:

    """Node objects represent the current state for the a* algorithm."""

    def __init__(self, state, g, path, move):
        self.state = state
        self.g = g
        self.path = path + move

    def __lt__(self, other):
        return self.g < other.g


def astar(start, goal, div):  # function A*(start,goal)
    """
    pathfinding algorithm using manhatan distance heuristic to find the
    shortest path from start to goal. returns a string representing the path
    that must be taken. Returns None.
    """
    closedset = set()
    openset = []
    startNode = Node(start, 0, '', '')
    heapq.heappush(openset, (fValue(startNode, goal), startNode))
    while(len(openset)):
        current = heapq.heappop(openset)[1]
        if (current.state == goal):
            return current.path
        closedset.add(str(current.state))
        for x in [[current.state[0]+0, current.state[1]+1],
                  [current.state[0]+0, current.state[1]-1],
                  [current.state[0]+1, current.state[1]+0],
                  [current.state[0]-1, current.state[1]+0]]:
            if(x not in [row[1].state for row in openset]):
                if ((current.state[1]-x[1]) == 1 and isNoWall(current.state, x, div,'N')):
                    curMove = 'N'
                elif ((current.state[1]-x[1]) == -1 and isNoWall(current.state, x, div,'S')):
                    curMove = 'S'
                elif ((current.state[0]-x[0]) == -1 and isNoWall(current.state, x, div,'E')):
                    curMove = 'E'
                elif ((current.state[0]-x[0]) == 1 and isNoWall(current.state, x, div,'W')):
                    curMove = 'W'
                else:
                    continue
                nextNode = Node(x, current.g+1, current.path, curMove)
                heapq.heappush(openset, (10, nextNode))


def isNoWall(currentXY, nextXY, div, direction):
    directions = {'N': 1, 'S': 2, 'E': 4, 'W': 8, }
    reverse = {'N': 2, 'S': 1, 'E': 8, 'W': 4, }
    if not ((0 <= currentXY[1] <= len(div)-1) and (0 <= currentXY[0] <= len(div[0])-1) and (0 <= nextXY[1] <= len(div)-1) and (0 <= nextXY[0] <= len(div[0])-1)):
        return False
    here = div[currentXY[1]][currentXY[0]]
    there = div[nextXY[1]][nextXY[0]]
    return here & directions[direction] == directions[direction] and there & reverse[direction] == reverse[direction]


def fValue(node, goal):
    h = abs(node.state[0]-goal[0]) + abs(node.state[1]-goal[1])
    f = node.g + h
    return f

def pathToList(path, start):
    icons = {'N' :'^', 'S' :'v', 'E' :'>', 'W' :'<'}
    distance= {'N' :[0,-1], 'S' :[0,1], 'E' :[1,0], 'W' :[-1,0]}
    outlist = []
    outlist.append([start[0], start[1], 'X'])
    location = start
    pathlist = list(path)
    for x in pathlist:
        location[0] += distance[x][0]
        location[1] += distance[x][1]
        outlist.append([location[0],location[1],icons[x]])
    outlist.append([0,0,'E'])
    return outlist




if __name__ == "__main__":
    main()