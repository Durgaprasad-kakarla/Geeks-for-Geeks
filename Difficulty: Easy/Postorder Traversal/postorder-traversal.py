'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        def post_order(root):
            if root:
                post_order(root.left)
                post_order(root.right)
                lst.append(root.data)
        lst=[]
        post_order(root)
        return lst
        
        