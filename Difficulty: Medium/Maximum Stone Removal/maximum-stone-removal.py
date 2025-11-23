class DisjointSet:
    def __init__(self,n):
        self.n=n+1
        self.size=[1]*(n+1)
        self.parent=[i for i in range(n+1)]
    def findupar(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.findupar(self.parent[node])
        return self.parent[node]
    def union_by_size(self,u,v):
        ulp_u=self.findupar(u)
        ulp_v=self.findupar(v)
        if ulp_u==ulp_v:
            return 
        if self.size[ulp_u]<=self.size[ulp_v]:
            self.size[ulp_v]+=self.size[ulp_u]
            self.parent[ulp_u]=ulp_v
        else:
            self.size[ulp_u]+=self.size[ulp_v]
            self.parent[ulp_v]=ulp_u
class Solution:
    def maxRemove(self, stones):
        # Code here
        max_row,max_col=0,0
        for u,v in stones:
            max_row=max(max_row,u)
            max_col=max(max_col,v)
        ds=DisjointSet(max_row+max_col+1)
        for u,v in stones:
            ds.union_by_size(u,v+max_row+1)
        st=set()
        for u,v in stones:
            if u==ds.findupar(u):
                st.add(u)
            if v+max_row+1==ds.findupar(v+max_row+1):
                st.add(v+max_row+1)
        return len(stones)-len(st)
        