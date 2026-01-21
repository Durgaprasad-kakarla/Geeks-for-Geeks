class Solution:
    def calculateSpan(self, arr):
        # code here
        n=len(arr)
        stack=[]
        ans=[]
        for i in range(n):
            tot=1
            while stack and stack[-1][0]<=arr[i]:
                tot+=stack.pop()[1]
            stack.append([arr[i],tot])
            ans.append(stack[-1][1])
        return ans
        
        