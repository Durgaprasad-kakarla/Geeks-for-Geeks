class Solution:
    def uniquePaths(self, grid):
        # code here 
        n,m=len(grid),len(grid[0])
        def unique_paths(i,j,grid):
            if i<0 or j<0 or grid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            l=unique_paths(i-1,j,grid)
            r=unique_paths(i,j-1,grid)
            dp[i][j]=l+r
            return l+r
        dp=[[-1 for i in range(m)] for j in range(n)]
        return unique_paths(n-1,m-1,grid)