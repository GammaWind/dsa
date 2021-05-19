'''
subsets 1 

A = [1,2,3]

TC =. 2^N
recursion 


ans. :   [[],[1],[1,2], [1,3] ,[1,2,3],[2],[2,3], [3]





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