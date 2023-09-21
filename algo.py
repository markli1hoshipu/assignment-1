# You can modify this file to implement your own algorithm
# The algorithm should return only the next direction in the form of [x, y]

from constants import *

"""
You can use the following values from constants.py to check for the type of cell:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""

"""
honestly i know this is not efficient but i wrote it at 1am just when the assignments are posted 
so all i did was going from left to right :)
good night!!!!
P.S. looking at the pacman moving around was fun
"""

def find_path(grid, st, ed):  
    explored = {tuple(st): [st]}
    pos_move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while tuple(ed) not in explored:
        temp_dict = {}
        for pos in explored:
            for move in pos_move:
                if valid_move(grid, pos, move):
                    new_pos = (pos[0] + move[0], pos[1] + move[1])
                    if new_pos not in explored:
                        new_path = explored[pos] + [new_pos]
                        temp_dict[new_pos] = new_path
        explored.update(temp_dict)
    return explored[tuple(ed)]

def valid_move(grid,start,move):
    pos_move = [[0,1],[0,-1],[1,0],[-1,0]] #[0,0] not included
    if move not in pos_move:
        return False
    pos = [start[0]+move[0],start[1]+move[1]]
    if grid[pos[0]][pos[1]] == 1:
        return False
    return True

def find_first_eat(grid):
    print(grid[3][5])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                return [i,j]
    return 'finished'


def get_next_direction(grid, start):
    #you should change <pacman_x, pacman_y = path> to <pacman_x += path[0], pacman_x += path[1]> if you want 'direction'
    # :)
    pos = find_first_eat(grid)
    print(pos)
    if pos == 'finished':
        return [0,0]
    path = find_path(grid,start,pos)
    return path[1]