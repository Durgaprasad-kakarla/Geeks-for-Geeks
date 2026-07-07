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
        ulp_u,ulp_v=self.findupar(u),self.findupar(v)
        if ulp_u==ulp_v:
            return 
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_v
            self.rank[ulp_v]+=1
    def union_by_size(self,u,v):
        ulp_u,ulp_v=self.findupar(u),self.findupar(v)
        if ulp_u==ulp_v:
            return
        if self.size[ulp_u]<=self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
class Solution:
    def largestArea(self, n, m, arr):
        # code here
        if not arr:
            return n*m
        rows = sorted(r for r, c in arr)
        cols = sorted(c for r, c in arr)

        maxRow = rows[0] - 1
        for i in range(1, len(rows)):
            maxRow = max(maxRow, rows[i] - rows[i - 1] - 1)
        maxRow = max(maxRow, n - rows[-1])

        maxCol = cols[0] - 1
        for i in range(1, len(cols)):
            maxCol = max(maxCol, cols[i] - cols[i - 1] - 1)
        maxCol = max(maxCol, m - cols[-1])

        return maxRow * maxCol