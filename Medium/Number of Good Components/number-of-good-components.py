
from typing import List
class Disjointset:
    def __init__(self,n):
        self.size=[1]*(n+1)
        self.parent=[i for i in range(n+1)]
        self.cnt_edges=[0]*(n+1)
    def findupar(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.findupar(self.parent[node])
        return self.parent[node]
    def unionbysize(self,u,v):
        upar=self.findupar(u)
        vpar=self.findupar(v)
        if upar!=vpar:
            if self.size[upar]<=self.size[vpar]:
                self.parent[vpar]=upar
                self.size[upar]+=self.size[vpar]
                self.cnt_edges[upar]+=self.cnt_edges[vpar]+1
            else:
                self.parent[upar]=vpar
                self.size[vpar]+=self.size[upar]
                self.cnt_edges[vpar]+=self.cnt_edges[upar]+1
        else:
            self.cnt_edges[upar]+=1
        # print(self.cnt_edges,u,v)

class Solution:
    def findNumberOfGoodComponent(self, e : int, n : int, edges : List[List[int]]) -> int:
        # code here
        ds=Disjointset(n)
        for u,v in edges:
            upar=ds.findupar(u)
            vpar=ds.findupar(v)
            ds.unionbysize(upar,vpar)
        cnt=0
        # print(ds.size,ds.parent,ds.cnt_edges)
        for i in range(1,n+1):
            if ds.parent[i]==i:
                x=ds.size[i]
                # print((x*(x-1))//2,ds.cnt_edges[i])
                if (x*(x-1))//2==ds.cnt_edges[i]:
                    cnt+=1
        return cnt
            
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        e = int(input())

        v = int(input())

        edges = IntMatrix().Input(e, 2)

        obj = Solution()
        res = obj.findNumberOfGoodComponent(e, v, edges)

        print(res)

# } Driver Code Ends