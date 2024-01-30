from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, mat):
		#Code here
        m=len(mat)
        n=len(mat[0])
        
        vis=[[0 for i in range(n)] for j in range(m)]
        dist=[[0 for i in range(n)] for j in range(m)]
        
        queue=deque()
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and mat[i][j]==1:
                    vis[i][j]=1
                    queue.append([i,j,0])
        while queue:
            row,col,d=queue.popleft()
            dist[row][col]=d
            dr=[0,-1,0,1]
            dc=[-1,0,1,0]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and not vis[nrow][ncol]:
                    vis[nrow][ncol]=1
                    queue.append([nrow,ncol,d+1])
        return dist

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends