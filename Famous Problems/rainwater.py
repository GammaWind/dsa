'''
Rain Water Trapped
Problem Description

Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000



Input Format
First and only argument is the vector A



Output Format
Return one integer, the answer to the question



Example Input
Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

1 unit is trapped on top of the 3rd element.
Explanation 2:

No water is trapped.
'''




class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    totalUnitsOfWater = 0
	    preMax = [0] * len(A)
	    
	    postMax = [0] * len(A)
	    
	    maxx = 0
	    #prefix max array
	    for i in range(len(A)):
	        preMax[i] = maxx
	        if A[i] > maxx:
	            maxx = A[i]
	        
	    
	    #suffix max array
	    maxx = 0
	    for j in range(len(A)-1,-1,-1):
	        postMax[j] = maxx
	        if A[j] > maxx:
	            maxx = A[j]
	   # print(preMax)      
	   # print(postMax)
	   # print(A)
	   
	    for i in range(1,len(A)-1):
	        units = (min(preMax[i],postMax[i]) - A[i])
	        if units > 0:
	            totalUnitsOfWater += units
	       # print(preMax[i],postMax[i],A[i],totalUnitsOfWater)
	    return totalUnitsOfWater 
	       
	       
	        
	    
	    
