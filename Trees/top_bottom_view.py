'''
return /print top view of binary tree
 """ 
         1
        / \
       2   3
        \
          4
           \
            5
              \
               6
    """

Time Complexity: O(N)

Space Complexity: O(N)
'''


from typing import List
from collections import OrderedDict


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def top_view(root: Node) -> List[int]:
    
    if not root:
        return root
    que = []
    map =OrderedDict()
    ans = []

    que.append([root, 0])

    while que:
        pair = que.pop(0)
        node = pair[0]
        level = pair[1]

        print(node.val, level)
        if not level in map:
            map[level] = node.val

        if node.left:
            que.append([node.left, level-1])

        if node.right:
            que.append([node.right, level+1])   
    
    for key in sorted(map):
        ans.append(map[key])

    return ans









    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

ans = [2 ,1, 3, 6 ]

anss = top_view(root)
print(f'top view of the tree is {anss}')



'''
Bottom view



'''

'''
return /print top view of binary tree
 """ 
         1
        / \
       2   3
        \
          4
           \
            5
              \
               6
    """

Time Complexity: O(N)

Space Complexity: O(N)
'''


from typing import List
from collections import OrderedDict


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bottom_view(root: Node) -> List[int]:
    
    if not root:
        return root
    que = []
    map =OrderedDict()
    ans = []

    que.append([root, 0])

    while que:
        pair = que.pop(0)
        node = pair[0]
        level = pair[1]

       
        
        map[level] = node.val

        if node.left:
            que.append([node.left, level-1])

        if node.right:
            que.append([node.right, level+1])   
    
    for key in sorted(map):
        ans.append(map[key])

    return ans









    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

ans = [2,4,5,6 ]

anss = bottom_view(root)
print(f'bottom view of the tree is {anss}')

