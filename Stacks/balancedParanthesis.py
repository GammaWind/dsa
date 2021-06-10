'''
Balanced Paranthesis
Problem Description

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.



Problem Constraints
1 <= |A| <= 100



Input Format
The first and the only argument of input contains the string A having the paranthesis sequence.



Output Format
Return 0, if the paranthesis sequence is not balanced.

Return 1, if the paranthesis sequence is balanced.



Example Input
Input 1:

 A = {([])}
Input 2:

 A = (){
Input 3:

 A = ()[] 


Example Output
Output 1:

 1 
Output 2:

 0 
Output 3:

 1 


Example Explanation
You can clearly see that the first and third case contain valid paranthesis.

In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.

APPROACH : push when open brace is there pop when close brace at end if stack is empty means paranthesis is balanced.
corner case : before popping make sure there are elements in stack else you can return 0 there itself and kill the paranthesis

Tc O(N)

'''


def solve( A):
    hset = ('{','(','[')
        
    hsetClose = ('}',')',']')
        
    stack = []
    for i in A:
        if i in hset:
            stack.append(i)
        elif i in hsetClose:
            if len(stack) > 0:
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
    return 0    
A = '{([])}'
print(solve(A))