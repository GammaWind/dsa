

from typing import List


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzag(root: Node) -> List[int]:

    if not root:
        return []
    ans = []    

    que = []
    left_to_right = True
    que.append(root) 

    while que:
        a = []
        r = len(que)
        for i in range(r):
            node = que.pop(0)

            a.append(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)        
        if not left_to_right:
            a.reverse()
        ans.append(a)
        a = None
        left_to_right = not left_to_right   
          
    return ans                  




root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)

'''
   20
  /  \
 8    22
/ \     \
4  12   25
   /\
 10  14      

'''

an = zigzag(root)
print(f'zigzag traversal is  {an}')