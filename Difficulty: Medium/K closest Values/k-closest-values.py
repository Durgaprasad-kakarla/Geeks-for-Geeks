'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getKClosest(self, root, target, k):
        # code here
        curr=root
        inorder=[]
        while curr:
            if not curr.left:
                inorder.append([abs(curr.data-target),curr.data])
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if prev.right:
                    inorder.append([abs(curr.data-target),curr.data])
                    prev.right=None
                    curr=curr.right
                else:
                    prev.right=curr
                    curr=curr.left
        inorder.sort()
        return [val for i,val in inorder[:k]]
            
    