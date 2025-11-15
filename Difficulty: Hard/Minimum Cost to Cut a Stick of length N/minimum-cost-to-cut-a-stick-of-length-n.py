class Solution:
    def minCutCost(self, n, cuts):
        # code here
        def func(i,j,cuts,dp):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=sys.maxsize
            for ind in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+func(i,ind-1,cuts,dp)+func(ind+1,j,cuts,dp)
                mini=min(mini,cost)
            dp[i][j]=mini
            return dp[i][j]
        c=len(cuts)
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        dp=[[-1 for j in range(c+1)] for i  in range(c+1)]
        return func(1,c,cuts,dp)
        