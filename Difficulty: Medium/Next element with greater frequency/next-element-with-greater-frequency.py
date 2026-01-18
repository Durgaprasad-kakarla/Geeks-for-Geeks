class Solution:
    def nextFreqGreater(self, arr):
        # code here
        n=len(arr)
        dic={}
        for i in range(n):
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
        freq=[-1]*n
        for i in range(n):
            freq[i]=dic[arr[i]]
        # print(freq)
        stack=[]
        ans=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1][1]<=freq[i]:
                stack.pop()
            if stack:
                ans[i]=arr[stack[-1][0]]
            stack.append([i,freq[i]])
        return ans
        