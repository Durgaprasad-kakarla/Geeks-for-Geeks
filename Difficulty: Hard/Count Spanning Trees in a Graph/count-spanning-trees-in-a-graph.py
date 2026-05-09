class DisjointSet:
    def __init__(self,n):
        self.n=n+1
        self.parent=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
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
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_u]=ulp_v
            self.rank[ulp_v]+=1
import numpy as np
class Solution:
    def countSpanTree(self, n, edges):
        # code here
        L = np.zeros((n, n), dtype=int)
        for u, v in edges:
            L[u][u] += 1
            L[v][v] += 1
            L[u][v] -= 1
            L[v][u] -= 1
        minor = L[:-1, :-1]
        return round(np.linalg.det(minor))