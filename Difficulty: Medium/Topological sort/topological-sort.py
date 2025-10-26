class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        def dfs(node):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i)
            stack.append(node)
        vis=[0]*(V)
        stack=[]
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return stack[::-1]