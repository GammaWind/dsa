'''
Sub-array with 0 sum
Problem Description

Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

If the given array contains a sub-array with sum zero return 1 else return 0.



Problem Constraints
1 <= |A| <= 100000

-10^9 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return whether the given array contains a subarray with a sum equal to 0.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [-1, 1]


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 No subarray has sum 0.
Explanation 2:

 The array has sum 0.


 APPOCH:  whenever you see subarray question with sum think of prefix sum

 here we generated prefix sum array if there are 2 same elements in prefix array that means that sum between these 2 elemnts is 0

 TC : O(N)
 SC : O(N)
'''





def solve( A):
    preFixSum = [0] * len(A)
    summ = 0
    for i in range(len(A)):
        summ += A[i]
        preFixSum[i] = summ
    hSet = set()
    hSet.add(0)
    for j in preFixSum:
        if j in hSet:
            return 1
        else:
            hSet.add(j)
                
    return 0        



A = [1, 2, 3, 4, 5]
print(solve(A))