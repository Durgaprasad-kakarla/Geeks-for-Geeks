#User function Template for python3
from collections import deque
class Solution:
    def numIslands(self, grid):
        # code here
        n,m=len(grid),len(grid[0])
        def bfs(row,col,grid,vis):
            n,m=len(grid),len(grid[0])
            queue=deque()
            queue.append([row,col])
            dr=[-1,-1,-1,0,1,1,1,0]
            dc=[0,1,-1,-1,0,-1,1,1]
            vis[row][col]=1
            while queue:
                row,col=queue.popleft()
                for i in range(8):
                    nrow=row+dr[i]
                    ncol=col+dc[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m and not vis[nrow][ncol] and grid[nrow][ncol]=='L':
                        vis[nrow][ncol]=1
                        queue.append([nrow,ncol])
        cnt=0
        vis=[[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='L' and not vis[i][j]:
                    bfs(i,j,grid,vis)
                    cnt+=1
        return cnt

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends