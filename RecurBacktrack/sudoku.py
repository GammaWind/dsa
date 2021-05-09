'''
Sudoku
Problem Description

Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.



A sudoku puzzle,



and its solution numbers marked in red.



Problem Constraints
N = 9


Input Format
First argument is an array of array of characters representing the Sudoku puzzle.


Output Format
Modify the given input to the required answer.


Example Input
Input 1:

A = [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]


Example Output
Output 1:

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]


Example Explanation
Explanation 1:

Look at the diagrams given in the question.



×
You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.

'''



'''

APPROACH - important parts of solution

1. check function
2.backtracking approach
3. base cases



how to check if the number we are putting in empty box is valid  ? 
1. that number shouldnt be in the same row 
2. shouldnt be in same column
3. shouldnt be in the 3*3 sub box

so we need a Check Function which given a number can verify if the number is present in that row , coulmn and the 3*3 box
checking the number in row col is easy but how would you check given row col that a number is unique in 3*2 sub matrices ????


well we can find the top left of the 3*3 sub matrices using some trick and if we have top left of box we cn scan of the element untill right bottom
so to point top left what we can do divide given indexes by 3 and multipy by 3
so this is check function



now how do we actually solve this problem? it might happend that if we place a number at empty box which is valid at that time but going forward it will make other numbers invalid i.e. will lead us to wrong combinations so we block ourselfs 

so to deal with this we use backtracking
so the appoach is to find empty box row by row and if found try putting number in that box starting from 1 to 9 if valid and apply our check function,
if check function is valid then good we return True 
but if check function doesnt return true then we backtrack that means we make that box again empty.

but hold on, this is recursion ,right ?????????
think of the base cases ???????? will you ???????


lets say you reach at the last row ???
what does it mean? it means that you have successfully filed all boxes so return true
i.e. if row >= 9:
        return True
    also 
        if col > 9:
            row += 1
            col = 0    





'''

def solveSudoku(A):
    solve(A, 0, 0)
    
    
    
def check( board, row, col, isValidNum):
    for i in range(9):
            
        if board[row][i] == str(isValidNum) or board[i][col] == str(isValidNum):
            return False
    x = (row//3) * 3
    y = (col//3) * 3
            
    for u in range(3):
        for v in range(3):
            if board[x + u][y + v] == str(isValidNum):
                return False
    return True     
        # for i in range(0,9):
        #     if board[row][i] == isValidNum:
        #         return False
        #     if board[i][col] == isValidNum:
        #         return False
        # rowGroup = (row//3) * 3
        # colGroup = (col//3) * 3 
        # for i in range(rowGroup, rowGroup+3):
        #     for j in range(colGroup, colGroup+3):
        #         if board[i][j] == isValidNum:
        #             return False
        # return True
        
def solve( board , row, col):
    if col >= 9:
        col = 0
        row += 1
            
    if row >= 9:
        return True
            
    if board[row][col] != '.':
        return solve(board, row, col + 1)
        
        
    elif board[row][col] == '.': 
        for i in range(1,10):
            if check(board, row, col, str(i)):
                board[row][col]= str(i)
                    
                if solve(board, row, col + 1):
                    return True
                board[row][col] = '.'    
        
    return False


A = [['5','3','.','.','7','.','.','.','.'], ['6','.','.','1','9','5','.','.','.'], ['.','9','8','.','.','.','.','6','.'], ['8','.','.','.','6','.','.','.','3'], ['4','.','.','8','.','3','.','.','1',], ['7','.','.','.','2','.','.','.','6'], ['.','6','.','.','.','.','2','8','.'], ['.','.','.','4','1','9','.','.','5'], ['.','.','.','.','8','.','.','7','9']]
print(solveSudoku(A))
print(A)

