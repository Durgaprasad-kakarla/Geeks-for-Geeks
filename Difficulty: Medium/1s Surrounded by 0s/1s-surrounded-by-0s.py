class Solution:
    def cntOnes(self, grid):
        # code here
        n,m=len(grid),len(grid[0])
        vis=[[0 for _ in range(m)] for _ in range(n)]
        def dfs(row,col):
            vis[row][col]=1
            dr=[0,1,0,-1]
            dc=[1,0,-1,0]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and \
                not vis[nrow][ncol] and grid[nrow][ncol]==1:
                    dfs(nrow,ncol)
        for i in range(m):
            if not vis[0][i] and grid[0][i]==1:
                dfs(0,i)
            if not vis[n-1][i] and grid[n-1][i]==1:
                dfs(n-1,i)
        for i in range(n):
            if not vis[i][0] and grid[i][0]==1:
                dfs(i,0)
            if not vis[i][m-1] and grid[i][m-1]==1:
                dfs(i,m-1)
        cnt=0
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]==1:
                    cnt+=1
        return cnt