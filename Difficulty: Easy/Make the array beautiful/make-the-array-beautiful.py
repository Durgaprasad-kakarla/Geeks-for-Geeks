class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        n=len(arr)
        stack=[]
        for i in range(n):
            flag=False
            if stack and ((stack[-1]>=0 and arr[i]<0) or (stack[-1]<0 and arr[i]>=0)):
                flag=True
                stack.pop()
            if not flag:
                stack.append(arr[i])
        return stack