
'''
Symmetric Binary Tree
Problem Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is the root node of the binary tree.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ).



Example Input
Input 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3
Input 2:

    1
   / \
  2   2
   \   \
   3    3


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The above binary tree is symmetric. 
Explanation 2:

The above binary tree is not symmetric.


APPROACH : 

we will send left node of the root as 1st parameter and right node of root as 2nd 

so if both nodes are null then we return true becoz that means they are same // Base CASE

if one is there and other is none then we return false


else


we check if vals of both nodes are same 

if same then we check recursively if isMirror for root1.left with root2.right and  root1.right with root2.left


TC : we are traversing each node once hence O(1)
SC : O(N) coz of recursion stack

'''



class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	
	def isMirror(self,root1, root2):
		if root1 is None and root2 is None:
			return True
		if (root1 is not None and root2 is not None):
			if root1.val == root2.val:
				return (self.isMirror(root1.left, root2.right)and self.isMirror(root1.right, root2.left))
						
		return False
	def isSymmetric(self, A):
	    return self.isMirror(A.left,A.right)
	    

sol = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print ("Symmetric") if sol.isSymmetric(root) == True else ("Not symmetric")
