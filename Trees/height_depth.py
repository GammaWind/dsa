
from typing import List


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def get_height(root: TreeNode) -> int:
    
    if not root:
        return 0

    ls = get_height(root.left)
    rs = get_height(root.right)


    return 1 + max(ls, rs)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
ans = get_height(root)
print(f'depth of the gievn tree is {ans}')

