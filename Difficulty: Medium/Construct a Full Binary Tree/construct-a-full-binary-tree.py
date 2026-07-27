''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        # code here
        def construct(prestart,preend):
            # print(prestart,preend)
            if prestart>preend:
                return None
            if prestart==preend:
                return Node(pre[prestart])
            inroot=mirror_dic[pre[prestart]]
            right=pre_dic[preMirror[inroot+1]]
            root=Node(pre[prestart])
            root.left=construct(prestart+1,right-1)
            root.right=construct(right,preend)
            return root
        n=len(pre)
        mirror_dic={}
        for i in range(n):
            mirror_dic[preMirror[i]]=i
        pre_dic={}
        for i in range(n):
            pre_dic[pre[i]]=i
        return construct(0,n-1)