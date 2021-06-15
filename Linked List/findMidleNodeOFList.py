'''
find middle node of a link list 

approach : use 2 pointer method
1 fast pointer 1 slow pointer

travel fast pointer with distance of 2 and slow pointer with distance of 1 , by doing this 
when the list ends the fast pointer will be at end and slow pointer will be at middle 
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
    
    def findMiddle(self):
        fast = self.head
        slow = self.head
        temp  = self.head

        while(fast is not None and fast.next is not None):
            
            fast = fast.next.next
            slow = slow.next
            

        print(slow.data)    


    # Function to reverse the linked list
    def reverse(self):
        prev  = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr =temp
            print(temp.data)
        self.head = curr
 
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
 
 
# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.push(83)
 
print ("Given Linked List")
llist.printList()
# llist.reverse()
# print ("\nReversed Linked List")

print ("\middle of Linked List")
llist.findMiddle()
# llist.printList()