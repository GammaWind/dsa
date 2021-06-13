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

Approach : O(N) Tc
calculate length of linked list first and second

then traverse the linked list untill   length - B point which needs to be removed

we mentain 2 vars as prev and curr while doing this  once we are at curr  = length - B1
we assign prev.next = curr.next
means curr is getting removed

'''
def removeNthFromEnd( A, B):
	    
	    
	    
	# we need to count the total length of list so copied head to start to traverse
    start = A
    length = 0
    while start:
        start = start.next
        length += 1
        
    if B >= length:
        return A.next
        
    length -= B
    i = 0
    curr = A
    prev = None
    while i < length:
        prev = curr
        curr = curr.next
        i += 1
            
            
            
    if curr.next is not None:
        prev.next =curr.next
    else:
        prev.next =None
    return A  


