'''
substes 2


complexity  =. N * 2 ^ N
A =[1,2,2 ]

ans : [] , [1], [1,2],[2],[2,2],[1,2,2]


approach :

here we can use subsets.1 ap







proach, i.e. at the base case before inserting a subset into the ans array we can check if the same subset exists in the answer array, but this apparch is costly so we need to rething the whole problem itself. how do we do that ?????


we can use backtracking here with topdown approach ,
here we will be using method parameters like

index , ansArr , currArr , A


idea is to traverse the array A from index idx to the end of A
adding the number at inedx i to currArr and callling the recursion with idx + 1. and currArr
and then backtrack after the recursive call removing that added element 


so. now whenever we enter into the recursion stack we will be adding currArr to the ansArr (answer) but this can lead to duplicate subsets being added to our ansArr so how can we avoid this ???


here when we are traversing from idx to end of array A
we ca check if the current i is not equal to i -1.
if i and i-1 are equal then there is not point in caling recursion as it will add a duplicate ans. also we need to checkif currennt idx is not the first i.e. (0)


so once in for all our check statement would look like 

if i != 0 and A[i] != A[i -1]:
	add the A[i] to curr 
	call recursion with idx. + -1
	remove A[i]
	
	
	
lets code this problem.....


'''


def solve(A):
	A.sort()
	ansArr = []
	subsetsTwo(A, 0, [], ansArr)


	return ansArr


def subsetsTwo(A, idx, currArr, ansArr):
	
	
	ansArr.append(currArr.copy())

	for i in range(idx, len(A)):
		


		if i != idx and A[i] == A[i - 1]:
			continue
		currArr.append(A[i])
		subsetsTwo(A, i + 1, currArr, ansArr)
		currArr.pop(len(currArr) - 1)


A = [6,6,3,3,6,5]
print(solve(A))
'''	
B = [1,2,3,4,5]
B.pop()
print(B)
'''
