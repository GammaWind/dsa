'''
subsets 1 

A = [1,2,3]

TC =. 2^N
recursion 


ans. :   [[],[1],[1,2], [1,3] ,[1,2,3],[2],[2,3], [3]

Subset
Problem Description

Given a set of distinct integers, A, return all possible subsets.

NOTE:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.


Problem Constraints
1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX


Input Format
First and only argument of input contains a single integer array A.



Output Format
Return a vector of vectors denoting the answer.



Example Input
Input 1:

A = [1]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:

[
    []
    [1]
]
Output 2:

[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]


Example Explanation
Explanation 1:

 You can see that these are all possible subsets.
Explanation 2:

You can see that these are all possible subsets.


APPROACH : 
here the intution is simple either choose or dont choose

base case would be if the index is len of (A) then we add the current ans to aour ans list

also we call recursion once adding the current letter/number with index + 1
and call once again when withoud adding the current lettter/number index +  1




'''



def solve(A):
	ansArr = []
	A.sort()
	
	def subsetsOne(A, idx, currArr, ansArr):
		if idx == len(A):
			print(currArr)
			ansArr.append(currArr.copy())
			return
		
		subsetsOne(A, idx+1, currArr + [A[idx]], ansArr)
		subsetsOne(A,idx + 1, currArr , ansArr)
	
	subsetsOne(A , 0, [], ansArr)
	ansArr.sort()
	
	return ansArr

	
A = ['a','b','c']
print(solve(A))
