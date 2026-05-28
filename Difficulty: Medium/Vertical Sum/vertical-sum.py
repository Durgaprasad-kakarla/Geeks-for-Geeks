# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

class Solution:
    def verticalSum(self, root):
        # code here
        vertical_sum_dic={}
        queue=deque([[0,root]])
        while queue:
            pos,node=queue.popleft()
            if pos not in vertical_sum_dic:
                vertical_sum_dic[pos]=node.data
            else:
                vertical_sum_dic[pos]+=node.data
            if node.left:
                queue.append([pos-1,node.left])
            if node.right:
                queue.append([pos+1,node.right])
        return [val for key,val in sorted(vertical_sum_dic.items())]