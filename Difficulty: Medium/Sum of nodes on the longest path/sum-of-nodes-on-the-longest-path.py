'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
        def max_longest_path(root,l,sm):
            global max_len,maxi
            if max_len<l:
                max_len=l
                maxi=sm
            if max_len==l:
                maxi=max(maxi,sm)
            if not root:
                return 0
            max_longest_path(root.left,l+1,sm+root.data)
            max_longest_path(root.right,l+1,sm+root.data)
        global max_len,maxi
        max_len,maxi=0,0
        max_longest_path(root,0,0)
        return maxi