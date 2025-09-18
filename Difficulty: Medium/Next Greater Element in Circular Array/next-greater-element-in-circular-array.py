class Solution:
    def nextGreater(self, arr):
        # code here
        n=len(arr)
        stack=arr[::-1].copy()
        next_greater=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                next_greater[i]=stack[-1]
            stack.append(arr[i])
        return next_greater