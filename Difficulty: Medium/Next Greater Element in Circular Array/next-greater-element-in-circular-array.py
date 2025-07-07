class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack=arr[::-1].copy()
        n=len(arr)
        next_greater=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                next_greater[i]=stack[-1]
            stack.append(arr[i])
        return next_greater