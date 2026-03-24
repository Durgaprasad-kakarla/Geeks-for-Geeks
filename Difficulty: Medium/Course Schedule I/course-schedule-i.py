class Solution:
    def canFinish(self, n, prerequisites):
        # code here 
        indegree=[0]*n
        adj=[[] for _ in range(n)]
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
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
        return len(topo)==n