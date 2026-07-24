'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque
class Solution:
    def longestConsecutive(self, root):
        # Code here
        def get_nodes_address(root):
            queue=deque()
            queue.append(root)
            dic={}
            while queue:
                node=queue.popleft()
                if node.data in dic:
                    dic[node.data].append(node)
                else:
                    dic[node.data]=[node]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return dic
            
        def visit(node):
            if not node:
                return 0
            vis.add(node)
            maxi=0
            if node.left and node.left.data==node.data+1:
                maxi=max(maxi,1+visit(node.left))
            if node.right and node.right.data==node.data+1:
                maxi=max(maxi,1+visit(node.right))
            return maxi
            
        dic=get_nodes_address(root)
        vis=set()
        maxi=0
        for i in sorted(dic):
            for j in dic[i]:
                if j not in vis:
                    # print(j.data,visit(j))
                    maxi=max(maxi,visit(j)+1)
        return maxi if maxi>1 else -1
            