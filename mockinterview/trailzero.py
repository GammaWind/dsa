
'''
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

    we need to swap non zero elements with first zero in the array

    hence we need to find first zero 
    
    while traversing array whenever we find nonzero we swap nonzero with firstzero and find new firstzero

    this way we will left with all 0 at the end maintaining order of non zero


'''


def shiftZeros(A):
    if len(A) == 1:
        return A
    firstZero = 0
    
    #finding first zero
    for i in range(len(A)):
        if A[i] == 0:
            firstZero = i
            break
    # we need to search for elements to swap after 0
    currEle = firstZero + 1    
    while currEle < len(A):
        if A[currEle] != 0:
            A[currEle] , A[firstZero] = A[firstZero] , A[currEle]

            
            #finding next zero and setting it as firstZero
            while firstZero < len(A):
                firstZero += 1
                if A[firstZero] == 0:
                    
                    break
        currEle += 1

        




        
            

    
    return A


A = [0,1,12,0,3,0,7]
B = [0,1,1,0,0,0,1]
print(shiftZeros(A))
print(shiftZeros(A))







            


