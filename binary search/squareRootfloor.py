'''
Square Root of Integer
Problem Description

Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.



Problem Constraints
0 <= A <= 1010



Input Format
The first and only argument given is the integer A.



Output Format
Return floor(sqrt(A))



Example Input
Input 1:

 11
Input 2:

 9


Example Output
Output 1:

 3
Output 2:

 3


Example Explanation
Explanation:

 When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
 When A = 9 which is a perfect square of 3, so we return 3.



 APPROACH:
 here trick is that we know that sqrt of A can lie between 1 to A//2
 idea is to apply binary search for possible sqrts and manipulate on basis of sqrt * sqrt
 but this would only work for perfect sqrts how we deal with not perfect squares ???

 notice here we will specify if mid * mid == A then return mid

 here thing to notice is that if lets say A = 9 and A = 11
 so for both floor(sqrt) would be 3

 so lets say if mid * mid < A then we can store it as possible answer and try to get bigger hence start would be mid  + 1

'''

















import sys
def sqrt( A):
    if (A == 0 or A == 1) :
        return A        
    start = 1
    end  = A//2
    ans = sys.maxsize
    while start <= end:
        mid = (start + end)//2
        if mid * mid == A:
            return mid
        if mid * mid > A:
            end  = mid -1
        elif mid * mid < A:
            ans = mid
            start = mid + 1
    return ans        


print(sqrt(11))