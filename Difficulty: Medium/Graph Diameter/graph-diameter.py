class Solution:
    def diameter(self, V, edges):
        # Code here
        adj=[[] for i in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=[0 for i in range(V)]
        global diameter
        diameter=0
        def dfs(node):
            global diameter
            vis[node]=1
            tot=0
            maxi=0
            paths=[]
            for i in adj[node]:
                if not vis[i]:
                    curr=dfs(i)
                    paths.append(curr)
                    maxi=max(maxi,curr)
            if paths:
                paths.sort()
                diameter=max(diameter,1+paths[-1]+(paths[-2] if len(paths)>1 else 0))
            return 1+maxi
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return diameter-1