''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        curr=root
        floor=float('inf')
        while curr:
            if curr.data>=x:
                floor=min(curr.data,floor)
                curr=curr.left
            else:
                curr=curr.right
        return floor if floor!=float('inf') else -1