from collections import deque
class Solution:
    def safeNodes(self, V, edges):
        # Code here
        adj=[[] for i in range(V)]
        indegree=[0]*V
        for u,v in edges:
            adj[v].append(u)
            indegree[u]+=1
        queue=deque()
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            node=queue.popleft()
            topo.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return topo