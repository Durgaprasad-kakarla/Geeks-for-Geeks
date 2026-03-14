'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        top_dic={}
        queue=deque([[root,0]])
        while queue:
            node,d=queue.popleft()
            if d not in top_dic:
                top_dic[d]=node.data
            if node.left:
                queue.append([node.left,d-1])
            if node.right:
                queue.append([node.right,d+1])
        return [top_dic[key] for key in sorted(top_dic.keys())]
        
        