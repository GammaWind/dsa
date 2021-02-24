
# Problem Description

# You are given a n x n 2D matrix A representing an image.

# Rotate the image by 90 degrees (clockwise).

# You need to do this in place.

# Note: If you end up using an additional array, you will only receive partial score.

# nput 1:

#  [
#     [1, 2],
#     [3, 4]
#  ]
# Input 2:

#  [
#     [1]
#  ]


# Example Output
# Output 1:

#  [
#     [3, 1],
#     [4, 2]
#  ]
# Output 2:

#  [
#     [1]
#  ]



def solve(A):
        
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            A[i][j],A[j][i] = A[j][i],A[i][j]
    for i in A:
        i.reverse()
        
    return A
arr = [[1,2],[3,4]]
ans  = solve(arr) 
print(ans)   