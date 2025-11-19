import heapq
class Solution:
    def minCostPath(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        heap=[]
        heapq.heappush(heap,[0,0,0])
        dist=[[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0]=0
        while heap:
            d,row,col=heapq.heappop(heap)
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and dist[nrow][ncol]>max(d,abs(mat[row][col]-mat[nrow][ncol])):
                    dist[nrow][ncol]=max(d,abs(mat[row][col]-mat[nrow][ncol]))
                    heapq.heappush(heap,[dist[nrow][ncol],nrow,ncol])
        return dist[n-1][m-1]
        
