class Solution:
    def fill(self, grid):
        # Code here
        n,m=len(grid),len(grid[0])
        vis=[[0 for i in range(m)] for _ in range(n)]
        def dfs(row,col):
            vis[row][col]=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]=='O' and not vis[nrow][ncol]:
                    dfs(nrow,ncol)
        for i in range(n):
            if grid[i][0]=='O' and not vis[i][0]:
                dfs(i,0)
            if grid[i][m-1]=='O' and not vis[i][m-1]:
                dfs(i,m-1)
        for i in range(m):
            if grid[0][i]=='O' and not vis[0][i]:
                dfs(0,i)
            if grid[n-1][i]=='O' and not vis[n-1][i]:
                dfs(n-1,i)
        for i in range(n):
            for j in range(m):
                if vis[i][j]:
                    grid[i][j]='O'
                else:
                    grid[i][j]='X'
        return grid
                
        