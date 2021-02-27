# Pascal Triangle
# Given numRows, generate the first numRows of Pascal's triangle.

# Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

# Example:

# Given numRows = 5,

# Return

# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

def pascalT(A):
    if A == 0:
        return [0]

    ansArr = [[1]]
    if A > 1:
        ansArr.append([1,1])
    if A > 2:    
            for i in range(2,A):
                adder = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        adder.append(1)
                    else:
                        adder.append(ansArr[i - 1][j] + ansArr[i - 1][j - 1])
                ansArr.append(adder)  
    return ansArr            

print(pascalT(5))
