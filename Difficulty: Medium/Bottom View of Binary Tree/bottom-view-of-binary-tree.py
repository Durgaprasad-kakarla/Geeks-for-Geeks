'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        queue=deque()
        queue.append([root,0])
        dic={}
        while queue:
            node,d=queue.popleft()
            dic[d]=node.data
            if node.left:
                queue.append([node.left,d-1])
            if node.right:
                queue.append([node.right,d+1])
        bottom_view=[dic[i] for i in sorted(dic)]
        return bottom_view
        
        