'''
NQueens
Problem Description

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer A, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.



Problem Constraints
1 <= A <= 10



Input Format
First argument is an integer n denoting the size of chessboard



Output Format
Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.



Example Input
Input 1:

A = 4
Input 2:

A = 1


Example Output
Output 1:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Output 1:

[
 [Q]
]


Example Explanation
Explanation 1:

There exist only two distinct solutions to the 4-queens puzzle:
Explanation 1:

There exist only one distinct solutions to the 1-queens puzzle:

APPROACH: BACKTRACKING

here the thing to notice is once you place a queen in one row you wont be able to place in that row again.

in each row we will traverse all the colums untill we found a position for which check funtion returns true. .i.e. a valid position for the ueen being placed.

check function will consists of 3 parameters :  board ,  row , columns
for the given row and column we will try to check if there exist a queen in same row, same column and to its diagonal positions

Now comes the recursion and backtarcking part

for each column in the given row we will try to find if the row column pos is valid if its a valid pos given by check function then we will try to place quin in next row so we will place q in valid pos row,col and call the recusrsion for row + 1 th row
lets say if we are blocked then we need to erase the placed queen so once recursion is ended we will remove the queen q from valid pos row col


also the base case would be if the row == the A ie. 4 (for 4*4 board) then we will store the answer in our answer (global) list
so to sum so by this way 
for first row our function will try to find the perfect palcements fro the queen for each column so this way we will get all of the answers


Time complexity analysis:


'''

                
                    
def solveNQueens(A):
    board = [['.']*A for _ in range(A)]
    ans = []
        
    def check(board, u ,v):
        for i in range(A):
            for j in range(A):
                if board[i][j] == 'Q':
                    if i == u or j == v or ((i - j) == (u - v)) or ((i + j ) == (u + v)):
                        return False
            
        return True
    def solve(board,row,ans):
        if row == A:
            newAns = [''.join(i) for i in board]
            ans.append(newAns.copy())
            return True
            
        for c in range(A):
                
            if check(board,row,c):
                board[row][c] = 'Q'
                solve(board,row + 1,ans)
                board[row][c] = '.'
                    
    solve(board,0,ans)
        
    return ans

A = 4

print(solveNQueens(A))