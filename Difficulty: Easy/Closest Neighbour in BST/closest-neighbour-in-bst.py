'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        global maxi
        maxi=-1
        def inorder(root):
            global maxi
            if root:
                inorder(root.left)
                if root.data<=k:
                    maxi=max(maxi,root.data)
                inorder(root.right)
        inorder(root)
        return maxi