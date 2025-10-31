from collections import deque
class Solution:
    def shortCycle(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans=float('inf')
        for src in range(V):
            dist,parent=[-1]*V,[-1]*V
            queue=deque([src])
            dist[src]=0
            while queue:
                node=queue.popleft()
                for i in adj[node]:
                    if dist[i]==-1:
                        dist[i]=dist[node]+1
                        parent[i]=node
                        queue.append(i)
                    elif parent[node]!=i:
                        ans=min(ans,dist[node]+dist[i]+1)
        return ans if ans!=float('inf') else -1