'''
Redundant Braces
Problem Description

Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

Chech whether A has redundant braces or not.

NOTE: A will be always a valid expression.



Problem Constraints
1 <= |A| <= 105



Input Format
The only argument given is string A.



Output Format
Return 1 if A has redundant braces, else return 0.



Example Input
Input 1:

 A = "((a+b))"
Input 2:

 A = "(a+(a+b))"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 ((a+b)) has redundant braces so answer will be 1.
Explanation 2:

 (a+(a+b)) doesn't have have any redundant braces so answer will be 0.

 APPROACH : here we will push chars in stack if they are amnog  '( + - * /' and pop when we get ')' while popping if we get '(' we return 1 esle we pop the

Time complexity: O(n) 
Auxiliary space: O(n)
  
'''




	# @param A : string
	# @return an integer
def braces( A):
	hset = set()
	hset.add('+')
	hset.add('-')
	hset.add('*')
	hset.add('/')
	hset.add('(')
	    
	stack = []
	for i in A:
	    if i in hset:
	        stack.append(i)
	    elif i == ')':
	        if stack.pop() == '(':
	            return 1
	        stack.pop()
	return 0          
	            
	    
A = "((a+b))"
print(braces(A))