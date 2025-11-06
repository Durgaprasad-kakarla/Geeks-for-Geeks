class Solution:
    def isCyclic(self, V, edges):
        # code here
        adj=[[] for i in range(V)]
        for u,v in edges:
            adj[u].append(v)
        def dfs(node):
            vis[node]=1
            path_vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    if dfs(i):
                        return True
                elif path_vis[i]:
                    return True
            path_vis[node]=0
            return False
        vis=[0]*V
        path_vis=[0]*V
        for i in range(V):
            if not vis[i]:
                if dfs(i):
                    return True
        return False