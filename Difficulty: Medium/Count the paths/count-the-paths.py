class Solution:
    def countPaths(self, edges, V, src, dest):
        #Code here
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        vis=[0]*V
        def dfs(node):
            if node==dest:
                return 1
            vis[node]=1
            tot=0
            for i in adj[node]:
                if not vis[i]:
                    tot+=dfs(i)
                else:
                    tot+=dic[i]
            dic[node]=tot
            return tot
        dic={}
        return dfs(src)