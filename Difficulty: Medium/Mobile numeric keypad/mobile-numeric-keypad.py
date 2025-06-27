class Solution:
	def getCount(self, n):
		# code here
		mat=[[1,1,1],[1,1,1],[1,1,1],[0,1,0]]
		def unique_sequences(row,col,cnt):
		    if cnt==n:
		        return 1
		    if (row,col,cnt) in dic:
		        return dic[(row,col,cnt)]
		    tot=unique_sequences(row,col,cnt+1)
		    dr=[-1,0,1,0]
		    dc=[0,-1,0,1]
		    for i in range(4):
		        nrow=row+dr[i]
		        ncol=col+dc[i]
		        if nrow>=0 and ncol<3 and nrow<4 and ncol>=0 and mat[nrow][ncol]==1:
		            tot+=unique_sequences(nrow,ncol,cnt+1)
		    dic[(row,col,cnt)]=tot
		    return tot
		tot=0
		dic={}
		for i in range(4):
		    for j in range(3):
		        if mat[i][j]==1:
		            tot+=(unique_sequences(i,j,1))
		return tot