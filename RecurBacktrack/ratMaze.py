'''
rat maze problem
determin if a rat starts ibn given 2d matrix will be able to reach food which is kept at bottom right 

given matrix  N * M

start  = A[0][0]
end / food at A[N-1][M-1]


We have discussed Backtracking and Knight’s tour problem in Set 1. Let us discuss Rat in a Maze as another example problem that can be solved using Backtracking.

A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down. 

In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination. Note that this is a simple version of the typical Maze problem. For example, a more complex version can be that the rat can move in 4 directions and a more complex version can be with a limited number of moves.





'''

def check(maze,x,y):
    N = len(maze)-1
    M = len(maze[0])-1
    print(x,y)
    if x == N and y == M:
        return True
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if maze[x][y] > 0:
        return False

    maze[x][y] = 2

    return check(maze, x + 1, y) or check(maze, x-1, y) or check(maze, x, y + 1) or check(maze, x, y -1 )                    






maze = [ [0, 1, 1, 1],
             [0, 0, 1, 0],
             [1, 0, 1, 1],
             [0, 0, 0, 0] ]

print(check(maze,0,0)) 
           



prod



