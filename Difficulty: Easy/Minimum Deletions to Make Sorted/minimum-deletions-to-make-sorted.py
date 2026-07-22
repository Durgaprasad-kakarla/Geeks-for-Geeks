from bisect import bisect_left
class Solution:
    def minDeletions(self, arr):
        # code here
        n=len(arr)
        ans=[]
        for i in range(n):
            ind=bisect_left(ans,arr[i])
            k=len(ans)
            if ind>=k:
                ans.append(arr[i])
            else:
                ans[ind]=arr[i]
        # print(ans)
        return n-len(ans)
                