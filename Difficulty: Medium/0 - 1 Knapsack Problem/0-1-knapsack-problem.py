class Solution:
    def knapsack(self, W, val, wt):
        # code here
        # n=len(val)
        # def knapsack(ind,W):
        #     if ind==0:
        #         if W>=wt[ind]:
        #             return val[ind]
        #         return 0
        #     if dp[ind][W]!=-1:
        #         return dp[ind][W]
        #     l=knapsack(ind-1,W)
        #     r=-float('inf')
        #     if W>=wt[ind]:
        #         r=val[ind]+knapsack(ind-1,W-wt[ind])
        #     dp[ind][W]=max(l,r)
        #     return max(l,r)
        # dp=[[-1 for _ in range(W+1)] for _ in range(n)]
        # return knapsack(n-1,W)
        n=len(val)
        dp=[[0 for _ in range(W+1)] for _ in range(n)]
        for i in range(W+1):
            if i>=wt[0]:
                dp[0][i]=val[0]
        for i in range(1,n):
            for j in range(W+1):
                l=dp[i-1][j]
                r=-float('inf')
                if j>=wt[i]:
                    r=val[i]+dp[i-1][j-wt[i]]
                dp[i][j]=max(l,r)
        return dp[n-1][W]