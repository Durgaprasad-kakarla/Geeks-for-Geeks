'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        #code here
        def dfs(node):
            if node is None:
                return None
            if node.data < l:
                return dfs(node.right)
            elif node.data > r:
                return dfs(node.left)
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
        
        return dfs(root)