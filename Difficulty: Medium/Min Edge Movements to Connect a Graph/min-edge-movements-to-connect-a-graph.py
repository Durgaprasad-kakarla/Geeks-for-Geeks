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
        ulp_u,ulp_v=self.findupar(u),self.findupar(v)
        if ulp_u==ulp_v:
            return 
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
class Solution:
    def minEdgesReq(self, n, edges):
        # code here
        ds=DisjointSet(n)
        extra_edges=0
        for u,v in edges:
            ulp_u,ulp_v=ds.findupar(u),ds.findupar(v)
            if ulp_u==ulp_v:
                extra_edges+=1
            ds.union_by_rank(ulp_u,ulp_v)
        components=0
        for i in range(n):
            if ds.findupar(i)==i:
                components+=1
        return components-1 if components-1<=extra_edges else -1