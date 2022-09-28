'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:
     1
    / \
   2   3
  / \
 4   5   


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

'''


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solve(root):     
    global var   
    
    def diameter(root: Node, var) -> int:
          
        if not root:
            return 0


        lh = diameter(root.left, var)
        rh = diameter(root.right, var)

        var[0] = max(var[0], lh +rh )
        

        return max(lh, rh) + 1
    
    var = [0]
    a = diameter(root, var)
    print(var)
    return var[0]    
    




root = Node(1)
root.right = Node(3)
root.left = Node(2) 
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

var = 0
ans = solve(root)
print(f'the diameter for given tree is {ans} in terms of nodes and in terms of edges its {ans}')
