import heapq
class Solution:
    def maxDistance(self, V, src, edges):
        # code here
        dist=[-float('inf') for _ in range(V)]
        adj=[[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
        heap=[]
        heapq.heappush(heap,[0,src])
        dist[src]=0
        while heap:
            d,node=heapq.heappop(heap)
            for i,wt in adj[node]:
                if dist[i]<d+wt:
                    dist[i]=d+wt
                    heapq.heappush(heap,[dist[i],i])
        for i in range(V):
            if dist[i]==-float('inf'):
                dist[i]='INF'
        return dist