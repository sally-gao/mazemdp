from MazeGenAlgo import MazeGenAlgo
from MazeGenAlgo import np
from random import choice, randrange
from mdpstate import MDPState
from copy import deepcopy
import random


"""
Duncan Rule, Sally Gao, Yi Hao
"""

"""
Adapted from:
https://github.com/illiterati1/python_maze
"""


class AldousBroder(MazeGenAlgo):
    """
    1. Choose a random cell.
    2. Choose a random neighbor of the current cell and visit it. If the neighbor has not
        yet been visited, add the traveled edge to the spanning tree.
    3. Repeat step 2 until all cells have been visited.
    """

    def __init__(self, h, w):
        super(AldousBroder, self).__init__(h, w)

    def generate(self):
        random.seed(0)
        # create empty grid, with walls
        a = np.empty((self.H, self.W), dtype=str)
        a.fill('#')
        grid = a

        crow = randrange(1, self.H, 2)
        ccol = randrange(1, self.W, 2)
        grid[crow][ccol] = ' '
        num_visited = 1

        while num_visited < self.h * self.w:
            # find neighbors
            neighbors = self._find_neighbors(crow, ccol, grid, True)

            # how many neighbors have already been visited?
            if len(neighbors) == 0:
                # mark random neighbor as current
                (crow, ccol) = choice(self._find_neighbors(crow, ccol, grid))
                continue

            # loop through neighbors
            for nrow, ncol in neighbors:
                if grid[nrow][ncol] != ' ':
                    # open up wall to new neighbor
                    grid[(nrow + crow)//2][(ncol + ccol)//2] = ' '
                    # mark neighbor as visited
                    grid[nrow][ncol] = ' '
                    # bump the number visited
                    num_visited += 1
                    # current becomes new neighbor
                    crow = nrow
                    ccol = ncol
                    # break loop
                    break
                
            #gridcopy = [['#']*len(grid[0]) for row in grid]
            #for i in range(len(grid)):
            #    for j in range(len(grid[i])):
            #        if grid[i][j] == 0:
            #            gridcopy[i][j] = ' '

        return(grid.tolist())
        
def maze_to_mdp(maze):
    
    """Returns a matrix of MDPState objects for each free space in a maze"""
    
    grid = deepcopy(maze)

    for i in range(1, len(maze) - 1):
        for j in range(1, len(maze[i]) - 1):
            
            #represent walls as #
            if maze[i][j] == '#':
                grid[i][j] = '#'
                continue
                
            if maze[i-1][j] == '#':
                north = (i, j)
            else:
                north = (i-1, j)
                
            if maze[i+1][j] == '#':
                south = (i, j)
            else:
                south = (i+1, j)
                
            if maze[i][j+1] == '#':
                east = (i, j)
            else:
                east = (i, j+1)
                
            if maze[i][j-1] == '#':
                west = (i, j)
            else:
                west = (i, j-1)
                
            grid[i][j] = MDPState(north, south, west, east)
            
    grid[1][1].reward = 10
            
    return(grid)
    
if __name__ == '__main__':
    test = AldousBroder(3, 3).generate()    
    print(test)