from collections import deque
class Solution:
	def nearest(self, grid):
		# code here
		n,m=len(grid),len(grid[0])
		dist=[[float('inf') for _ in range(m)] for _ in range(n)]
		queue=deque()
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==1:
		            queue.append([0,i,j])
		            dist[i][j]=0
        while queue:
		    d,row,col=queue.popleft()
		    dr=[-1,0,1,0]
		    dc=[0,-1,0,1]
		    for i in range(4):
		        nrow=row+dr[i]
		        ncol=col+dc[i]
		        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==0 and dist[nrow][ncol]>d+1:
		            queue.append([d+1,nrow,ncol])
		            dist[nrow][ncol]=d+1
        return dist
		            