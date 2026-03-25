class Solution:
    def minHeightRoot(self, V, edges):
        # Code here
        adj=[[] for _ in range(V)]
        indegree=[0]*V
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        queue=[]
        for i in range(V):
            if indegree[i]==1:
                queue.append(i)
        ans=[]
        while queue:
            next_queue=[]
            for curr in queue:
                for nxt in adj[curr]:
                    indegree[nxt]-=1
                    if indegree[nxt]==1:
                        next_queue.append(nxt)
            # print(queue)
            ans=queue
            queue=next_queue
        return ans