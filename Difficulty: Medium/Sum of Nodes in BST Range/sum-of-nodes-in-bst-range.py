"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        # code here
        global tot
        tot=0
        def inorder(root):
            global tot
            if root:
                inorder(root.left)
                if root.data>=l and root.data<=r:
                    tot+=root.data
                inorder(root.right)
        inorder(root)
        return tot
                
        
        
