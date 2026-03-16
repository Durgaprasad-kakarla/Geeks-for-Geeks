'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def countAllPaths(self, root, k):
        # code here
        def count_all(root,sm,dic):
            global cnt
            if not root:
                return 0
            sm+=root.data
            if sm-k in dic:
                cnt+= dic[sm-k]
            if sm in dic:
                dic[sm]+=1
            else:
                dic[sm]=1
            count_all(root.left,sm,dic)
            count_all(root.right,sm,dic)
            dic[sm]-=1
            if dic[sm]==0:
                del dic[sm]
        global cnt
        cnt=0
        count_all(root,0,{0:1})
        return cnt