class Solution:
    def maxChocolate(self, grid):
        # code here
        def check(row,col):
            if row<0 or row>=n or col<0 or col>=m:
                return True
            return False
        def chocolate_pickup(i1,j1,i2,j2):
            if check(i1,j1) or check(i2,j2):
                return -float('inf')
            if i1==n-1 and i2==n-1:
                if j1==j2:
                    return grid[i1][j1]
                return grid[i2][j2]+grid[i1][j1]
            if dp[i1][j1][i2][j2]!=-1:
                return dp[i1][j1][i2][j2]
            if i1==i2 and j1==j2:
                sm=grid[i1][j1]
            else:
                sm=grid[i1][j1]+grid[i2][j2]
            maxi=-float('inf')
            for i in range(-1,2):
                for j in range(-1,2):
                    maxi=max(maxi,
                            chocolate_pickup(i1+1,j1+i,i2+1,j2+j))
            dp[i1][j1][i2][j2]=maxi+sm
            return dp[i1][j1][i2][j2]
        n,m=len(grid),len(grid[0])
        dp=[[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
        return chocolate_pickup(0,0,0,m-1)