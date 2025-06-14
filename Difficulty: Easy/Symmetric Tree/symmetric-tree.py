'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        #Code Here
        def symmetric(root1,root2):
            if not root1 or not root2:
                return True
            if root1.data!=root2.data:
                return False
            return symmetric(root1.left,root2.right) and symmetric(root1.right,root2.left)
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        return symmetric(root.left,root.right)