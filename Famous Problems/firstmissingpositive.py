'''
First Missing Integer
Problem Description

Given an unsorted integer array A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.



Problem Constraints
1 <= N <= 1000000

-109 <= A[i] <= 109



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the first missing positive integer.



Example Input
Input 1:

[1, 2, 0]
Input 2:

[3, 4, -1, 1]
Input 3:

[-8, -7, -6]


Example Output
Output 1:

3
Output 2:

2
Output 3:

1


Example Explanation
Explanation 1:

A = [1, 2, 0]
First positive integer missing from the array is 3.

'''


'''

TRICK TO SOLVE IN O(N) IS TO FOCUS ON INDEX BCOZ THE NUMBERS SUPPOSED TO BE HERE ARE 1-N

TRAVERSE ECH ELEMENT AND IF ELEMENT IS VALID IE. IF ELEMTNT > 0 AND eLEMENT <= N then 
swap the elemtnt with its actual index untill elemnt is equl to index or we get some invalid elemtnt
 A[i] , A[correctPos] = A[correctPos] , A[i]

'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        for i in range(len(A)):
            correctPos = A[i]-1
            while 1 <= A[i] <= len(A) and A[i] != A[correctPos]:
                
                #swap
                A[i] , A[correctPos] = A[correctPos] , A[i]
                correctPos = A[i]-1
                
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
        return len(A) + 1
                
