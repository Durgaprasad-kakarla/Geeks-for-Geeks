''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        # code here
        def lca(root):
            if not root or root.data==p or root.data==q:
                return root
            left=lca(root.left)
            right=lca(root.right)
            # print(left,right)
            if left and right:
                return root
            elif left:
                return left
            return right
        start=lca(root)
        if not start:
            return -1
        
        queue1=deque([[start,0,'left']])
        queue2=deque([[start,0,'right']])
        def func(queue):
            dic={}
            while queue:
                node,turn_cnt,dir=queue.popleft()
                dic[node.data]=turn_cnt
                # if node.data==p:
                #     continue
                # if node.data==q:
                #     continue
                if node.left:
                    if dir=='left':
                        queue.append([node.left,turn_cnt,'left'])
                    else:
                        queue.append([node.left,turn_cnt+1,'left'])
                if node.right:
                    if dir=='right':
                        queue.append([node.right,turn_cnt,'right'])
                    else:
                        queue.append([node.right,turn_cnt+1,'right'])
            # print(dic)
            sm=dic[p]+dic[q]
            return sm
        sm1=func(queue1)
        sm2=func(queue2)
        sm=min(sm1,sm2)
        return sm if sm!=0 else -1
                
        