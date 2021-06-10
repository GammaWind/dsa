'''
Kth Smallest Element
Problem Description

Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in <= B swaps.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= min(|A|, 500)

1 <= A[i] <= 109



Input Format
First argument is vector A.

Second argument is integer B.



Output Format
Return the Bth smallest element in given array.



Example Input
Input 1:

A = [2, 1, 4, 3, 2]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 2


Example Explanation
Explanation 1:

 3rd element after sorting is 2.
Explanation 2:

 2nd element after sorting is 2.

 Approach : we can sort also but nlogn if number of elements in arrays are 10^9 then we get TLE

 approach 2 : use selection sort, we will limit our swaps only to B and the find the smallest elemet and swap them at first of the arrays
 TC : O(N * K)  k will be the number of swaps

'''

import sys
def kthsmallest(A, B):
	    
	if len(A) is 1:
	    return A[0]
	brr = list(A)
	for i in range(B):
	    minn = sys.maxsize
	    minind = -1
	    for j in range(i,len(brr)):
	        if brr[j] < minn:
	            minn = brr[j]
	            minind = j
	                
	            
	    temp = brr[i]
	    brr[i] = brr[minind]
	    brr[minind] = temp
	                
	                
	return brr[B-1]
	            
	            
A = [2, 1, 4, 3, 2]
B = 3
print(kthsmallest(A, B))	                 
	            
