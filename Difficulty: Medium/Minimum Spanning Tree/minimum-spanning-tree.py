import heapq
class Solution:
    def spanningTree(self, V, edges):
        # code here
        heap=[]
        adj=[[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        heapq.heappush(heap,[0,0])
        vis=[0]*V
        cost=0
        while heap:
            d,node=heapq.heappop(heap)
            if vis[node]:
                continue
            vis[node]=1
            cost+=d
            for i,wt in adj[node]:
                if not vis[i]:
                    heapq.heappush(heap,[wt,i])
        return cost
        