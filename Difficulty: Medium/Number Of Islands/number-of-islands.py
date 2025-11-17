#User function Template for python3

from typing import List
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
        if self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        elif self.rank[ulp_v]>self.rank[ulp_u]:
            self.parent[ulp_u]=ulp_v
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        ds=DisjointSet(rows*cols)
        mat=[[0 for _ in range(cols)] for _ in range(rows)]
        ans=[]
        for u,v in operators:
            node1=u*m+v
            mat[u][v]=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=u+dr[i]
                ncol=v+dc[i]
                if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and mat[nrow][ncol]==1:
                    node2=nrow*m+ncol
                    ulp_u=ds.findupar(node1)
                    ulp_v=ds.findupar(node2)
                    if ulp_u==ulp_v:
                        continue
                    ds.union_by_rank(node1,node2)
            # print(node1,ds.findupar(node1))
            cnt=0
            for i in range(rows*cols):
                if ds.findupar(i)==i and mat[i//cols][i%cols]==1:
                    cnt+=1
            ans.append(cnt)
        return ans
                
                
                
                
                