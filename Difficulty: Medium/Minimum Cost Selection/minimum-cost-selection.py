class Solution:

    def minCost(self, mat):
        """code here"""
        def min_cost(ind,prev):
            if ind==0:
                mini=float('inf')
                for i in range(3):
                    if prev!=i:
                        mini=min(mini,mat[ind][i])
                return mini
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            mini=float('inf')
            for i in range(3):
                if i!=prev:
                    mini=min(mini,mat[ind][i]+min_cost(ind-1,i))
            dp[ind][prev+1]=mini
            return mini
        n=len(mat)
        dp=[[-1 for _ in range(4)] for _ in range(n)]
        return min_cost(n-1,-1)