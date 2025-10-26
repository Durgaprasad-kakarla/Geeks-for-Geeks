class Solution:
    def isCyclic(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        indegree=[0]*(V)
        for u,v in edges:
            adj[u].append(v)
            indegree[v]+=1
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
        return False if len(topo)==V else True