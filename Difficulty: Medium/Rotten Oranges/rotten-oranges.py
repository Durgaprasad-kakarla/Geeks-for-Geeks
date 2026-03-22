class Solution:
	def orangesRot(self, mat):
		# code here
		n,m=len(mat),len(mat[0])
		queue=deque()
		for i in range(n):
		    for j in range(m):
		        if mat[i][j]==2:
		            queue.append([i,j,0])
		t=0
		while queue:
		    row,col,t=queue.popleft()
		    dr=[-1,0,1,0]
		    dc=[0,-1,0,1]
		    for i in range(4):
		        nrow=row+dr[i]
		        ncol=col+dc[i]
		        if nrow>=0 and nrow<n and ncol>=0 and ncol<m and mat[nrow][ncol]==1:
		            mat[nrow][ncol]=2
		            queue.append([nrow,ncol,t+1])
		for i in range(n):
		     for j in range(m):
		         if mat[i][j]==1:
		             return -1
		return t