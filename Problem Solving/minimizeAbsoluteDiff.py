'''

Minimize the absolute difference
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively. i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.


APPRAOCH: here the idea is to bring the minimum numbers .i.e. other 2 numbers as near as maximum

so how do we do that??
simple idea is we shift smallest number by one and compare on each shift untill any  of the array finishesh
that will give us the answer

'''
def solve( A, B, C):
	i,j,k = 0,0,0
	minnAns = max(A[0], B[0], C[0]) - min(A[0], B[0], C[0])
	while i < len(A) and j < len(B) and k < len(C):
	    maxi = max(A[i],B[j],C[k])
	    mini =  min(A[i],B[j],C[k])
	        
	    ans  = maxi - mini
	    minnAns = min(ans, minnAns)
	        
	        
	        
	    if A[i] == mini:
	        i += 1
	    elif B[j] == mini:
	        j += 1
	    else:
	        k += 1
	    
	return minnAns 


A = [ 1, 4, 5, 8, 10 ]
B = [ 6, 9, 15 ]
C = [ 2, 3, 6, 6 ]

print(solve(A,B,C))

