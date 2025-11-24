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
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
class Solution:
    def secondMST(self, V, edges):
        # code her
        edges.sort(key=lambda x:x[2])
        def get_mst(edges):
            ds=DisjointSet(V)
            tot=0
            E=len(edges)
            considered_edges=[]
            for i in range(E):
                if not edges[i]:
                    continue
                u,v,wt=edges[i]
                ulp_u,ulp_v=ds.findupar(u),ds.findupar(v)
                if ulp_u==ulp_v:
                    continue
                considered_edges.append(i)
                tot+=wt
                ds.union_by_rank(ulp_u,ulp_v)
            return tot,considered_edges
        min1,considered=get_mst(edges)
        min2=float("inf")
        E=len(edges)
        for i in considered:
            edge=edges[i]
            edges[i]=[]
            tot,_=get_mst(edges)
            if tot>min1:
                min2=min(min2,tot)
            edges[i]=edge
        return min2 if min2!=float('inf') else -1
            
        
        
