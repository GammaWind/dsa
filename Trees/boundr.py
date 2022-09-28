from typing import List

'''
approach:

left boundry with left left .....if not left go right only add if not leaf

add all leafs from left subtree and right subtree --> use preorder or in order

right boundry with root = root.right if not right then root = root.left and reverse the response and append


'''


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def print_boundry(node: Node) -> List[int] :
    ans = []
    root1 = node
    root2 = node
    root3 = node

    def isleaf(root):
        if root.left or root.right:
            return False
        return True

    def left_boundry(root):
        while root:
            if not isleaf(root):
                ans.append(root.val)
            if root.left:
                root = root.left
            else:
                root = root.right    

    def right_boundry(root):
        root = root.right
        r = []
        while root:
            print(f'val {r}')
            if not isleaf(root):
                r.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left 
        return r     

    def leaf_nodes(root):
        if not root:
            return root
        if isleaf(root):
            ans.append(root.val)
        leaf_nodes(root.left)
        leaf_nodes(root.right)
    left_boundry(root1)
    #print(ans)
    leaf_nodes(root2)
    print(ans)
    r= right_boundry(root3)
    r = r.reverse()
    ans.extend(r)
    
    return ans            
        




# root = Node(20)
# root.left = Node(8)
# root.left.left = Node(4)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)
# root.right = Node(22)
# root.right.right = Node(25)

aa = print_boundry(None)

verify = [20, 8, 4, 10, 14, 25, 22]
print(aa)