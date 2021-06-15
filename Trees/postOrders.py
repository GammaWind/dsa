'''
PostORder Traversal


Left, Right, root

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
	    self.postOrderTraversal(root.left)
	    self.postOrderTraversal(root.right)
	    self.answer.append(root.val)
        
    def postOrderTraversal(self, A):
	    self.recursive(A)
	    return self.answer


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("PostOrder traversal of binary tree is")
Tr = Solution()
ans = Tr.postOrderTraversal(root)
print(ans)
 
