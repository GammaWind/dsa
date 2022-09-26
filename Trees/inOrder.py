'''
Inorder Traversal


Left, root, Right

Approach 1 : recursively 




'''

from typing import List


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# class Solution:
#     def __init__(self):
#         self.answer = []
#     def recursive(self,root):
# 	    if root:
#             self.recursive(root.left)
#             self.answer.append(root.val)
#             self.recursive(root.right)
        
#     def inOrderTraversal(self, A):
# 	    self.recursive(A)
# 	    return self.answer


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("PostOrder traversal of binary tree is")
# Tr = Solution()
# ans = Tr.inOrderTraversal(root)
# print(ans)


#iterative approach using stack

def inorder_iterative(root: TreeNode) -> List[int]:
    if not root:
        return []
    ans: List[int] = []
    stack: List[TreeNode] =[]
    # stack.append(root.val)

    while stack or root:

        if root:
            stack.append(root)
            root = root.left
        else:

            root = stack.pop()
            ans.append(root.val)
            root = root.right
    return ans

anss = inorder_iterative(root)
print(f'iterative apporach ans is {anss}')                   
        

 
