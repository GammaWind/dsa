'''
Problem Description

Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks.

The first stair would require only one block, the second stair would require two blocks and so on.

Find and return the maximum height of the staircase.



Problem Constraints
0 <= A <= 109


Input Format
The only argument given is integer A.



Output Format
Return the maximum height of the staircase using these blocks.



Example Input
Input 1:

 A = 10
Input 2:

 20


Example Output
Output 1:

 4
Output 2:

 5



 APPROACH:
    here you can easily use sum of natural number formula ie. (n * (n+1))//2 and calculate the required blocks in order to form n levels.

    Brute force would be to try the values of n from 1 to untill A is flushed. 
    TC O(sqrt(N))

    Optimazed using binary search to log(N):
    how ?
    find the mid and try if n is feasible for give A
    if yes then try greater values of n
    if not then try smaller values of n




    '''


def maxHeight(A):
    start = 0
    end  = A
    ans = -1
    
    while start <= end:
        mid  = (start + end) // 2
        cost = (mid * (mid + 1))//2
        print((mid,cost))
        if cost == A:
            return mid
        if cost <= A:
            ans  = mid
        if cost < A:
            start = mid + 1
        elif cost > A:
            end = mid - 1
    return ans

print(maxHeight(28))


    