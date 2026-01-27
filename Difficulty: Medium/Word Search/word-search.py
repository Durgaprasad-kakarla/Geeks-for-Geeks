class Solution:
	def isWordExist(self, mat, word):
		# Code here
		def dfs(row,col,ind):
		  #  print(row,col,ind)
		    if ind==len(word)-1:
		        return True
		    vis[row][col]=1
		    dr=[-1,0,1,0]
		    dc=[0,-1,0,1]
		    for i in range(4):
		        nrow=row+dr[i]
		        ncol=col+dc[i]
		        if nrow>=0 and ncol>=0 and nrow<n and ncol<m and not vis[nrow][ncol] and  ind+1<len(word) and word[ind+1]==mat[nrow][ncol]:
		            if dfs(nrow,ncol,ind+1):
		                return True
		    vis[row][col]=0
		    return False
		n,m=len(mat),len(mat[0])
		vis=[[0 for _ in range(m)] for _ in range(n)]
		for i in range(n):
		    for j in range(m):
		        if mat[i][j]==word[0]:
		            if dfs(i,j,0):
		                return True
		return False