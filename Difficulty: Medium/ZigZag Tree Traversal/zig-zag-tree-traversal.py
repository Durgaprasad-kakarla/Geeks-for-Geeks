'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        # code here
        queue=deque()
        queue.append(root)
        zig_zag_lst=[]
        k=0
        while queue:
            n=len(queue)
            lst=[]
            for i in range(n):
                node=queue.popleft()
                lst.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if k&1==0:
                zig_zag_lst+=lst
            else:
                zig_zag_lst+=lst[::-1]
            k+=1
        return zig_zag_lst