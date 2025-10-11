'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        # code 
        global max_sum
        max_sum=-float('inf')
        def max_path_sum(root):
            global max_sum
            if not root:
                return 0
            left=max_path_sum(root.left)
            right=max_path_sum(root.right)
            max_sum=max(max_sum,root.data+left+right,root.data+left,root.data+right,root.data)
            return max(max(left,right)+root.data,0)
        max_path_sum(root)
        return max_sum