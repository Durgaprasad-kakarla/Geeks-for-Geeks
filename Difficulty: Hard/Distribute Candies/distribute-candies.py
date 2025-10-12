'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandy(self, root):
        # code here
        global ans
        ans=0
        def func(node):
            global ans
            if not node:
                return 0
            left,right=func(node.left),func(node.right)
            ans+=abs(left)+abs(right)
            return node.data+left+right-1
        func(root)
        return ans