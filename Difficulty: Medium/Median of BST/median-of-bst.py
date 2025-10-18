'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMedian(self, root):
        # code here
        inorder=[]
        curr=root
        while curr:
            if not curr.left:
                inorder.append(curr.data)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if prev.right:
                    inorder.append(curr.data)
                    prev.right=None
                    curr=curr.right
                else:
                    prev.right=curr
                    curr=curr.left
        n=len(inorder)
        # print(inorder)
        if n&1:
            return inorder[n//2]
        else:
            return inorder[n//2-1]