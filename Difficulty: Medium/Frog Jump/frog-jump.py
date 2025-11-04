class Solution:
    def minCost(self, height):
        # code here
        n=len(height)
        def func(ind,arr):
            if ind<0:
                return float('inf')
            if ind==0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            l,r=float('inf'),float('inf')
            if ind>0:
                l=abs(arr[ind]-arr[ind-1])+func(ind-1,arr)
            if ind>1:
                r=abs(arr[ind]-arr[ind-2])+func(ind-2,arr)
            dp[ind]=min(l,r)
            return min(l,r)
        dp=[-1]*n
        return func(n-1,arr)