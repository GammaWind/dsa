'''
Longest Consecutive Sequence
Problem Description

Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from the array A.



Problem Constraints
1 <= N <= 106

-106 <= A[i] <= 106



Input Format
First argument is an integer array A of size N.



Output Format
Return an integer denoting the length of the longest set of consecutive elements from the array A.



Example Input
Input 1:

A = [100, 4, 200, 1, 3, 2]
Input 2:

A = [2, 1]


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2:

 The set of consecutive elements will be [1, 2].
'''


'''
APPROACH : here O(N) apporach would be to determine some way to find the start of a range
we can store all elements in hashset

lets say current element is 8 and we want to find if 8 is the start of range or not, how can we do that ?????
we will check if there exists 7 in given list and yes that hashset can give us O(1) lookup time

so once you found the elements which are start of the ranges we can  simpley try to find if there consicative numbers exists in hashset in O(1) lookup time
and if they exiists then we will increase our count 


by this way we will calculate the length of ranges and return max

TC : O(N)
SC : O(N)

'''
def longestConsecutive( A):
	    #insert all elements in set to make the lookup easy
	ans = 0
	hSet = set(A)
	for i in A:
	    if i - 1 in hSet:
	        pass
	    elif i -1 not in hSet:
	        consecutive = 0
	        rangeStart = i
	        while rangeStart in hSet:
	            consecutive += 1
	            rangeStart += 1
	        ans = max(ans,consecutive)    
	return ans

A = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(A))