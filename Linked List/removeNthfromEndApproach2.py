'''
Remove Nth Node from List End
Problem Description

Given a linked list A, remove the B-th node from the end of list and return its head.

For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.

NOTE: Try doing it using constant additional space.



Problem Constraints
1 <= |A| <= 106



Input Format
The first argument of input contains a pointer to the head of the linked list.

The second argument of input contains the integer B.



Output Format
Return the head of the linked list after deleting the B-th element from the end.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 2
Input 2:

A = [1]
B = 1


Example Output
Output 1:

[1, 2, 3, 5]
Output 2:

 [] 


Example Explanation
Explanation 1:

In the first example, 4 is the second last element.
Explanation 2:

In the second example, 1 is the first and the last element.

approach 2 :  

we use 2 pointers here ie. fast and slow 

first we run fast pinter unill point B

then we run both fast and slow pointers unill fast is True i.e. not None


slow.next is the element needed to be remove so we assign slow.next  = slow.next.next

O(N) Tc
SPACE = O(1)

'''



def removeNthFromEnd(A, B):
    #if not A:   Cornder case
    #    return A 
	
	fast, slow = A, A
	   
	i = 0
	for _ in range(B):
	    if fast.next:
	        fast = fast.next
	    else:
	        return A.next
	            
	while fast.next:
	    fast = fast.next
	    slow = slow.next
	slow.next = slow.next.next     
	    
	return A
	    
	    