'''
K reverse linked list
Problem Description

Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return modified linked list.



Problem Constraints
1 <= |A| <= 103

B always divides A



Input Format
The first argument of input contains a pointer to the head of the linked list.

The second arugment of input contains the integer, B.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5, 6]
 B = 2
Input 2:

 A = [1, 2, 3, 4, 5, 6]
 B = 3


Example Output
Output 1:

 [2, 1, 4, 3, 6, 5]
Output 2:

 [3, 2, 1, 6, 5, 4]


Example Explanation
Explanation 1:

 For the first example, the list can be reversed in groups of 2.
    [[1, 2], [3, 4], [5, 6]]
 After reversing the K-linked list
    [[2, 1], [4, 3], [6, 5]]
Explanation 2:

 For the second example, the list can be reversed in groups of 3.
    [[1, 2, 3], [4, 5, 6]]
 After reversing the K-linked list
    [[3, 2, 1], [6, 5, 4]]

Approach : TC O(N) // SC O(Auxiliary Space: O(n/k). )    


we can reverse the list untill given B and the iteratively call this function for next element and attach the result to head.next at last we can return prev as in generic reverse LL program

'''

def reverseList(head, B):
    if head is None:
        return head
	
    next = None
    prev = None
    count = 0
    current  = head
	while (current is not None and count < B):
        next = current.next
        current.next = prev 
        prev = current 
        current = next 
        count += 1
	        
	    
	if next is not None:
	    head.next = reverseList(next , B)
	    
	return prev


