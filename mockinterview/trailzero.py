
'''

 COUNT SORT PROBLEM
2) [0,1,0,0,1,0] description is same as 3

if A = 




3)
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''



'''
Approach 

    take firstnonzero var start from 0
    if we add all nonzero to array from start with firstnonzero index increasing

    then we can add left zeros in array from firstnonzero to last


'''


def shiftZeros(A):

    if len(A) == 1:
        return A
    
    
    
    


    firstnonZero = 0

    for i in range(len(A)):
        if A[i] != 0:
            A[firstnonZero] = A[i]
            firstnonZero += 1

    for j in range(firstnonZero,len(A)):
        A[j] = 0        

    
  
    return A
            
    

        




        
            

    


A = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
B = [0,0,0,0,0,0,0]

print(shiftZeros(A))
print(shiftZeros(B))







            


