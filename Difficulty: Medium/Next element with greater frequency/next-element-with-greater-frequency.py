class Solution:
    def findGreater(self, arr):
        # code here
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        n=len(arr)
        stack,next_great_freq=[],[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0]<=dic[arr[i]]:
                stack.pop()
            if stack:
                next_great_freq[i]=stack[-1][1]
            stack.append([dic[arr[i]],arr[i]])
        return next_great_freq
        