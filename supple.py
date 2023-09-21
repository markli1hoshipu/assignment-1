# just a few function that i felt ur game.py might modify with:

#case 1: still using <pacman_x, pacman_y = path>
def valid_return(grid,pos,re):
    if re[0] >=len(grid) or re[1] >=len(grid):
        return False
    pos_move = [[0,1],[0,-1],[1,0],[-1,0],[0,0]]
    if [re[0]-pos[0],re[0]-pos[0]] not in pos_move:
        return False
    if grid[re[0]][re[1]] == '1':  #here i'll assume nobody is teleporting the pac-bot to outside of walls
        return False
    return True

# case 2: use <pacman_x += path[0],pacman_y += path[1]>
def valid_move(grid,start,move):
    pos_move = [[0,1],[0,-1],[1,0],[-1,0],[0,0] ]
    if move not in pos_move:
        return False
    pos = [start[0]+move[0],start[1]+move[1]]
    if grid[pos[0]][pos[1]] == 1:
        return False
    return True