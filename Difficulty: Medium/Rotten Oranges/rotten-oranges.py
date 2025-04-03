from collections import deque
class Solution:
	def orangesRotting(self, mat):
		#Code here
        n,m=len(mat),len(mat[0])
        vis=[[0 for _ in range(m)] for _ in range(n)]
        def bfs(mat,vis):
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            queue=deque()
            d=0
            for i in range(n):
                for j in range(m):
                    if mat[i][j]==2 and not vis[i][j]:
                        queue.append([i,j,0])
                        vis[i][j]=1
            while queue:
                row,col,d=queue.popleft()
                for i in range(4):
                    nrow=row+dr[i]
                    ncol=col+dc[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m and mat[nrow][ncol]==1 and not vis[nrow][ncol]:
                        vis[nrow][ncol]=1
                        queue.append([nrow,ncol,d+1])
            return d
        mini=bfs(mat,vis)
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1 and not vis[i][j]:
                    return -1
        return mini

#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends