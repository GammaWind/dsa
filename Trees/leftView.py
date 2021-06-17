'''
Left view of binary tree
Problem Description

Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.

Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side

NOTE: The value comes first in the array which have lower level.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 109



Input Format
First and only argument is a root node of the binary tree, A.



Output Format
Return an integer array denoting the left view of the Binary tree.



Example Input
Input 1:

            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:

 [1, 2, 4, 8]
Output 2:

 [1, 2, 4, 5]


Example Explanation
Explanation 1:

 The Left view of the binary tree is returned.

Approach : same approach as level order but just we need the 1st element on each level

remember that we also need to push the right of the root each time as well as there could be some element which is first for that level from left

TC : O(N)
SC : O(N)

'''

# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if A == None:
	        return A
        answer = []
        queue = []
        queue.append(A)
        
        while len(queue) > 0:
	        
	        answer.append(queue[0].val)
	        for i in range(len(queue)):
	            
	            node = queue.pop(0)
	            if node.left :
	                queue.append(node.left)
	            if node.right:
	                queue.append(node.right)
        return answer  


sol = Solution()

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(sol.solve(root))    