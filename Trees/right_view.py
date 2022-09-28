'''
Given a Binary Tree, print the Right view of it. 

The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.

Examples: 

Input:
          1
       /     \
     2        3
   /   \       /  \
  4     5   6    7
                 \
                   8
Output: Right view of the tree is 1 3 7 8

TRICK:  here we save the comparisions using lenth of ds (ans) with the level
tc - O(n)
sc -> O(h)

'''
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def right_view_recursive(root, level,ds):

    if not root:
        return root

    if level == len(ds):
        ds.append(root.val)    

    right_view_recursive(root.right, level +1 , ds)
    right_view_recursive(root.left, level +1 , ds)    



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
answer = [1, 3, 7, 8]

ans = []
right_view_recursive(root, 0, ans)
print(ans)