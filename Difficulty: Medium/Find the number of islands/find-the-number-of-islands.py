from collections import deque
class Solution:
    def numIslands(self, grid):
        # code here
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        def bfs(row,col,vis,grid):
            queue=deque()
            queue.append([row,col])
            vis[row][col]=1
            while queue:
                row,col=queue.popleft()
                dr=[-1,-1,-1,0,1,1,1,0]
                dc=[-1,0,1,1,1,0,-1,-1]
                for i in range(8):
                    nrow=row+dr[i]
                    ncol=col+dc[i]
                    if nrow>=0 and ncol>=0 and nrow<n and ncol<m and not vis[nrow][ncol] and grid[nrow][ncol]==1:
                        queue.append([nrow,ncol])
                        vis[nrow][ncol]=1
        cnt=0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j]==1:
                    cnt+=1
                    bfs(i,j,vis,grid)
        return cnt
        # n,m=len(grid),len(grid[0])
        # def dfs(row,col):
        #     vis[row][col]=1
        #     dr=[-1,-1,-1,0,1,1,1,0]
        #     dc=[-1,0,1,1,1,0,-1,-1]
        #     for i in range(8):
        #         nrow=row+dr[i]
        #         ncol=col+dc[i]
        #         if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1 and not vis[nrow][ncol]:
        #             dfs(nrow,ncol)
        # vis=[[0 for i in range(m)] for j in range(n)]
        # cnt=0
        # for i in range(n):
        #     for j in range(m):
        #         if not vis[i][j] and grid[i][j]==1:
        #             dfs(i,j)
        #             cnt+=1
        # return cnt

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends