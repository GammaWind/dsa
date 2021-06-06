'''
Evaluate Expression
Problem Description

An arithmetic expression is given by a charater array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each character may be an integer or an operator.



Problem Constraints
1 <= N <= 105



Input Format
The only argument given is character array A.



Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.



Example Input
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Input 2:
    A = ["4", "13", "5", "/", "+"]


Example Output
Output 1:
    9
Output 2:
    6


Example Explanation
Explaination 1:
    starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9
Explaination 2:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    1 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6
Approach :  its simple we want to eval postfix expression
by the help of stack whenever we get an operator in list we pop() 2 elements from stack and per form operation using the encountered operator and the push the result iagain in the stack.


'''
import operator
def evalRPN( A):
	if(len(A)) == 1:
	    return A[-1]
	ops = { "+": operator.add, "-": operator.sub, "*" : operator.mul,"/" : operator.truediv} # etc.
	    
	    
	stack  = []
	for i in A:
	    if  i in ops:
	        num_2 = stack.pop()
	        num_1 = stack.pop()
	        result= ops[i](num_1,num_2)
	        stack.append(result)
	    else:
	        stack.append(int(i))
	            
	return int(stack.pop())

A =   ["2", "1", "+", "3", "*"]
print(evalRPN(A))    