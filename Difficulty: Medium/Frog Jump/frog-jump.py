class Solution:
    def minCost(self, height):
        # code here
        def min_cost(ind,dp):
            if ind==0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            l=abs(arr[ind]-arr[ind-1])+min_cost(ind-1,dp)
            r=float('inf')
            if ind>1:
                r=abs(arr[ind]-arr[ind-2])+min_cost(ind-2,dp)
            dp[ind]=min(l,r)
            return dp[ind]
        n=len(height)
        dp=[-1 for _ in range(n)]
        return min_cost(n-1,dp)