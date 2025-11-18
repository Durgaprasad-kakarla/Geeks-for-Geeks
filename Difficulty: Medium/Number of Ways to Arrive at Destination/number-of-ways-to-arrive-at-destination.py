class Solution:
    def countPaths(self, n, edges):
        # code here
        dist=[float('inf')]*n 
        adj=[[] for i in range(n)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        heap=[]
        heapq.heappush(heap,[0,0])
        dist[0]=0
        ways=[0]*n
        ways[0]=1
        while heap:
            d,node=heapq.heappop(heap)
            for i,wt in adj[node]:
                if wt+d<dist[i]:
                    dist[i]=wt+dist[node]
                    ways[i]=ways[node]
                    heapq.heappush(heap,[dist[i],i])
                elif wt+d==dist[i]:
                    ways[i]+=ways[node]
        return ways[n-1]%(10**9+7)