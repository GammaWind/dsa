'''
Sum the Difference
Problem Description

Given an integer array A of size N.
You have to find all possible non-empty subsequence of the array of numbers and then, for each subsequence, find the difference between the largest and smallest numbers in that subsequence Then add up all the differences to get the number.

As the number may be large, output the number modulo 1e9 + 7 (1000000007).

NOTE: Subsequence can be non-contiguous.



Problem Constraints
1 <= N <= 10000

1<= A[i] <=1000



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the output.



Example Input
Input 1:

A = [1, 2]
Input 2:

A = [1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

All possible non-empty subsets are:
[1]    largest-smallest = 1 - 1 = 0
[2]    largest-smallest = 2 - 2 = 0
[1 2]  largest-smallest = 2 - 1 = 1
Sum of the differences = 0 + 0 + 1 = 1
So, the resultant number is 1
Explanation 2:

 Only 1 subsequence of 1 element is formed.
 


 
 APPROACH :  HERE trick is to measure the contribution of each element as max and min in each subarrays
 to do so easily we need to sort the array if we sort then we can easily calculate the contribution of elemt ]]

 lets say we have array [1,2,3,4,5] which is sorted
 then we can say that 3 element occures as minimum in 2 to the power 2 times i.e. the number of elemets to its right
 so in total 4 subarrays 3 will act as minimum

 similarly the 3 will act as maximum n 2 to the power 2 eemyents i.e. elemts to its right
 so in total 4 arrays 3 will act as minimum


 so if we take contribution of each element as minimum and sum it up  sumMin

 also

 we take contribution of each element as maximum and sum it up sumMAx

 then SumMAx - SumMin will give us ans



 '''


def solve(A):
	A.sort()
	sumL = 0
	sumR = 0
	    
	for i in range(len(A)):
	    sumL += A[i] * (2**(len(A)-1-i))
	    
	for j in range(len(A)):
	    sumR += A[j] * (2**j)
	    
	return (sumR - sumL)  % 1000000007

A = [1, 2]

print(solve(A))