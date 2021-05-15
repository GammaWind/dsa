'''
MAXIMUM AND MINIMUM MAGIC
Problem Description

Given an array of integers A of size N where N is even.

Divide the array into two subsets such that

1.Length of both subset is equal.
2.Each element of A occurs in exactly one of these subset.
Magic number = sum of absolute difference of corresponding elements of subset.

Note: You can reorder the position of elements within the subset to find the value of magic number.

For Ex:- 
subset 1 = {1, 5, 1}, 
subset 2 = {1, 7, 11}
Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12
Return an array B of size 2, where B[0] = maximum possible value of Magic number modulo 109 + 7, B[1] = minimum possible value of a Magic number modulo 109 + 7.



Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109

N is even



Input Format
The first argument given is the integer array A.



Output Format
Return an array B of size 2, where B[0] = maximum possible value of Magic number % 109 + 7,B[1] = minimum possible value of a Magic number % 109 + 7.



Example Input
Input 1:

 A = [3, 11, -1, 5]
Input 2:

 A = [2, 2]


Example Output
Output 1:

 [14, 10]
Output 2:

 [0, 0]


Example Explanation
Explanation 1:

 All possible magical numbers:-
 sub1 = {3, 11}, sub2 = {-1, 5}, Magic Number = abs(3 - -1) + abs(11 - 5) = 10
 sub1 = {3, -1}, sub2 = {11, 5}, Magic Number = abs(3 - 11) + abs(-1 - 5) = 14 
 sub1 = {3, 5}, sub2 = {11, -1}, Magic Number = abs(3 - 11) + abs(5 - -1) = 14
 sub1 = {11, -1}, sub2 = {3, 5}, Magic Number = abs(11 - 3) + abs(-1 - 5) = 14
 sub1 = {11, 5}, sub2 = {3, -1}, Magic Number = abs(11 - 3) + abs(5 - -1) = 14
 sub1 = {-1, 5}, sub2 = {3, 11}, Magic Number = abs(-1 - 3) + abs(5 - 11) = 10 
 maximum of all magic number = 14 % 10^9 + 7 = 14
 minimum of all magic number = 10 % 10^9 + 7 = 10
Explanation 2:

 Answer is evident.
'''

'''
Approach : solution is easy if we obeserve 
            If we sort the elements and put adjusent elements in diff arrays and subtract each other it will give min values
            vice versa if we diveide sorted array in 2 parts the differece would be more which will result in maximum magic value

            here we dont actually need to create 2 subarrays

            TC = nlogn (sorting)
            SC = O(1)

        CORNER CASES : none

'''


def solve( A):
    A.sort()
    minn = 0
    maxx = 0
    i = 0
    while i < len(A)-1:
        diff  = A[i+1] - A[i]
        minn += diff
        i += 2
    j = 0
    k = len(A) // 2
        
    while j < len(A) // 2 :
        diff  = A[k] - A[j]
        maxx += diff
        j += 1
        k += 1
            
            
        
        
    return [maxx% 1000000007, minn % 1000000007]        
        

A = [3, 11, -1, 5]
print(solve(A))