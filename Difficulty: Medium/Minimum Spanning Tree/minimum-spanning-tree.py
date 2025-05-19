#User function Template for python3
from typing import List
import heapq
class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
    def findupar(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.findupar(self.parent[node])
        return self.parent[node]
    def unionbyrank(self,u,v):
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
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        ds=DisjointSet(V)
        edges=[]
        for i in range(len(adj)):
            for j,wt in adj[i]:
                edges.append([wt,i,j])
        edges.sort()
        tot=0
        for wt,u,v in edges:
            if ds.findupar(u)!=ds.findupar(v):
                # print(wt,u,v)
                ds.unionbyrank(u,v)
                tot+=wt
        return tot
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
        print("~")

# } Driver Code Ends