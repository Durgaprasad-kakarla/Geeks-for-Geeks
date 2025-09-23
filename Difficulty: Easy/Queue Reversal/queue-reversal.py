class Solution:
    def reverseQueue(self, q):
        # code here
        stack=[]
        i=0
        while q:
            x=q.popleft()
            stack.append(x)
        # print(stack)
        while stack:
            q.append(stack.pop())
        return q
        