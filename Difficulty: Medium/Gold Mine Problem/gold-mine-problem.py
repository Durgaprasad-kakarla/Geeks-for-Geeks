class Solution:
    def maxGold(self, mat):
        # code here
        def gold_mine(i,j):
            if j<0 or i<0 or i>=n or j>=m:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            d_up=mat[i][j]+gold_mine(i-1,j-1)
            d_down=mat[i][j]+gold_mine(i+1,j-1)
            right=mat[i][j]+gold_mine(i,j-1)
            dp[i][j]=max(d_up,d_down,right)
            return max(d_up,d_down,right)
        n,m=len(mat),len(mat[0])
        dp=[[-1 for i in range(m)] for j in range(n)]
        maxi=0
        for i in range(n):
            maxi=max(maxi,gold_mine(i,m-1))
        return maxi