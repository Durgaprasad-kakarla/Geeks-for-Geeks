class Solution:
    def visibleBuildings(self, arr):
        # code here
        n=len(arr)
        stack=[]
        prev_greater=[-1]*n
        for i in range(n):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                prev_greater[i]=stack[-1]
            stack.append(arr[i])
        # print(prev_greater)
        return  prev_greater.count(-1)