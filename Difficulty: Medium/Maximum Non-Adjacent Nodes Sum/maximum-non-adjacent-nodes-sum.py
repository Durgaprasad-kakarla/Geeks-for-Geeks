'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        #code here
        def helper(node):
            if not node:
                return (0, 0)
            
            left = helper(node.left)
            right = helper(node.right)
            
            include = node.data + left[1] + right[1]
            
            exclude = max(left) + max(right)
            
            return (include, exclude)
        
        include, exclude = helper(root)
        return max(include, exclude)