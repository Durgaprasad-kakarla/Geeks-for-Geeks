# Definition for Node
from collections import defaultdict
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def isSubTree(self, root1, root2):
        # code here
        curr=root1
        # node_val_dic=defaultdict(list)
        required_nodes=[]
        while curr:
            if not curr.left:
                if curr.data==root2.data:
                    required_nodes.append(curr)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if prev.right:
                    curr=curr.right
                    prev.right=None
                else:
                    if curr.data==root2.data:
                        required_nodes.append(curr)
                    prev.right=curr
                    curr=curr.left
        def identical(root1,root2):
            if not root1 and not root2:
                return True 
            if (not root1 and root2) or (root1 and not root2):
                return False
            return root1.data==root2.data and identical(root1.left,root2.left) and identical(root1.right,root2.right)
        for node in required_nodes:
            # print(node.data,root2.data)
            # print(identical(node,root2))
            if identical(node,root2):
                return True
        return False
        
        
        
        
        