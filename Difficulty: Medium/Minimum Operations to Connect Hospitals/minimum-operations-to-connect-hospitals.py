class DisjointSet:
    def __init__(self,n):
        self.n=n+1
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
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
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
    def union_by_size(self,u,v):
        ulp_u=self.findupar(u)
        ulp_v=self.findupar(v)
        if ulp_u==ulp_v:
            return 
        if self.size[ulp_u]<=self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=1
        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=1
        
    
    
    
class Solution:
    def minConnect(self, V, edges):
        # code here
        ds=DisjointSet(V)
        extra_edges=0
        for u,v in edges:
            ulp_u=ds.findupar(u)
            ulp_v=ds.findupar(v)
            if ulp_u==ulp_v:
                extra_edges+=1
                continue
            ds.union_by_size(ulp_u,ulp_v)
        components=0
        for i in range(V):
            if ds.findupar(i)==i:
                components+=1
        if extra_edges>=components-1:
            return components-1
        return -1
        
        
