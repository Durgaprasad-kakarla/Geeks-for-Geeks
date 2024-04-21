from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
        n,m=len(grid),len(grid[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        queue=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append([0,i,j])
                    vis[i][j]=1
        d=0
        while queue:
            d,row,col=queue.popleft()
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and ncol>=0 and nrow<n and ncol<m and grid[nrow][ncol]==1 and not vis[nrow][ncol]:
                    queue.append([d+1,nrow,ncol])
                    vis[nrow][ncol]=1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    return -1
        return d
#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends