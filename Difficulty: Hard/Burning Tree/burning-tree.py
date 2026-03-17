'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        # code here
        def get_parent_dic(root):
            queue=deque([root])
            parent_dic={root:None}
            start=None
            while queue:
                node=queue.popleft()
                if node.data==target:
                    start=node
                if node.left:
                    parent_dic[node.left]=node
                    queue.append(node.left)
                if node.right:
                    parent_dic[node.right]=node
                    queue.append(node.right)
            return parent_dic,start
        parent_dic,start=get_parent_dic(root)
        vis=set()
        queue=deque([[start,0]])
        vis.add(start)
        while queue:
            node,d=queue.popleft()
            if parent_dic[node] and parent_dic[node] not in vis:
                queue.append([parent_dic[node],d+1])
                vis.add(parent_dic[node])
            if node.left and node.left not in vis:
                queue.append([node.left,d+1])
                vis.add(node.left)
            if node.right and node.right not in vis:
                queue.append([node.right,d+1])
                vis.add(node.right)
        return d
            