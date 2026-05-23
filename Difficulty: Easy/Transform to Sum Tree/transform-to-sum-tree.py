# Structure for Tree Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        # code here
        def postorder(root):
            if not root:
                return 0
            l=postorder(root.left)
            r=postorder(root.right)
            curr_data=root.data
            root.data=l+r
            return curr_data+l+r
        postorder(root)
        return root