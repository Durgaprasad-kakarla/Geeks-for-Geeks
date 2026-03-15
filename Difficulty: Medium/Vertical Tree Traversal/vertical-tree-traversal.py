'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # code here
        queue=deque([[root,0]])
        vertical_dic={}
        while queue:
            node,pos=queue.popleft()
            if pos in vertical_dic:
                vertical_dic[pos].append(node.data)
            else:
                vertical_dic[pos]=[node.data]
            if node.left:
                queue.append([node.left,pos-1])
            if node.right:
                queue.append([node.right,pos+1])
        vertical_order=[]
        for i in sorted(vertical_dic):
            vertical_order.append(vertical_dic[i])
        return vertical_order
        