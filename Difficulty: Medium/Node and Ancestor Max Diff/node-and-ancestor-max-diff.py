''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # code here
        queue=deque([[root,-float('inf')]])
        max_diff=-float('inf')
        while queue:
            node,parent=queue.popleft()
            max_diff=max(parent-node.data,max_diff)
            max_node=max(node.data,parent)
            if node.left:
                queue.append([node.left,max_node])
            if node.right:
                queue.append([node.right,max_node])
        return max_diff