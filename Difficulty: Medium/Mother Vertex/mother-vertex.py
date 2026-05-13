class DisjointSet:
    def __init__(self,n):
        self.n=n+1
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
    def findupar(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.findupar(self.parent[node])
        return self.parent[node]
    def union_by_rank(self,u,v):
        ulp_u=self.findupar(u)
        ulp_v=self.findupar(v)
        if ulp_u==ulp_v:
            return 
        self.parent[ulp_v]=ulp_u
class Solution:
    def findMotherVertex(self, V, edges):
        # code here
        adj =[[] for i in range(V)]
        for u, v in edges:
            adj[u].append(v)

        # DFS function
        def dfs(node, visited):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, visited)

        # Step 1: Find candidate mother vertex
        visited = [False] * V
        candidate = -1

        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                candidate = i

        # Step 2: Verify candidate
        visited = [False] * V
        dfs(candidate, visited)

        if not all(visited):
            return -1

        # Step 3: Find smallest mother vertex
        ans = candidate
        for i in range(candidate):
            visited = [False] * V
            dfs(i, visited)
            if all(visited):
                ans = i
                break

        return ans