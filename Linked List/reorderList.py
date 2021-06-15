'''
Reorder List
Problem Description

Given a singly linked list A

 A: A0 → A1 → … → An-1 → An 
reorder it to:

 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values.



Problem Constraints
1 <= |A| <= 106



Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5] 
Input 2:

 A = [1, 2, 3, 4] 


Example Output
Output 1:

 [1, 5, 2, 4, 3] 
Output 2:

 [1, 4, 2, 3] 


Example Explanation
Explanation 1:

 The array will be arranged to [A0, An, A1, An-1, A2].
Explanation 2:

 The array will be arranged to [A0, An, A1, An-1, A2].


Approach :

here we determine the middle -1 of the list by fast pointer slow pointer technique with slow = head and fast = slow.next coz we want middle -1 element
after getting middle-1 element we will store its next in var called MIDDLE and we will break the link pointer
so now we have 2 LL. 1. head 2. MIDDLE

now we will reverse the middle list

after that we need to mrege both the lists

TC O(N)
Time Complexity : O(n) 
Auxiliary Space : O(1) 

 '''


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def findMiddle(self, starter):

        slow = starter
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # copying middlle node
        middleNode = slow.next

        # breakig the link
        slow.next = None
        
        return middleNode

    def reverseList(self, start):
        prev = None
        curr = start

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def mergeList(self, head1, head2):
        dummy = Node(0)
        curr = dummy
        while (head1 is not None or head2 is not None):
            if head1 is not None:
                curr.next = head1
                curr = curr.next
                head1 = head1.next

            if head2 is not None:
                curr.next = head2
                curr = curr.next
                head2 = head2.next

        return dummy.next


    def reorderList(self, A):
        if not A or not A.next:
	        return A
        middle = self.findMiddle(A)
        
        revFrom_middle = self.reverseList(middle)
        
        
        final = self.mergeList(A,revFrom_middle)
        return final

    def printListWith(self,head):
        temp = head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Function to insert a new node at the beginning

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def returnList(self):
        return self.head

# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
lst = llist.returnList()
answer = llist.reorderList(lst)






print("\reordered Linked List")
llist.printListWith(answer)

