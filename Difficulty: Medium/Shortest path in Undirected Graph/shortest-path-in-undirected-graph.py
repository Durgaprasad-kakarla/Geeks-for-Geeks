#User function Template for python3
import heapq
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        heap=[]
        heapq.heappush(heap,[0,src])
        dist=[float('inf')]*n 
        dist[src]=0
        while heap:
            d,node=heapq.heappop(heap)
            for i in adj[node]:
                if dist[i]>dist[node]+1:
                    dist[i]=dist[node]+1
                    heapq.heappush(heap,[dist[i],i])
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends