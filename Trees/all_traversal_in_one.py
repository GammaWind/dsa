# Definition for a  binary tree node
from typing import List, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def all_traverse(root: TreeNode):

    if not root:
        return None

    pre_order = []
    in_order = []
    post_order = []
    stack: List[List[TreeNode, int]] = []
    stack.append([root, 1])

    while stack:
        node = stack.pop()
        if node[1] == 1:
            pre_order.append(node[0].val)
            node[1] += 1
            stack.append(node)
            if node[0].left:
                stack.append([node[0].left, 1])
        elif node[1] == 2:
            in_order.append(node[0].val)
            node[1] += 1
            stack.append(node)
            if node[0].right:
                stack.append([node[0].right, 1])

        else:
            post_order.append(node[0].val)
    return [pre_order,  in_order, post_order]

ans = all_traverse(root)
print(f'here are traversals {ans}')                                



        