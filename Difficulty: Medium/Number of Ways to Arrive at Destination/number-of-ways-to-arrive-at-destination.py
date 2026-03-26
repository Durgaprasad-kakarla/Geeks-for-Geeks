class Solution:
    def countPaths(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        dist=[float('inf') for _ in range(V)]
        ways=[0 for _ in range(V)]
        dist[0],ways[0]=0,1
        heap=[]
        heapq.heappush(heap,(0,0))
        while heap:
            d,node=heapq.heappop(heap)
            for i,wt in adj[node]:
                if dist[i]>d+wt:
                    dist[i]=d+wt
                    ways[i]=ways[node]
                    heapq.heappush(heap,(dist[i],i))
                elif dist[i]==d+wt:
                    ways[i]+=ways[node]
        return ways[V-1]
        