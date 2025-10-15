'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        # code here
        def inorder(root):
            if root:
                inorder(root.left)
                inorder_lst.append(root.data)
                inorder(root.right)
        inorder_lst=[]
        inorder(root)
        return inorder_lst[k-1] if (k-1<len(inorder_lst)) else -1