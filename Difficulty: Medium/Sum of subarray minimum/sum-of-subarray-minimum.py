from collections import deque
class Solution:
    def sumSubMins(self, arr):
        # Code here
        n=len(arr)
        stack,tot=[(0,0)],0
        for i in range(n):
            while stack and stack[-1][0]>arr[i]:
                ele,ind=stack.pop()
                tot+=(i+1-ind)*(ind-stack[-1][1])*ele
            stack.append([arr[i],i+1])
        while stack and stack[-1][0]!=0:
            last,ind=stack.pop()
            tot+=(n-ind+1)*(ind-stack[-1][1])*last
        return tot