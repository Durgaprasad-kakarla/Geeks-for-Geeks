'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        # code here
        global prev,next,flag
        prev,next,flag=None,None,0
        def inorder(root):
            global prev,next,flag
            if root:
                inorder(root.left)
                if key>root.data:
                    if prev:
                        if prev.data<root.data:
                            prev=root
                    else:
                        prev=root
                if key<root.data:
                    if next:
                        if next.data>root.data:
                            next=root
                    else:
                        next=root
                inorder(root.right)
        inorder(root)
        return [prev,next]