'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        # code here
        def get_inorder(root,assign=False):
            inorder=[]
            curr=root
            i=0
            while curr:
                if not curr.left:
                    if assign:
                        curr.data=inorder_greater_sum_tree[i]
                        i+=1
                    else:
                        inorder.append(curr.data)
                    curr=curr.right
                else:
                    prev=curr.left
                    while prev.right and prev.right!=curr:
                        prev=prev.right
                    if prev.right:
                        if assign:
                            curr.data=inorder_greater_sum_tree[i]
                            i+=1
                        else:
                            inorder.append(curr.data)
                        prev.right=None
                        curr=curr.right
                    else:
                        prev.right=curr
                        curr=curr.left
            return inorder
        inorder=get_inorder(root)
        n=len(inorder)
        inorder_greater_sum_tree=[0]*n
        for i in range(n-2,-1,-1):
            inorder_greater_sum_tree[i]+=inorder_greater_sum_tree[i+1]+inorder[i+1]
        # print(inorder_greater_sum_tree)
        get_inorder(root,assign=True)
        return root
        
