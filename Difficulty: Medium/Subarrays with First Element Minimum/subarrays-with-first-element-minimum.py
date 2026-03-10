class Solution:
    def countSubarrays(self, arr):
        # code here
        n=len(arr)
        stack=[]
        tot=0
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                ind=stack.pop()
                tot+=(i-ind)
            stack.append(i)
        while stack:
            ind=stack.pop()
            tot+=(n-ind)
        return tot