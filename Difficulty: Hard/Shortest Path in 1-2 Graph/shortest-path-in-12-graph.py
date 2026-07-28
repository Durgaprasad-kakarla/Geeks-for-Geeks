import heapq
class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # code here
        dist=[float('inf') for _ in range(V)]
        dist[src]=0
        heap=[]
        heapq.heappush(heap,[0,src])
        adj=[[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        while heap:
            d,node=heapq.heappop(heap)
            for i,wt in adj[node]:
                if dist[i]>d+wt:
                    dist[i]=d+wt
                    heapq.heappush(heap,[dist[i],i])
        return dist[dest] if dist[dest]!=float('inf') else -1