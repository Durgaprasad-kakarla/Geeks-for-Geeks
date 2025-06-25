from collections import deque
class Solution:
	def minStepToReachTarget(self, knight, targetPos, n):
		#Code here
		queue=deque()
		queue.append([0,knight[0]-1,knight[1]-1])
		dist=[[float('inf') for i in range(n)] for j in range(n)]
		dist[knight[0]-1][knight[1]-1]=0
		while queue:
		    d,row,col=queue.popleft()
		    dr=[2,2,1,1,-2,-2,-1,-1]
		    dc=[-1,1,-2,2,-1,1,-2,2]
		    for i in range(8):
		        nrow=row+dr[i]
		        ncol=col+dc[i]
		        if nrow>=0 and nrow<n and ncol>=0 and ncol<n and dist[nrow][ncol]>dist[row][col]+1:
		            dist[nrow][ncol]=dist[row][col]+1
		            queue.append([d+1,nrow,ncol])
		return dist[targetPos[0]-1][targetPos[1]-1]