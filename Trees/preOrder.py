'''
Preorder Traversal


Root,  Left, Right

Approach 1 : recursively 




'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    def __init__(self):
        self.answer = []
    def recursive(self,root):
	    if root == None:
	        return root
	    self.answer.append(root.val)
	    self.preorderTraversal(root.left)
	    self.preorderTraversal(root.right)
        
    def preorderTraversal(self, A):
	    self.recursive(A)
	    return self.answer


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Preorder traversal of binary tree is")
Tr = Solution()
ans = Tr.preorderTraversal(root)
print(ans)
 
