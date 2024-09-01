import heapq
class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		#Code here
		n,m=len(grid),len(grid[0])
	    heap=[]
	    heapq.heappush(heap,[grid[0][0],0,0])
	    dist=[[float('inf') for i in range(m)] for j in range(n)]
	    dist[0][0]=grid[0][0]
	    while heap:
	        d,row,col=heapq.heappop(heap)
	        dr=[-1,0,1,0]
	        dc=[0,-1,0,1]
	        for i in range(4):
	            nrow=row+dr[i]
	            ncol=col+dc[i]
	            if nrow>=0 and nrow<n and ncol<m and ncol>=0 and dist[nrow][ncol]>dist[row][col]+grid[nrow][ncol]:
	                dist[nrow][ncol]=dist[row][col]+grid[nrow][ncol]
	                heapq.heappush(heap,[dist[nrow][ncol],nrow,ncol])
        return dist[n-1][m-1]	            
            

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends