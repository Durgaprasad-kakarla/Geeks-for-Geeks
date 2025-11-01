class Solution:
    def findOrder(self, n, prerequisites):
        # code here 
        adj=[[] for _ in range(n)]
        indegree=[0]*n
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        queue=deque()
        for i in range(n):
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
        return topo[::-1] if len(topo)==n else []
